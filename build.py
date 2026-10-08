# ILANG: static builder; reads brand and providers from .ilang/site.ilang.
# ILANG: omit unknown offer prices and dates from page content and structured data.
import html,json,re,shutil,hashlib
from datetime import date,datetime,timezone
from pathlib import Path
from urllib.parse import quote
R=Path(__file__).parent;OUT=R/'site'
# Published /deals/ addresses that must survive a scraper rewrite. The scraper never writes
# page_slug, so a changed offer title would otherwise rename the address and 404 the old one.
STATIC_LEGACY=[('/deals/hostinger-student-discount','/providers/hostinger#plan-hostinger-student-discount'),
 ('/deals/hostinger-70-off-hostinger-vps-page','/providers/hostinger#plan-hostinger-70-off-hostinger-vps-page'),
 ('/deals/hostinger-67-off-hostinger-vps-page','/providers/hostinger#plan-hostinger-67-off-hostinger-vps-page'),
 ('/deals/hostinger-63-off-hostinger-vps-page','/providers/hostinger#plan-hostinger-63-off-hostinger-vps-page'),
 ('/deals/hostinger-65-off-hostinger-vps-page','/providers/hostinger#plan-hostinger-65-off-hostinger-vps-page')]
def cfg():
 c={'providers':[],'discovery':[],'coupon_guides':[],'brand':'Lumafare','niche':'VPS hosting deals','domain':'https://lumafare.com','contact_email':'','updates_every':'not specified'};sec=''
 for raw in (R/'.ilang/site.ilang').read_text(encoding='utf8').splitlines():
  s=raw.strip()
  if s.startswith('::STATE'):c.update({k:v.strip() for k,v in re.findall(r'(brand|niche|domain|locale|contact_email):([^,}]+)',s)})
  elif s.startswith('::MODULE{PROVIDERS'):sec='providers'
  elif s.startswith('::MODULE{DISCOVERY'):sec='discovery'
  elif s.startswith('::MODULE{COUPON_GUIDES'):sec='coupon_guides'
  elif s.startswith('::MODULE{'):sec=''
  elif s.startswith('::RULE{updates_every:'):
   match=re.search(r'updates_every:([^}]+)',s)
   if match:c['updates_every']=match.group(1)
  elif sec and '|' in s and not s.startswith('::'):
   p=[x.strip() for x in s.split('|')]
   if len(p)>=3:
    if sec=='coupon_guides':c[sec].append({'slug':p[0],'name':p[1],'sources':p[2:]})
    else:c[sec].append({'name':p[0],'url':p[1],'source_url':p[2],'affiliate_url':p[3] if len(p)>3 else ''})
 if not c['providers']:c['providers']=c['discovery']
 return c
def e(x):return html.escape(str(x),quote=True)
def slug(s):return re.sub(r'[^a-z0-9]+','-',s.lower()).strip('-')[:90] or 'offer'
def parse_article(path):
 raw=path.read_text(encoding='utf8')
 match=re.match(r'\A---\s*\n(.*?)\n---\s*\n?(.*)\Z',raw,re.S)
 if not match:raise ValueError(f'{path}: expected YAML frontmatter delimited by ---')
 meta={};key=None
 for line in match.group(1).splitlines():
  if not line.strip() or line.lstrip().startswith('#'):continue
  item=re.match(r'^([a-z_]+):\s*(.*)$',line)
  if item:
   key=item.group(1);value=item.group(2).strip()
   if value.startswith('[') and value.endswith(']'):
    meta[key]=[v.strip().strip('"\'') for v in value[1:-1].split(',') if v.strip()]
   elif value:meta[key]=value.strip('"\'')
   else:meta[key]=[] if key=='sources' else ''
  elif line.startswith(('  - ','- ')) and key=='sources':meta[key].append(line.split('-',1)[1].strip().strip('"\''))
  else:raise ValueError(f'{path}: invalid frontmatter line: {line}')
 unknown=set(meta)-{'title','slug','date','description','question','sources'}
 if unknown:raise ValueError(f'{path}: unsupported frontmatter fields: {", ".join(sorted(unknown))}')
 for required in ('title','slug','date','description'):
  if not isinstance(meta.get(required),str) or not meta[required].strip():raise ValueError(f'{path}: frontmatter requires {required}')
 if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',meta['slug']):raise ValueError(f'{path}: slug must contain lowercase letters, digits, and single hyphens')
 try:date.fromisoformat(meta['date'])
 except ValueError as exc:raise ValueError(f'{path}: date must be an ISO calendar date') from exc
 if not isinstance(meta.get('sources',[]),list):raise ValueError(f'{path}: sources must be a URL list')
 for source in meta.get('sources',[]):
  if not re.match(r'^https?://',source):raise ValueError(f'{path}: source URL must use http or https')
 meta['sources']=meta.get('sources',[])
 meta['body']=match.group(2).strip()
 return meta
def inline_markdown(value):
 parts=[];tokens=[]
 def hold(rendered):
  token=f'\x00{len(tokens)}\x00';tokens.append(rendered);return token
 value=re.sub(r'!\[([^\]]*)\]\(([^)]+)\)',lambda m:hold(f'<img src="{e(m.group(2))}" alt="{e(m.group(1))}" loading="lazy">'),value)
 value=re.sub(r'\[([^\]]+)\]\(([^)]+)\)',lambda m:hold(f'<a href="{e(m.group(2))}">{html.escape(m.group(1))}</a>') if re.match(r'^(https?://|mailto:|/|#)',m.group(2)) else hold(html.escape(m.group(0))),value)
 value=html.escape(value)
 value=re.sub(r'`([^`]+)`',r'<code>\1</code>',value)
 value=re.sub(r'\*\*(.+?)\*\*',r'<strong>\1</strong>',value)
 for i,rendered in enumerate(tokens):value=value.replace(f'\x00{i}\x00',rendered)
 return value
def render_markdown(source):
 out=[];paragraph=[];listing=None;code=[];in_code=False
 def flush_paragraph():
  if paragraph:out.append('<p>'+inline_markdown(' '.join(paragraph))+'</p>');paragraph.clear()
 def close_list():
  nonlocal listing
  if listing:out.append(f'</{listing}>');listing=None
 for line in source.splitlines():
  if line.startswith('```'):
   flush_paragraph();close_list()
   if in_code:
    out.append('<pre><code>'+html.escape('\n'.join(code))+'</code></pre>');code=[];in_code=False
   else:in_code=True
   continue
  if in_code:
   code.append(line);continue
  if not line.strip():flush_paragraph();close_list();continue
  heading=re.match(r'^(#{1,6})\s+(.+?)\s*#*$',line)
  if heading:
   flush_paragraph();close_list();level=len(heading.group(1));out.append(f'<h{level}>{inline_markdown(heading.group(2))}</h{level}>');continue
  item=re.match(r'^\s*([-*]|\d+\.)\s+(.+)$',line)
  if item:
   flush_paragraph();kind='ol' if item.group(1)[0].isdigit() else 'ul'
   if listing!=kind:close_list();out.append(f'<{kind}>');listing=kind
   out.append('<li>'+inline_markdown(item.group(2))+'</li>');continue
  paragraph.append(line.strip())
 if in_code:out.append('<pre><code>'+html.escape('\n'.join(code))+'</code></pre>')
 flush_paragraph();close_list()
 return '\n'.join(out)
def article_records():
 folder=R/'content/articles'
 records=[parse_article(path) for path in sorted(folder.glob('*.md'))] if folder.exists() else []
 seen=set()
 for record in records:
  if record['slug'] in seen:raise ValueError(f'duplicate article slug: {record["slug"]}')
  seen.add(record['slug'])
 return records
def main():
 c=cfg();
 if not c.get('contact_email') or '@' not in c['contact_email'] or not c['contact_email'].lower().endswith('@lumafare.com'):
  raise RuntimeError('Contact page requires the owner-provided, working @lumafare.com email address; no address was guessed.')
 if OUT.resolve().parent!=R.resolve():raise RuntimeError('Refusing to clean output outside project root')
 # Validate every required input first: a failed build must never leave the previous site deleted.
 d=json.loads((R/'data/offers.json').read_text(encoding='utf8')) if (R/'data/offers.json').exists() else {'offers':[]}
 if not d.get('source_scan_at'):raise RuntimeError('A completed scraper run is required; data/offers.json has no source_scan_at.')
 try:scan_time=datetime.fromisoformat(d['source_scan_at'].replace('Z','+00:00')).astimezone(timezone.utc)
 except ValueError as exc:raise RuntimeError('Invalid source_scan_at in data/offers.json.') from exc
 site_check_at=scan_time.isoformat(timespec='seconds');scan_date=scan_time.date().isoformat()
 today=datetime.now(timezone.utc).date().isoformat();all_offers=d.get('offers',[]);offers=[o for o in all_offers if o.get('status','active')=='active' and (not o.get('valid_until') or o['valid_until']>=today)];base=c['domain'].rstrip('/')
 # Keep the existing generated tree in place and overwrite deterministic outputs.
 # This avoids a broad recursive delete before a build has completed successfully.
 OUT.mkdir(exist_ok=True)
 assets=R/'assets'
 if assets.is_dir():shutil.copytree(assets,OUT/'assets',dirs_exist_ok=True)
 css=r"""*{box-sizing:border-box}
body{margin:0;background:radial-gradient(ellipse at 50% -18rem,rgba(211,229,255,.62),transparent 42rem),#f6f8fc;color:#132238;font:16px/1.65 Inter,ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;-webkit-font-smoothing:antialiased}
a{color:#2457d6;text-decoration-thickness:1px;text-underline-offset:3px}
a:hover{color:#143b9e}
header{position:sticky;top:0;z-index:5;display:flex;align-items:center;justify-content:space-between;gap:18px;padding:15px max(24px,calc((100vw - 1120px)/2));background:rgba(255,255,255,.88);border-bottom:1px solid rgba(218,228,241,.9);backdrop-filter:blur(16px)}
header>a:first-child{color:#132238;text-decoration:none;font-size:1.12rem;letter-spacing:-.03em}
header>a:first-child b{font-weight:800}
header nav{display:flex;align-items:center;justify-content:flex-end;gap:8px;flex-wrap:wrap}
header nav a{padding:8px 12px;border:1px solid #dce5f2;border-radius:999px;color:#334a68;text-decoration:none;font-size:.9rem;font-weight:650;white-space:nowrap}
header nav a:hover{background:#eef4ff;border-color:#c7d7f3;color:#1d4ed8}
header>a:last-child:hover{background:#eef4ff;border-color:#c7d7f3;color:#1d4ed8}
main{max-width:1120px;margin:0 auto;padding:42px 24px 72px}
h1,h2,h3{color:#132238;letter-spacing:-.035em;line-height:1.2}
h1{font-size:clamp(2.35rem,5.2vw,4.4rem);margin:.3em 0 .42em}
h2{font-size:clamp(1.45rem,3vw,2rem);margin:48px 0 20px}
h3{font-size:1.12rem;margin:0}
p{margin:0 0 1em}
.hero{position:relative;isolation:isolate;overflow:hidden;margin:4px 0 52px;padding:clamp(34px,6.5vw,76px);border:1px solid rgba(159,219,241,.22);border-radius:30px;background:radial-gradient(ellipse at 88% 18%,rgba(76,201,240,.28),transparent 34%),linear-gradient(130deg,#10233f 0%,#173b68 62%,#19556d 100%);box-shadow:0 26px 60px rgba(20,48,82,.18);color:#fff}
.hero:after{position:absolute;z-index:-1;right:-82px;bottom:-190px;width:390px;height:390px;border:1px solid rgba(205,239,255,.18);border-radius:50%;box-shadow:0 0 0 32px rgba(205,239,255,.035),0 0 0 70px rgba(205,239,255,.025);content:"";pointer-events:none}
.hero h1{max-width:820px;color:#fff}
.hero p{max-width:700px;color:#d8e7f7;font-size:1.08rem}
.hero p:first-child{margin:0 0 14px;color:#9fdbf1;font-size:.78rem;font-weight:750;letter-spacing:.13em;text-transform:uppercase}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,280px),1fr));align-items:stretch;gap:16px}
.card{display:flex;flex-direction:column;align-items:flex-start;gap:12px;min-width:0;min-height:148px;margin:0;padding:23px;border:1px solid #e1e8f2;border-radius:19px;background:linear-gradient(155deg,#fff 35%,#fafdff);box-shadow:0 5px 18px rgba(21,43,73,.045);transition:transform .18s ease,border-color .18s ease,box-shadow .18s ease}
.card:hover{transform:translateY(-3px);border-color:#c5d7ef;box-shadow:0 14px 28px rgba(21,43,73,.085)}
.plan{scroll-margin-top:100px}
.plan-details,.page-details{width:100%;padding:18px 20px;border:1px solid #e1e8f2;border-radius:14px;background:#f7faff}
.plan-details h4{margin:0 0 12px;color:#132238}
.plan-details p,.page-details p{margin:7px 0;color:#435671;font-size:.93rem;font-weight:400;overflow-wrap:anywhere}
.page-details{margin-top:36px}
.table-wrap{width:100%;overflow-x:auto;border:1px solid #e1e8f2;border-radius:14px;background:#fff}
.verification-table{width:100%;min-width:660px;border-collapse:collapse;text-align:left}
.verification-table th,.verification-table td{padding:14px 16px;border-bottom:1px solid #e8edf4;vertical-align:top}
.verification-table th{background:#f7faff;color:#435671;font-size:.84rem}
.verification-table td{overflow-wrap:anywhere}
.verification-table tr:last-child td{border-bottom:0}
.card small{color:#61738d;font-size:.78rem;font-weight:750;letter-spacing:.08em;text-transform:uppercase}
.card h2,.card h3{margin:0}
.card p{margin:0;color:#435671;font-weight:650}
.card>a{display:inline-flex;align-items:center;gap:5px;margin-top:auto;color:#2457d6;font-weight:700;text-decoration:none}
.card>a:hover{text-decoration:underline}
main>h2{display:flex;align-items:center;gap:12px}
main>h2:after{width:34px;height:3px;border-radius:99px;background:linear-gradient(90deg,#2d6ce4,#56c3d8);content:""}
main>h1{max-width:850px;font-size:clamp(2.1rem,4.6vw,3.65rem)}
main:has(>p:first-child a){max-width:880px;padding-top:36px}
main>p:first-child a{transition:background .15s ease,border-color .15s ease}
main>p:first-child a:hover{border-color:#c7d7f3;background:#eef4ff;color:#1d4ed8}
a:focus-visible{outline:3px solid #75a7ff;outline-offset:4px;border-radius:4px}
.crumbs{margin:0 0 16px;color:#61738d;font-size:.9rem}
.crumbs a{color:#2457d6}
.crumbs span{color:#132238;font-weight:650}
.siblings{display:flex;gap:8px;flex-wrap:wrap;margin:12px 0 0}
.siblings a{padding:8px 12px;border:1px solid #dce5f2;border-radius:999px;background:#fff;color:#334a68;text-decoration:none;font-size:.9rem;font-weight:650}
.siblings a:hover{background:#eef4ff;border-color:#c7d7f3;color:#1d4ed8}
main>p:first-child a{display:inline-flex;align-items:center;padding:7px 12px;border:1px solid #dce5f2;border-radius:999px;background:#fff;color:#435671;text-decoration:none;font-size:.9rem}
footer{padding:24px max(24px,calc((100vw - 1120px)/2)) 34px;border-top:1px solid #e2e9f1;color:#687991;font-size:.9rem}
footer p{margin:0}
footer nav{margin-top:10px;display:flex;gap:8px;flex-wrap:wrap}
@media(max-width:640px){
 body{font-size:15px}
 header{gap:10px;padding:12px 18px}
 header>a:first-child{font-size:1.02rem}
 header nav{justify-content:flex-start;gap:6px}
 header nav a{padding:7px 10px;font-size:.82rem}
 main{padding:22px 18px 48px}
 .hero{margin:0 0 32px;padding:28px 23px;border-radius:23px}
 .hero:after{right:-185px;bottom:-245px;width:330px;height:330px}
 .hero h1{font-size:clamp(2.05rem,9vw,3.1rem)}
 .hero p{font-size:1rem}
 h2{margin:36px 0 16px}
 .grid{grid-template-columns:repeat(auto-fit,minmax(min(100%,235px),1fr));gap:13px}
 .card{min-height:132px;padding:19px;border-radius:17px}
 main:has(>p:first-child a){padding-top:25px}
 footer{padding:21px 18px 28px}
}
@media(max-width:360px){
 header{align-items:flex-start;flex-direction:column}
 header>a:last-child{align-self:flex-start}
 .hero{padding:25px 19px}
}"""
 def page(title,desc,path,body,ld=None,template_name=None):
  template_name=template_name or ('index' if path=='/' else 'compare' if path=='/compare.html' else 'provider' if path.startswith('/providers/') else 'coupon' if path=='/contabo-coupon-code.html' else 'deal')
  template=(R/'templates'/f'{template_name}.html').read_text(encoding='utf8')
  schema='<script type="application/ld+json">'+json.dumps(ld,ensure_ascii=False).replace('<','\\u003c')+'</script>' if ld else ''
  values={'TITLE':title,'DESCRIPTION':desc,'CANONICAL':base+path,'STYLE':css,'JSONLD':schema,'BRAND':c['brand'],'BODY':body}
  for key,value in values.items():template=template.replace('{{'+key+'}}',e(value) if key in ('TITLE','DESCRIPTION','CANONICAL','BRAND') else value)
  template=re.sub(rf'({re.escape(base)})(/[^"\'<>\s?#]+)\.html(?=[?"\'<>\s#])',r'\1\2',template)
  template=re.sub(r'(?<![A-Za-z0-9:/])(/[^"\'<>\s?#]+)\.html(?=[?"\'<>\s#])',r'\1',template)
  tool_script='''<script>(()=>{const c=document.modelContext;if(!c?.registerTool)return;const api="/api/agent/articles";c.registerTool({name:"search_vps_articles",description:"Search Lumafare's public VPS deal and evaluation articles. Return source links and dates; unknown details remain unknown.",inputSchema:{type:"object",properties:{query:{type:"string",description:"Search words from a VPS hosting question"},limit:{type:"integer",minimum:1,maximum:10}},required:["query"]},execute:async({query,limit})=>{const u=new URL(api,location.origin);u.searchParams.set("q",query);if(limit)u.searchParams.set("limit",String(limit));const r=await fetch(u);if(!r.ok)throw new Error("Article search unavailable");return await r.json()}});c.registerTool({name:"read_vps_article",description:"Read one public Lumafare article by its exact slug. Do not infer unpublished facts.",inputSchema:{type:"object",properties:{slug:{type:"string",pattern:"^[a-z0-9]+(?:-[a-z0-9]+)*$"}},required:["slug"]},execute:async({slug})=>{const u=new URL(api,location.origin);u.searchParams.set("slug",slug);const r=await fetch(u);if(!r.ok)throw new Error(r.status===404?"Article not found":"Article read unavailable");return await r.json()}})})()</script>'''
  template=template.replace('</body>',tool_script+'</body>')
  return template
 def card(o):
  if o.get('status','active')!='active':return ''
  path='/deals/'+quote(o.get('page_slug') or slug(o.get('provider','')+' '+o.get('title','')))+'.html'
  provider=next((p for p in c['providers'] if p['name']==o.get('provider')), {})
  destination=provider.get('affiliate_url') or o.get('offer_url','#')
  link_label='Visit provider ↗' if provider.get('affiliate_url') else 'Official offer page ↗'
  price=f'<p>{e(o["currency"])} {e(o["price"])}{e("/"+o["price_period"]) if o.get("price_period") else ""}</p>' if o.get('price') and o.get('currency') else '<p>Currently no verified price available.</p>'
  return f'<article class="card"><small>{e(o.get("provider","Provider"))}</small><h3><a href="{path}">{e(o.get("title","Official offer"))}</a></h3>{price}<a href="{e(destination)}" rel="{'sponsored nofollow' if provider.get('affiliate_url') else 'nofollow'}">{link_label}</a></article>'
 def details(items=(),source_links=()):
  sources=source_links or sorted({o.get('source_url') for o in items if o.get('source_url')})
  source_html=', '.join(f'<a href="{e(u)}">{e(u)}</a>' for u in sources) if sources else 'First-party site information.'
  uncertain='No additional plan terms are verified here; confirm current terms on the linked official page.' if items else 'No additional details are asserted on this page.'
  return f'<section class="page-details"><h2>Verification details</h2><p><strong>Source scan run:</strong> {e(site_check_at)}</p><p><strong>Source page:</strong> {source_html}</p><p><strong>Update cadence:</strong> {e(c["updates_every"])}</p><p><strong>Unconfirmed items:</strong> {uncertain}</p></section>'
 providers_html=''.join(f'<article class="card"><h3><a href="/providers/{slug(p["name"])}">{e(p["name"])}</a></h3><a href="{e(p["source_url"])}">Official source ↗</a></article>' for p in c['providers'])
 home_sources=[p['source_url'] for p in c['providers']]
 coupon_guides_html=''.join(f'<article class="card"><h3><a href="/{e(g["slug"])}">{e(g["name"])} coupon code</a></h3><p>Check what could be confirmed from official sources.</p><a href="/{e(g["slug"])}">Read the source check ↗</a></article>' for g in c['coupon_guides'])
 coupon_guides_section=f'<h2>Coupon code checks</h2><section class="grid">{coupon_guides_html}</section>' if coupon_guides_html else ''
 articles=article_records()
 articles_section=('''<h2>Latest articles</h2><section class="grid">'''+''.join(f'<article class="card"><small>{e(a["date"])}</small><h3><a href="/articles/{e(a["slug"])}/">{e(a["title"])}</a></h3><p>{e(a["description"])}</p></article>' for a in articles)+'''</section>''') if articles else ''
 body=f'<main><section class="hero"><p>Independent VPS directory · {scan_time:%B %Y}</p><h1>VPS deals, checked at the source.</h1><p>Official provider promotion links. No invented prices or expired claims.</p></section><h2>Providers</h2><section class="grid">{providers_html}</section>{coupon_guides_section}{articles_section}{details(source_links=home_sources)}</main>'
 urls=['/','/compare.html'];item={'@context':'https://schema.org','@type':'ItemList','itemListElement':[{'@type':'ListItem','position':i+1,'url':base+'/providers/'+slug(p['name'])} for i,p in enumerate(c['providers'])]}
 (OUT/'index.html').write_text(page(f'{c["brand"]} — VPS deals directory','Official VPS provider promotion links.','/',body,item),encoding='utf8')
 body='<main><h1>Compare VPS providers</h1><p>This directory compares providers using the same dimensions where their official pages publish them: plan price and billing terms, vCPU, RAM, storage, bandwidth, and included features. Details can vary by region and checkout term, so each card links to the provider’s official plans for current terms.</p><section class="grid">'+''.join(f'<article class="card"><h2>{e(p["name"])}</h2><p>Compare published pricing, billing terms, compute, memory, storage, bandwidth, and included features.</p><a href="/providers/{slug(p["name"])}">View our {e(p["name"])} page ↗</a><a href="{e(p["source_url"])}">Verify on official plans ↗</a></article>' for p in c['providers'])+'</section>'+details(source_links=[p['source_url'] for p in c['providers']])+'</main>'
 ld={'@context':'https://schema.org','@type':'ItemList','itemListElement':[{'@type':'ListItem','position':i+1,'url':base+'/providers/'+slug(p['name'])+'.html'} for i,p in enumerate(c['providers'])]}
 (OUT/'compare.html').write_text(page('Compare VPS providers | '+c['brand']+' · '+f'{scan_time:%B %Y}','Compare VPS providers at official plan pages.','/compare.html',body,ld),encoding='utf8')
 for p in c['providers']:
  s=slug(p['name']);path='/providers/'+s+'.html';urls.append(path);(OUT/'providers').mkdir(exist_ok=True)
  provider_offers=[o for o in offers if o.get('provider')==p['name']]
  if p['name']=='Hostinger':
   plans=[]
   for o in provider_offers:
    plan_id='plan-'+(o.get('page_slug') or slug(o.get('provider','')+' '+o.get('title','')))
    specs=''.join(f'<li>{e(k)}: {e(v)}</li>' for k,v in o.get('specs',{}).items())
    price=f'<p>{e(o["currency"])} {e(o["price"])}{e("/"+o["price_period"]) if o.get("price_period") else ""}</p>' if o.get('price') and o.get('currency') else '<p>Currently no verified price available.</p>'
    discount=f'<p>Officially displayed discount: {e(o["discount"])} off.</p>' if o.get('discount') else ''
    checked=site_check_at
    price_note='<p>The provider states that plans are paid upfront; the monthly rate is the total plan price divided by the number of months.</p>' if o.get('price_period') else ''
    plans.append(f'<article class="card plan" id="{e(plan_id)}"><h3>{e(o.get("title","Official offer"))}</h3>{discount}{price_note}{price}<p>Plan specifications published on the official page:</p><ul>{specs}</ul><p>Prices and availability can change. Confirm the total and current terms with the provider before purchasing.</p><p><a href="{e(o.get("offer_url",p["source_url"]))}" rel="nofollow">Open official provider source ↗</a></p><section class="plan-details"><h4>Verification details</h4><p><strong>Source scan run:</strong> {e(checked)}</p><p><strong>Source page:</strong> <a href="{e(o.get("source_url",p["source_url"]))}">{e(o.get("source_url",p["source_url"]))}</a></p><p><strong>Update cadence:</strong> {e(c["updates_every"])}</p><p><strong>Unconfirmed items:</strong> No additional plan terms are verified here; confirm current terms on the linked official page.</p></section></article>')
   plan_content='<h2>Promotion links</h2><section class="grid">'+''.join(plans)+'</section>'
  else:
   plan_content='<h2>Promotion links</h2><section class="grid">'+''.join(card(o) for o in provider_offers)+'</section>'
  siblings=''.join(f'<a href="/providers/{slug(q["name"])}">{e(q["name"])}</a>' for q in c['providers'] if q['name']!=p['name'])
  b=f'<main><nav class="crumbs"><a href="/">Home</a> › <span>{e(p["name"])} VPS</span></nav><h1>{e(p["name"])} VPS</h1><p>See current plans and promotions on the official provider page.</p><p><a href="{e(p["source_url"])}">Official source ↗</a></p>{plan_content}<h2>Other providers in this directory</h2><nav class="siblings">{siblings}<a href="/compare">Compare all providers</a></nav>{details(provider_offers, [p["source_url"]])}</main>'
  provider_ld={'@context':'https://schema.org','@graph':[{'@type':'Product','name':p['name']+' VPS hosting','brand':{'@type':'Brand','name':p['name']},'url':p['url']},{'@type':'BreadcrumbList','itemListElement':[{'@type':'ListItem','position':1,'name':'Home','item':base+'/'},{'@type':'ListItem','position':2,'name':p['name'],'item':base+path.replace('.html','')}]}]}
  (OUT/'providers'/f'{s}.html').write_text(page(p['name']+' VPS offers | '+c['brand']+' · '+f'{scan_time:%B %Y}','Official source links for '+p['name']+'.',path,b,provider_ld),encoding='utf8')
 for guide in c['coupon_guides']:
  path='/'+guide['slug']+'.html';urls.append(path);checked=site_check_at
  sources=guide['sources'];source_links=' · '.join(f'<a href="{e(u)}">Official source ↗</a>' for u in sources)
  help_source='https://help.contabo.com/en/support/solutions/articles/103000327514-how-can-i-get-a-refund-'
  coupon_answer='No Contabo-issued coupon code could be verified during this review, so no code is listed. This means only that this review did not verify a public code; it is not a claim that no code exists.'
  refund_answer='Contabo Support says a private account may request revocation within 14 days of purchase; domains are excluded. A renewal payment made within the last 72 hours may also be eligible. Contact Contabo Support for eligibility and instructions.'
  body=(f'<main><nav class="crumbs"><a href="/">Home</a> › <span>Contabo Coupon Code</span></nav><section class="hero"><p>Official-source check · {e(checked)}</p><h1>Contabo Coupon Code</h1><p><strong>Looking for a Contabo coupon code?</strong> {e(coupon_answer)}</p><p><a href="https://contabo.com/en/" rel="nofollow">Check Contabo official offers ↗</a></p></section>'
        '<h2>Official offer check</h2><div class="table-wrap"><table class="verification-table"><thead><tr><th>Offer or term</th><th>How to get it</th><th>Official source</th><th>Source scan run</th></tr></thead><tbody>'
        f'<tr><td>Public coupon code</td><td>No code was verified in this review; no code is supplied here. Check Contabo directly for any current offer.</td><td>{source_links}</td><td>{e(checked)}</td></tr>'
        f'<tr><td>Refund and withdrawal terms</td><td>{e(refund_answer)}</td><td><a href="{e(help_source)}">Contabo Support: refund eligibility ↗</a></td><td>{e(checked)}</td></tr>'
        '</tbody></table></div><h2>What remains unconfirmed</h2><p>Contabo’s official product and pricing pages returned a security check or 403 during this review. Current coupon-code availability, shipping terms, membership discounts, and subscription discounts could not be confirmed; none are claimed here. Check the linked official pages before ordering.</p>'
        '<h2>Frequently asked questions</h2><h3>Does Contabo have a coupon code?</h3><p>'+e(coupon_answer)+'</p>'
        '<h3>How can I check or redeem a current offer?</h3><p>Use Contabo’s official website and verify the offer terms in the order flow. This page does not provide third-party codes.</p>'
        '<h3>What does Contabo say about refunds?</h3><p>'+e(refund_answer)+' <a href="'+e(help_source)+'">Read Contabo’s official refund guidance ↗</a></p>'
        f'<section class="page-details"><h2>Verification details</h2><p><strong>Source scan run:</strong> {e(checked)}</p><p><strong>Official pages checked:</strong> {source_links} · <a href="{e(help_source)}">Refund guidance ↗</a></p><p><strong>Update cadence:</strong> {e(c["updates_every"])}</p><p><strong>Unconfirmed items:</strong> Current code-only campaigns, shipping terms, and account-specific subscription offers.</p></section></main>')
  guide_ld={'@context':'https://schema.org','@type':'FAQPage','mainEntity':[
   {'@type':'Question','name':'Does Contabo have a coupon code?','acceptedAnswer':{'@type':'Answer','text':coupon_answer}},
   {'@type':'Question','name':'How can I check or redeem a current offer?','acceptedAnswer':{'@type':'Answer','text':'Use Contabo’s official website and verify the offer terms in the order flow. This page does not provide third-party codes.'}},
   {'@type':'Question','name':'What does Contabo say about refunds?','acceptedAnswer':{'@type':'Answer','text':refund_answer}}
  ]}
  (OUT/f'{guide["slug"]}.html').write_text(page('Contabo Coupon Code: Official Offers Check | '+c['brand'], 'Check whether an official Contabo coupon code could be verified, and read Contabo’s official refund guidance.',path,body,guide_ld),encoding='utf8')
 # The four legacy deal URLs are preserved as redirects into their corresponding Hostinger plan sections.
 def info_page(path,title,description,content):
  body='<main><nav class="crumbs"><a href="/">Home</a> › <span>'+e(title)+'</span></nav>'+content+details()+'</main>'
  (OUT/f'{path}.html').write_text(page(title+' | '+c['brand'],description,'/'+path+'.html',body),encoding='utf8')
 info_page('about','About','How Lumafare gathers and presents VPS provider information.','<h1>About Lumafare</h1><p>Lumafare is an independent directory of VPS providers and publicly available offers. It links to providers’ own plan and promotion pages so readers can check current terms at the source.</p><h2>How listings are made</h2><p>The site configuration names each provider and its public official source. The refresh script reads public pages, respects the source site’s robots.txt, and records source URLs and retrieval times for information it can verify. It does not sign in, bypass access controls, or infer an offer when a source cannot be read.</p><p>Provider terms and availability can vary by region and checkout term. Verify them on the provider page before purchasing. Lumafare does not sell or operate the listed VPS services.</p>')
 contact_link=f'<a href="mailto:{e(c["contact_email"])}">{e(c["contact_email"])}</a>'
 info_page('privacy','Privacy','What information this static VPS directory processes.','<h1>Privacy</h1><p>Lumafare is a static information site. It has no visitor accounts, checkout, contact form, analytics, or advertising scripts.</p><p>Site hosting and delivery providers process ordinary request and connection data needed to deliver pages and protect the service under their own policies. Following a provider link takes you to that provider, which handles your visit under its own privacy policy.</p><p>The automated refresh process retrieves public provider pages and stores listing details, source URLs, and retrieval times in the project repository. It does not collect information from visitors through this site.</p><p>For a privacy question, email '+contact_link+'.</p>')
 info_page('contact','Contact','Contact Lumafare about directory accuracy or privacy.','<h1>Contact</h1><p>For corrections to a provider listing, questions about a source link, or privacy inquiries, email the site owner:</p><p><a href="mailto:'+e(c['contact_email'])+'">'+e(c['contact_email'])+'</a></p><p>Please identify the page and include the official provider URL that supports a correction.</p>')
 (OUT/'404.html').write_text(page('Page not found | '+c['brand'],'This page does not exist on Lumafare.','/404.html','<main><h1>Page not found</h1><p>The address does not match a page in this directory.</p><p><a href="/">Return to Lumafare home</a></p>'+details()+'</main>'),encoding='utf8')
 urls.extend(['/about.html','/privacy.html','/contact.html'])
 for article in articles:
  article_path='/articles/'+article['slug']+'/'
  article_dir=OUT/'articles'/article['slug'];article_dir.mkdir(parents=True,exist_ok=True)
  question=f'<p><strong>Question:</strong> {e(article["question"])}</p>' if article.get('question') else ''
  source_list=''.join(f'<li><a href="{e(source)}">{e(source)}</a></li>' for source in article['sources'])
  sources_html=f'<section><h2>Sources</h2><ul>{source_list}</ul></section>' if source_list else ''
  article_body=(f'<main><nav class="crumbs"><a href="/">Home</a> › <span>Articles</span></nav><article><h1>{e(article["title"])}</h1><p>{e(article["description"])}</p><p><small>Published: {e(article["date"])}</small></p>{question}{render_markdown(article["body"])}{sources_html}<section class="page-details"><h2>Verification details</h2><p><strong>Source scan run:</strong> {e(site_check_at)}</p></section></article></main>')
  (article_dir/'index.html').write_text(page(article['title']+' | '+c['brand'],article['description'],article_path,article_body,template_name='article'),encoding='utf8')
  urls.append(article_path)
 # Sitemap lastmod uses the exact same source scan instant shown on every page.
 stamp=scan_time.isoformat(timespec='seconds').replace('+00:00','Z')
 (OUT/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+''.join(f'<url><loc>{e(base+x.removesuffix(".html"))}</loc><lastmod>{stamp}</lastmod></url>\n' for x in urls)+'</urlset>\n',encoding='utf8')
 redirects=[];emitted=set()
 def add_redirect(old,target):
  # One rule per legacy address: first writer wins, so pinned legacy targets are never shadowed.
  if old in emitted:return
  emitted.add(old)
  redirects.append(f'{old}.html {old} 308')
  redirects.append(f'{old} {base}{target} 301')
 # The scraper does not write page_slug, so generated deal slugs drift when offer titles change.
 # These five addresses are already published and indexed; they stay pinned to their plan anchors.
 for legacy,legacy_target in STATIC_LEGACY:add_redirect(legacy,legacy_target)
 for o in all_offers:
  old='/deals/'+quote(o.get('page_slug') or slug(o.get('provider','')+' '+o.get('title','')))
  target='/providers/'+slug(o.get('provider',''))+'#plan-'+(o.get('page_slug') or slug(o.get('provider','')+' '+o.get('title','')))
  add_redirect(old,target)
 (OUT/'_redirects').write_text('\n'.join(redirects)+'\n',encoding='utf8')
 (OUT/'robots.txt').write_text(f'User-agent: *\nAllow: /\nContent-Signal: search=yes, ai-input=yes, ai-train=no\nSitemap: {base}/sitemap.xml\n',encoding='utf8')
 # Agent discovery is generated from the exact same article source as the visible article pages.
 public_articles=[{'slug':a['slug'],'title':a['title'],'description':a['description'],'question':a.get('question') or None,'date':a['date'],'sources':a['sources'],'url':base+'/articles/'+a['slug']+'/','body':a['body']} for a in articles]
 (OUT/'agent-articles.json').write_text(json.dumps({'articles':public_articles},ensure_ascii=False,separators=(',',':'))+'\n',encoding='utf8')
 (OUT/'ai').mkdir(exist_ok=True)
 (OUT/'ai'/'index.html').write_text('<!doctype html><html lang="en"><meta charset="utf-8"><title>Lumafare agent service</title><main><h1>Lumafare public article lookup</h1><p>This read-only service searches and reads published VPS deal and evaluation articles.</p><p>Use <a href="/openapi.json">the API contract</a>, <a href="/mcp">the MCP endpoint</a>, or <a href="/ai/skills/site-lookup/SKILL.md">the agent skill</a>. Search returns a bounded set. Read requires an exact published slug. Sources and publication dates are retained; unavailable facts remain unknown.</p></main></html>\n',encoding='utf8')
 (OUT/'ai'/'index.ilang').write_text('::ILANG\n[TYPE:agent-instructions][LANG:en]\nUse the Lumafare public article search/read service only. Preserve article identifiers, publication dates, qualifiers and source URLs. Answer in the visitor language and cite the relevant article. Do not infer missing prices, discounts, expirations or provider terms. If no published article supports a fact, say it is unknown.\n',encoding='utf8')
 skill='---\nname: site-lookup\ndescription: Search and read Lumafare public VPS deal and evaluation articles with source links.\n---\n# Lumafare site lookup\n\nUse the read-only search and read API for published articles. Keep identifiers, dates, qualifiers, and source URLs intact. Answer in the visitor language, cite the article URL, and state unknowns without filling gaps. Do not infer current prices, discounts, or expiry dates.\n\nSearch: `GET /api/agent/articles?q=<terms>&limit=<1..10>`\nRead: `GET /api/agent/articles?slug=<exact-slug>`\n'
 skill_bytes=skill.encode('utf8');skill_path=OUT/'ai'/'skills'/'site-lookup'/'SKILL.md';skill_path.parent.mkdir(parents=True,exist_ok=True);skill_path.write_bytes(skill_bytes)
 digest='sha256:'+hashlib.sha256(skill_bytes).hexdigest()
 (OUT/'.well-known'/'agent-skills').mkdir(parents=True,exist_ok=True)
 (OUT/'.well-known'/'agent-skills'/'index.json').write_text(json.dumps({'$schema':'https://schemas.agentskills.io/discovery/0.2.0/schema.json','skills':[{'name':'site-lookup','type':'skill-md','description':'Search and read public VPS articles with official sources.','url':base+'/ai/skills/site-lookup/SKILL.md','digest':digest}]},indent=2)+'\n',encoding='utf8')
 article_schema={
  'type':'object','required':['slug','title','description','date','sources','url','body'],
  'properties':{'slug':{'type':'string'},'title':{'type':'string'},'description':{'type':'string'},'question':{'type':['string','null']},'date':{'type':'string','format':'date'},'sources':{'type':'array','items':{'type':'string','format':'uri'}},'url':{'type':'string','format':'uri'},'body':{'type':'string'}}}
 search_schema={'type':'object','required':['query','count','results'],'properties':{
  'query':{'type':'string'},'count':{'type':'integer'},'results':{'type':'array','items':{'type':'object','required':['slug','title','description','url','published'],
   'properties':{'slug':{'type':'string'},'title':{'type':'string'},'description':{'type':'string'},'question':{'type':['string','null']},'url':{'type':'string','format':'uri'},'source_url':{'type':['string','null'],'format':'uri'},'published':{'type':'string','format':'date'}}}}}}
 error_schema={'type':'object','required':['error'],'properties':{'error':{'type':'string'},'slug':{'type':'string'},'max_length':{'type':'integer'}}}
 json_response=lambda schema:{'content':{'application/json':{'schema':schema}}}
 openapi={
  'openapi':'3.1.0','info':{'title':'Lumafare public article lookup','version':'1.0.0','description':'Read-only search and retrieval of published articles.'},'servers':[{'url':base}],
  'paths':{'/api/agent/articles':{'get':{
   'operationId':'searchOrReadArticles','summary':'Search published articles or read one by exact slug',
   'parameters':[{'name':'q','in':'query','description':'Search text; omit or leave empty for no results.','schema':{'type':'string','maxLength':200}},{'name':'slug','in':'query','description':'Exact published article slug. Takes precedence over q.','schema':{'type':'string','pattern':'^[a-z0-9]+(?:-[a-z0-9]+)*$'}},{'name':'limit','in':'query','description':'Maximum number of search results.','schema':{'type':'integer','minimum':1,'maximum':10,'default':5}}],
   'responses':{'200':{'description':'Search results or one article record.','content':{'application/json':{'schema':{'oneOf':[{'$ref':'#/components/schemas/SearchResponse'},{'$ref':'#/components/schemas/Article'}]}}}},'400':{'description':'Invalid slug or query length. **No article data is changed.**',**json_response({'$ref':'#/components/schemas/Error'})},'404':{'description':'Article slug not found.',**json_response({'$ref':'#/components/schemas/Error'})}}
  }}},
  'components':{'schemas':{'Article':article_schema,'SearchResponse':search_schema,'Error':error_schema}}
 }
 (OUT/'openapi.json').write_text(json.dumps(openapi,indent=2)+'\n',encoding='utf8')
 (OUT/'.well-known'/'api-catalog').write_text(json.dumps({'linkset':[{'anchor':base+'/api/agent/articles','service-desc':[{'href':base+'/openapi.json','type':'application/vnd.oai.openapi+json;version=3.1'}],'service-doc':[{'href':base+'/ai/','type':'text/html'}]}]},indent=2)+'\n',encoding='utf8')
 construction={'status':'under_construction','available':False,'capabilities_status':'planned_contract_only','message':'Coming soon; authentication is not available. Public article lookup remains available without authentication.','launch_date':None,'issuer':base,'authorization_endpoint':base+'/agent-auth/authorize','token_endpoint':base+'/agent-auth/token','jwks_uri':base+'/.well-known/jwks.json','grant_types_supported':['authorization_code','urn:ietf:params:oauth:grant-type:jwt-bearer'],'response_types_supported':['code'],'code_challenge_methods_supported':['S256'],'scopes_supported':['site:read'],'agent_auth':{'status':'under_construction','available':False,'capabilities_status':'planned_contract_only','skill':base+'/auth.md','register_uri':base+'/agent-auth/register','claim_uri':base+'/agent-auth/claim','identity_types_supported':['anonymous'],'anonymous':{'status':'under_construction','available':False,'capabilities_status':'planned_contract_only','credential_types_supported':['access_token'],'claim_uri':base+'/agent-auth/claim'}}}
 (OUT/'.well-known'/'oauth-authorization-server').write_text(json.dumps(construction,indent=2)+'\n',encoding='utf8')
 prm={'status':'under_construction','available':False,'capabilities_status':'planned_contract_only','message':'Coming soon. Existing public lookup remains available without authentication.','launch_date':None,'resource':base,'planned_resource_endpoint':base+'/agent-auth/resource','authorization_servers':[base],'scopes_supported':['site:read'],'bearer_methods_supported':['header']}
 (OUT/'.well-known'/'oauth-protected-resource').write_text(json.dumps(prm,indent=2)+'\n',encoding='utf8')
 (OUT/'.well-known'/'jwks.json').write_text(json.dumps({'status':'under_construction','available':False,'keys':[]},indent=2)+'\n',encoding='utf8')
 (OUT/'auth.md').write_text(f'''# auth.md

## Authentication status

status: under_construction
available: false
capabilities_status: planned_contract_only

Authentication, account creation, and token issuance are not available. The public article lookup remains usable without signing in.

## Agent Registration

Registration endpoint: `{base}/agent-auth/register`
register_uri: `{base}/agent-auth/register`
registration_status: under_construction
registration_available: false

The planned anonymous registration method is described by these fields:

```json
{{
  "register_uri": "{base}/agent-auth/register",
  "claim_uri": "{base}/agent-auth/claim",
  "identity_types_supported": ["anonymous"],
  "anonymous": {{
    "credential_types_supported": ["access_token"],
    "claim_uri": "{base}/agent-auth/claim"
  }}
}}
```

Anonymous agent registration is a future design only. While `available` is `false`, do not call the registration or claim endpoint or attempt to create an identity. The reserved endpoints currently return HTTP 503 and do not store submitted data, create accounts, issue credentials, or start an authorization flow. No login or token exchange is active.

## Available public service

The read-only article lookup works without authentication. See the [API contract](/openapi.json), [agent instructions](/ai/), and [public article search and read endpoint](/api/agent/articles).
''',encoding='utf8')
 (OUT/'.well-known'/'mcp').mkdir(parents=True,exist_ok=True)
 mcp_card={'name':'com.lumafare/articles','title':'Lumafare public article lookup','description':'Read-only search and retrieval of published Lumafare VPS articles.','version':'1.0.0','serverInfo':{'name':'com.lumafare/articles','version':'1.0.0'},'supportedVersions':['2025-11-25'],'remotes':[{'type':'streamable-http','url':base+'/mcp'}],'capabilities':{'tools':{'listChanged':False}}}
 (OUT/'.well-known'/'mcp'/'server-card.json').write_text(json.dumps(mcp_card,indent=2)+'\n',encoding='utf8')
 (OUT/'mcp').mkdir(exist_ok=True)
 (OUT/'mcp'/'server-card').write_text(json.dumps(mcp_card,indent=2)+'\n',encoding='utf8')
 (OUT/'.well-known'/'agent-card.json').write_text(json.dumps({'name':'Lumafare public article lookup','description':'Read-only search and retrieval of published Lumafare VPS articles.','supportedInterfaces':[{'url':base+'/a2a','protocolBinding':'JSONRPC','protocolVersion':'1.0'}],'provider':{'url':base},'version':'1.0.0','capabilities':{'streaming':False,'pushNotifications':False,'stateTransitionHistory':False},'securitySchemes':{},'securityRequirements':[],'defaultInputModes':['text/plain'],'defaultOutputModes':['text/plain'],'skills':[{'id':'site-lookup','name':'Public article lookup','description':'Search or read published VPS articles and return source URLs.','tags':['articles','VPS'],'examples':['Find articles about comparing VPS plans','Read an article by exact slug']}],'signatures':[]},indent=2)+'\n',encoding='utf8')
 ard={'specVersion':'1.0','host':{'displayName':'Lumafare','identifier':'did:web:lumafare.com'},'entries':[{'identifier':'urn:air:lumafare.com:api:articles','displayName':'Article lookup API','type':'application/vnd.oai.openapi+json;version=3.1','url':base+'/openapi.json','representativeQueries':['Find articles about VPS billing terms']},{'identifier':'urn:air:lumafare.com:mcp:articles','displayName':'Lumafare article lookup MCP server','type':'application/mcp-server-card+json','url':base+'/mcp/server-card','representativeQueries':['Search public VPS articles']},{'identifier':'urn:air:lumafare.com:a2a:articles','displayName':'Lumafare public article agent','type':'application/json','url':base+'/.well-known/agent-card.json','representativeQueries':['Read a public article by exact slug']},{'identifier':'urn:air:lumafare.com:skill:site-lookup','displayName':'Site lookup skill','type':'text/markdown','url':base+'/ai/skills/site-lookup/SKILL.md','representativeQueries':['Find and cite a public VPS article']}]}
 (OUT/'.well-known'/'ai-catalog.json').write_text(json.dumps(ard,indent=2)+'\n',encoding='utf8')
 (OUT/'_headers').write_text('''/\n  Link: <https://lumafare.com/.well-known/api-catalog>; rel="api-catalog"; type="application/linkset+json", <https://lumafare.com/openapi.json>; rel="service-desc"; type="application/vnd.oai.openapi+json", <https://lumafare.com/ai/>; rel="service-doc"; type="text/html"\n\n/.well-known/*\n  Access-Control-Allow-Origin: *\n\n/.well-known/ai-catalog.json\n  Content-Type: application/ai-catalog+json; charset=utf-8\n\n/.well-known/api-catalog\n  Content-Type: application/linkset+json; profile="https://www.rfc-editor.org/info/rfc9727"; charset=utf-8\n\n/.well-known/oauth-authorization-server\n  Content-Type: application/json; charset=utf-8\n\n/.well-known/oauth-protected-resource\n  Content-Type: application/json; charset=utf-8\n\n/.well-known/jwks.json\n  Content-Type: application/jwk-set+json; charset=utf-8\n\n/.well-known/agent-card.json\n  Content-Type: application/json; charset=utf-8\n\n/.well-known/agent-skills/index.json\n  Content-Type: application/json; charset=utf-8\n\n/.well-known/mcp/*\n  Content-Type: application/mcp-server-card+json; charset=utf-8\n\n/mcp/server-card\n  Access-Control-Allow-Origin: *\n  Content-Type: application/mcp-server-card+json; charset=utf-8\n\n/openapi.json\n  Access-Control-Allow-Origin: *\n  Content-Type: application/vnd.oai.openapi+json;version=3.1\n\n/auth.md\n  X-Robots-Tag: noindex\n\n/.well-known/oauth-authorization-server\n  X-Robots-Tag: noindex\n\n/.well-known/oauth-protected-resource\n  X-Robots-Tag: noindex\n\n/.well-known/jwks.json\n  X-Robots-Tag: noindex\n''',encoding='utf8')
 print(f'Built {len(urls)} canonical pages; consolidated {len(redirects)} offer sections; agent article records: {len(public_articles)}')
if __name__=='__main__':main()
