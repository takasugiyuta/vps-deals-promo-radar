# ILANG: static builder; reads brand and providers from .ilang/site.ilang.
# ILANG: omit unknown offer prices and dates from page content and structured data.
import html,json,re,shutil
from datetime import datetime,timezone
from pathlib import Path
from urllib.parse import quote
R=Path(__file__).parent;OUT=R/'site'
def cfg():
 c={'providers':[],'discovery':[],'coupon_guides':[],'brand':'vps-deals','niche':'VPS hosting deals','domain':'https://vps-deals-promo-radar.pages.dev','contact_email':'','updates_every':'not specified'};sec=''
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
def main():
 c=cfg();
 if not c.get('contact_email') or '@' not in c['contact_email'] or not c['contact_email'].lower().endswith('@lumafare.com'):
  raise RuntimeError('Contact page requires the owner-provided, working @lumafare.com email address; no address was guessed.')
 if OUT.resolve().parent!=R.resolve():raise RuntimeError('Refusing to clean output outside project root')
 if OUT.exists():shutil.rmtree(OUT)
 d=json.loads((R/'data/offers.json').read_text(encoding='utf8')) if (R/'data/offers.json').exists() else {'offers':[]}
 if not d.get('source_scan_at'):raise RuntimeError('A completed scraper run is required; data/offers.json has no source_scan_at.')
 try:scan_time=datetime.fromisoformat(d['source_scan_at'].replace('Z','+00:00')).astimezone(timezone.utc)
 except ValueError as exc:raise RuntimeError('Invalid source_scan_at in data/offers.json.') from exc
 site_check_at=scan_time.isoformat(timespec='seconds');scan_date=scan_time.date().isoformat()
 today=datetime.now(timezone.utc).date().isoformat();all_offers=d.get('offers',[]);offers=[o for o in all_offers if o.get('status','active')=='active' and (not o.get('valid_until') or o['valid_until']>=today)];base=c['domain'].rstrip('/');OUT.mkdir(exist_ok=True)
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
 def page(title,desc,path,body,ld=None):
  template_name='index' if path=='/' else 'compare' if path=='/compare.html' else 'provider' if path.startswith('/providers/') else 'coupon' if path=='/contabo-coupon-code.html' else 'deal'
  template=(R/'templates'/f'{template_name}.html').read_text(encoding='utf8')
  schema='<script type="application/ld+json">'+json.dumps(ld,ensure_ascii=False).replace('<','\\u003c')+'</script>' if ld else ''
  values={'TITLE':title,'DESCRIPTION':desc,'CANONICAL':base+path,'STYLE':css,'JSONLD':schema,'BRAND':c['brand'],'BODY':body}
  for key,value in values.items():template=template.replace('{{'+key+'}}',e(value) if key in ('TITLE','DESCRIPTION','CANONICAL','BRAND') else value)
  template=re.sub(rf'({re.escape(base)})(/[^"\'<>\s?#]+)\.html(?=[?"\'<>\s#])',r'\1\2',template)
  template=re.sub(r'(?<![A-Za-z0-9:/])(/[^"\'<>\s?#]+)\.html(?=[?"\'<>\s#])',r'\1',template)
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
 body=f'<main><section class="hero"><p>Independent VPS directory · {datetime.now(timezone.utc):%B %Y}</p><h1>VPS deals, checked at the source.</h1><p>Official provider promotion links. No invented prices or expired claims.</p></section><h2>Providers</h2><section class="grid">{providers_html}</section>{coupon_guides_section}{details(source_links=home_sources)}</main>'
 urls=['/','/compare.html'];item={'@context':'https://schema.org','@type':'ItemList','itemListElement':[{'@type':'ListItem','position':i+1,'url':base+'/providers/'+slug(p['name'])} for i,p in enumerate(c['providers'])]}
 (OUT/'index.html').write_text(page(f'{c["brand"]} — VPS deals directory','Official VPS provider promotion links.','/',body,item),encoding='utf8')
 body='<main><h1>Compare VPS providers</h1><p>This directory compares providers using the same dimensions where their official pages publish them: plan price and billing terms, vCPU, RAM, storage, bandwidth, and included features. Details can vary by region and checkout term, so each card links to the provider’s official plans for current terms.</p><section class="grid">'+''.join(f'<article class="card"><h2>{e(p["name"])}</h2><p>Compare published pricing, billing terms, compute, memory, storage, bandwidth, and included features.</p><a href="/providers/{slug(p["name"])}">View our {e(p["name"])} page ↗</a><a href="{e(p["source_url"])}">Verify on official plans ↗</a></article>' for p in c['providers'])+'</section>'+details(source_links=[p['source_url'] for p in c['providers']])+'</main>'
 ld={'@context':'https://schema.org','@type':'ItemList','itemListElement':[{'@type':'ListItem','position':i+1,'url':base+'/providers/'+slug(p['name'])+'.html'} for i,p in enumerate(c['providers'])]}
 (OUT/'compare.html').write_text(page('Compare VPS providers | '+c['brand']+' · '+datetime.now(timezone.utc).strftime('%B %Y'),'Compare VPS providers at official plan pages.','/compare.html',body,ld),encoding='utf8')
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
  (OUT/'providers'/f'{s}.html').write_text(page(p['name']+' VPS offers | '+c['brand']+' · '+datetime.now(timezone.utc).strftime('%B %Y'),'Official source links for '+p['name']+'.',path,b,provider_ld),encoding='utf8')
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
 info_page('about','About Lumafare','How Lumafare gathers and presents VPS provider information.','<h1>About Lumafare</h1><p>Lumafare is an independent directory of VPS providers and publicly available offers. It links to providers’ own plan and promotion pages so readers can check current terms at the source.</p><h2>How listings are made</h2><p>The site configuration names each provider and its public official source. The refresh script reads public pages, respects the source site’s robots.txt, and records source URLs and retrieval times for information it can verify. It does not sign in, bypass access controls, or infer an offer when a source cannot be read.</p><p>Provider terms and availability can vary by region and checkout term. Verify them on the provider page before purchasing. Lumafare does not sell or operate the listed VPS services.</p>')
 contact_link=f'<a href="mailto:{e(c["contact_email"])}">{e(c["contact_email"])}</a>'
 info_page('privacy','Privacy','What information this static VPS directory processes.','<h1>Privacy</h1><p>Lumafare is a static information site. It has no visitor accounts, checkout, contact form, analytics, or advertising scripts.</p><p>Site hosting and delivery providers process ordinary request and connection data needed to deliver pages and protect the service under their own policies. Following a provider link takes you to that provider, which handles your visit under its own privacy policy.</p><p>The automated refresh process retrieves public provider pages and stores listing details, source URLs, and retrieval times in the project repository. It does not collect information from visitors through this site.</p><p>For a privacy question, email '+contact_link+'.</p>')
 info_page('contact','Contact','Contact Lumafare about directory accuracy or privacy.','<h1>Contact</h1><p>For corrections to a provider listing, questions about a source link, or privacy inquiries, email the site owner:</p><p><a href="mailto:'+e(c['contact_email'])+'">'+e(c['contact_email'])+'</a></p><p>Please identify the page and include the official provider URL that supports a correction.</p>')
 (OUT/'404.html').write_text(page('Page not found | '+c['brand'],'This page does not exist on Lumafare.','/404.html','<main><h1>Page not found</h1><p>The address does not match a page in this directory.</p><p><a href="/">Return to Lumafare home</a></p>'+details()+'</main>'),encoding='utf8')
 urls.extend(['/about.html','/privacy.html','/contact.html'])
 stamp=scan_date
 (OUT/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+''.join(f'<url><loc>{e(base+x.removesuffix(".html"))}</loc><lastmod>{stamp}</lastmod></url>\n' for x in urls)+'</urlset>\n',encoding='utf8')
 redirects=[]
 for o in all_offers:
  old='/deals/'+quote(o.get('page_slug') or slug(o.get('provider','')+' '+o.get('title','')))
  target='/providers/'+slug(o.get('provider',''))+'#plan-'+(o.get('page_slug') or slug(o.get('provider','')+' '+o.get('title','')))
  redirects.append(f'{old}.html {old} 308')
  redirects.append(f'{old} {base}{target} 301')
 # Legacy deal URL that no longer has a matching offer: keep the address alive with a 301 instead of letting it 404.
 for legacy,legacy_target in [('/deals/hostinger-student-discount','/providers/hostinger')]:
  redirects.append(f'{legacy}.html {legacy} 308')
  redirects.append(f'{legacy} {base}{legacy_target} 301')
 (OUT/'_redirects').write_text('\n'.join(redirects)+'\n',encoding='utf8')
 (OUT/'robots.txt').write_text(f'User-agent: *\nAllow: /\nSitemap: {base}/sitemap.xml\n',encoding='utf8');print(f'Built {len(urls)} canonical pages; consolidated {len(redirects)} offer sections')
if __name__=='__main__':main()
