ILANG
TYPE:project-guidance PROJECT:vps-deals-radar LANG:zh
::STATE{@PROJECT, purpose:Static VPS deal directory fed by official public provider pages}
::RULE{scraper.py and build.py read .ilang/site.ilang as sole brand and provider configuration}
::RULE{preserve source_url and fetched_at; omit unknown prices and expiry dates}
::BOUNDARY{never:invent offers prices discounts expirations or commission|scope:permanent}
::BOUNDARY{never:bypass robots.txt login walls rate limits or anti-bot controls|scope:permanent}
::BOUNDARY{never:add runtime inference APIs keys paid services or server components|scope:permanent}
::RULE{affiliate links require owner-supplied approved URLs and program terms}
::ALLOW{edit parsers templates styles workflow and .ilang config within these constraints}
