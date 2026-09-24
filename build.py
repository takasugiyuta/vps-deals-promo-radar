# ILANG: static builder; reads brand and providers from .ilang/site.ilang.
# ILANG: omit unknown offer prices and dates from page content and structured data.
import html,json,re,shutil
from datetime import datetime,timezone
from pathlib import Path
from urllib.parse import quote
R=Path(__file__).parent;OUT=R/'site'
def cfg():
 c={'providers':[],'discovery':[],'brand':'vps-deals','niche':'VPS hosting deals','domain':'https://vps-deals-promo-radar.pages.dev'};sec=''
 for raw in (R/'.ilang/site.ilang').read_text(encoding='utf8').splitlines():
  s=raw.strip()
  if s.startswith('::STATE'):c.update({k:v.strip() for k,v in re.findall(r'(brand|niche|domain|locale):([^,}]+)',s)})
  elif s.startswith('::MODULE{PROVIDERS'):sec='providers'
  elif s.startswith('::MODULE{DISCOVERY'):sec='discovery'
  elif s.startswith('::MODULE{'):sec=''
  elif sec and '|' in s and not s.startswith('::'):
   p=[x.strip() for x in s.split('|')]
   if len(p)>=3:c[sec].append({'name':p[0],'url':p[1],'source_url':p[2],'affiliate_url':p[3] if len(p)>3 else ''})
 if not c['providers']:c['providers']=c['discovery']
 return c
def e(x):return html.escape(str(x),quote=True)
def slug(s):return re.sub(r'[^a-z0-9]+','-',s.lower()).strip('-')[:90] or 'offer'
def main():
 c=cfg();
 if OUT.resolve().parent!=R.resolve():raise RuntimeError('Refusing to clean output outside project root')
 if OUT.exists():shutil.rmtree(OUT)
 d=json.loads((R/'data/offers.json').read_text(encoding='utf8')) if (R/'data/offers.json').exists() else {'offers':[]};today=datetime.now(timezone.utc).date().isoformat();offers=[o for o in d.get('offers',[]) if o.get('status')!='unverified' and (not o.get('valid_until') or o['valid_until']>=today)];base=c['domain'].rstrip('/');OUT.mkdir(exist_ok=True)
 css='body{max-width:1050px;margin:auto;padding:24px;background:#f4f6fb;color:#162139;font:16px/1.6 system-ui}a{color:#3157c8}.hero,.card{padding:22px;margin:14px 0;background:white;border:1px solid #e2e6ef;border-radius:16px}.hero{background:#e7edff;padding:48px}.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:12px}'
 def page(title,desc,path,body,ld=None):
  template_name='index' if path=='/' else 'compare' if path=='/compare.html' else 'provider' if path.startswith('/providers/') else 'deal'
  template=(R/'templates'/f'{template_name}.html').read_text(encoding='utf8')
  schema='<script type="application/ld+json">'+json.dumps(ld,ensure_ascii=False).replace('<','\\u003c')+'</script>' if ld else ''
  values={'TITLE':title,'DESCRIPTION':desc,'CANONICAL':base+path,'STYLE':css,'JSONLD':schema,'BRAND':c['brand'],'BODY':body}
  for key,value in values.items():template=template.replace('{{'+key+'}}',e(value) if key in ('TITLE','DESCRIPTION','CANONICAL','BRAND') else value)
  return template
 def card(o):
  if o.get('status')=='unverified':return ''
  path='/deals/'+quote(slug(o.get('provider','')+' '+o.get('title','')))+'.html'
  provider=next((p for p in c['providers'] if p['name']==o.get('provider')), {})
  destination=provider.get('affiliate_url') or o.get('offer_url','#')
  link_label='Visit provider ↗' if provider.get('affiliate_url') else 'Official offer page ↗'
  price=f'<p>{e(o["currency"])} {e(o["price"])}</p>' if o.get('price') and o.get('currency') else ''
  return f'<article class="card"><small>{e(o.get("provider","Provider"))}</small><h3><a href="{path}">{e(o.get("title","Official offer"))}</a></h3>{price}<a href="{e(destination)}" rel="{'sponsored nofollow' if provider.get('affiliate_url') else 'nofollow'}">{link_label}</a></article>'
 offershtml=''.join(card(o) for o in offers) or '<article class="card"><h2>No verified promotion links found yet</h2><p>We only list explicit promotion links found on provider pages. Check providers directly for current pricing.</p></article>'
 body=f'<main><section class="hero"><p>Independent VPS directory · {datetime.now(timezone.utc):%B %Y}</p><h1>VPS deals, checked at the source.</h1><p>Official provider promotion links. No invented prices or expired claims.</p></section><h2>Latest official offers</h2><section class="grid">{offershtml}</section><h2>Providers</h2><section class="grid">'+''.join(f'<article class="card"><h3><a href="/providers/{slug(p["name"])}.html">{e(p["name"])}</a></h3><a href="{e(p["source_url"])}">Official source ↗</a></article>' for p in c['providers'])+'</section></main>'
 urls=['/','/compare.html'];item={'@context':'https://schema.org','@type':'ItemList','itemListElement':[{'@type':'ListItem','position':i+1,'url':base+'/deals/'+quote(slug(o.get('provider','')+' '+o.get('title','')))+'.html'} for i,o in enumerate(offers)]}
 (OUT/'index.html').write_text(page(f'{c["brand"]} — VPS deals {datetime.now(timezone.utc):%B %Y}','Official VPS provider promotion links.','/',body,item),encoding='utf8')
 body='<main><h1>Compare VPS providers</h1><p>Compare plans on official provider pages; prices vary by region and billing term.</p><section class="grid">'+''.join(f'<article class="card"><h2>{e(p["name"])}</h2><a href="{e(p["source_url"])}">Official plans and offers ↗</a></article>' for p in c['providers'])+'</section></main>'
 ld={'@context':'https://schema.org','@type':'ItemList','itemListElement':[{'@type':'ListItem','position':i+1,'url':base+'/providers/'+slug(p['name'])+'.html'} for i,p in enumerate(c['providers'])]}
 (OUT/'compare.html').write_text(page('Compare VPS providers | '+c['brand']+' · '+datetime.now(timezone.utc).strftime('%B %Y'),'Compare VPS providers at official plan pages.','/compare.html',body,ld),encoding='utf8')
 for p in c['providers']:
  s=slug(p['name']);path='/providers/'+s+'.html';urls.append(path);(OUT/'providers').mkdir(exist_ok=True)
  b=f'<main><p><a href="/">Home</a></p><h1>{e(p["name"])} VPS</h1><p>See current plans and promotions on the official provider page.</p><p><a href="{e(p["source_url"])}">Official source ↗</a></p><h2>Promotion links</h2><section class="grid">'+''.join(card(o) for o in offers if o.get('provider')==p['name'])+'</section></main>'
  provider_ld={'@context':'https://schema.org','@type':'Product','name':p['name']+' VPS hosting','brand':{'@type':'Brand','name':p['name']},'url':p['url']}
  (OUT/'providers'/f'{s}.html').write_text(page(p['name']+' VPS offers | '+c['brand']+' · '+datetime.now(timezone.utc).strftime('%B %Y'),'Official source links for '+p['name']+'.',path,b,provider_ld),encoding='utf8')
 for o in offers:
  if o.get('status')=='unverified':continue
  s=slug(o.get('provider','')+' '+o.get('title',''));path='/deals/'+quote(s)+'.html';urls.append(path);(OUT/'deals').mkdir(exist_ok=True)
  provider=next((x for x in c['providers'] if x['name']==o.get('provider')), {})
  target=provider.get('affiliate_url') or o.get('offer_url','#'); label='Continue to provider ↗' if provider.get('affiliate_url') else 'Open official provider source ↗'
  b=f'<main><p><a href="/">Home</a></p><h1>{e(o.get("title","Official offer"))}</h1><p>Confirm price, availability and terms on the original provider page.</p><p><a href="{e(target)}" rel="{'sponsored nofollow' if provider.get('affiliate_url') else 'nofollow'}">{label}</a></p></main>'
  ld=None
  if o.get('price') and o.get('currency'):
   ld={'@context':'https://schema.org','@type':'Offer','name':o.get('title'),'url':o.get('offer_url'),'price':o['price'],'priceCurrency':o['currency'],'availability':'https://schema.org/InStock'}
   if o.get('valid_until'):ld['priceValidUntil']=o['valid_until']
  (OUT/'deals'/f'{s}.html').write_text(page(o.get('title','Offer')+' | '+c['brand'],'Official '+o.get('provider','provider')+' offer source.',path,b,ld),encoding='utf8')
 stamp=(d.get('fetched_at') or datetime.now(timezone.utc).date().isoformat())[:10]
 (OUT/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+''.join(f'<url><loc>{e(base+x)}</loc><lastmod>{stamp}</lastmod></url>\n' for x in urls)+'</urlset>\n',encoding='utf8')
 (OUT/'robots.txt').write_text(f'User-agent: *\nAllow: /\nSitemap: {base}/sitemap.xml\n',encoding='utf8');print(f'Built {len(urls)} pages with {len(offers)} offer links')
if __name__=='__main__':main()
