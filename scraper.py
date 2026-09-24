# ILANG: scraper; uses .ilang/site.ilang as the only provider source configuration.
# ILANG: public official pages only, robots.txt respected, no invented deal or price fields.
import json,re,urllib.robotparser
from datetime import datetime,timezone
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin,urlparse
from urllib.request import Request,urlopen
from xml.etree import ElementTree as ET
ROOT=Path(__file__).parent

def config():
 c={'providers':[],'discovery':[],'brand':'vps-deals','niche':'VPS hosting deals','domain':'https://lumafare.com','locale':'en-US'}; section=''
 for line in (ROOT/'.ilang/site.ilang').read_text(encoding='utf8').splitlines():
  s=line.strip()
  if s.startswith('::STATE'):
   c.update({k:v.strip() for k,v in re.findall(r'(brand|niche|domain|locale):([^,}]+)',s)})
  elif s.startswith('::MODULE{PROVIDERS'): section='providers'
  elif s.startswith('::MODULE{DISCOVERY'): section='discovery'
  elif s.startswith('::MODULE{'): section=''
  elif section and '|' in s and not s.startswith('::'):
   p=[x.strip() for x in s.split('|')]
   if len(p)>=3:c[section].append({'name':p[0],'url':p[1],'source_url':p[2],'affiliate_url':p[3] if len(p)>3 else ''})
 if not c['providers']:c['providers']=c['discovery']
 return c
class Links(HTMLParser):
 def __init__(self): super().__init__();self.links=[];self.href=None;self.text=[];self.visible=[];self.hidden=0
 def handle_starttag(self,t,a):
  if t in ('script','style','noscript'):self.hidden+=1
  if t=='a':self.href=dict(a).get('href');self.text=[]
 def handle_data(self,d):
  if not self.hidden:self.visible.append(d)
  if self.href is not None:self.text.append(d)
 def handle_endtag(self,t):
  if t in ('script','style','noscript') and self.hidden:self.hidden-=1
  if t=='a' and self.href is not None:self.links.append((self.href,' '.join(' '.join(self.text).split())));self.href=None

def fetch(url):
 p=urlparse(url);robots=urllib.robotparser.RobotFileParser();robots.set_url(f'{p.scheme}://{p.netloc}/robots.txt')
 try:
  with urlopen(Request(robots.url,headers={'User-Agent':'VPSDealsRadarBot/1.0'}),timeout=12) as r:robots.parse(r.read().decode('utf8','replace').splitlines())
  if not robots.can_fetch('VPSDealsRadarBot',url):return ''
  with urlopen(Request(url,headers={'User-Agent':'VPSDealsRadarBot/1.0','Accept':'text/html'}),timeout=20) as r:
   if not any(kind in r.headers.get('Content-Type','').lower() for kind in ('html','xml','rss','atom','text/plain')):return ''
   return r.read(2000000).decode('utf8','replace')
 except Exception:return ''

def source_pages(source,provider):
 raw=fetch(source)
 if not raw:return []
 if 'html' in raw[:2000].lower():return [(source,raw)]
 try:root=ET.fromstring(raw)
 except ET.ParseError:return []
 urls=[]
 for node in root.iter():
  tag=node.tag.rsplit('}',1)[-1].lower()
  value=(node.text or '').strip() if tag in ('loc','link','guid') else node.attrib.get('href','').strip()
  if value.startswith(('http://','https://')) and urlparse(value).netloc==urlparse(provider['url']).netloc:
   if re.search(r'(deal|offer|promo|discount|coupon|special)',urlparse(value).path,re.I):urls.append(value)
 pages=[]
 for url in list(dict.fromkeys(urls))[:8]:
  content=fetch(url)
  if content:pages.append((url,content))
 return pages

def main():
 c=config();now=datetime.now(timezone.utc).isoformat(timespec='seconds');offers=[]
 old_path=ROOT/'data/offers.json'
 try: previous=json.loads(old_path.read_text(encoding='utf8')).get('offers',[])
 except Exception: previous=[]
 failed=set()
 for p in c['providers']:
  pages=source_pages(p['source_url'],p)
  if not pages:
   failed.add(p['name']);continue
  seen=set()
  for page_url,html in pages:
   parser=Links();parser.feed(html)
   for href,label in parser.links:
    target=urljoin(page_url,href)
    if label and re.search(r'\b(deal|offer|promo|discount|save|coupon|special)\b',label,re.I) and urlparse(target).netloc==urlparse(p['url']).netloc:
     key=(label,target)
     if key not in seen: offers.append({'provider':p['name'],'title':label[:240],'offer_url':target,'source_url':page_url,'fetched_at':now});seen.add(key)
   # Only emit a discount headline when that exact discount is visible on the provider page.
   visible=' '.join(' '.join(parser.visible).split())
   for match in re.finditer(r'(?i)(?:up to\s+)?(\d{1,2}\s*%\s*(?:off|discount|reduction|sale))',visible):
    percent=' '.join(match.group(1).split()); title=f'{percent} — {p["name"]} VPS page'
    key=(title,page_url)
    if key not in seen: offers.append({'provider':p['name'],'title':title,'offer_url':page_url,'source_url':page_url,'fetched_at':now});seen.add(key)
 for item in previous:
  if item.get('provider') in failed:item['status']='unverified';offers.append(item)
 out=ROOT/'data/offers.json';out.parent.mkdir(exist_ok=True);out.write_text(json.dumps({'fetched_at':now,'offers':offers},indent=2,ensure_ascii=False)+'\n',encoding='utf8');print(f'Saved {len(offers)} official offer records; {len(failed)} providers could not be verified')
if __name__=='__main__':main()
