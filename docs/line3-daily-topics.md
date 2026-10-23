# 线三 · 每日三跑清单 (topic bank)

Single source for "tomorrow's article topic". Run all three every day, append one block
per day. Never pick a topic the morning of — take it from the newest block below.

Rules (locked):
1. One block per calendar day, newest at the bottom. A missing block = a broken cycle.
2. A: 原创内容邪修 — 3 entries min. Must be things rivals cannot copy without copying us.
3. B: 谷歌搜索查词 — 5 entries min, real queries actually run, with what the SERP showed.
4. C: 老外怎么说 — 5 entries min, real phrases used by English buyers/operators, with where.
5. Each block ends with `明日候选` — 1–3 concrete article titles pulled from that day's B + C.
6. Core word `vps deals` stays locked; long-tails orbit it, they do not replace it.

---

## 2026-10-07 (Day 1)

### A. 原创内容邪修

| # | 邪修点 | 为什么别人抄不走 |
|---|---|---|
| A1 | 五列判定表做成可复制的资产（workload fit / continuing bill / management tasks / recovery path / network or region limits）+ 三态标记 verified / unknown / does not fit | 是方法不是观点，抄就等于照搬我们的表格 |
| A2 | "计划卡 vs 结算页"字段差异记录：同一字段两处不一致时，以结算页为准并留证 | 需要真的去结算页走一遍，写手站不会做 |
| A3 | 每篇挂一份当日抓取的官方报价快照（我们自己的 offers.json + scan 时间戳） | 一手数据，别人没有同一个抓取管道 |
| A4 | 反着写：不问"哪家便宜"，问"哪个字段会先成为瓶颈" | 与所有榜单文的写法相反 |
| A5 | 日期化：每篇带 scan 时间戳，且正文里出现具体月份 | 常青文不敢带日期，带了就过期 |

### B. 谷歌搜索查词（今天真跑过的）

| query | SERP 上看到了什么 | 判断 |
|---|---|---|
| `vps deals` | 核心词，低质量聚合站多，官方页少 | 锁 28 天不动 |
| `compare vps deals total cost` | 有计算器站（smarterbuylab、toolrelief）在做"promo vs renewal" | 计算器是我们差异化点 |
| `vps renewal price vs promo price` | 大量中文站 + 少量英文计算器，英文深度文稀缺 | 可做 |
| `unmetered vs unlimited bandwidth vps` | vps-craft / lumovps 在讲，但都是中文 | 英文位空缺，可做 |
| `vps backup retention restore self-service` | HostAdvice / usavps / bitvps 都是泛讲 | 有缝，可做 |
| `cheap vps hosting deals` | lowendbox 首页占位 | 对标站主词，硬碰 |
| `vps deal tracker` | toolrelief 占位 | 功能型词，观察 |

### C. 老外怎么说（真在用的说法）

| phrase | 谁在用 / 什么意思 |
|---|---|
| "renews at $X" | LET/LEB 评论里说续费价的标准说法 |
| "recurring price" | 与 promo price 对立的说法 |
| "price locks in at renewal" | 续费同价（搬瓦工式机制）的英文说法 |
| "out of stock" | LEB 上套餐售罄的高频词，比"sold out"更常用 |
| "YABS" | Yet Another Benchmark Script，社区自己跑分的行话 |
| "provider went dark / went MIA" | 商家跑路、失联 |
| "oversold node" / "noisy neighbors" | 超售与邻居抢资源 |
| "FUP" / "stealth limits" | 公平使用政策 / 不明说的限速 |
| "sticker price vs all-in cost" | 标价 vs 全包成本，美式说法 |
| "unmanaged means you own the pager" | 非托管=你自己背告警 |

### 明日候选

1. **What "Renews at $X" Actually Means on a VPS Deal Page** — B3 + C1/C2/C3
2. **Unmetered vs Unlimited vs FUP: Reading a VPS Transfer Label** — B4 + C8
3. **The First Bottleneck Test: Which VPS Field Runs Out First for Your Workload** — A4

已用：`compare-vps-deals-total-cost`（总持有成本对比法，2026-10-07 已发布）

---

## 2026-10-08 (Day 2)

### A. 原创内容邪修

| # | 邪修点 | 为什么别人抄不走 |
|---|---|---|
| A1 | 拿我们自己的抓取失败清单做文章：本次 scan 里 Vultr、Linode(Akamai)、Contabo 三条官方定价页 `readable: false`，就写"这几个官方页我们现在抓不到，所以我们不报价，并说明怎么自己核" | 只有我们有这条每日 scan 的失败记录；商业站不会公开承认自己拿不到数据 |
| A2 | 同一官方页多折扣并存：Hostinger VPS 页一次抓出 70% / 67% / 65% / 63% 四条折扣，写"一个官方页面上同时出现四个折扣数字时该信哪个" | 需要同一时段的多条目抓取快照，写手站只有单一时刻的手抄价 |
| A3 | 反向写法：不评"哪家便宜"，评"哪个数字会在第 13 个月变"——把 VPS 当会涨价的订阅来算，而不是当一次性商品 | 与所有榜单/促销文写法相反，榜单站不敢这么写（会得罪广告主） |
| A4 | 标签词典：把 `unmetered port` / `unmetered inbound` / `5TB monthly outbound` / `1Gbps shared port` 四类标签各给一句"这句话到底承诺了什么"的判定句，每条挂当日 scan 时间戳 | 术语判定基于我们当天抓到的真实字段，别人只能泛泛解释 |
| A5 | 可复制的三问细字表：published cap 有没有 → limiting mechanism 是 throttling / overage / suspension 哪一种 → inbound 算不算，做成可直接抄走的表格 | 是工具不是观点，抄走就等于署名我们 |

### B. 谷歌搜索查词（今天真跑过的）

| query | SERP 上看到了什么 | 判断 |
|---|---|---|
| `vps deals` | 核心词。前 5 条里 4 条是中文聚合站（spacevps.cc、naibabiji、github 中文榜、vpsclub.cc），只有 vpsdeck.com 一个英文分类页 | 核心词锁 28 天不动；英文位仍是空的，说明英文内容供给不足而非需求不足 |
| `cheap vps deals reddit 2026` | HostAdvice 的 "Best Cheap VPS by Reddit" 占了主词+澳洲站两条，其余是中文聚合 | Reddit 意图被 HostAdvice 垄断，硬碰不划算；可作为素材不做主攻 |
| `vps promo price vs renewal price explained` | toolrelief 的续费计算器、hostingdive 的 "Hostinger 真实成本：promo vs renewal"，中文站一堆 | 英文深度文只有 2 篇，是最明显的空位 —— 主攻 |
| `lowendbox vps deal out of stock renews at` | LEB 首页+Best Cheap VPS 页占位，另有一条厂商 LET 专页（logicweb.com/vps-hosting/lowendbox-vps-promo） | 厂商自己也在做 "lowendbox/lowendtalk" 关键词，说明这批词有商业价值 |
| `vps fair use policy unmetered bandwidth fine print` | Cloudicts 的 FUP 条款页、affordablevpsserver 的 metered vs unmetered 长文、valebyte 的 TB vs unmetered | 英文位有内容但都停在"解释"，没人给判定表 —— 有缝，可做 |
| `best vps for self-hosted backups storage deals` | vpsnew / bestvpsproviders / selfhostable.dev 的实测文 | 需求真实但偏"选型"不偏"deal"，与本站核心词距离远 —— 暂缓 |

### C. 老外怎么说（真在用的说法）

| phrase | 谁在用 / 什么意思 |
|---|---|
| "renews at $49" | LowEndTalk 标题原文："$49/year, renews at $49"。买家写续费价的标准句式 |
| "$21.60/year ($48/year upon renewal)" | LowEndBox Best Cheap VPS 页原文（Godlike.Host）。"upon renewal" 是评测站标续费价的写法 |
| "lifetime discount" | LET 标题 "August 30% lifetime discount"：不是终身免费，是"之后每一期都打折" |
| "50% off your first payment, any billing term" | LET 标题。"any billing term" = 月付/年付都吃这个折扣；"first payment" = 只吃第一期 |
| "month-to-month" | LET 标题 "up to $180/mo, crypto, month-to-month"：不签长约，按月滚 |
| "1000 Mbps Unmetered Port" / "5TB Monthly Outbound Bandwidth" / "1Gbps Unmetered Inbound Bandwidth" | LEB 套餐字段原文。注意 inbound 单独写 unmetered、outbound 给死数字，是低价套餐的常见拆法 |
| "oversubscription on the host nodes" | LEB 正文原文（讲 OpenVZ）：超售的书面说法，比口语 "oversold" 更像评测站语气 |
| "Resident Host" | LEB 对长期在社区发帖、可被翻旧帖的商家的称呼，等于"有社区信用记录" |
| "LF" / "WTB" | LowEndTalk 求购区缩写 = Looking For / Want To Buy，帖子标题前缀 |
| "Restock" / "PRESALE" | LET/LEB 的库存语言："VPS Restock"、"DEDICATED SERVER PRESALE"，比 sold out 更常见 |
| "Exit Scam Alert / Scam Warning" | LET 板块名，商家跑路的正式说法 |
| "suspended me for 'high utilization'" | LET 标题原文：被以"高占用"为由停机，是 FUP 落地的真实场景 |
| "temporary speed reduction (throttling)" / "Throttled speeds generally reduce to 100 Mbps until the next billing reset" | Cloudicts FUP 条款页原文，厂商自己的限速措辞 |
| "sustained 100% port utilization" | Cloudicts FUP 原文：触发限速的判定条件写法 |
| "1Gbps down to 10Mbps" / "overage fees" / "soft limit" / "shared uplink" | affordablevpsserver 英文评测文里的细字四件套：限速幅度、超量费、软上限、共享上行 |

### 明日候选

1. **"Renews at $X": How VPS Deal Pages Hide Next Year's Price** — B3 + C1/C2/C4
2. **Unmetered Port, Metered Reality: Reading the Bandwidth Fine Print on Cheap VPS** — B4 + C6/C13/C15
3. **"Lifetime Discount" vs "First Payment": What a VPS Coupon Actually Renews At** — C3/C4/C5

已用：`compare-vps-deals-total-cost`（总持有成本对比法，2026-10-07 已发布）；`vps-deals-renews-at-x`（renews at $X 换算公式，2026-10-08 已发布）

剩余候选（未被消耗）：Unmetered Port, Metered Reality（B4 + C6/C13/C15）；"Lifetime Discount" vs "First Payment"（C3/C4/C5）

---

## 2026-10-09 (Day 3)

### A. 原创内容邪修

| # | 邪修点 | 为什么别人抄不走 |
|---|---|---|
| A1 | 公开自己的**抓取缺口地图**：本次 scan（`2026-10-08T18:33:22Z`）8 个官方 URL 里只有 3 个可读（Hostinger / Hetzner / DigitalOcean），Vultr、Linode (Akamai)、Contabo 三个全返回不可读。写成"这六家官方页我们今天抓到什么、没抓到什么、你自己怎么核"，并挂时间戳 | 商业站和榜单站永远不会公开自己拿不到哪几家的数据——那是自曝其短。只有每天真跑一遍抓取的站才有这张表 |
| A2 | Hetzner 官方首页抓出来的**唯一一条 offer 是 Server Auction（`/sb` 二手服务器拍卖）**，不是折扣。反向写：官方把"清库存"排在"做促销"前面，而所有榜单站只抄它家的常规套餐价，没人看它首页推的第一件事是什么 | 观察来自我们自己抓取到的 offer 顺序和内容，抄走就必须复制我们的抓取结果 |
| A3 | **"折扣条数 vs 套餐档位"数量不匹配检测**：Hostinger 一个官方页同时抓出 `70% / 67% / 65% / 63% off` 四条折扣 + 一条 `Student discount`，共 5 条 deal，但官方档位是 KVM 1/2/4/8 四个——必然有一条是叠加标注或重复计数。给读者一条可复制的核对动作（数 deal 条数、数档位数、不等就别信标签） | 是方法不是观点；需要同一时刻的多条目抓取快照，写手站只有单一时刻手抄的一个价 |
| A4 | **双管道交叉验证**：机器抓到的是"折扣标签"（offers.json 的 6 条），人工读官方页算出来的是"每 GB 单价"（$1.62–$9.00）。把两列并排放，不一致的地方就是选题——标签说便宜、单价说贵，就是该写的那篇 | 需要同时拥有抓取管道和人工核价两条线，竞品只有一条 |
| A5 | 反向写法：不写"今天有哪些 deal"，写"**这条 deal 在我们的时间线上活了几天**"。我们自 09-24 起每天 scan，`70%/67%/63%/65% off` 这组标签已连续出现多日；现在能诚实写的是"存活天数 + 方法"，不是"失效榜"——**至今零个真实失效事件**，这个事实本身就要写进正文 | 需要连续日期的抓取历史才敢说"活了几天"；单篇榜单文没有时间维度 |

### B. 谷歌搜索查词（今天真跑过的）

| query | SERP 上看到了什么 | 判断 |
|---|---|---|
| `vps deals` | **核心词**。前 5 条：vpsdeck.com 分类页（唯一英文）、spacevps.cc/deals、naibabiji、uvps.org/deals（23 小时前更新）、github 中文榜 topseo123/VPStuijian。4 条中文聚合 + 1 条英文分类页 | 核心词锁 28 天不动。连续两天同一格局：英文位仍只有分类页占位，说明是英文供给不足而非需求不足 |
| `vps hourly billing rate per hour convert to monthly cost` | racira 计算器、affordablevpsserver 的 "Per-Hour vs Monthly VPS Billing"（英文，2026-09-11）、rafftechnologies 的 "VPS Pricing Models: Monthly vs Hourly Billing"（英文，2026-07-29），另两条中文（calculatorlib、lightnode） | 英文位有 2 篇但都停在"按小时还是按月"的选型对比，**没人把官方页上的小时费率 × 730 折成月费**。有缝，可做（对应缺口台账可用 #3） |
| `lowendtalk provider went dark refund recourse` | lowendtalk 的 "RAVNIX offline?" 帖原文（"we should have found a way to notify you **before anything went dark**"）、LET Reviews 分类、services.lowendtalk.com 工单系统，加一条中文 PayPal 争议攻略（vps-craft） | 英文原生素材密集但散在论坛帖里，没人整理成"商家失联后的三步"。可做，注意写成流程不写成法律建议 |
| `vps money back guarantee days provider comparison refund policy` | affordablevpsserver 的英文对比表已占位（InterServer 30 天 / RackNerd 30 天 / Hostwinds 72 小时月付-30 天年付 / Contabo 30 天 / Database Mart 7 天 / Vultr 与 DigitalOcean "No refund (hourly billing)"），其余全是中文站 | 英文位已被占且我们有 `vps-deals-refund-window` 已发——**不再写第二篇**，降级为素材来源 |
| `cheap vps restock notification out of stock waitlist` | hosthum（中文）、vps-supermarket.vercel.app、stock.vpsknow.com、vpsdalao.com、github 的 vmiss-restock-guide——**5 条里 0 条英文** | 库存监控这个需求几乎全被中文站的工具吃掉，英文内容位空缺明显；而 `restock` 恰是 LET 高频词（见 C3）→ **可做，存候选** |
| `"per GB of RAM" VPS price comparison value tier` | stackvaluelab.com "VPS Price per GB of RAM: Every Major Provider, 2026"、pikkly.dev（338 plans / 7 providers / 6 Oct 2026）、hostingsift.com "711 Plans, 39 Hosts"（英文），加 vps.fund、vpssos 两条中文 | 三个英文站在做，说明我们昨天那篇角度被验证；但也说明这个坑开始挤——**不再写第二篇**，要写就换带日期的时间线角度 |

### C. 老外怎么说（真在用的说法）

| phrase | 谁在用 / 什么意思 |
|---|---|
| "$49/year, **renews at** $49" | LowEndTalk 标题原文（D4 Networks）：续费价的标注句式，已是第三天仍在首页出现 |
| "**Price Locked on Renewal**" | LET 标题原文（[WLX] Hong Kong Dedicated）：与 "renews at" 对立的信任信号，意思是续费不涨价 |
| "**Regular VPS Restock**" / "VPS Restock" | LET 标题原文（DeluxHost.net，两帖）：补货。比 sold out / out of stock 更常用，是低价套餐的常态动作 |
| "[**WTB**]" | LET 求购区标题前缀（"[WTB] ISP/RESI IPV6 /44 & Larger + Server"）= Want To Buy |
| "[**Transfer**]" / "Service Transfers" | LET 板块与标题（"[Transfer] Letting go of my beloved KS-5-A - OVH CA"）：转让的是**合同**不是机器，和 WTS 不同 |
| "**Exit Scam Alert / Scam Warning**" + `v4vm[dot]com` | LET 板块名与标题原文；社区故意把域名写成 `[dot]` 以免给骗子站送外链 |
| "**stuck in AI support loop**" | LET 标题原文（"PulsedMedia Server Offline Since Sept 27th: Stuck in AI Support Loop"）：新兴行话，指自动化客服不升级到人工 |
| "**suspended me for 'high utilization'**" | LET 标题原文：被以"高占用"为由停机，引号表示用户对这个理由有异议 |
| "**brand is being retired** as of March 2027" | LET 帖（Prometeus）：品牌退场，常是改名或退出的前兆 |
| "does not own the **ASN**" | LET 标题（"Reject provider tags when the provider does not own the ASN"）：社区判定"真厂商"的硬标准 |
| "**Promo code: LET10**" / "25% off: **LET25**" | LET 侧栏标题原文：给论坛专属的码，写法是"折扣 + 冒号 + 码名" |
| "KVM VPS from $5.99/mo \| 2-4GB **Unmetered**" | LET 标题原文（PrivateByte）：虚拟化类型 + 起价 + unmetered 三件套 |
| "bonus vCPU, RAM, or **Double Transfer Data**" | LET 标题原文（"VPS Promo 10.10 50% OFF"）：加量不加价的三种说法 |
| "**YABS** (**Yet Another Benchmark Script**)" | LowEndBox 正文原文："largest collection of YABS benchmarks on the planet, with over 10,000 user-submitted reports" |
| "**IPv6-only**" / "**LXC** (Linux Container)" | LowEndBox 正文原文（SoftShellWeb）：低价套餐常见形态，IPv4 要加钱 |
| "$16.99/**YR**" / "from $24.95/**mo**" / "UNDER $10/**YEAR**" | LEB/LET 标题：年付月付的写法，几乎不用 "annual" 这个词 |
| "Full refund" / "**Exclusions**" / "Setup fees ... non-refundable" / "**No refund (hourly billing)**" / "pay as you go" | affordablevpsserver 英文评测站对比表原文：退款条的五个字段说法 |
| "**excessive resources** — a vague term they can define retroactively" | 同上，英文评测站对退款除外条款的批评原话 |
| "**monthly cap**" / "monthly maximum" / "ceiling" / "**proration**" / "billing granularity" | rafftechnologies 厂商文档原文：按小时计费的上限、折算、计费粒度 |
| "**Do not assume that shutting down the operating system or powering off the VM ends infrastructure billing**" | 同上原文：关机不等于停计费，厂商文档里明确警告 |
| "the number of hours used to calculate the **monthly maximum**" | 同上原文：就是那个 730，但厂商只说"用来算月上限的小时数"，不写出来 |

### 明日候选

1. **Hourly Rate × 730: What a $0.007/hr VPS Actually Costs Per Month** — B2 + C19/C20/C21（对应缺口台账「可用 #3」）
2. **"VPS Restock" Explained: Why Cheap Plans Sell Out and How the Wait Actually Works** — B5 + C3/C11
3. **"Stuck in an AI Support Loop": What to Do When a Cheap VPS Provider Goes Quiet** — B3 + C6/C7/C8/C9

已用：`compare-vps-deals-total-cost`（10-07）、`vps-deals-renews-at-x`（10-08）、`vps-deals-refund-window`（10-09，退款天数）、`vps-deals-cost-per-gb-ram`（10-09，每 GB 单价，**最后一篇已发布**）。

已降级/不再写第二篇：退款天数（英文位被 affordablevpsserver 占 + 已发）、每 GB 单价（三个英文站在做 + 已发）。

剩余候选（未被消耗）：Unmetered Port, Metered Reality（Day2 B4 + C6/C13/C15）；"Lifetime Discount" vs "First Payment"（Day2 C3/C4/C5）

---

## 2026-10-10 (Day 4)

### A. 原创内容邪修

| # | 邪修点 | 为什么别人抄不走 |
|---|---|---|
| A1 | **「可读 ≠ 有 deal」三态表**。本次 scan（`2026-10-09T18:31:28Z`，= 北京时间 10-10 02:31）8 个官方 URL 三态：可读且有 offer（Hostinger 5 条 / Hetzner 1 条）、可读但 **0 条 offer**（DigitalOcean `/pricing/droplets` 抓通了、一条折扣都没吐出来）、不可读（Vultr / Linode / Contabo×3）。把这三态并排列出来 | 榜单站只有"有价格"一种状态。要写出"抓通了但没有 deal"这一态，必须自己跑解析并记录 readable 布尔值——没有抓取管道的写手连这个区别都看不见 |
| A2 | **同一个厂商试了三个入口，三个都没进去**。Contabo 今天有 3 条 URL 在 source_checks 里（`contabo.com/en/`、`/en/server-outlet/`、`/en-us/pricing/`），**3 条全 false**。失败面从"一条"扩到"整站三个入口"，这是性质判断：不是临时抽风，是整站反爬。公开写成"我们为一个厂商试了三个入口，全被挡" | 竞品只会写"某厂商价格如下"。要敢写"我们进不去"，必须先真的进去过三次；这是自曝其短，商业站永远不做 |
| A3 | **Hetzner 首页第一件事，连续两个 scan 都是二手拍卖**。10-08 18:33Z 和 10-09 18:31Z 两次 scan，Hetzner 抓到的**唯一** offer 都是 `Server Auction`（`/sb`，"refurbished servers"）。官方把"清库存"排在"做促销"前面，而且是连续两天。反向写：不看它卖多少钱，看它首页推的第一件事是什么 | 需要连续日期的同源快照才敢说"连续"。单篇榜单文只有一个时刻的手抄价，没有时间维度 |
| A4 | **官方页上的 deal，有多少条其实指向别的页面**。Hostinger 5 条 offer 里 4 条 `offer_url` = `https://www.hostinger.com/vps-hosting`（回到本页），但第 1 条 `Student discount` 的 `offer_url` = `https://www.hostinger.com/student-discount` —— **20% 的"VPS 折扣"其实导去了另一个业务线**。给读者一条可复制动作：把官方页上每条 deal 的链接域名/路径列出来，跳出去的那几条不是套餐折扣 | 需要解析并比对 `offer_url` 与 `source_url` 的路径差异。手抄价的人看到"5 条折扣"就写 5 条，不会发现其中一条根本不在 VPS 页里 |
| A5 | **用 `fetched_at` 的秒级精度拆穿"实时价格"**。Hostinger 4 条折扣（70% / 67% / 63% / 65% off）的 `fetched_at` **完全相同，都是 `2026-10-09T18:31:21+00:00`**，和 Hetzner 那条差 1 秒，整个 scan 7 秒跑完。这说明这些百分比是同一份 HTML 里的静态文案，不是实时价接口。教读者一个动作：看到同页多个折扣标签且时间戳同一秒，就别把它当动态价格 | 需要秒级 `fetched_at` 字段 + 一次抓取里的多条目。没有管道就没有任何时间戳，更谈不上从"同一秒"推出"静态文案" |

### B. 谷歌搜索查词（今天真跑过的）

| query | SERP 上看到了什么 | 判断 |
|---|---|---|
| `vps deals` | **核心词**。只返回 3 条：spacevps.cc/deals（中文，"按日期更新"）、uvps.org/deals（中文，1 天前）、vpsdeck.com/categories/vps-deals/（唯一英文，且是分类页不是文章）。连续第三天同一格局：中文聚合占 2/3，英文位只有一个分类页占位 | 核心词锁 28 天不动。三天一致 → 是英文供给不足，不是需求不足 |
| `cheap vps unmetered bandwidth fair use policy throttled speed fine print` | 5 条：lumovps、vps-craft 两条中文；**affordablevpsserver.com 英文原文**（2026-07-21，"VPS Bandwidth Policies: Throttling, Overage Fees, and Fair-Use Limits"）；hostadvice.com/vps/unmetered/（英文，但只是"10 Best Unmetered VPS Hosting Providers"榜单）；vpsbang 中文 | 真讲条款的英文文只有 1 篇，另一篇是榜单。且我们有自己的抓取时间戳 + 三态表可以做得更硬 → **可做，升为明日候选 #1** |
| `lowendtalk provider went dark no response refund recourse steps` | 5 条：services.lowendtalk.com/submitticket.php、lowendtalk.com/categories/help、lowendtalk.com 首页、services 公告页，加一条 maxlaw.cn 中文法律问答 | **全是 LET 自己的服务台页，0 篇把这件事整理成流程的文章**。需求明确存在（LET 有独立 help 板块），英文内容位仍然空 → 保留候选，写成流程不写法律建议 |
| `vps hourly billing rate convert to monthly cost 730 hours cap` | 5 条：calculatorlib 中文版 + **英文版**（"730 hours、8760 hours 行业标准"）、racira 计算器、**calculory.com**（"monthly cost equals hourly rate times 730 hours"）、**hourlyvps.com/guides/**（英文，6 天前更新，整站只做按小时计费）。**新信号：昨天还没有 hourlyvps 这个站** | 英文站清一色用 730，但今天实测 DigitalOcean 官方写的是**封顶 672 小时（28 天）**，且 v5 机型"no monthly usage cap"。**整个英文互联网在用一个厂商文档里根本不存在的数字** → 缝很大，**可做，升为明日候选 #2** |
| `vps deal recurring price first term renewal increase how much` | 5 条：vps-craft（中文）、vpscost.com 两篇（英文域名、中文正文）、vpsdoge.com/watch（中文）、vpstier（中文）。**5 条里 0 条英文正文** | 英文位完全空缺；但 `vps-deals-renews-at-x` 已于 10-08 发布 → **不写同角度第二篇**。要写就换 LET 原生词角度（`recurring` / `Price Locked on Renewal` / `ALWAYS`） |
| `lowendbox YABS benchmark results how to read vps performance` | 5 条：vpsart、stellaroam、vps69、banwagongvps **四条中文**（全是"YABS 怎么用"），加 lowendbox.com 英文原帖 "How To Use YABS To Check Your New VPS Or Dedicated Server"（2022 年，讲怎么跑、不讲怎么读） | 中文站把"怎么跑"抄烂了，**英文位只有一篇 2022 年的"怎么跑"，没有"怎么读结果"**。可做 → **升为明日候选 #3** |

### C. 老外怎么说（真在用的说法）

| phrase | 谁在用 / 什么意思 |
|---|---|
| "Usage is **capped at 672 hours (28 days)** per month" | DigitalOcean 官方文档原文：捆绑套餐的月封顶是 672 小时，**不是行业惯例的 730**。整个英文互联网换算时都在用错的数字 |
| "billed per second with a **minimum charge of 60 seconds or $0.01, whichever is higher**" | 同上：按秒计费 + 最低 60 秒/1 分钱，取高者 |
| "**v5 Droplets do not have a monthly usage cap.** The monthly total ... varies based on the number of hours in the month" | 同上：v5 机型干脆没有月上限，月费随当月实际小时数浮动——厂商自己承认"每月不一样" |
| "You are **still billed for ... Droplets that are powered off** because the compute resources stay reserved on the hypervisor" | 同上：关机照样计费，因为资源在宿主上仍被占着。**停计费的唯一方法是 destroy** |
| "Additional outbound transfer is billed at **$0.01 per GiB**. Inbound transfer to Droplets is free." | 同上：出向超量单价，入向免费 |
| "Transfer allowance and usage is **pooled cumulatively ... at the team level, not individually** per Droplet" | 同上：流量额度是**团队池**不是单机池 |
| "**Accrued transfer does not roll over** between months" | 同上：没用完的流量不结转 |
| "**Throttle** — Port speed drops (e.g. from 1 Gbps to 10 Mbps) until the reset date" | affordablevpsserver 英文评测站：三种执法模型之一，限速到重置日 |
| "**Bill per GB** — Overage charged at $0.01–$0.05/GB on the next invoice" | 同上：第二种执法模型，超量按 GB 计费 |
| "**Suspend** — Server paused or network cut until renewal or manual top-up" | 同上：第三种执法模型，直接停机 |
| "\"Unlimited\" bandwidth **does not exist on a shared network port**; what exists is a fair-use policy" | 同上原文：不存在"无限带宽"，只有 FUP |
| "Providers phrase the limits as \"**reasonable use**\" precisely so they can act without publishing a number" | 同上原文：厂商故意用"合理使用"这种不含数字的说法，好让自己随时可以动手 |
| "**Treat port speed as a ceiling, not an allowance**" | 同上原文：端口速率是天花板，不是额度 |
| "**YABS** ... the name \"yabs\" stands for \"**yet another bench script**\"" | LowEndBox 英文教程原文：跑分脚本的行话全称，名字本身是梗（致敬 Yacc） |
| "A bench test hopefully tells us whether we really are **getting everything our Provider's ad promised**" | 同上原文：社区对跑分的真实动机——验广告 |
| "**AES-NI** : ✔ Enabled" / "**VM-x/AMD-V** : ✔ Enabled" | 同上 YABS 输出原文：开箱先看的两项硬件直通，直接决定能不能干某些活 |
| "**fio** Disk Speed Tests (Mixed R/W 50/50)" / "**iperf3** Network Speed Tests (IPv4)" / "**Geekbench 5** Benchmark Test" | 同上 YABS 输出三段标题原文：磁盘、网络、CPU 的称呼方式 |
| "**10,000 YABS**" / "largest collection of YABS ... benchmarks on the planet, with over 10,000 user-submitted reports" | LowEndBox / ServerVerify 原文：社区把跑分库存量当卖点 |
| "D4 Networks \| 4GB KVM, 80-120GB NVMe \| **$49/year, renews at $49**" | LowEndTalk 标题原文：续费价标注句式，第四天仍在首页 |
| "[WLX] Hong Kong Dedicated ... \| **Price Locked on Renewal**" | LET 标题原文：与 "renews at" 对立的信任信号 |
| "[UK] VirexNode ... \| From $3.31/mo **recurring**" | LET 标题原文：**recurring = 一直这个价**，和首单促销价对立 |
| "**RPiServers 2.0 -- $3.14 ALWAYS!**" / "**$5 for 5 Years?!** Dewlance® - **Quinquennially**" | LET 标题原文：不涨价声明的两种写法（`ALWAYS`、五年一付的 `Quinquennially`） |
| "**25G Unmetered** 30% lifetime discount" / "Regular **VPS Restock**" | LET 标题原文：unmetered 与补货，低价套餐的常态措辞 |
| "**[TRANSFER]** HostBilby 12c/24GB/160GB NVMe ($60/yr) + DartNode Ryzen 9950X 2c/4GB ($45/yr)" | LET 转让区标题原文：转让的是**合同**，标题里必须写清原套餐与原价 |
| "**BYOASN/BYOIP**" / "Only Providers/**LIRs** are allowed to post offers" | LET 公告与标题原文：自带 ASN/IP；社区对"谁有资格发 offer"的硬门槛 |
| "**VirMach LA outage**" / "VSYS Host: UA data centers. **What happened and where recovery stands?**" | LET 标题原文：出事后的问法——不问"好不好"，问"发生了什么、恢复到哪一步" |
| "**Netcup price increase (September 2026)**" / "**cPanel: Price increase 2027**" / "**Should I just get a VDS**" | LET 标题原文：涨价有月份，VDS 是区别于 VPS 的独立品类名 |

### 明日候选

1. **672, Not 730: Why Your VPS Hourly Rate Doesn't Convert to a Month the Way Every Calculator Says** — B4 + C1/C2/C3/C4（DigitalOcean 官方 672 封顶 + v5 无封顶 + 关机仍计费 + 按秒最低 60 秒；对应缺口台账「可用 #3」）
2. **Unmetered Port, Metered Reality: What Actually Happens When You Hit a VPS Bandwidth Cap** — B2 + C8/C9/C10/C11/C12/C13（三种执法模型 + FUP + 端口是天花板不是额度）
3. **YABS in Plain English: How to Read a VPS Benchmark You Didn't Run** — B6 + C14/C15/C16/C17（怎么读结果，不是怎么跑）

已用：`compare-vps-deals-total-cost`（10-07）、`vps-deals-renews-at-x`（10-08）、`vps-deals-refund-window`（10-09）、`vps-deals-cost-per-gb-ram`（10-09）、`vps-deals-who-collects-vat`（10-09，**最后一篇已发布**）。

已降级/不再写第二篇：退款天数（英文位被 affordablevpsserver 占 + 已发）、每 GB 单价（三个英文站在做 + 已发）、renews at 换算（已发，且 B5 显示英文位 0 篇正文 → 想写只能换成 recurring / price locked 原生词角度）。

剩余候选（未被消耗）："Lifetime Discount" vs "First Payment"（Day2 C3/C4/C5）；VPS Restock 等待机制（Day3 B5 + C3/C11）；"Stuck in an AI Support Loop"（Day3 B3 + C6/C7/C8/C9）。

---

## 2026-10-11 (Day 5)

### A. 原创内容邪修

| # | 邪修点 | 为什么别人抄不走 |
|---|---|---|
| A1 | **三天同一时刻的受控快照**。连续三次 scan 的 UTC 墙钟是 10-08 `18:33Z`、10-09 `18:31:28Z`、10-10 `18:30:32Z`——**三天落在同一个三分钟窗口里**。这意味着前后两天看到的任何差异都是页面真的改了，而不是"我看的时间不同"。本次 scan（`2026-10-10T18:30:32+00:00` = 北京 10-11 02:30）Hostinger 的 `70% / 67% / 63% / 65% off` 四个标签与 48 小时前逐字相同 | 榜单站是"想起来截一张"，时间点随机，永远分不清"价格变了"和"我看晚了"。要把时间变量锁死，必须有一个每天固定时刻自动跑的管道 |
| A2 | **反向写：我们的 deal 总数三天恒为 6**。10-08、10-09、10-10 三次 scan 都是 Hostinger 5 条 + Hetzner 1 条 = **6 条，且构成逐日一致**。所有 deals 站都在暗示"每天都有新货"，我们直接写"这个数字三天没动过，以及为什么不动比乱动更有用" | 别人不敢写"我这儿没变化"——那等于承认自己没内容。而且要先有连续三天的同源计数才敢下这个结论 |
| A3 | **Hetzner 连续第三天，首页推的第一件事还是二手拍卖**。三次 scan 抓到的唯一 offer 都是 `Server Auction`（`/sb`）。且我们抓到的标题是**被截断的句子**："Server Auction Save money and do good for the planet with refurbished servers from"——停在介词 `from` 上。这是解析器的接缝，我们原样发布 | 竞品的标题都是人手润色过的完整句。要露出"…servers from"这种断句，必须是真的从 HTML 里切出来的。自曝解析瑕疵，商业站不会做 |
| A4 | **抓取预算的不对称，公开写出来**。本次 source_checks 共 8 条 URL，其中 3 条属于 Contabo（`contabo.com/en/`、`/en/server-outlet/`、`/en-us/pricing/`）——**一家厂商吃掉 37.5% 的抓取预算，连续三次 scan 产出 0 条 offer**，我们照样每天抓。理由写进正文：确认"它今天也没有促销"本身就是数据 | 只有自己分配抓取预算的人才会算这笔账。读者看到的都是"某厂商价格如下"，没人告诉他采集方在谁身上白花了多少钱 |
| A5 | **我们自己的日志里有 3/8 条记录没有 provider 字段**。source_checks 前 5 条都带 `provider`（Hostinger / Hetzner / DigitalOcean / Vultr / Linode），后 3 条只有 `url` 和 `readable`，**没有厂商名**。把它变成一条给读者的方法：想判断一个 deals 站是真抓的还是手抄的，去看它的记录里有没有空字段——**一份零空字段的清单，多半是人填的** | 需要先拥有并敢公开自己的抓取日志结构。承认数据管道有洞，是没有管道的人连想都想不到的角度 |

### B. 谷歌搜索查词（今天真跑过的）

| query | SERP 上看到了什么 | 判断 |
|---|---|---|
| `vps deals` | **核心词**。5 条：spacevps.cc/deals、uvps.org/deals（2 天前）、vpshub.org（23 小时前，377 个套餐）、vpsclub.cc/deals 四条中文，加 **vpsdeck.com/categories/vps-deals/**（唯一英文，仍是分类页不是文章）。**新变化：今天多了 vpshub、vpsclub 两个中文聚合站，英文位仍是同一个分类页** | 核心词锁 28 天不动。连续第四天同一格局，且中文站数量在增加、英文位始终只有一个分类页占位 → "英文供给不足而非需求不足"的结论更硬了 |
| `hetzner server auction refurbished servers buy dedicated` | 5 条里 3 条英文：hetzner.com/sb 官方拍卖页（1 天前）、hetzner.com/blog 官方解释文（"How the Hetzner Server Auction works"，2026-06-10）、biswashost.com（英文，转卖 Hetzner 拍卖硬件）、auction.akua.dev/guide（英文，专门做拍卖捡漏的工具站），加 1 条中文（laoda.de） | **英文生态已存在，但全是第三方捡漏工具 + 厂商自述，没人把它当"一个 VPS 厂商首页在推什么"来写**。而我们手上有连续三天的一手快照 → **可做，升为明日候选 #1** |
| `vps cpu steal time high noisy neighbor explained` | 5 条里 3 条英文且都很新：virtualserversvps.com（2026-09-12）、hostna.com（5 天前）、voxfor.com（2026-08-02），加 2 条中文（jiyueip、getcloudworth） | 英文位已被三篇讲透（定义、阈值、命令、容器与 KVM 差异）。**不写同一角度**。但里面那句 "steal time is the difference between owning cycles and renting them" 是好素材 → 收进 C 栏备用 |
| `lowendtalk provider went dark prepaid yearly chargeback` | 5 条：vps-craft 中文攻略、chdh.me 中文、lowendtalk.com 首页、**lowendtalk.com/categories/outages/（新发现：LET 有独立的 Outages 板块）**、warpnav 中文导航 | 英文位仍只有 LET 自己的板块页，**0 篇把这个流程整理成文章**。需求真实（论坛专门开了板块），供给空缺 → 保留候选，写流程不写法律建议 |
| `vps promo deal expiry how long first term only lifetime discount` | **5 条全部英文**：freedom251.com（"first month, first invoice, or first billing term"）、**fasthosts.co.uk/terms/… 官方促销条款页**、affordablevpsserver.com "VPS Renewal Price Hikes"（2026-10-08，四种涨价结构）、positioniseverything、llhost.eu 官方博客（"20% lifetime discount … as long as that VPS is continuously renewed"） | 今天唯一 **5/5 全英文** 的词，说明英文内容密集 → **不写泛泛的"续费会涨价"**。但有个缝：官方条款页和评测站各自列了折扣结束的方式，**没人把四种机制并列成一张表** → 升为明日候选 #2（用"分类法"角度，避开已发的 renews-at） |
| `vps deals site expired dead offers stale listings` | 5 条：pennyclouds.com 英文文 "why expired hosting deals still show up online and how to avoid them"（直接讲过期 deal 为什么还在排名）、**vpsrankings.com/en/deals（英文 deals 聚合页，1 天前）**、vpsrankings.com/deals 中文版、vpsclub.cc、vpsdeck 分类页 | **新信号：vpsrankings.com/en/deals 是五天内第一个出现在核心词周边的英文 deals 聚合页**，值得盯。pennyclouds 已占"过期 deal"英文角度 → 我们从 A2 的"三天恒为 6"切进去，靠一手时间戳打，不靠观点打 |

### C. 老外怎么说（真在用的说法）

| phrase | 谁在用 / 什么意思 |
|---|---|
| "**no setup fee**" / "there's no one-time setup fee, **since the server was already set up**" | Hetzner 官方拍卖页与官方博客原文：二手拍卖机的第一卖点，装机费为零 |
| "**no minimum contract term**" | Hetzner 官方原文：无最短合约期，拍卖机区别于常规独立服务器的核心条款 |
| "**Dutch-style auction** / Prices start out low and keep dropping … at **randomly chosen intervals**" | Hetzner 官方博客原文：荷兰式拍卖，降价间隔是随机的 |
| "The longer you wait, the cheaper your dream server can get. **The catch: with every passing minute, the risk grows that someone else beats you to it**" | 同上原文：等越久越便宜，但可能被别人抢走 |
| "we **securely wipe the previous owner's data** beforehand in a careful, documented process" | 同上原文：二手机的清数据流程，厂商主动交代 |
| "we extend a server's life from an average of **three to four years to around eight**" | 同上原文：延寿说法，厂商的环保叙事口径 |
| "**Server Auction ID: 3086830**" / "**#FSN1-DC1**" / "**15:15:04 left**" / "Traffic: **unlimited**" | Hetzner 拍卖页字段原文：每台机器有唯一 auction ID + 机房编号 + 倒计时 |
| "the discount is applied for the first three months, then **automatically reverts to** the standard … price" | Fasthosts 官方促销条款页原文：折扣到期自动回原价的标准句式 |
| "**Subsequent terms and renewals will be charged at the standard pricing specified at the time of renewal**" | 同上官方条款原文：续费按"续费当时的"标准价，不是你买的时候的价 |
| "**Pay-As-You-Go contract types are excluded** from this promotion" / "does not apply to **upgrades, migrations, or renewals**" | 同上原文：促销排除项的两种写法 |
| "This offer is valid from 1 July 2026 **until further notice**" | 同上原文：没有到期日的促销，实际意思是"随时可撤" |
| "**Silent list-price changes.** The provider reissues the price sheet; existing customers follow unless they hold a lock" | affordablevpsserver 英文评测站：四种涨价结构里最隐蔽的一种——重发价目表 |
| "**Promotional first term**" / "**Annual escalation clauses**" / "**Add-on repricing**" | 同上：另外三种——仅首个计费期、年度递增条款、附加项重定价 |
| "A plan's value is **its renewal price, not its introduction**" / "the tie-breaker is the one that stays affordable **on day 366**" | 同上原话：第 366 天才是分水岭 |
| "**retention offers**" / "**loyalty rate**" / "match the new-customer rate" | 同上：续费谈判的三个词——挽留报价、老客价、要求匹配新客价 |
| "**flat pricing with no promotional cliffs**" / "**Track the total, not the headline**" | 同上：无促销悬崖的平价；看总价不看标题价 |
| "**Steal time is the difference between owning cycles and renting them**" | virtualserversvps 英文技术文原话：解释 steal 最狠的一句 |
| "**steal**" / "**%st**" / "the `st` column in `vmstat`" / "`mpstat -P ALL`" | 同上：同一指标在三种工具里的叫法，运维真这么喊 |
| "On a well-behaved host it stays **under 1-2%**. **Above 5%** you are losing meaningful throughput" | 同上：社区公认的两个阈值 |
| "Steal is not your process being slow. **It is your process not being allowed to run**" | 同上原文：区分"慢"和"不给跑" |
| "**oversubscription ratio**" / "**Ask to be moved to a quieter host**" | 同上：超售比；开工单时的标准请求句式 |
| "On container-based plans (LXC/OpenVZ) 'steal' **may read zero even while you are being throttled**" / "`nr_throttled` and `throttled_usec`" | 同上：LXC/OpenVZ 下 steal 恒为 0，得改看 cgroup 限流计数器 |
| "**RAVNIX is Back!** New Atlanta Location, Upgraded Network & VPS Offers Starting at $14/Year!" | LowEndTalk 标题原文：商家消失后回归的宣告句式 |
| "**1G plans moved to EPYC, same price**" | LowEndTalk 标题原文（SKRIME）：换硬件不涨价的说法 |
| "**LET YABS Thread**" / "**ServerVerify** … over 10,000 user-submitted reports" | LET 有专门的 YABS 汇总帖；LowEndBox 原文称 ServerVerify 库里已有 1 万份用户提交跑分 |
| "**pubnix**" / "**GLWS**" / "**dedi**" | LET/LEB 社区行话：公共 Unix shell、Good Luck With Sale、独立服务器的简称 |
| "**Free /48 For Everyone**" / "**Auto LOAs**" / "**BGP & ASN Portal**" | LET 标题原文（IPYE.com）：IP 租赁业务的三件套说法 |
| "**Weeks later: … pt 2: 3 different licensing stories in 1 ticket**" | LET 评测区标题原文：一个工单里给出三种说法，社区数落厂商的固定写法 |
| "**OVH Server Renewal Issue – Only Option Is to Cancel the Service**" | LET Help 区标题原文：续费出问题只能取消 |
| "**Black Friday 2026 - Wishlist Thread**" | LET 标题原文：黑五前社区开许愿帖，旺季节奏已启动 |
| "**Hourly Billing**" / "**30% lifetime discount**" / "**First Year**" | LowEndBox 标题原文：计费周期与折扣时长的三种标注写法 |

### 明日候选

1. **Why Hetzner's Front Page Sells Used Servers Before It Sells New VPS** — A3（连续三天一手快照）+ B2 + C1–C7（官方拍卖页原文：no setup fee / no minimum contract term / Dutch auction / 随机降价 / 会被抢）。缝：英文生态只有第三方捡漏工具和厂商自述，没人从"厂商首页在推什么"切入
2. **"Automatically Reverts to Standard Pricing": The Four Ways a VPS Discount Quietly Ends** — B5 + C8–C16（Fasthosts 官方条款原文 + affordablevpsserver 的四种结构：Promotional first term / Annual escalation clauses / Add-on repricing / Silent list-price changes）。必须写成**分类法表格**，避开 10-08 已发的 `vps-deals-renews-at-x`
3. **"Regular VPS Restock": Why the Cheap Plan Is Out of Stock and How the Wait Actually Works** — Day3 遗留候选 + 今天 LET 首页两条 DeluxHost 补货帖（`Regular VPS Restock` / `VPS Restock`）。英文位此前实测 5 条里 0 条英文

已用：`compare-vps-deals-total-cost`（10-07）、`vps-deals-renews-at-x`（10-08）、`vps-deals-refund-window`（10-09）、`vps-deals-cost-per-gb-ram`（10-09）、`vps-deals-who-collects-vat`（10-09）、`vps-deals-hourly-to-monthly`（10-10，**最后一篇已发布**）。

已降级/不再写第二篇：退款天数（英文位被 affordablevpsserver 占 + 已发）、每 GB 单价（三个英文站在做 + 已发）、renews at 换算（已发）、Hourly ×672/730（Day4 候选 #1，已由 10-10 的 `vps-deals-hourly-to-monthly` 消耗）、CPU steal 诊断（B3 显示英文位已有三篇新文占满）、过期 deal（B6 显示 pennyclouds 已占英文位）。

剩余候选（未被消耗）：Unmetered Port, Metered Reality（Day2 B4 + C6/C13/C15）；"Stuck in an AI Support Loop"（Day3 B3 + C6/C7/C8/C9）；YABS 怎么读结果（Day4 候选 #3）。

---

## 2026-10-12 (Day 6)

### A. 原创内容邪修

| # | 邪修点 | 为什么别人抄不走 |
|---|---|---|
| A1 | **同一家厂商的两份官方页面，对同一个拍卖的起价方向说法相反**。Hetzner 官方博客（2026-06-10）写 "Prices **start out low** and keep dropping over the course of the day, at randomly chosen intervals"；Hetzner 官方文档 FAQ 写 "The prices **start high**, and go down over time"，还补了一句 "For each server model, Hetzner decides the starting price. When we add a server from that model to the Auction, it **always starts at the same price**"。一个说起价低、一个说起价高，且两页今天都在线 | 必须同时读过厂商博客**和**厂商文档并逐字比对。二手评测站只抄博客那一句（今天 SERP 上 reviewplan.com 就是这么干的），榜单站一个源都不读。而且第三方不敢写"大厂自己两页打架"——要贴两份原文并排才站得住 |
| A2 | **我们每天扫完整个促销盘，只用 8 秒**。本次 scan `2026-10-11T18:31:15Z`，六条 offer 的 `fetched_at` 落在 `18:31:07`–`18:31:09`，八条 URL 检查全部在这 8 秒内完成。把这个真实耗时当作正文的一部分写出来 | 需要每条 offer 落盘时带自己的秒级 `fetched_at`。榜单站没有"抓取耗时"这个概念，只有一个"最后更新：今天"。而且自曝"我的管道只要 8 秒"等于承认自己很小，商业站不会这么写 |
| A3 | **折扣标签不是按大小排的**。Hostinger 四条是 `70% → 67% → 63% → 65%`——**第三个（63）比第四个（65）小**。这说明顺序来自页面 DOM，不是"最优惠在前"。而几乎所有 deals 站都按折扣百分比降序排列：那个排序是他们自己加的，厂商页面上根本不存在 | 要判断"顺序无意义"，得连续多天看到同一组数字在页面里的位置不变，**并且**注意到它不单调。只截一次图的人会照抄这个顺序，还会默认 70% 是最好的那个 |
| A4 | **六条 offer 里，唯一一个把你带离 VPS 页面的链接是学生折扣**。五条 `70/67/63/65 off` 的 `offer_url` 全部指回 `https://www.hostinger.com/vps-hosting`——**自指**，即"促销就是这一页本身"。只有 `Student discount` 指向 `/student-discount`。VPS 定价页上唯一一个真正改变目的地的链接，跟配置、价格、机房全都无关，只跟"你是谁"有关 | 需要把 `offer_url` 和 `source_url` **分开存储**并逐条做相等性判断。多数 deals 站只保留一个"去购买"链接，两类 URL 混在一个字段里，永远做不出"自指 vs 外跳"这个区分 |
| A5 | **我们自己两个数据文件的年龄差了两天**。offers.json 的 scan 是 `2026-10-11T18:31:15Z`（本地 mtime 10-12 07:02），provider_facts.json 的本地 mtime 停在 10-10 15:56。促销每天刷，厂商事实两天没动 | 得先有两个分开维护的数据文件，并且敢公开它们更新不同步。把它变成给读者的方法：看一个 deals 站的"促销块"和"厂商参数块"是不是同一天更新的——不是的话，参数块就是旧的，而它通常还是你比价的依据 |

### B. 谷歌搜索查词（今天真跑过的）

| query | SERP 上看到了什么 | 判断 |
|---|---|--|
| `vps deals` | **核心词**。5 条：spacevps.cc/deals、uvps.org/deals（3 天前）、vpshub.org/zh/0_100/（1 天前，**380 个套餐**）、vpsdeck.com/categories/vps-deals/（唯一英文，仍只是分类页不是文章）、vpsclub.cc/deals。**与昨天的差异：vpshub 套餐数 377→380；昨天刚出现的 vpsrankings.com/en/deals 今天掉了** | 核心词锁 28 天不动。英文位连续第五天只有同一个分类页占位，中文聚合站还在增加 → "英文供给不足而非需求不足"继续加固 |
| `vps deal out of stock restock notification waitlist cheap plan` | 5 条**全部中文**：hostf4.com/zh-hans/stock（英文站却给中文路径）、vpsdoge.com/restock-alerts、stockvps.org、hosthum.com、vpsrestock.com（10-12 更新）。**英文位 0** | 补货监控这个需求在中文圈已经被做成一整类站点（库存监控站、TG 机器人、订阅提醒），**英文位完全空缺** → **升为明日候选 #1**（Day5 候选 #3 今天第一次拿到"5/5 中文"的硬证据） |
| `hetzner server auction how it works refurbished server buy` | 5 条里 4 条英文：hetzner.com/blog（官方解释文）、hetzner.com/sb（官方拍卖页）、**docs.hetzner.com/robot/general/server-auction-faqs（官方文档，Day5 没挖到，今天新发现）**、reviewplan.com（英文，2023），加 1 条中文 vpstop.cn | **官方文档页是 Day5 没找到的新源，且它与官方博客的说法直接冲突（见 A1）** → Hetzner 候选不但成立，还多出一个独家切口 → **继续列明日候选 #2** |
| `vps unmetered bandwidth fair use policy port speed throttle explained` | **5 条全部英文且都是长文**：vpshostreview.com（新英文站，逐段拆 unlimited 的三种实现）、affordablevpsserver.com 两篇（计量三模型 + 超量 $0.01–$0.15/GB）、positioniseverything.net、infotechna.hu（匈牙利厂商自己写的 FUP 条款页，9 节） | 英文位**已被占满**，且 vpshostreview 已经写了我们原本打算写的"端口速率 → 理论月上限"表（1 Gbps ≈ 330 TB/月）→ **把 Day2 遗留候选「Unmetered Port, Metered Reality」正式降级，不写**。但 infotechna 那份 FUP 是厂商自己列的逐条清单，是好素材 → 收进 C 栏 |
| `hostinger vps 70% off student discount deal terms` | 5 条：webseotrends.com（英文，"up to **85%** off"）、studentbeans.com（英文，"up to **67%** off n8n VPS Hosting"）、hostadvice.com / zh.hostadvice.com 两条（中文，写"**74%**"） | **同一件事在 SERP 上出现 85% / 74% / 67% 三个互不相同且都偏离官方页面的数字**，而我们从官方页面抓到的是 70/67/63/65。第三方数字全部不是页面上的数 → 缝很大，但与 A4 同源，**合并进候选 #3，不单独开题** |
| `lowendtalk support ticket AI chatbot escalate human` | 5 条**全是 SaaS 客服产品页和 GitHub 项目**（builtabot "human handoff" 指南、chatbot.com、endurancesoftwares、两个 AI 工单分类 GitHub repo），**0 条讲 VPS 买家视角** | 这个词的 SERP 被"卖 AI 客服的"占满，不是我们的战场 → **把 Day3 遗留候选「Stuck in an AI Support Loop」正式降级**。除非改写成 LET 原生词角度（`no ticket reply in 5 days` / `3 different licensing stories in 1 ticket`），这两个今天在 LET 首页就有原文（见 C 栏） |

### C. 老外怎么说（真在用的说法）

| phrase | 谁在用 / 什么意思 |
|---|---|
| "The prices **start high**, and go down over time" | Hetzner 官方文档 FAQ 原文：拍卖起价**高**，往下走。与官方博客那句 "start out low" 直接冲突（见 A1） |
| "For each server model, Hetzner decides the starting price. When we add a server from that model to the Auction, it **always starts at the same price**" | 同上原文：同型号每次上架起价相同，所以同型号价格不同只因挂了不同时长 |
| "So you might see the same server model at different prices because the servers have been on the Server Auction for **different amounts of time**" | 同上原文：同型号不同价的官方解释 |
| "We use software to **randomly decide how much time there is between price drops**" / "We at Hetzner **do not manipulate the prices**" | 同上原文：降价间隔由软件随机决定；厂商主动声明不操纵价格 |
| "It is a **Dutch-style auction** where customers can find servers" | 同上原文：厂商自己的品类说法 |
| "All of the servers in the Auction are **'old' servers**… When we … introduce the next generation of new servers, we make the 'old' servers available" | 同上原文：拍卖货源就是被新品换代下来的旧机型 |
| "**There are no setup fees for these servers.**" / "Since these servers do not have setup fees, they are a bit more affordable than our newest models" | 同上原文：零装机费，且官方自己把它当价格优势讲 |
| "The **cancellation period** for these servers is usually **immediately**" | 同上原文：官方文档对"最短合约期"的答法——不说"无最短期限"，说"取消期通常即时" |
| "They are **unmanaged servers**, and you, the customer, are the only person who has root access to them" | 同上原文：unmanaged + 你独自拥有 root，责任全在你 |
| "You are also responsible for preventing any kind of abuse on the server, and for quickly removing any issues if our **Abuse Team** contacts you" | 同上原文：Abuse Team 是厂商侧对口的那个部门名 |
| "Our technicians will make sure that the server is **connected to the internet**" / "our team can **attach a KVM console** … or … run a **full hardware test**" | 同上原文：官方划出"免费支持"的边界——只到联网和硬件 |
| "Usually, we can deploy these servers **within 1 business day**" / "if you are a new Hetzner customer, our **sales technicians** will first review your account information" | 同上原文：1 个工作日交付；新客要过一遍人工审核 |
| "We only add servers to the Auction **once the previous user has cancelled them**" | 同上原文：拍卖库存取决于上一位客户什么时候退 |
| "If you open a ticket and write something vague like, **'My server's acting weird. I think the drives are defective,'** our team will ask you for more information, and that will slow down the process" | 同上原文：**厂商文档里教你怎么写工单**——模糊工单会被打回，直接拖慢处理 |
| "All dedicated root servers (including those from the Server Auction) have **unlimited traffic**" / "a dedicated uplink with **guaranteed bandwidth of 1 Gbit/s**" | 同上原文：二手拍卖机照样 unlimited traffic + 1 Gbit/s 保证带宽 |
| "**E-waste** is a growing global problem" / "**reduce, reuse, recycle**" / "**one of the best ways to reduce the environmental footprint of hardware is to use it for as long as possible**" | 同上原文：厂商对二手业务的环保叙事口径，与博客一致 |
| "Prices **start out low** and keep dropping over the course of the day, at **randomly chosen intervals**" | Hetzner 官方博客（2026-06-10）原文：与上面 docs 那句"start high"**相反**。两页都是官方、都是英文 |
| "The longer you wait, the cheaper your dream server can get. **The catch: with every passing minute, the risk grows that someone else beats you to it**" | 同上原文：等越久越便宜 vs 被抢走，厂商自己把这个权衡讲明 |
| "there's **no one-time setup fee, since the server was already set up**" | 同上原文：零装机费的理由——机器早就装好了 |
| "we extend a server's life from an average of **three to four years to around eight**" | 同上原文：延寿口径，3–4 年拉到约 8 年 |
| "Since there's **no minimum contract term**, the auction works well for short-term projects too" | 同上原文：博客口径写的是"无最短合约期"（docs 写的是"取消期通常即时"，两种答法） |
| "**Regular VPS Restock**" / "**VPS Restock**" | LowEndTalk 首页 DeluxHost 两条标题原文：低价套餐补货的**固定栏目式说法**，不是临时公告 |
| "our popular plans are **back**!" / "Taiwan VPS Deals are **BACK**!" | LET / LEB 原文：补货的另一种写法，用"回来"而不是"上架" |
| "**Servitro: unusable IPv4 (broadcast address), no ticket reply in 5 days**" / "**Servitro down for over 24 hours**" | LET 标题原文：出事帖的标准写法——给出具体故障（不可用的广播地址）+ 工单无回复的天数 |
| "**Weeks later: ServerHost / VPSHostingService.co, pt 2: 3 different licensing stories in 1 ticket**" | LET 评测区标题原文：一个工单里三种说法；`Weeks later` + `pt 2` 是社区追更帖的写法 |
| "**Cloudzy account suspended without warning: 4 servers offline, no explanation, no way to retrieve dat[a]**" | LET 标题原文：停机投诉的四段式写法（无预警 / 几台离线 / 无解释 / 取不回数据） |
| "**[WARNING] NoBanHost … Assigned a non-routable IANA documentation IP (198.51.100.251)**" / "**HostDZire IPv6 Allocation Violation: Service Terminated After Configuration Error**" | LET 标题原文：`[WARNING]` 前缀 + 具体技术违规；社区用 RFC 文档地址段举例说明厂商发错 IP |
| "**ReliableSite ending referral program, says GTFO before 30 October**" | LET 标题原文：社区直接引用厂商原话（GTFO）当标题 |
| "**Why are people posting First Second Third and GLWS on basically every thread?**" | LET 标题原文：有人公开问行话——说明 `First/Second/Third` 抢楼和 `GLWS`（Good Luck With Sale）已是默认礼仪 |
| "**[FREE] shellter.me — FreeBSD pubnix (bash, 60MB ZFS, 3× IPv6, self-service revDNS)**" | LET 标题原文：免费公共 Unix 机的规格写法，`pubnix` 和 `self-service revDNS` 是社区默认词 |
| "**[Request] 16TB+ Storage VPS/Dedi – 10Gbps, 100TB/mo, ~$200/2yr (Black Friday?)**" | LET 求购帖标题原文：需求 + 预算 + 周期一行写完，末尾挂 `(Black Friday?)` 表示在等旺季 |
| "**offers rss broke again?**" | LET 标题原文：社区靠 RSS 订阅 offer，`broke again` 说明它经常坏 |
| "**Exclusive LowEndBox Pricing: 2GB KVM VPS for $1.83/Month First Year! Godlike.Host is Back!**" | LowEndBox 原创帖标题原文：`Exclusive … Pricing`（站方专属价）+ `First Year`（暗示次年另算）+ `is Back`（商家回归） |
| "**Another year, another cPanel / WHMCS price increase. What are you actually getting for the surging cost…**" | LEB 标题原文：对年度涨价的固定吐槽句式 `Another year, another … price increase` |
| "**Welcome back, Kainode! This is the third time we've featured them on LowEndBox**" | LEB 原文：站方会数这是第几次收录某商家——`featured` 是 LEB 的收录用词 |
| "**10,000 YABS!**" / "largest collection of YABS (**Yet Another Benchmark Script**) benchmarks on the planet, with over 10,000 user-submitted reports" | LEB 原文：跑分库存量当卖点，`YABS` 全称在站内被正式展开 |
| "'**Unmetered bandwidth**' means that your VPS plan does not impose a fixed monthly data transfer limit … However, **this does not equate to unlimited or unrestricted usage**" | infotechna.hu 厂商 FUP 条款页原文：厂商自己定义 unmetered 并立刻否定 unlimited |
| "**Sustained usage at or near the maximum capacity for extended periods may be considered excessive**" | 同上原文：FUP 里"超限"的实际判据——不是总量，是**长时间贴近端口上限** |
| "**No Overage Fees:** Since your plan is unmetered, you will not incur additional bandwidth charges."（同页第 6 节又写 "we may **throttle** your bandwidth … or … temporarily **suspend** your VPS"） | 同上原文：厂商 FUP 的自相矛盾处——不收超量费，但可以限速或停机 |
| "A plan advertising 'unlimited bandwidth' on a 100 Mbps port is making a claim that the port speed already makes difficult to violate. **The physics of the connection do most of the limiting.**" | vpshostreview.com 英文评测文原话：解释"为什么厂商敢写 unlimited"最狠的一句 |
| "1 Gbps **~330 TB**" / "A 100 Mbps port maxes out at roughly **33 TB** per month" | 同上原文的换算表：端口速率对应的理论月流量上限 |
| "**Overage** — per-GB charges after the cap, often **$0.01–$0.15/GB** depending on provider and region" | affordablevpsserver 英文评测站：超量单价区间 |
| "A **2TB cap with a 100Mbps throttle** is very different from a **2TB cap with $0.05/GB overage** fees" | 同上原文：同样 2TB 额度，执法方式不同就是两种产品——社区比价时真正看的东西 |

### 明日候选

1. **"Regular VPS Restock": Why the Cheap Plan You Want Is Out of Stock — and How the Wait Actually Works** — B2（英文位 5/5 中文、0 英文）+ C22/C23（LET 两条 DeluxHost 补货标题 + `plans are back` / `Deals are BACK`）。缝：中文圈已把补货做成监控站、TG 机器人、订阅提醒一整类，英文位一篇都没有
2. **Hetzner Sells Used Servers First: What a Dutch Auction Does to the Price — and Why Hetzner's Own Two Pages Disagree** — A1（博客 "start out low" vs 文档 "start high"，两页原文并排）+ B3（官方文档页是 Day5 没找到的新源）+ C1–C21
3. **The Only Link on a VPS Pricing Page That Leaves the Page Is the Student Discount** — A3（标签顺序不单调）+ A4（五条 offer 自指，只有学生折扣外跳）+ B5（SERP 上 85% / 74% / 67% 三个数都不是页面上的 70/67/63/65）

已用：`compare-vps-deals-total-cost`（10-07）、`vps-deals-renews-at-x`（10-08）、`vps-deals-refund-window`（10-09）、`vps-deals-cost-per-gb-ram`（10-09）、`vps-deals-who-collects-vat`（10-09）、`vps-deals-hourly-to-monthly`（10-10）、`vps-deals-cost-per-gb-disk`（10-11，**最后一篇已发布**）。

已降级/不再写第二篇：退款天数（已发）、每 GB 单价（已发）、renews at 换算（已发）、Hourly ×672/730（已由 10-10 消耗）、CPU steal 诊断（英文位三篇新文占满）、过期 deal（pennyclouds 已占）、**Unmetered Port, Metered Reality（Day2 遗留，B4 实测英文位被 vpshostreview + affordablevpsserver×2 + positioniseverything 占满，今日降级）**、**Stuck in an AI Support Loop（Day3 遗留，B6 实测 SERP 被 AI 客服 SaaS 页和 GitHub 项目占满，今日降级；若要写只能改用 LET 原生词角度）**。

剩余候选（未被消耗）：YABS 怎么读结果（Day4 候选 #3）；"Automatically Reverts to Standard Pricing" 四种折扣结束方式（Day5 候选 #2，今天无新证据，保留未升级）。

---

## 2026-10-13 (Day 7)

### A. 原创内容邪修

| # | 邪修点 | 为什么别人抄不走 |
|---|---|---|
| A1 | **一天扫 5 次，六条 offer 一个字节都没变**。10-12 当天我们在 `00:41:33`、`02:19:33`、`06:40:40`、`12:50:49`、`18:34:16`（UTC）各扫了一次。把 5 份快照摆在一起：6 条 offer 的 `title`、`offer_url`、排列顺序**完全相同**——连 Hetzner 那条截断在介词上、以 `...refurbished servers from` 结尾的残缺标题都一字不差。一个把"限时/促销"挂在标题上的 deals 站，如果它的全部库存跨 18 小时、5 次扫描一个字节都没动，那这些"促销"就是常驻文案，不是限时活动 | 必须一天内多次快照**并且保留每一次的原始字符串**，才能证明"没变"——单次抓取只能证明"现在有"。而且把"我的 6 条 deal 一整天没变"写进正文等于自曝库存是死的；商业 deals 站的收入模型建立在"每天都有新东西"，不会这么写 |
| A2 | **六条 offer 其实只来自两次页面读取**。本次 scan 里 5 条 Hostinger offer 的 `fetched_at` **全部落在 `18:34:07` 同一秒**，Hetzner 是 `18:34:09`。6 条 deal 对应 2 次 HTTP 抓取，其中 5 条是同一页上的第 2–6 个折扣标签。而且"Hostinger 比 Hetzner 早 2 秒"这个节奏当天多次 scan 完全一致（`27→29`、`43→45`、`07→09`） | 需要每条 offer 落盘时带自己的**秒级**时间戳，并且要意识到"同一秒 = 同一次读取"。deals 站按 provider 只存一条"最后更新"，永远看不出 6 条 deal 其实只有 2 个来源页——他们会把这个数字当成"6 个不同来源"来写 |
| A3 | **8 条 URL 里唯一"读得到、却一条促销都没有"的是 DigitalOcean**。三态很清楚：`readable: true` 的是 Hostinger / Hetzner / DigitalOcean，`false` 的是 Vultr、Linode(Akamai)、Contabo×3。但 6 条 offer 只出自 Hostinger + Hetzner——DigitalOcean 的 droplets 定价页完全读得到，产出是 0 | 需要把"抓取结果"（`source_checks`）和"促销结果"（`offers`）**分开存两处**。只有 offers 数组的站，抓不到就写成"这家今天没促销"，把"页面没取到"和"取到了但真的没促销"混成一件事。分开存才写得出中间这一态 |
| A4 | **三条 Contabo URL 全部不可读，但其中一条的路径本身就是事实：`/en/server-outlet/`**。`outlet` 这个词说明这家厂商确实有一个二手/清仓机页面——我们一条数据都没抓到，却已经知道这个页面存在、叫什么、挂在哪。抓取失败不等于零产出 | 需要把**失败的那条 URL 原样存下来**（我们把 8 条 `source_checks` 的 url 全留了）。只展示成功结果的站，永远不会让读者看到"这 3 个地址我们试了但进不去"，更不会指出其中一条叫 server-outlet——那恰恰是读者能自己点进去验的东西 |
| A5 | **我们的"更新于"时间，比我们的数据新**。本次 `source_scan_at` 是 `18:34:16`，最新一条 offer 的 `fetched_at` 是 `18:34:09`——文件上的时间戳比最新数据晚 7 秒；当天几次 scan 里这个差值在 4–7 秒之间浮动 | 需要 scan 级和 offer 级两个时间戳同时存在才能做这个差。只有 offer 级时间戳的人做不出；只有 scan 级时间戳的人（绝大多数站）压根不知道自己的"Updated 5 minutes ago"是**写文件**的时间，不是**数据**的时间 |

### B. 谷歌搜索查词（今天真跑过的）

| query | SERP 上看到了什么 | 判断 |
|---|---|--|
| `vps deals` | **核心词**。今天只返回 **2 条**（昨天 5 条）：spacevps.cc/deals、vpshub.org/zh/0_100/。**vpsdeck、uvps、vpsclub 全部掉出前五，英文位归零**。且 vpshub 页面自己写着"数据更新于 **2026-10-10**"——今天 10-13，一个按日更新的 deals 页挂着 3 天前的日期 | 核心词锁 28 天不动。SERP 变薄说明这个词的竞争正在洗牌。**vpshub 自曝 3 天未更新**是 A5 的外部佐证 → 与 A5 合并成明日候选 #2 |
| `cheap vps black friday 2026 deals` | 5 条：vpspaihang.com（中文，黑五汇总 + 前瞻各一篇）、**vpsledger.com/black-friday-vps-deals/（英文，"Verified Against Official Pages"，"188 plans verified as of 2026-10-10"）**、hostadvice.com/vps/black-friday/（英文）、**vpsledger.com/black-friday-vps-deals-2026/（英文 tracker，"across 13 providers"，明写 "**Sale prices are TBA until verified**"）** | **黑五（11/27）旺季已经开打，英文位出现 3 条**。关键发现：离黑五还有 6 周，deals 站已经开始发 tracker 页，而价格栏是空的 → **全新角度，升为明日候选 #1** |
| `hetzner server auction dutch auction price drop starting price` | 5 条：docs.hetzner.com（官方 FAQ）、hetzner.com/blog（官方博客）、**akua.dev/servers/hetzner-auction（英文第三方，"ranked by CPU benchmark per euro, with the time of each next price drop"）**、**radar.iodev.org/guide（英文第三方完整指南）**、hetzner.com/sb（官方拍卖页） | **Hetzner 拍卖的英文位今天明显变挤**：Day6 时只有官方两页 + 1 条中文，今天多出两个英文第三方工具站，且都做了"下次降价时间 / 价格历史"。"拍卖怎么运作"已被完整覆盖 → **Day6 候选 #2 今日降级（见下），改角度再写** |
| `vps student discount eligibility verification proof required` | 5 条：vpscost.com（中文）、world.taobao.com 英文导购页 ×2、help.aliyun.com（阿里云学生认证）、csdn（中文）。**英文母语内容 0 条** | 学生折扣——也就是 VPS 定价页上唯一一个把你带离本页的链接（Day6 A4 同源）——英文侧完全没人写。缝真实存在，但搜索量看起来很薄 → **留池，优先级低于黑五** |
| `lowendtalk yabs benchmark results how to read` | 5 条：csdn 中文搬运 ×2、**lowendtalk.com/discussion/183625（英文原帖）**、**lowendtalk.com/discussion/177260 "How to read a YABS score"（英文原帖）**、github.com/masonr/yet-another-bench-script | **英文位只有 LET 原帖和 GitHub，0 篇英文教程型文章**讲"怎么读 YABS 结果"。而 LEB 自己说 ServerVerify 库里有 1 万份用户提交跑分——有量、没人教怎么读 → **剩余候选「YABS 怎么读结果」今天拿到硬证据，升为明日候选 #3** |
| `vps renewal price increase grandfathered locked pricing existing customers` | 5 条：**getcloudworth.com/en/guides（英文，5 signals）**、solopreneur.global（中文，祖父价）、vps-craft.com（中文，续费陷阱）、payproglobal（中文）、likacloud（中文，Netcup 涨价） | 英文位只有 1 条，且它是中文站的英文版（通篇 `old-user tax` / `old customer tax` 这种直译口径）。真·英文母语内容几乎空缺 → **有价值但不升候选**：10-12 刚发 `vps-deals-auto-renewal-notice`，Day5 的"四种折扣结束方式"也还在池里，先不重复开题 |

### C. 老外怎么说（真在用的说法）

| phrase | 谁在用 / 什么意思 |
|---|---|
| "**Despite the name, there is no bidding.**" | radar.iodev.org 英文第三方指南原文：拍卖其实没有竞价——这是英文圈解释 Hetzner 拍卖时最爱用的一句开场 |
| "Each listing **starts at a fixed price for its model** and the price then drops at **randomized intervals** until someone orders the server" | 同上原文：站到了 Hetzner **官方文档**那一侧（固定起价），与官方博客 "start out low" 相反——第三方工具站实测后选了 docs 的说法 |
| "**Once it's ordered, it's gone** — identical configurations may reappear later, but there is no way to predict when" | 同上原文：卖掉即消失，同配置何时再来不可预测 |
| "Hetzner does not document a **minimum price** or a **maximum listing duration**, so waiting for a lower price is always **a gamble against other buyers watching the same listing**" | 同上原文：没有底价、没有最长挂单时长，等低价是在跟盯同一台的人赌 |
| "monthly pricing with **no setup fee and no minimum contract term**, a dedicated 1 Gbit/s uplink with **unlimited traffic**" | 同上原文：拍卖机的标准条款三件套，英文站复述时几乎一字不改 |
| "provisioning usually **within one business day** — often much faster, since the hardware is **already racked**" | 同上原文：交付快的理由——机器本来就插在机架上 |
| "The primary IPv4 address is a **removable add-on** (€1.70/month) — ordering **IPv6-only shaves that off** the monthly price" | 同上原文：IPv4 是可拆的加购项，`IPv6-only` 是压月租的标准做法，`shave off` 是那个动词 |
| "also known as **Server-Bidding** or **Serverbörse**" | 同上原文：德语原名 Serverbörse，英文圈两种叫法并存 |
| "**Defective hardware is replaced free of charge** during the contract" | 同上原文：二手机的硬件保修口径 |
| "roughly **3% on auction listings**, applied to **new orders and existing contracts alike**" | 同上原文（引 Hetzner 2026-02 涨价公告）：涨 3%，且新单和老合同一起涨 |
| "server **DRAM contract prices rose over 40%** in late 2025" | 同上原文：涨价的真实原因是内存合约价 |
| "individual listings still get cheaper the longer they sit, but **the overall price level has shifted upward**" | 同上原文：单台越挂越便宜，但整体水位上移——两句要一起读才对 |
| "When a listing **disappears between two snapshots**, we know it was taken" | 同上原文：**用快照差值判定成交**——这正是我们 A1 那套方法的第三方版本 |
| "a far better signal of what a server is actually worth than **asking prices** alone" | 同上原文：成交价（sold price）比挂牌价（asking price）有意义 |
| "When a type is sold out, **the order simply fails**: there is **no waitlist, no restock announcement**, and no way to see … whether a type has been gone for an hour or a month" | 同上原文：缺货的三连否定。这是英文位第一次有人把"没有候补名单、没有补货公告"讲出来 |
| "whether a sold-out type **blips back** several times a day, **returns in bursts**, or has been gone for a month" | 同上原文：`blips back` / `returns in bursts` —— 描述补货节奏的两个原生说法 |
| "**Stringing those snapshots together is what turns a price tag into a story.**" | 同上原文：把快照串起来才让一个价签变成一段故事 |
| "A €45 listing can be **expensive** if the same configuration regularly hits €38" | 同上原文：绝对价格没有意义，要看同配置的历史区间 |
| "**slam the cpu 24/7**" | LowEndTalk "How to read a YABS score" 帖原文：能不能把 CPU 压满跑——低端机的关键判断 |
| "as long as that score **doesn't go below 500** you got a good deal" | 同上原文：GB5 单核 500 是"没买亏"的下限 |
| "for an average vps everything in the range of **600-800 seems okay**, especially if the **multicore score scales properly**" | 同上原文：普通 VPS 的合理区间 |
| "if you get 4 cores, multi core result should be **2.5-3.5x of single core** to make it a good one" | 同上原文：**用多核/单核比值判断核心是不是真的给你**——社区真这么算 |
| "**E5 won't get there**" / "**don't buy an E5 and complain about the 'bad GB score'**" / "you simply picked the wrong product" | 同上原文：E5 跑不出高分是预期内的，买了再抱怨是你选错了产品 |
| "As long as you are getting **the expected gb5 for the cpu model** then it's alright" | 同上原文：正确读法是"跟这颗 CPU 应有的分数比"，不是跟绝对数比 |
| "**moooaaar is always better**" / "**MOARRRRRRRRRRRRRRRRRRRRRRRRRR**" | 同上原文：社区对跑分的通用起哄方式，拉长元音表示"越多越好" |
| "**GB4** / **GB5**"（Geekbench 代际简称）+ "**Full Test \| https://browser.geekbench.com/v5/cpu/…**" | 同上原文 + YABS 输出格式：社区直接说 GB 分数；贴跑分必须带 Full Test 链接供人验 |
| "**AES-NI : ✔ Enabled**" / "**VM-x/AMD-V : ✔ Enabled**" | YABS 输出头部字段原文：先看这两个勾，再谈跑分 |
| "**UptimeRobot Raised Pricing by ~62% Any one got Email?**" | LowEndTalk 首页标题原文：涨价帖的标准写法——给出百分比 + 问有没有收到邮件 |
| "**Kimsufi/Soyoustart/OVH Rise New Price**" | LET 首页标题原文：涨价帖另一种写法，`Rise New Price`（主谓倒装，社区味） |
| "**xTom VPS lost my entire virtual disk during maintenance – no backups available**" | LET 标题原文：丢数据投诉的三段式（丢了什么 / 什么场景下 / 没有备份） |
| "**Metanet.ch - Unreachable/Bankrupt**" | LET Outages 区标题原文：厂商倒掉就用 `Unreachable/Bankrupt` 两个词并列 |
| "**Regular VPS Restock**" / "**VPS Restock**" / "our popular plans are **back**!" | LET 首页 DeluxHost 两条 + 另一家标题原文：补货的栏目式说法 + `back` 写法 |
| "**Per Minute Billing**" / "**Hourly Billing**" / "**10.10 Deal**" | LET 首页标题原文：计费粒度与节日促销的写法（10.10 = 双十） |
| "**UNMETERED BW**" / "**25G Unmetered**" / "**NAT VPS**" / "**NAT LXC VPS**" | LET 首页标题原文：带宽与 NAT 类产品的固定标法 |
| "**paid up to Sept 2027**" | LET Service Transfers 区标题原文：转让帖必须写明"已付到哪个月" |
| "**Bring Your Own Server**" / "**WTB:**" / "**crypto, month-to-month**" | LET 首页原文：自带机器、求购缩写、支持加密货币且按月付 |
| "**DeluxHost review: 6 VPSes, ~5 weeks, a lot of tickets**" | LET Reviews 区标题原文：评测帖的三段式（几台 / 多久 / 多少工单） |
| "**$1.83/Month First Year**" / "**25% off 3 months**" / "**Exclusive LowEndBox Pricing**" | LowEndBox 首页标题原文：折扣时长必须写出来；`Exclusive … Pricing` 是站方专属价的标法 |
| "**1GB VPSes … starting at only $9.95/year! Those are IPv6-only, but they have IPv4 as well for only $17.95 a year!**" | LEB 正文原文：**IPv6-only 与含 IPv4 是两种价**，英文站会主动把差价讲出来 |
| "You'll need our **special coupon code** to get these deals!" | LEB 原文：用码是默认前提，不是附加信息 |
| "**old-user tax**" / "**old customer tax**" / "**premium rate**" / "**loyalty tax coefficient**" | getcloudworth 英文指南原文：给"老用户被宰"起的四个名字，其中 premium rate 是 FinOps 借来的术语 |
| "**silent downgrade**" / "**neighbors are stealing CPU**" / "you may have been **scheduled to an oversold node**" | 同上原文：不降配、不涨价，但把你挪到超售节点——隐性降级的三种说法 |
| "**Don't renew on sentiment; choose your path with data.**" | 同上原文：续费决策的口号句 |
| "**stop the instance but don't release it**, save a snapshot, and contact them again a few days later" | 同上原文：谈判技巧——停机但不释放，等挽留券 |

### 明日候选

1. **"Sale Prices Are TBA Until Verified": What the 2026 Black Friday VPS Trackers Actually Tell You Six Weeks Out** — B2（英文 tracker 已上线、价格栏写 TBA、"188 plans verified"、13 家 providers）+ C 栏 LET 首页三条黑五帖（`Black Friday 2026 - Wishlist Thread` / RackNerd `TRENDING NOW` / `[Request] … (Black Friday?)`）。缝：黑五还有 6 周，英文站已经开始发 tracker 页但一个价格都填不出来——**没人写"预售期 tracker 页本身"这个现象**
2. **"Updated 5 Minutes Ago" Is a Lie You Can Check: How to Read a Deals Site's Timestamp** — A1（5 次扫描 18 小时零变化）+ A2（6 条 offer 只来自 2 次读取）+ A5（scan 戳比数据晚 4–7 秒）+ B1（vpshub 页面自曝"数据更新于 2026-10-10"，3 天未更新）。缝：所有 deals 站都把"更新于"当卖点，**没有任何一篇教读者去验它**，而我们有一手对照数据
3. **How to Read a YABS Score: The Numbers LowEndTalk Actually Argues About** — B5（英文位只有 LET 原帖 + GitHub，0 篇英文教程）+ C 栏 LET 原帖原文（`slam the cpu 24/7` / 500 下限 / 600-800 区间 / 多核应为单核 2.5-3.5x / `E5 won't get there` / `moooaaar`）。缝：LEB 说库里有 1 万份跑分，但英文世界没有一篇"怎么读"

已用：`compare-vps-deals-total-cost`（10-07）、`vps-deals-renews-at-x`（10-08）、`vps-deals-refund-window`（10-09）、`vps-deals-cost-per-gb-ram`（10-09）、`vps-deals-who-collects-vat`（10-09）、`vps-deals-hourly-to-monthly`（10-10）、`vps-deals-cost-per-gb-disk`（10-11）、`vps-deals-auto-renewal-notice`（10-12，**最后一篇已发布**）。

已降级/不再写第二篇：退款天数（已发）、每 GB 单价（已发）、renews at 换算（已发）、Hourly ×672/730（已消耗）、CPU steal 诊断（英文位占满）、过期 deal（pennyclouds 已占）、Unmetered Port Metered Reality（Day2，英文位占满）、Stuck in an AI Support Loop（Day3，SERP 被 SaaS 页占满）、**Hetzner 拍卖"怎么运作"（Day6 候选 #2，今日降级：B3 实测英文位新增 akua.dev 与 radar.iodev.org 两个第三方工具站，"no bidding / 固定起价 / 随机降价 / 每次降价时间"已被完整覆盖。若重写只能走我们独有的"同一天 5 次快照"角度，不能写科普）**。

剩余候选（未被消耗）：学生折扣（B4，英文位 0，优先级低于黑五）；"Automatically Reverts to Standard Pricing" 四种折扣结束方式（Day5 候选 #2，仍无新证据）；低价套餐断货/补货（Day6 候选 #1，**今日缩范围**：radar.iodev.org 已把 Hetzner Cloud 那一半写掉，只剩"跨厂商通用断货现象"可写，且要改用 `no waitlist, no restock announcement` 这个英文原生说法切入）。

---

## 2026-10-14 (Day 8)

### A. 原创内容邪修

| # | 邪修点 | 为什么别人抄不走 |
|---|---|---|
| A1 | **六天 39 次扫描，库存只变过一次，而且那一次是 +1（新增），不是替换**。我们把 git 里从 `2026-10-07T18:33:30Z` 到本次 `2026-10-13T18:37:52Z` 的 39 次独立快照全部取出，对每条 offer 的 `provider + title + offer_url + source_url` 做逐字节签名——**只得到 2 种签名**。分界点精确落在 `2026-10-08T12:37:03Z`：此前 7 次扫描是 5 条（全 Hostinger），此后 32 次扫描是 6 条（多出 Hetzner 拍卖那条）。也就是说：此后连续 **5 天、32 次扫描，一条没增、一条没删、标题一个字没改**。Lumafare 这个促销雷达，六天里库存只发生过一次**单向增加** | 必须保留 39 份原始快照并对同一组字段做逐字节 diff，才说得清"只变过一次"。deals 站只存当前状态，没有历史，既无法证明"没变"，也说不出"变的那一次是什么"。更难的是意愿：公开写明"我五天的库存净变化是 +1 条"等于自曝更新极慢，商业 deals 站的收入模型不会允许 |
| A2 | **我们的数据结构里根本没有"折扣"这一列**。每条 offer 只有 5 个字段：`provider`、`title`、`offer_url`、`source_url`、`fetched_at`。**没有 price，没有 expiry，没有 coupon/code**。我们存的是"某个官方页面上声称有折扣"这个事实，不存"打几折、到哪天、用什么码"。这是项目规则 `omit unknown prices and expiry dates` 落到 schema 上的直接结果 | 需要愿意让数据结构**缺列**。任何靠展示 "$X off / ends in N days" 拿转化的 deals 站，schema 里一定有价格列和到期列——那是它的商业模式。反过来，把"Lumafare 没有价格列，所以我们永远不会给你一个编出来的数字"公开写出来，是自断卖点，但恰恰是读者最该知道的事：一排字段摊开给他看，他就能自己判断这个站会不会编数 |
| A3 | **首推位在 39 次扫描里 39 次是同一条，而那条 deal 上没有任何数字**。`offers[0]` 在全部 39 份快照里都是 Hostinger 的 `Student discount`——排在最前面的条目，标题里没有百分比、没有价钱，是全场 6 条里唯一一个"资格类"条目（其余 5 条要么带 70/67/63/65% 的数字，要么来自拍卖页）。一个价格雷达的第一名，是一条不含价格的条目，而且六天没换过 | 需要"顺序"是采集时的原始顺序且被原样保留。绝大多数 deals 站会按折扣力度、价格或佣金重排，首推位每次刷新都在变，压根不存在"六天同一条"这回事。而"我们排名第一的 deal 上没有任何数字"这句自曝，商业站不会写——它宁愿把学生折扣挪到页面角落 |
| A4 | **我们看不见什么，是可以算出来的：最长盲窗 6 小时 10 分**。把 39 个 `source_scan_at` 两两相减：最短间隔 **4.8 分钟**，中位 **260.8 分钟**（4h21m），最长 **370.3 分钟**（6h10m），另有 5 个间隔落在 367–370 分钟。结论很硬：**任何存活时间短于 6 小时的闪购，这套采集必然错过**。这不是认错，是把观测边界量化给读者看 | 必须把每一次 scan 的起始时间戳当数据存下来（我们把 `source_scan_at` 写进文件并随 git 留档），才可能算出间隔分布。只展示"最后更新时间"的站算不出自己的盲窗，更不会公布"我漏得掉短于 6 小时的活动"——那是把读者推给竞品的话 |
| A5 | **8 个来源里唯一"路径自带 deal 语义"的，恰好是我们完全读不进去的那个**：`https://contabo.com/en/server-outlet/`。今天从厂商官网自己的页脚导航确认了它的对外名字——**`Server Deals`**。也就是说，这家厂商明确有一个名为 Deals 的清仓入口，我们登记了它、也试了它，`readable: false`，一条数据没拿到。同一厂商的另外两个入口（`/en/`、`/en-us/pricing/`）同样 `false`。8 个来源中 3 个可读、5 个不可读，而唯一叫 Deals 的那个在不可读侧 | 必须把**失败的那条 URL 原样存下来**（8 条 `source_checks` 一条不删），并且要真的去厂商官网核对它在导航里叫什么。只展示成功结果的站永远看不到这一层；更关键的是，指出"有个叫 Server Deals 的页面我们进不去"其实是给读者一个他自己能点进去验的入口——这是把失败转成可用的唯一写法 |

### B. 谷歌搜索查词（今天真跑过的）

| query | SERP 上看到了什么 | 判断 |
|---|---|--|
| `vps deals` | **核心词**。今天 5 条，且**英文位从昨天的 0 条反弹到 3 条**，全是全新面孔：**vpsticker.com**（"Independent VPS price radar — real prices from public sources **updated every 6 hours**"，但页面自己写着 `last refresh **2026-10-02**`）、**vpsfilter.com**（"Updated daily"）、**rackbazaar.com**（"The bazaar for VPS deals"，"3 providers, 9 plans. Updated daily. **No dark patterns**"）。昨天的两个中文站 spacevps/vpshub 全掉 | 核心词锁 28 天不动。**今日最大外部发现：vpsticker 声称 6 小时刷新一次，页面上的 last refresh 却是 11 天前**——这正是我们 A4 盲窗话题的第三方活证据，直接进明日候选 #2 |
| `cheap vps black friday 2026 deals tracker verified` | 5 条：**contabo.com/en-us/black-friday/（厂商官方，标题 `Black Friday Deals Coming Soon!`）**、ovh.com/asia/black-friday/（厂商官方）、vpsticker.com、bloggingjoy 黑五汇总、moonglowsoftware AI 工具券页 | **黑五线今天拿到全新一类证据：厂商官方的"预热落地页"**。Contabo 的黑五页已经上线，但价格栏里放的是**常规价**（`$5.28 for the first 24 months`），一句黑五价都没有 → 与 vpsledger 的 "Sale prices are TBA until verified" 互证，**明日候选 #1 证据链完整了** |
| `vps hostinger student discount eligibility proof required verification` | 5 条：**抖音 Gemini 学生认证话题**、GitHub 中文 SheerID 验证工具、freevps.edu.pl、PHP中文网 Perplexity Pro 学生折扣、DreamHost 一个 promo 落地页。**真正在讲 VPS 学生折扣资格的英文内容 0 条** | 和昨天结论一致，英文位仍为 0 且今天更脏（被 AI 工具学生认证内容挤占）。缝是真实的，但**这条缝只在我们自己的数据里成立**（A3：它是六天不变的首推位）→ 升为明日候选 #3，写法必须走"我们的一手数据"，不能走科普 |
| `vps deal page stale outdated last updated price no longer available` | 5 条：DreamHost "Best VPS Hosting: 10-Point Buyer's Checklist"（**英文买家清单，但通篇不讲数据新鲜度**）、serverdeal.net（**"Price re-checks ⚡"** 标签，英文）、Atlassian API changelog（噪声）、vpsdime、GitHub pbgui。**讲"deals 站数据会过期 / 怎么识别过期"的英文文章 0 条** | **今天挖到的最大空白**。全英文长文在讲怎么挑 VPS，没有一篇讲"你正在看的这个价格有多旧"。serverdeal.net 已经把 "Price re-checks" 当卖点挂在页面上，却没人把它展开成文章 → **与 A1/A4 合并成明日候选 #2** |
| `lowendtalk yabs benchmark results how to read score` | 5 条：Intel "How to Read and Understand CPU Benchmarks"、UCSF Chimera benchmark 文档、Basemark Web、vpsbenchmarks.com/yabs（**"Most Recent Yab Runs"，英文跑分库**）、CSDN 中文 YABS 指南。**昨天还在前五的两条 LET 原帖今天全部掉出** | YABS 英文位**波动极大**：昨天是 LET 原帖，今天是通用 CPU 基准科普。唯一稳定存在的英文资产是 vpsbenchmarks 的跑分**库**（不是教程）。"怎么读 YABS" 的英文教程位仍空着 → **留在池里，今天不升候选**（已有更强的两个新题） |
| `vps restock out of stock waitlist notification low end` | 5 条：MB Aura 音箱 "Out of Stock · Join the Waitlist"、NetSuite backorder 词条、Shopify "Notify Me!" 插件、WooCommerce 候补插件测评、雨果网 eBay 库存文。**VPS 相关结果 0 条，全是零售电商** | **今日降级**。这个 query 被电商语义 100% 占满，说明 `waitlist` 在英文里是零售词——VPS 世界根本没有候补名单（与 C 栏 radar.iodev.org 的 "no waitlist, no restock announcement" 一致）。缝真实但搜不到人，写了没人来 → **从候选池移除** |

### C. 老外怎么说（真在用的说法）

| phrase | 谁在用 / 什么意思 |
|---|---|
| "**real prices from public sources updated every 6 hours**" | vpsticker.com 英文首页原文：第三方价格雷达自报刷新频率的标准句式 |
| "**last refresh 2026-10-02**" + "**in stock** / **checked 2026-10-02**" | 同上原文：每条 deal 后面挂 `in stock` 和 `checked <日期>`——英文站把"库存 + 核验日期"做成固定后缀 |
| "**Lowest monthly price we could read off each provider's own public pricing page**" | 同上原文：`read off` 是那个动词，强调"从人家页面上读下来的"，不是问来的 |
| "**Prices are pulled as-is — nothing is estimated.**" | 同上原文：第三方站撇清"我不估算"的标准声明句式 |
| "**VPS Deals, read straight from the source**" | 同上 H1 原文：`straight from the source` 是英文站标榜一手数据的固定说法 |
| "**In stock**" / "**Sold out**" / "**In stock · 12 left**" / "**In stock · 1 left**" | rackbazaar.com 英文列表原文：库存标签三档，且**带剩余台数**（`N left`）——比vpsticker 的裸 `in stock` 更细 |
| "`/annual`" vs "`/annually`" | 同上原文：同一张表上两种写法并存，说明英文站的计费周期标签**没有统一规范** |
| "**— TB**" / "**— GB**" | 同上原文：带宽/磁盘未知时的占位写法（破折号 + 单位），不是写 N/A |
| "**compare VPS and dedicated server deals**" / "**View Deal →**" | 同上原文：全网约 120 个列表共用同一个 CTA 字符串 |
| "**Black Friday Deals Coming Soon!**" | contabo.com 官方黑五页标题原文：厂商的**预热页**标准标题 |
| "**High-value hosting that delivers - coming soon.**" / "**skip the slogans and beat the buzzwords**" | 同上原文：预热页的文案套路——先自嘲黑五全是口号，再说自己不玩这套 |
| "**Even our regular prices offer better value than most deals you'll find elsewhere.**" | 同上原文：**预热页没价格可放时，就放常规价并自称比别家促销更划算**——这是黑五预热期的标准动作 |
| "**for the first 24 months**" / "**for the first 12 months**" | 同上原文：折扣期限的写法（首 24 个月 / 首 12 个月），比 "first year" 更长 |
| "**No noisy neighbors.**" | 同上原文（VDS 区块）：`noisy neighbors` 作为卖点被厂商自己写在官网上 |
| "**Server Deals**"（指向 `/en/server-outlet/`） | 同上页脚导航原文：**厂商把 outlet/清仓页对外命名为 Server Deals** |
| "**VPSBenchmarks Verified**" | vpsbenchmarks.com/yabs 跑分列表原文：跑分记录上的**核验徽章**字样 |
| "**Run on: October 13th 2026**" / "**CPU cores:** / **CPU type:** / **RAM:**" | 同上原文：跑分条目的字段标法，日期写法是 `Run on:` |
| "**yabs.sh … is a simple and powerful script that runs Geekbench, Fio and Iperf3 on your server**" | 同上原文：YABS 的英文一句话定义，三个组件名固定 |
| "**You can save, organize and visualize your yabs for free**" | 同上原文：跑分库拉新的句式 |
| "**renews at $49**" | LowEndTalk 首页 D4 Networks 标题原文：`$49/year, renews at $49`——**续费价内联写进标题**，且此处首年=续费 |
| "**Price Locked on Renewal**" | LowEndTalk 首页 [WLX] 标题原文：续费锁价的标准写法 |
| "**lifetime discount**" / "**Lifetime Deal**" / "**LIFETIME LICENSES**" / "**PERPETUAL $1/Year VPS**" | LET 首页多个标题原文：`lifetime` 与 `PERPETUAL` 两种叫法并存，后者全大写做强调 |
| "**No Bait-and-Switch**" | LET 首页 Tier.Net 标题原文：反"低价引流换配置"的自我声明，`bait-and-switch` 是原生词 |
| "**One Time Fee**" | LET 首页 StackCP 标题原文：一次性费用的写法（对比 recurring） |
| "**paid up to Sept 2027**" | LET Service Transfers 区标题原文：转让帖必须写明已付到哪个月 |
| "**VPS Restock**" / "**our popular plans are back!**" / "**More Capacity**" | LET 首页 DeluxHost / 另一家 / LayerOne 标题原文：补货的三种写法，`back` 最口语 |
| "**Unreachable/Bankrupt**" / "**down?**" / "**outage**" | LET Reviews & Outages 区标题原文：厂商出事的三档措辞，最重的一档是两个词并列 |
| "**brand is being retired as of March 2027**" | LET Providers 区标题原文：厂商品牌关停的正式说法，`retired` + 具体年月 |
| "**support has been silent for months - Storage VM keeps getting slower**" | LET 标题原文：投诉帖的两段式（服务静默多久 + 实际劣化现象） |
| "**FLASH SALES**" / "**Limited Flash Offers**" / "**DOUBLE PROMOTIONS**" | LET 首页标题原文：闪促的三种放大写法，全大写 |
| "**Black Friday 2026 - Wishlist Thread**" / "**What will you buy on Black Friday 2026?**" / "**TRENDING NOW: RackNerd's BLACK FRIDAY!**" | LET 首页三条原文：黑五的社区三种句式——许愿帖、提问帖、置顶促销帖 |
| "**[Request] 16TB+ Storage VPS/Dedi \| 1Gbps+ \| $400-500/2yr \| Black Friday**" | LET Requests 区标题原文：求购帖的竖线分隔格式，末尾挂节点名 |
| "**Rent once, see a 30% markup. Even on your own subnet!**" | LET 首页 IPXO 帖标题原文：`markup` 是加价的标准词 |
| "**NAT VPS**" / "**NAT KVMs**" / "**25G Unmetered**" / "**10G FULL UNMETERED**" | LET 首页标题原文：NAT 类与不限量带宽的固定标法，`FULL` 大写加强 |
| "**zero-knowledge**" / "**Encrypted RAM & Disk**" / "**100% Anonymous**" | LET 首页 Servury / Blackbox 标题原文：隐私向 VPS 的三件套话术 |
| "**AI-Ready VPS**" / "**AI Templates**" | LET 首页标题原文：2026 年英文圈的新品类词 |
| "**Exclusive LowEndBox Pricing: 2GB KVM VPS for $1.83/Month First Year!**" | LowEndBox 首页标题原文：专属价 + **First Year** 限定词的组合写法 |
| "**You'll need our special coupon code to get these deals!**" | LEB 正文原文：用码是默认前提，不是附加信息 |
| "**Those are IPv6-only, but they have IPv4 as well for only $17.95 a year!**" | LEB 正文原文：**IPv6-only 与含 IPv4 是两种价**，英文站会主动把差价讲出来 |
| "**Yet Another cPanel and WHMCS Price Increase. But You're Getting More Value. Right? (Right?)**" | LEB 标题原文：涨价的讽刺式写法，`Yet Another` + 两个 `(Right?)` |
| "**Another year, another cPanel / WHMCS price increase.**" | LEB 正文原文：`Another year, another X` 是抱怨年度涨价的标准开场 |
| "**you may not be aware your service is being downgraded.**" | LEB 讲 Microsoft 365 缩存储的正文原文：隐性降配的提醒句式 |
| "**Microsoft Slashes the Storage that Comes with Your 365 Plan by 60%**" | LEB 标题原文：`Slashes … by N%` 是砍配的标准动词搭配 |

### 明日候选

1. **"Black Friday Deals Coming Soon": What a Pre-Landing Page Tells You Before There Are Any Prices** — B2（Contabo 官方黑五页标题 `Coming Soon!`、价格栏放的是常规价 `$5.28 for the first 24 months`、`skip the slogans and beat the buzzwords`）+ Day7 B2 的 vpsledger tracker（"Sale prices are TBA until verified"、"188 plans verified"）+ C 栏 LET 三条黑五句式（`Wishlist Thread` / `What will you buy on Black Friday 2026?` / `TRENDING NOW`）。缝：黑五还有 6 周，**厂商已经在发预热页、第三方已经在发 tracker，但两边都填不出一个价格**——没人写"预热期本身"这个现象
2. **Our VPS Deal Radar Ran 39 Scans in Six Days — Here's Exactly What It Missed** — A1（39 次扫描只有 2 种库存签名，唯一一次变化是 +1）+ A4（最长盲窗 6h10m，可量化）+ A2（schema 里没有 price/expiry 列）+ B1（vpsticker.com 声称 `updated every 6 hours`，页面 `last refresh` 却是 11 天前）+ B4（英文位 0 篇文章讲"deals 页数据有多旧"；serverdeal.net 只把 `Price re-checks ⚡` 当标签挂着，没展开）。缝：所有 deals 站都把"实时/每日更新"当卖点，**没有一篇把自己的观测边界和盲窗算出来给读者看**，而我们有一手快照序列和外部自曝证据
3. **The Deal With No Number On It: Why "Student Discount" Sat at the Top of a Price Radar for Six Days** — A3（39/39 次扫描 `offers[0]` 都是 `Student discount`，全场唯一无数字条目）+ A1（六天库存只 +1，这条从未动过）+ B3（英文位 0 条真内容，SERP 被 Gemini/SheerID 学生认证噪声占满）+ C 栏 LET 的 `No Bait-and-Switch` / `Price Locked on Renewal` / `lifetime discount`（英文圈对"资格类折扣"的三种自证写法）。缝：价格雷达的第一名是一条没有价格的条目——只有握着 39 份快照的人能写出来

已用：`compare-vps-deals-total-cost`（10-07）、`vps-deals-renews-at-x`（10-08）、`vps-deals-refund-window`（10-09）、`vps-deals-cost-per-gb-ram`（10-09）、`vps-deals-who-collects-vat`（10-09）、`vps-deals-hourly-to-monthly`（10-10）、`vps-deals-cost-per-gb-disk`（10-11）、`vps-deals-auto-renewal-notice`（10-12）、`vps-deals-port-25-smtp-blocked`（10-13，**最后一篇已发布**）。

已降级/不再写第二篇：退款天数（已发）、每 GB 单价（已发）、renews at 换算（已发）、Hourly ×672/730（已消耗）、CPU steal 诊断（英文位占满）、过期 deal（pennyclouds 已占）、Unmetered Port Metered Reality（Day2）、Stuck in an AI Support Loop（Day3）、Hetzner 拍卖"怎么运作"（Day6）、**低价套餐断货/候补（Day6 候选 #1，今日正式降级：B6 实测 SERP 被 Shopify/NetSuite/WooCommerce 电商候补内容 100% 占满，VPS 语境 0 条；`waitlist` 在英文里是零售词，写了搜不到人）**。

剩余候选（未被消耗）：YABS 怎么读结果（Day4 候选 #3，**今日未升级**：B5 显示 LET 原帖已掉出 SERP，英文位波动大，唯一稳定英文资产是 vpsbenchmarks 的跑分库而非教程，等 SERP 稳定再开）；"Automatically Reverts to Standard Pricing" 四种折扣结束方式（Day5 候选 #2，仍无新证据）。

---

## 2026-10-15 (Day 9)

### A. 原创内容邪修

| # | 邪修点 | 为什么别人抄不走 |
|---|---|---|
| A1 | **61 次扫描、9 天，8 个受检来源的 `readable` 一次都没变过——而其中有一家从头到尾"能读"，却一次都没产出过 deal**。把 git 里 120 个提交的 `data/offers.json` 全部取出、按 `source_scan_at` 去重，得到 **61 次独立扫描**（`2026-10-05T12:36:04Z` → `2026-10-14T18:49:34Z`）。对每次的 8 条 `source_checks` 做签名：**61 次只有 1 种签名**。也就是说 3 个 `true` / 5 个 `false` 这个格局，九天里一次都没动过。更关键的是：**DigitalOcean 的 `pricing/droplets` 全程 `readable: true`，但 61 次扫描里它产出的 offer 数是 0**——九天里出现过 offer 的厂商只有 Hostinger 和 Hetzner 两家 | 必须同时留档 `source_checks` 和 `offers` 两张表、并跨 61 次扫描对照，才能说出"能读 ≠ 有 deal"。只展示结果的站根本不存在"读到了但没提取出东西"这一层——它会被直接过滤掉。更难的是意愿：公开写"我登记的 8 个来源里 5 个从来没成功过、还有 1 个成功了九年也没给我一条数据"，等于承认这个雷达只有 2/8 的转化率，商业 deals 站不会这么写 |
| A2 | **"6 个 deal" 其实是 3 个网页，其中 4 个 deal 是同一个 URL**。当前 6 条 offer 里 `offer_url` 去重后只有 **3 个**：`hostinger.com/vps-hosting`（4 条）、`hostinger.com/student-discount`（1 条）、`hetzner.com/sb`（1 条）。而那 4 条同 URL 的条目，title 是**同一个模板**——`70% off — Hostinger VPS page` / `67% off ...` / `63% off ...` / `65% off ...`，长度全是 28 字符，只有数字不同。它们是同一张页面上并存的四个百分比，不是四个独立活动 | 需要愿意把 `deal 条数` 和 `实际覆盖页面数` 分开统计并同时公开。任何把条数当 KPI 的站（首页挂 "29 live offers" "23 Current offers" 那种）都不可能自己拆穿自己的计数口径。而"我首页说 6 个 deal，其实是 3 个页面、其中 4 个数字出自同一个页面"这句话，只有握着原始 URL 字段的人写得出来，也只有愿意自曝的人敢写 |
| A3 | **我们展示的 6 条 deal 里，有 2 条指向我们从不复核的页面**。每天受检的是配置里写死的 8 个 URL；而 6 条 offer 的 `offer_url` 中有 **2 条不在这 8 个里面**：`https://www.hostinger.com/student-discount` 和 `https://www.hetzner.com/sb`。这两条是从受检页面（`vps-hosting` / `hetzner.com/hosting/`）上**顺手捡到的外链**——我们存了它、展示了它，但九天 61 次扫描里**从未把它当作受检来源去复核过一次** | 必须把"受检清单"和"展示清单"作为两套数据分别留档，才看得见这两个集合不相等。绝大多数 deals 站压根没有"受检清单"这个概念——它的展示列表就是它的全部。而指出"我展示的链接里有三分之一我自己不复核"是自曝短板，同时也是把这两个 URL 变成读者能自己点进去验的东西；这是唯一能把失败写成可用信息的写法 |
| A4 | **我们"扫描全球 VPS 促销"这个动作，最长 3 秒**。拿每次扫描内首条与末条 `fetched_at` 相减（harvest span），61 次扫描的分布是：**0 秒 × 24 次、1 秒 × 7 次、2 秒 × 29 次、3 秒 × 1 次**——没有一次超过 3 秒。这不是因为我们跑得快，是因为我们只读 8 个写死的 URL。3 秒这个数字本身就是采集范围的度量衡 | 必须把每一条 offer 的 `fetched_at` 原始存下来（而不是只存一个"全站更新时间"），才可能算出单次采集的真实跨度。展示"Updated daily / every 6 hours"的站算不出自己的 harvest span，更不会公布——因为"3 秒"这个数字一旦写出来，读者立刻知道这个雷达只看了 8 个页面 |
| A5 | **页面上那个"更新于"，其实是收尾时间，不是开始时间**。61 次扫描里 `source_scan_at` 始终**晚于**当次最后一条 `fetched_at`，滞后量分布为 **3–10 秒**（7s × 17 次、6s × 11 次、8s × 9 次、5s × 9 次、4s × 8 次、9s × 4 次、10s × 2 次、3s × 1 次）。即：读者看到的"最后更新"比真实抓取时刻晚几秒，而这几秒是写盘与落库的开销，不含任何采集 | 需要同时保留"扫描时间戳"和"每条记录的抓取时间戳"两个时间维度并逐次相减。只存 `last_updated` 的站无法把开始与结束拆开，也不会去算——因为"我给你的更新时间比你以为的晚 3 到 10 秒"听起来像在给自己的可信度打折 |

### B. 谷歌搜索查词（今天真跑过的）

| query | SERP 上看到了什么 | 判断 |
|---|---|--|
| `vps deals` | **核心词**。5 条，英文位 3 条且**与昨天完全同面**：vpsticker.com、vpsfilter.com、rackbazaar.com；另 2 条掉到中文站 vncoupon.com（RackNerd 法国 `$17.98/Year`、CloudCone 标签页）。**vpsticker 首页计数今天升级了：`15 providers tracked` / `29 live offers` / `15/15 providers returning data`，但 `last refresh` 仍然是 2026-10-02**——距今 13 天 | 核心词锁 28 天不动。**"声称 15/15 全部返回数据、页面刷新日期却是 13 天前"这个自相矛盾比昨天更刺眼**，直接进 C 栏与候选 #3 |
| `digitalocean promo code discount official page droplets pricing` | 5 条：`digitalocean.com/pricing/droplets`（官方定价页，第 1）、paperspace.com/pricing、digitalocean.com/products/droplets/cpu-optimized、**docs.digitalocean.com/platform/billing/promo-codes/（官方文档）**、developers.digitalocean.com。官方文档原文：`$5 signup credit`、`No promo code is required.`、`Signup credits expire 90 days after signup.`、`subject to DigitalOcean's Promotional Credit & Discount Terms` | **今天最有用的一条外部证据**：英文位 0 条"DigitalOcean 官方促销/折扣码页"，原因不是我们没搜到——**是它官方确实没有促销码页，只有一个自动发放的 `$5` 注册额度**。这条从外部坐实 A1（DO 全程 `readable: true`，61 次扫描 0 条 offer）→ 升为候选 #1 的佐证 |
| `vps deals site how offers are verified crawl method sources listed` | 5 条：**bestvpsdeal.com（全新英文站，`Best VPS Deal – Current VPS offers, compared with sources and transparent disclosures.`，正文位置写着 `No monitored offers have been published yet.`）**、windowsvps.host、Rakuten 服务条款、Coursera 电商 SEO 文、Chaindesk AI 工具券页 | **英文位第一次出现"把来源与披露当卖点"的 VPS deals 站，而它的库存是 0 条**。缝真实存在、有人想占、没人做成 → 候选 #1 / #3 的外部佐证。（注：该站 WebFetch 两次均 `fetch failed`，只能引用 SERP 摘要，不能引正文） |
| `black friday 2026 vps hosting deals tracker announced prices` | 5 条：**vpsbenchmarks.com/vps_coupons 排第 1，标题 `VPS Coupons and Deals`，正文已有 `Black Friday 2026 VPS Discounts · Current offers 23`**，且**带真实价格与到期日**（Antihost `40 % discount`，`$1.79 / mo`，`Regular: $2.99`，`Expires on November 30 2026`，`Discount only applies to first billing cycle`；BlastVPS `40% OFF Your First Month`，`Expires on November 12 2026`）；其余 liquidweb 券页、blackfriday.org、theblackfriday.website（通用零售） | **Day8 候选 #1 的前提被推翻了一半**：黑五"填不出价格"这回事已经不成立了——vpsbenchmarks 填出了 23 条带价带日期的。**但新缝立刻出现：所有价格后面都跟着同一句 `Discount only applies to first billing cycle`**。黑五线改写为"填出来的价全是首周期价"，不再写"没价格" |
| `hostinger student discount vps eligibility verification sheerd` | 5 条：groupon.co.uk Hostinger 券页（`Eligibility-Based Discounts: Students and Referrals`、`25% Off for Students via Student Beans`、`verifying through Student Beans`）、sharexirfad.com（Somali 课程站，`SHEER20` 码）、hostinger.com 官网、peering.hostinger.com、couponforhost.com | 英文位**首次出现 1 条真内容**，且第一次给出这种折扣的英文名：**`Eligibility-Based Discounts`**，验证渠道是 `via Student Beans`。但它只是券聚合页，不是教程，且**数字是 25%，与我们抓到的 Hostinger 页面百分比完全不是一回事**。Day8 候选 #3 保留在池中，但降到池底（英文位仍仅 1 条聚合页，形不成搜索需求） |
| `hetzner server auction sb price drops how it works bidding` | 5 条，**4 条是厂商自己或官方镜像**：hetzner.com/dedicated-rootserver/brands/（`Prices drop & excitement mounts. Place bids in our Server Auction!`）、hetzner.com 首页（`The clock is ticking! It's this easy: 1. Enter your desired hardware specification... 4. Snap up your offer. But, don't wait too long or somebody`）、docs.hetzner.com/robot/general/server-auction-faqs（`For each server model, Hetzner decides the starting price... Then, over time, the price for that server goes down.`）、serverbidding.com；仅 1 条中文 | **英文位 100% 被厂商自己占满**（3 个官方域名 + 1 个官方镜像）。Day6 已降级的"Hetzner 拍卖怎么运作"**维持降级**——第三方在这个词上写不过官网。但一次采到 4 条硬行话，全部进 C 栏 |

### C. 老外怎么说（真在用的说法）

| phrase | 谁在用 / 什么意思 |
|---|---|
| "**Expires on November 30 2026**" / "**Expires on November 12 2026**" / "**Expires on December 15 2026**" | vpsbenchmarks.com/vps_coupons 原文：券的到期日就写 `Expires on <月 日 年>`，不加介词 |
| "**Discount only applies to first billing cycle**" | 同上原文（Antihost / BlastVPS 两条都挂）：**折扣只作用于首个计费周期**——英文站声明折扣范围的标准句 |
| "**Regular: $2.99**" / "**Regular: $32.40**" | 同上原文：折前价一律标 `Regular:`，不是 `was` / `list price` |
| "**Monthly**" / "**Annual**" 双栏 + "**$1.79 / mo**" / "**$19.44 / yr**" | 同上原文：月付/年付并列展示，单位写法是 `/ mo` 与 `/ yr` |
| "**New customers only.**" / "**First time customers only, first year only.**" | 同上原文：新客限定的两种写法，后者把"新客"与"首年"两个限制叠在一起 |
| "**Valid for new and existing customers for the entire life of the VPS.**" | 同上（Nobull Networks）原文：**终身折扣**的正式写法是 `for the entire life of the VPS` |
| "**This code gives a reoccurring 10% off**" | 同上原文：`reoccurring`（不是 recurring）在英文券站里真实存在，指续费也打折 |
| "**"Apply only once per order" is the limiter, so the coupon can be applied multiple times as long as it is individual orders.**" | 同上原文：解释码的复用规则，`limiter` 是那个词 |
| "**unlimited traffic**" / "**Transfer: Unlimited**" / "**Bandwidth: 1000 Mbps**" | 同上原文：**流量（Transfer）与带宽（Bandwidth）是两行分开写**的，unlimited 只挂在 transfer 上 |
| "**Specifications & Location**" / "**Data Centers:**" | 同上原文：规格区块的固定标题 |
| "**Last updated on October 13th 2026**" | 同上页脚原文：英文券站自报更新日期的句式 |
| "**Black November: Lite plan at a lite price, 40% lighter**" / "**Black Friday? Let it last all autumn!**" | 同上原文：**黑五被拉长整季的写法叫 `Black November`**，2026 年新词 |
| "**Black Friday Promotion: 40% OFF Your First Month**" | 同上原文：黑五促销标题的标准结构（节点 + 数字 + `Your First Month`） |
| "**Nearly a year ago... 10,000 user-submitted reports in its database.**" / "**We recently hit the 10,000 YABS mark.**" | LowEndBox 首页原文：跑分库规模的量级说法，`hit the N YABS mark` 是社区里的固定表达 |
| "**YABS (Yet Another Benchmark Script)**" / "**the largest collection of YABS benchmarks on the planet**" | 同上原文：YABS 全称第一次在今天的素材里被展开写 |
| "**This site is the largest collection of YABS ... A Provider Comparison tool**" | 同上原文：ServerVerify 的英文自我介绍句式 |
| "**Velohost Returns With Even Cheaper Prices!**" / "**Godlike.Host is Back!**" | LEB 首页标题原文：厂商"回归"的固定写法是 `Returns` 与 `is Back` |
| "**I guess Velohost has never heard of inflation. Eight months ago, they were selling a 4GB VPS ... for 3.00€/month. Now they're selling that same package for only 2.60€/month!**" | LEB 正文原文：**"没听说过通胀"是英文圈夸降价的固定梗**，且必须给出 "八个月前的价 → 现在的价" 两个数字 |
| "**all 100 VPS instances have now been given away**" | LEB 正文原文：赠送名额告罄的写法，`given away` 不是 sold out |
| "**A VPS for UNDER $10/YEAR! Wow!**" / "**VPS Under $1/Month USD**" | LEB 标题与导航原文：`UNDER $X/YEAR` 与 `VPS Under $N/Month USD` 两种价位栏目写法 |
| "**Reverse DNS: What Is It Good For? Absolutely Nothing? No, But…**" | LEB 标题原文：自问自答式技术科普标题的固定套路 |
| "**$5 signup credit**" / "**No promo code is required.**" | docs.digitalocean.com 官方文档原文：**没有促销码页时，官方的说法是"注册额度 + 无需码"** |
| "**Signup credits expire 90 days after signup.**" / "**You cannot transfer signup credits to other teams.**" | 同上原文：额度的两条硬限制，期限写法是 `expire N days after signup` |
| "**The credit is visible in the Control Panel's top navigation bar as a Signup Credit balance.**" | 同上原文：余额在 UI 里的呈现方式称为 `Signup Credit balance` |
| "**Last verified 15 Jul 2026**" | 同上页眉原文：**厂商官方文档页自带"上次核验"日期**，格式 `Last verified <日 月 年>` |
| "**Promotional Credit & Discount Terms**" | 同上原文：DO 把促销条款单独成一份法律文件，名字就叫这个 |
| "**Prices drop & excitement mounts. Place bids in our Server Auction!**" | hetzner.com 官方品牌服务器页原文：拍卖的宣传句，`Prices drop` 是官方用词 |
| "**The clock is ticking! It's this easy: 1. Enter your desired hardware specification. 2. Compare offers. 3. Keep an eye on price changes. 4. Snap up your offer.**" | hetzner.com 首页原文：官方四步说明，`Snap up your offer` 是"抢下"的原生动词 |
| "**But, don't wait too long or somebody**" | 同上原文（被截断）：官方制造紧迫感的句式 |
| "**For each server model, Hetzner decides the starting price. When we add a server from that model to the Auction, it always starts at the same price. Then, over time, the price for that server goes down.**" | docs.hetzner.com 拍卖 FAQ 原文：**官方亲口说清"起价固定、随时间下降"**，与"出价"措辞并存 |
| "**Refurbished server for sale in Hetzner Server Auction**" / "**Prices are dropping on our Server Auction.**" | serverbidding.com（官方镜像站）原文：`refurbished` 是翻新机的固定词 |
| "**Eligibility-Based Discounts: Students and Referrals**" / "**25% Off for Students via Student Beans**" / "**verifying through Student Beans befor**" | groupon.co.uk 英文券页原文：**资格类折扣第一次有了名字 `Eligibility-Based Discounts`**，验证方是 Student Beans |
| "**15 providers tracked**" / "**29 live offers**" / "**15/15 providers returning data**" | vpsticker.com SERP 摘要原文：第三方雷达自报覆盖面的三件套写法 |
| "**Best VPS Deal – Current VPS offers, compared with sources and transparent disclosures.**" / "**No monitored offers have been published yet.**" | bestvpsdeal.com SERP 摘要原文：**"带来源 + 透明披露"是英文站的 positioning 话术**，而"尚无受监控 offer 发布"是库存为空时的标准说法 |
| "**Introducing ServerVerify: built with the LowEndTalk community in mind**" | LowEndTalk 置顶原文：新工具发布的社区向措辞 |
| "**10,000 Benchmarks! The Future of ServerVerify: Interview with Jon Biloh**" / "**Have You Checked Out ServerVerify Lately? 10,000 YABS! New Features!**" | LET 与 LEB 各一条原文：**同一件事两个站的标题写法完全不同**（LEB 用陈述句，LET 用第二人称提问） |
| "**DartNode - Countdown to Black Friday - Dedicated Server Deals and Giveaway! Live now!**" | LET 首页原文：黑五倒计时的标准标题结构，`Live now!` 收尾 |
| "**HostBrr \| BF2025 Deals \| AMD Threadripper VPS €15/year**" | LET 原文：**`BF2025` 是黑五的社区缩写**，直接当前缀用 |
| "**Countdown to Black Friday**" / "**TRENDING NOW: RackNerd's BLACK FRIDAY!**" / "**Black Friday 2026 - Wishlist Thread**" | LET 首页三条原文：黑五的三种社区句式（倒计时 / 置顶促销 / 许愿帖） |
| "**ph24 first vps deal in 2026 + flash sale**" / "**End of Summer Sale \| Free Bonus + Giveaway Inside \| Up to 55% Off**" | LET 首页原文：**节点促销的两种命名法：`flash sale` 与 `<季节> Sale`** |
| "**Check every day for new chickens across USA**" | LET 首页原文：**`chickens` 是 LET 圈内对"上架机器"的黑话**，字面是完全无关的词 |
| "**Oplink 100% price increase**" / "**UptimeRobot Raised Pricing by ~62% Any one got Email?**" | LET 讨论区原文：涨价的两种写法——`N% price increase` 与 `Raised Pricing by ~N%`，后者带 `~` 表示约数 |
| "**Prometeus brand is being retired as of March 2027**" / "**Are providers winding down their operations in Russia?**" | LET 原文：**退出用 `retired`（品牌）与 `winding down`（业务）两个不同的词** |
| "**Metanet.ch - Unreachable/Bankrupt**" / "**VSYS Ukraine down?**" / "**Servarica down?**" / "**HostHatch (web console) down?**" | LET Outages 区原文：故障的四档措辞，从 `down?`（疑问）到 `Unreachable/Bankrupt`（并列判定） |
| "**SoftBank-owned IDCF Cloud Hit by Ransomware: East-1 Wiped**" | LET 原文：安全事故的标题写法，`Hit by` + `Wiped` |
| "**WebyStrata's $51.98 "Lifetime Web Hosting" — legit or a trap? What I could verify.**" | LET Reviews 区原文：**`legit or a trap?` 是质疑终身套餐的固定问法**，后半句 `What I could verify` 限定自己只讲可验证部分 |
| "**DeluxHost – Unusable VPS due to severe disk I/O, refund requested – Order #21899**" | LET 原文：投诉帖的三段式（现象 + 诉求 + 订单号），订单号是硬证据 |
| "**HostDZire IPv6 Allocation Violation: Service Terminated After Configuration Error**" | LET 原文：**`Service Terminated After ...` 是官方/社区通报停服的写法** |
| "**MXRoute bulk closing support tickets**" | LET 原文：`bulk closing` 指批量关单，是负面信号词 |
| "**Looking for a Hetzner Alternative? Compare Our Cloud VPS**" | LET 厂商帖原文：竞品替代的标准开场 `Looking for a X Alternative?` |
| "**[Update] K.N Cloud — LET Cloud VPS Offers in Miami, Frankfurt & Amsterdam \| Hourly Billing**" / "**CloudBlast WORKERS ARE LIVE! App Platform, Per Minute Billing**" | LET 原文：**`Hourly Billing` 与 `Per Minute Billing` 是计费粒度的两种标法**，后者更细 |
| "**DeluxHost.net \| VPS Restock \| Improved Storage Servers!**" | LET 原文：`VPS Restock` 是补货帖的固定前缀标签 |
| "**[WTB]**" / "**[Request]**" / "**[$600] Looking for OVH KS-MYSTERY 128GB**" / "**[$1000] Wanted OVH KS-MYSTERY E-2288G**" | LET Requests 区原文：**`[WTB]`（Want To Buy）与 `[$N]`（预算）是求购帖的固定前缀**，`KS-MYSTERY` 是 OVH 清仓系列的专有叫法 |
| "**I want a 512mb ram VM/box**" / "**i wanna buy ipv4 in miami**" | LET 原文：求购帖里 `VM/box` 与 `ipv4` 都被当成可数名词用 |
| "**Own Datacenter**" / "**Since 2016**" / "**Since 2017**" | LET 厂商标题原文：**自建机房与经营年限是英文圈的默认信任信号** |

### 明日候选

1. **"6 Deals, 3 Pages, 8 Checked URLs": Exactly What This VPS Radar Can and Cannot Re-Check** — A1（61 次扫描只 1 种 `source_checks` 签名；DigitalOcean 全程 `readable: true` 却 61 次 0 条 offer）+ A2（6 条 offer 只来自 3 个 URL，4 条同 URL 且同模板 70/67/63/65）+ A3（2/6 的 `offer_url` 不在受检清单里）+ B2（DO 官方文档 `No promo code is required.` / `$5 signup credit` / `expire 90 days after signup`——它真的没有促销码页）+ B3（英文站 bestvpsdeal.com 把 `compared with sources and transparent disclosures` 写在标题里，`No monitored offers have been published yet` 写在正文里）。缝：**每个 deals 站都在说"我们有来源"，没有一个告诉你"我展示的链接我自己复不复核"**——因为只有把受检清单和展示清单分开存的人才答得出来
2. **The Same Hostinger Page Said 70% to Us and 10% to Everyone Else** — A2（我们对 `hostinger.com/vps-hosting` 这一个页面存了 4 个百分比：70 / 67 / 63 / 65，四条 title 长度全为 28 字符）+ C 栏 vpsbenchmarks.com/vps_coupons 同期原文（同一个厂商、同一个 URL：`10 % discount`、`10% off on all VPS plans when selecting 12m + subscriptions`、`First time customers only, first year only`、码 `VPSBENCHMARKS10`）+ B5（groupon 英文页给的是第三个数字：`25% Off for Students via Student Beans`）+ C 栏 `Discount only applies to first billing cycle` / `Regular:` / `for the entire life of the VPS`。缝：**同一家厂商的同一个页面，不同采集者读出来的折扣相差 60 个百分点**——没人愿意写这个，因为它等于承认"折扣数字取决于你怎么读那一页"
3. **"Last Updated" Is a Finish Time: What a 3-Second VPS Deal Scan Actually Covers** — A4（61 次扫描 harvest span 分布 0s×24 / 1s×7 / 2s×29 / 3s×1，最长 3 秒）+ A5（`source_scan_at` 恒定晚于末条 `fetched_at` 3–10 秒，7s 最多见）+ B1（vpsticker.com 首页 `15/15 providers returning data` 与 `last refresh 2026-10-02` 并列，相差 13 天）+ B3（bestvpsdeal.com 声称透明披露但库存 0 条）+ C 栏 `Last updated on October 13th 2026` / `Last verified 15 Jul 2026`（英文站自报日期的两种句式）。缝：**所有站都把"更新频率"当卖点，没有一个解释自己的"更新于"到底指什么、一次更新覆盖了几个页面**

已用：`compare-vps-deals-total-cost`（10-07）、`vps-deals-renews-at-x`（10-08）、`vps-deals-refund-window`（10-09）、`vps-deals-cost-per-gb-ram`（10-09）、`vps-deals-who-collects-vat`（10-09）、`vps-deals-hourly-to-monthly`（10-10）、`vps-deals-cost-per-gb-disk`（10-11）、`vps-deals-auto-renewal-notice`（10-12）、`vps-deals-port-25-smtp-blocked`（10-13）、`vps-deals-sla-credit-how-to-claim`（10-14，**最后一篇已发布**）。

已降级/不再写第二篇：退款天数（已发）、每 GB 单价（已发）、renews at 换算（已发）、Hourly ×672/730（已消耗）、CPU steal 诊断（英文位占满）、过期 deal（pennyclouds 已占）、Unmetered Port Metered Reality（Day2）、Stuck in an AI Support Loop（Day3）、低价套餐断货/候补（Day6）、Hetzner 拍卖"怎么运作"（Day6，**今日二次确认维持降级**：B6 英文位 4/5 是厂商官方域名或官方镜像，第三方写不过官网）、**黑五"预热期填不出价格"（Day8 候选 #1，今日改写：B4 显示 vpsbenchmarks 已挂出 `Current offers 23` 且带价带到期日，原前提不成立；若再写黑五只能走"填出来的价全是 `first billing cycle`"这个新角度，不能写"没价格"）**。

剩余候选（未被消耗）：YABS 怎么读结果（Day4 候选 #3，仍未升：英文位只有 ServerVerify/LEB 两家自述，教程位仍空）；"Automatically Reverts to Standard Pricing" 四种折扣结束方式（Day5 候选 #2，**今日拿到成组新证据**：C 栏 vpsbenchmarks 一次给出四种结束写法——`Discount only applies to first billing cycle` / `Expires on <date>` / `unused credit expires after N days` / `for the entire life of the VPS`，下轮可考虑升级）；Hostinger 学生折扣/资格类折扣（Day8 候选 #3，**今日降到池底**：B5 英文位仅 groupon 一条券聚合页，形不成搜索需求，但拿到了英文名 `Eligibility-Based Discounts`）。

---

## 2026-10-16 (Day 10)

### A. 原创内容邪修

| # | 邪修点 | 为什么别人抄不走 |
|---|---|---|
| A1 | **11 天、70 次扫描、392 行 offer 记录，从来没有一个 deal 下架过**。把 git 里 100 个提交的 `data/offers.json` 全取出来按 `source_scan_at` 去重，得到 **70 次独立扫描**（`2026-10-04T23:49:08Z` → `2026-10-15T18:49:00Z`）。对全部 6 个 title 做"出现次数 vs 应出现次数"（首见→末见区间内的扫描数）比对：**5 个 title 是 70/70，1 个是 42/42，全部等于应出现次数**——即一个 title 一旦被抓到，就再没消失过一次。offer 总数只变过 **1 次**：5 → 6（发生在 `2026-10-08T12:37:03Z`），**从未下降过**。最后 1 次扫描时，6 个 title 全部仍在场 | 必须把每一次扫描的完整 offer 列表留档、并逐 title 做"是否存在断档"的校验，才说得出口"我的库存里没有'下架'这个事件"。真实 deals 站的核心情节就是"过期/售罄/下架"，**我们的数据里这件事发生次数是 0**——这是自曝，但也是唯一能引出下一条的硬事实：我们的 schema 只有 5 个字段（provider / title / offer_url / source_url / fetched_at），**没有 expiry 列，结构上就无法表达"这个 deal 结束了"**。把"我记录不了结束"写出来，等于承认这个雷达没有生命周期，商业站不会这么写 |
| A2 | **一天 24 小时里，我们有 13 个小时一次都没看过**。70 次扫描的 UTC 小时分布是：0 点×13、6 点×12、12 点×11、18 点×11（这四个小时合计 **47/70 = 67.1%**），另有 1 点×4、2 点×7、15 点×6、8 点×1、13 点×1、17 点×2、23 点×2。**从未被扫过的 UTC 小时有 13 个：3、4、5、7、9、10、11、14、16、19、20、21、22**。也就是说，任何在这 13 个小时里上线又下线的促销，我们的雷达在结构上不可能看见 | 必须把每一次扫描的 UTC 时刻留够 70 次、再按小时做覆盖率统计，才可能算出"我漏掉了哪几个小时"。只写 "Updated daily" 的站算不出自己的时段覆盖，更不会公布——因为"有 13 个小时我从没看过"一旦写出来，读者立刻知道"每天更新"这个词有多空。这个数字比 Day8 的"最长盲窗 6 小时"更具体，因为它点名了是哪 13 个小时 |
| A3 | **我们那四班"每天"的扫描，时刻一直在往后滑，约每天 +2 到 +3 分钟**。同样取 70 次扫描的时刻，按班次分组看漂移：18 点班 `10-09 18:31:28` → `10-15 18:49:00`，6 天晚了 **17 分 32 秒（≈2.9 分钟/天）**；0 点班 `10-11 00:38:18` → `10-15 00:50:06`，4 天晚了 **11 分 48 秒（≈2.95 分钟/天）**；6 点班 `10-06 06:34:27` → `10-15 06:52:11`，9 天晚了 17 分 44 秒（≈2.0 分钟/天）；12 点班 `10-06 12:34:33` → `10-15 12:53:16`，9 天晚了 18 分 43 秒（≈2.1 分钟/天）。**四班全都朝同一个方向滑**——这是调度排队延迟留下的痕迹 | 必须把每一次扫描的真实时刻（而不是"每天一次"这句话）存上十天，并对同一班次做逐日相减，才看得见这个单调漂移。外部读者看到一个站写 "Updated daily"，没有任何办法知道它的"每天"正在每天往后挪 3 分钟；而我们能把四个班次的斜率分别算出来。这也是自曝：等于说我们的调度并不像一个 cron 那样准点 |
| A4 | **我们叫它 "VPS deals radar"，但 89.3% 的记录行来自同一家厂商**。392 行 offer 里 **Hostinger 350 行（89.3%）、Hetzner 42 行（10.7%）**；当前 6 条里 Hostinger 占 5 条。而受检清单是 8 个 URL、覆盖 5 个厂商主体（Hostinger / Hetzner / DigitalOcean / Vultr / Linode 各 1 条，另有 3 条**连 provider 字段都没有**的 Contabo URL）——**被检查的 5 家里只有 2 家曾经产出过任何一行**。Hostinger 用 1/8 = 12.5% 的采集预算，产出了 89% 的行 | 必须把"采集预算"和"产出"作为两张表分开统计并放一起比。任何 deals 站的首页都在暗示自己覆盖面广，不会自己算"我 89% 的数据来自一家"——因为这个数字一出来，"多厂商雷达"这个定位就塌了。更难的是那 3 条缺 `provider` 字段的 Contabo URL：把它们算进去会暴露配置本身就不完整 |
| A5 | **6 条 deal 里只有 4 条带数字，另外 2 条是纯文案**。逐条扫 title 里的数字：`70% / 67% / 63% / 65% off — Hostinger VPS page` 四条带数字，**且长度全是 28 字符**（同一模板）、**全部指向同一个 URL**（`hostinger.com/vps-hosting`）；剩下两条一个数字都没有——`Student discount`（16 字符）和 Hetzner 那条 `Server Auction Save money and do good for the planet with refurbished servers from`（**82 字符，且以介词 `from` 结尾，句子是被截断的**）。也就是说，能被叫作"折扣"的只有 4/6 = 67%，而这 4 个数字出自 1 个页面 | 必须愿意把"deal 条数"拆成"带数字的条数"和"只是文案的条数"。首页挂 "29 live offers""23 Current offers" 的站不可能自己做这个拆分——那等于承认自己的计数里混进了没有价格的条目。而把 Hetzner 那条截断在介词上的 title 原样摆出来，还需要愿意展示自己解析器留下的毛边 |

### B. 谷歌搜索查词（今天真跑过的）

| query | SERP 上看到了什么 | 判断 |
|---|---|--|
| `vps deals` | **核心词**。5 条，英文位 3 条、与昨天基本同面：vpsticker.com（`15 providers tracked` / `29 live offers` / `15/15 providers returning data`，**`last refresh` 仍写 `2026-10-02`**）、vpsfilter.com（`Updated daily`）、rackbazaar.com（`3 providers, 9 plans` / `Updated daily` / **`No dark patterns`**）；另 2 条是中文站 vncoupon.com（RackNerd 法国 `$17.98/Year`、CloudCone 标签页） | 核心词锁 29 天不动。**vpsticker "声称 15/15 全部返回数据、刷新日期却是 13 天前"的自相矛盾已连续 3 天复现**，作为外部佐证稳定可用 |
| `cheap vps black friday 2026 deal recurring price renewal` | 5 条：**vps.blackfriday（第 1，英文，`VirMach's rotating VPS offers are back for Black Friday. Don't blink or you might miss it.` / `Offer may expire or change a…`）**、blackfriday.bloggingjoy.com（通用零售，GreenGeeks `80% OFF`）、ovh.com/fr/black-friday（**法文页**）、vncoupon ×2 | 英文位只有 2 条且**都不含"renews at / recurring price"的实质内容**。但 vps.blackfriday 拿到两条硬行话（`rotating VPS offers`、`Don't blink or you might miss it`），进 C 栏。黑五线仍不新开题 |
| `lowendtalk vps offer out of stock restock provider went dark` | 5 条：DreamHost 论坛/博客/合作页 3 条（噪声）、lowendtalk.com/categories、**racksniff.com（`0 new VPS deals today. 0 this week. Sniffed from LowEndTalk, LowEndBox, and direct provider drops.`）** | **今天最大的新发现**：racksniff 是一个英文 VPS deals 站，**公开展示 0 条**。此前假设"deals 站都会撑满库存"不成立。直接进 C 栏与候选 #1 |
| `vps coupon code first billing cycle then renews at regular price` | 5 条：vpsbenchmarks.com/vps_coupons（第 1，`VPSLab 20 % discount ... Applies to the first billing cycle.`）、boomhost.startupworld.com FAQ（**`Usually, the intro discount is just for the first term. After that, it renews at the regular price.`**）、**namecheap.com/wordpress 官方页（`5 EasyWP promotional price applies to the first billing cycle only with renewals available at the regular price.`）**、vncoupon ×2 | **Day5 候选 #2（四种折扣结束方式）拿到三份独立英文证据**：第三方券站 `Applies to the first billing cycle`、FAQ `intro discount … first term … renews at the regular price`、厂商官方脚注 `first billing cycle only with renewals available at the regular price`。且 **namecheap 官网真有一张 `Renews at $X/mo` 对照表**——`EasyWP $3.24/mo Renews at just $5.74/mo`、`Hostinger $3.99/mo Renews at $10.99/mo`、`HostGator $5.00/mo Renews at $18.69/mo`，表下注明 `were updated on July 27, 2026` |
| `vps deals page last updated how often are prices verified accurate` | 5 条：vpsticker.com（**第 1，且正文直接回答：`How often is this updated? The scraper and the site rebuild run on a schedule, every 6 hours. Every page carries the exact UTC timestamp of the fetch it was built from`**）、**bestvpsdeal.com（已开始发 guide：`VPS Backups vs Snapshots: What Actually Protects Your Data?`、`How to Compare VPS Plans Without Relying on Headline Price`）**、dontpayfull（OVH 券页）、DreamHost 买家清单、blog.naibabiji.com | **重要修正**：Day8/Day9 说"没人解释自己的更新口径"**不完全成立**——vpsticker 解释了，且声称 `every 6 hours` + `exact UTC timestamp`。**但它首页的 `last refresh` 是 2026-10-02**，所以缝从"没人解释"变成"解释了但做不到"。另：**bestvpsdeal 已从"0 offers"转去发 guide，其中一篇叫 `How to Compare VPS Plans Without Relying on Headline Price`，与我们的选题正面撞车**——以后每轮都要复查它 |
| `YABS results how to read vps benchmark disk cpu score` | 5 条：CSDN ×2（中文）、知乎（中文）、github.com/masonr/yet-another-bench-script、**yabsdb.com（`YABSdb - The largest database of YABS server benchmarks`）**；另有 lowendboxes.review 出现在相关位 | **英文"怎么读 YABS"教程位仍然是 0**，英文位只有工具站与跑分库，没有教程。Day4 候选 #3（YABS 怎么读）**连续第 2 次确认不升级**。但 yabsdb 是新英文源，一次出多条原生说法，进 C 栏 |
| `lowendbox vps sold out limited stock flash sale gone quickly` | 5 条：lowendbox.org 首页、lowendbox.com/tag/texas、52pchome.net（中文，转写 LEB 的 Velohost 文）、**racksniff.com（又是 0 条）**、**lowendboxes.review（`Stocks are limited and if you don't want to miss out ... buy your box immediately`）** | 英文"售罄"位命中 1 条真内容且质量极高：`Stocks are limited` / `buy your box immediately` / `better grab this offer before it is sold out!`。**与我们 A1（库存从不下架）形成直接对照** → 升为候选 #3 |

### C. 老外怎么说（真在用的说法）

| phrase | 谁在用 / 什么意思 |
|---|---|
| "**0** new in last 24h" / "**0** this week" / "**0** live deals total" | racksniff.com 首页原文：**英文 deals 站把"库存为零"直接挂在首屏当状态展示**，不回避 |
| "**No live deals right now.**" | 同上原文：库存为空时的标准陈述句 |
| "**No fluff, no fake countdowns.**" | 同上原文：**把"不做假倒计时"当卖点**——反过来说，假倒计时是行业默认 |
| "**Flash deals · sorted by recency**" / "**Newest on top.**" | 同上原文：`flash deal` 是英文圈对限时促销的标准分类词，与下条成对出现 |
| "**→ evergreen listings on rackbazaar**" | 同上原文：**`evergreen listings` 是 `flash deals` 的对义词**，指长期在售的常规套餐。英文圈靠这两个词把"限时"和"长期"分开 |
| "**Sniffed from LowEndTalk, LowEndBox, and direct provider drops.**" | 同上原文：来源说明的写法，`provider drops` 指厂商直接放出的货 |
| "**Stocks are limited and if you don't want to miss out this first ever HostDoc LES Ryzen LA deal, buy your box immediately**" | lowendboxes.review 原文：**`Stocks are limited` + `buy your box immediately` 是英文评测站催单的固定组合** |
| "**better grab this offer before it is sold out!**" | 同上原文：`grab this offer` 是"抢下"的原生说法，`sold out` 是售罄 |
| "**Just buy it already.**" / "**Shut up and take my money now!**" | 同上原文：英文评测文里的社群式催单两句，语气远超中文站 |
| "**The Whitelist**" / "**de-listing Bandit Host (ceased operations)**" / "**de-list HostDoc from the Whitelist with effect from today**" | 同上原文：**英文圈有一套"白名单 + 除名"机制**，`de-list` 是动词，`with effect from today` 是生效写法 |
| "**compromising customers' private data is a red line**" / "**we will consider reinstating HostDoc**" | 同上原文：`red line`（红线）与 `reinstating`（恢复资格）是这套机制的判词 |
| "**Please do not order any service from them.**" / "**please back up your data and file disputes with your payment processor as soon as possible**" | 同上原文：**出事厂商的标准处置通告**，`file disputes with your payment processor` 是让你去走支付争议 |
| "**A list of apparently low-end hosts have suddenly announced their collective closure of their low end box hosting business.**" | 同上原文：`collective closure` 指一批厂商同时关门 |
| "**we prefer to under-sell and over-deliver than the other way round**" | 同上厂商原话：`under-sell and over-deliver` 是英文圈自证诚意的固定搭配 |
| "**you get 16 months instead of 12 months with the Switcher special**" / "**an additional month of service credit, making a total of 17 months**" | 同上原文：**`service credit` 是"送时长"的正式说法**，不是"免费几个月" |
| "**The overall LEBRE score of 141**" | 同上原文：`LEBRE score` 是这家自有的综合跑分指标名 |
| "**we ran daily for 35 days from 13 December 2019 to 16 January 2020**" | 同上原文：**长周期实测的写法要交代跑了几天、起止日期** |
| "**25% Recurring OFF \| LET Exclusive**" / "**Recurring Discounts**" / "**$75/mo Recurring**" | LowEndTalk 首页原文：**`Recurring` 指续费也继续打折**，与"首周期折扣"严格对立，是英文圈最重要的定价词之一 |
| "**LIFETIME $18 Shared/Reseller Hosting**" / "**25 x PERPETUAL $1/Year VPS**" | LET 原文：**`LIFETIME` 与 `PERPETUAL` 是"一次付费永久"的两种写法**，后者更常见于赠品类 |
| "**LET Exclusive**" / "**Bonus for LET Members**" / "**Another LET Post!**" | LET 厂商帖原文：**给社区的专属价有固定标签**，且必须是 `Exclusive` 而不是普通折扣 |
| "**DeluxHost.net \| VPS Restock \| Improved Storage Servers!**" | LET 原文：`VPS Restock` 是补货帖的固定前缀 |
| "**DartNode - Countdown to Black Friday - Dedicated Server Deals and Giveaway! Live now!**" | LET 原文：`Countdown to …` + `Live now!` 是节日促销帖的标准结构 |
| "**Prometeus brand is being retired as of March 2027**" | LET 原文：**品牌退市用 `retired`，且要给出生效日期 `as of <date>`** |
| "**Servarica down?**" / "**Deluxhost: VPS unstable for weeks, no reply from support**" / "**Famesystems unauthorized acces detected**" / "**DartNode VPSes rolled back to July?**" | LET 原文：故障与信任事件的四种写法，`no reply from support` 与 `unauthorized acces detected`（原文拼写如此）都是社群常用句 |
| "**Kimsufi/Soyoustart/OVH Rise New Price**" / "**OVH launches 2027 VPS line**" | LET 原文：涨价的名词化写法 `Rise New Price` |
| "**VSYS Host: UA data centers. What happened and where recovery stands?**" | LET 原文：**`where recovery stands` 是问恢复进度的固定说法** |
| "**[$1000] Wanted OVH KS-MYSTERY E-2288G**" | LET 原文：`[$N]` 是求购预算前缀，`KS-MYSTERY` 是 OVH 清仓系列的专有叫法 |
| "**[FREE] shellter.me — FreeBSD pubnix**" / "**[Free] your NAT LXC VPS :>**" | LET 原文：**`pubnix` 是公共 Unix 主机的圈内黑话**，`NAT LXC` 是免费机的常见形态 |
| "**Well, all 100 VPS instances have now been given away. But apparently, 100 wasn't enough!**" | LowEndBox 首页原文：`given away` 是赠品告罄的写法 |
| "**More of RackNerd & AdminBolt! Here's 50 More FREE VPS + 10 Lifetime Licenses!**" | LEB 原文：`N More ...` 是加码赠送的标题写法 |
| "**Exclusive LowEndBox Pricing: 2GB KVM VPS for $1.83/Month First Year!**" / "**You'll need our special coupon code to get these deals!**" | LEB 原文：`Exclusive <站点> Pricing` + `First Year` 限定 |
| "**A VPS for UNDER $10/YEAR! Wow!**" / "**$500 in cold hard cash!**" / "**No tricks here, just a wonderful treat:**" | LEB 原文：`UNDER $X/YEAR`、`cold hard cash`（现钱）、`No tricks here` 都是固定口语搭配 |
| "**I guess Velohost has never heard of inflation.**" | LEB 原文：夸降价的反讽开场，必须配"几个月前的价 → 现在的价"两个数字 |
| "**Applies to the first billing cycle.**" | vpsbenchmarks.com/vps_coupons（VPSLab）原文：折扣范围的标准限制句 |
| "**25% discount for 6 months. Valid for first purchase on any plan.**" | 同上（INET.WS）原文：**`Valid for first purchase` 是"仅限首单"的写法** |
| "**50% off on new VPS purchase for new customers on first order for monthly plan.**" | 同上（OnetSolutions）原文：`first order` 与"月付"叠加限制 |
| "**The credit is issued as cloud tokens and applied to the first invoices. It has to be used within 90 days of redemption.**" | 同上（dataforest cloud）原文：`cloud tokens` + `used within N days of redemption` |
| "**New Cloud Server customers get a credit of up to $100 applied to their first month's bill. The credit is valid for 1 month and any unused credit expires following the first invoice.**" | 同上（IONOS）原文：**额度失效写成 `expires following the first invoice`** |
| "**Unused portion of $300 credit expires after 30 days.**" / "**Unused credits expire after 60 days.**" | 同上（Vultr / LunaNode）原文：`Unused ... credit expires after N days` 是额度失效的统一句式 |
| "**Referred users must be active for 30+ days and use at least $100 in payments to be counted as verified sales.**" | 同上（Vultr）原文：`verified sales` 是联盟结算里的判定词 |
| "**Plan deal**" / "**Coupon**" | 同上页内两个分区标题原文：**英文券站把"套餐自带折扣"和"优惠码"分成两类展示** |
| "**Last updated on October 13th 2026**" | 同上页眉原文：英文券站自报更新日期的句式 |
| "**$3.24/mo Renews at just $5.74/mo**" / "**Hostinger $3.99/mo Renews at $10.99/mo**" / "**HostGator $5.00/mo Renews at $18.69/mo**" / "**Pressable $20.83/mo Renews at $20.83/mo**" | **namecheap.com/wordpress 官方页原文**：**厂商自己把竞品的续费价做成对照表，栏目就叫 `Renews at`，且同价的两家（Pressable/WP Engine/Kinsta）也照写不误**。`renews at` 是英文里讲续费价的头号说法 |
| "**Monthly price and renewal price by hosting provider**" / "**Compare upfront and renewal costs**" | 同上原文：`renewal price` 与 `upfront` 是"续费价/首期价"的正式对仗 |
| "**promotional price applies to the first billing cycle only with renewals available at the regular price.**" | 同上官方脚注原文：厂商自己声明折扣边界的完整句式 |
| "**were updated on July 27, 2026**" / "**subject to change by the respective provider at any time**" | 同上原文：厂商自报竞品数据日期 + 免责声明 |
| "**Was $5.74/mo**" / "**Billed yearly**" / "**44% off**" | 同上定价卡原文：折前价写 `Was`，计费周期写 `Billed yearly` |
| "**Easy 30-day cancel**" / "**30-day money-back guarantee**" / "**99.9% Uptime**" | 同上原文：退款与可用性的三种标法 |
| "**The ultimate database for server benchmarks.**" / "**curl -sL yabs.sh \| bash -s -- -s "https://yabsdb.com/add"**" | yabsdb.com 首页原文：跑分库的自我介绍与**一行上传命令**，`add` 端点就是投稿方式 |
| "**Total YABS 1,088**" / "**Last 24H 0**" / "**Last 48H 0**" / "**Claimed 2139**" / "**CPUs 448**" / "**Locations 443**" | 同上平台统计原文：**跑分库也把"最近 24 小时新增 0"当指标公开**——与 racksniff 的 0 条同构 |
| "**No Geekbench 6 results**" / "**Disk Performance**" / "**4K / 64K / 1M**" / "**↑ ↓ ⟷**" / "**Network Performance**" / "**Runtime: 11:22**" | 同上结果卡原文：YABS 结果的三段结构（无 Geekbench / 磁盘 4K-64K-1M / 网络按城市 + 延迟），`Runtime:` 是耗时 |
| "**How often is this updated? The scraper and the site rebuild run on a schedule, every 6 hours. Every page carries the exact UTC timestamp of the fetch it was built from**" | vpsticker.com 原文：**第三方雷达解释自己更新口径的完整写法**，`the fetch it was built from` 是"本次页面由哪次抓取生成"的说法 |
| "**3 providers, 9 plans. Updated daily. No dark patterns.**" | rackbazaar.com 原文：**`No dark patterns` 被当成卖点写进简介** |
| "**VirMach's rotating VPS offers are back for Black Friday. Don't blink or you might miss it.**" / "**Offer may expire or change a…**" | vps.blackfriday 原文：`rotating offers`（轮换上架）与 `Don't blink or you might miss it`（眨眼就错过） |
| "**How to Compare VPS Plans Without Relying on Headline Price**" / "**VPS Backups vs Snapshots: What Actually Protects Your Data?**" | bestvpsdeal.com 原文：该站已从"0 offers"转为发 guide，标题套路是 `Without Relying on …` 与 `What Actually …` |

### 明日候选

1. **"0 Live Deals Right Now": Two English VPS Radars Showed Zero on the Day Ours Showed Six** — A1（70 次扫描、392 行，**没有任何一个 title 出现过断档，5 个是 70/70、1 个是 42/42；总数只变过一次 5→6，从未下降**）+ B3（racksniff.com 首页 `0 new in last 24h` / `0 this week` / `0 live deals total` / `No live deals right now.`）+ B6（yabsdb.com `Last 24H 0` / `Last 48H 0`）+ A1 的结构性原因（schema 无 expiry 列，我们记录不了"结束"）。缝：**同一天里，两个英文站的库存是 0，我们的库存是 6 且十一天没变过**——"库存为零"和"库存冻结"是同一件事的两面，但没有人把它们放进同一篇文章对照，因为前者要承认自己空、后者要承认自己不会减少
2. **Our VPS Deal Radar Has Never Looked at 13 of the 24 Hours — and Its Schedule Slides ~3 Minutes Later Every Day** — A2（70 次扫描只覆盖 11 个 UTC 小时，**13 个小时从未被扫过**；0/6/12/18 四点占 67.1%）+ A3（四班全部朝后滑：18 点班 6 天晚 17 分 32 秒≈2.9 分钟/天，0 点班 4 天晚 11 分 48 秒≈2.95 分钟/天，6 点班 9 天晚 17 分 44 秒，12 点班 9 天晚 18 分 43 秒）+ B5（vpsticker 公开解释 `every 6 hours` + `exact UTC timestamp`，但首页 `last refresh` 是 2026-10-02）。缝：**"每天更新"这个词没人拆开过**——没人告诉你它覆盖了哪几个小时、以及"每天"这个时刻本身正在漂移
3. **"Flash Deals" vs "Evergreen Listings": The Two Words English Deal Sites Use — and Our Six Have Neither** — C 栏 racksniff 原文（`Flash deals · sorted by recency` / `→ evergreen listings on rackbazaar` / `No fluff, no fake countdowns.`）+ C 栏 lowendboxes.review 原文（`Stocks are limited` / `better grab this offer before it is sold out!` / `buy your box immediately`）+ C 栏 LET（`VPS Restock` / `Countdown to Black Friday`）+ A1（我们的 6 条从不下架）+ A5（6 条里只有 4 条带数字，4 个数字出自同一个 URL）。缝：**英文圈用 flash / evergreen 两个词把"限时"和"长期"分开，且只有 flash 才有"售罄"这回事**；我们的 6 条两个标签都没有，因为 schema 里没有 expiry 列——所以我们的读者无法判断眼前这条是"马上没了"还是"一直都在"

已用：`compare-vps-deals-total-cost`（10-07）、`vps-deals-renews-at-x`（10-08）、`vps-deals-refund-window`（10-09）、`vps-deals-cost-per-gb-ram`（10-09）、`vps-deals-who-collects-vat`（10-09）、`vps-deals-hourly-to-monthly`（10-10）、`vps-deals-cost-per-gb-disk`（10-11）、`vps-deals-auto-renewal-notice`（10-12）、`vps-deals-port-25-smtp-blocked`（10-13）、`vps-deals-sla-credit-how-to-claim`（10-14）、**`vps-deals-payment-methods-accepted`（10-15，最后一篇已发布，Day9 时还未上线故未记入）**。

已降级/不再写第二篇：退款天数（已发）、每 GB 单价（已发）、renews at 换算（已发）、Hourly ×672/730（已消耗）、CPU steal 诊断（英文位占满）、过期 deal（pennyclouds 已占）、Unmetered Port Metered Reality（Day2）、Stuck in an AI Support Loop（Day3）、低价套餐断货/候补（Day6）、Hetzner 拍卖"怎么运作"（Day6）、黑五"预热期填不出价格"（Day8，已改写）、**"deals 站都会撑满库存"（Day10 今日证伪：B3 的 racksniff 公开显示 `0 live deals total`、B6 的 yabsdb 显示 `Last 24H 0`，假设不成立，原"库存充盈"类写法作废）**。

剩余候选（未被消耗）：YABS 怎么读结果（Day4 候选 #3，**连续第 2 次确认不升级**：B6 英文位只有 GitHub 仓库、yabsdb 跑分库、lowendboxes.review 三类工具站，教程位仍为 0，中文位被 CSDN/知乎占满）；"Automatically Reverts to Standard Pricing" 四种折扣结束方式（Day5 候选 #2，**今日拿到三份独立英文证据并首次拿到厂商官方页**：vpsbenchmarks `Applies to the first billing cycle`、boomhost FAQ `the intro discount is just for the first term … renews at the regular price`、namecheap 官方脚注 `applies to the first billing cycle only with renewals available at the regular price`，且 namecheap 官网真有 `Renews at $X/mo` 竞品对照表——**但 `vps-deals-renews-at-x` 已于 10-08 发布，若开此题必须与已发那篇完全不同的切口：写"厂商自己公开竞品续费价"这个现象，而不是解释 renews at 这个词**）；Hostinger 学生折扣/资格类折扣（Day8 候选 #3，维持池底）。

---

## 2026-10-17 (Day 11)

### A. 原创内容邪修

| # | 邪修点 | 为什么别人抄不走 |
|---|---|---|
| A1 | **75 次扫描、13 个 UTC 日，只有 1 天出现过"日内变化"；98.6% 的相邻扫描字节级完全相同**。把 git 里 105 个提交中的 `data/offers.json` 全取出来按 `source_scan_at` 去重，得到 **75 次独立扫描**（`2026-10-04T23:49:08Z` → `2026-10-16T18:46:03Z`，其中 30 个早期快照没有 `source_scan_at`）。按 UTC 自然日分组、比较当天**第一次**与**最后一次**扫描的 offers 数组：13 天里 **12 天完全一样**，唯一变化的一天是 `2026-10-08`（那天从 5 条变 6 条）。再看相邻扫描的 74 次转换：**73 次 offers 数组内容一字未改 = 98.6%**。而我们在 `2026-10-05` 一天里就跑了 **12 次**扫描（平时是 5 次） | 必须把每一次扫描的完整 offers 数组留够 75 次、再对相邻对做逐字节比对，才说得出"我多出来的那几次扫描一次新信息都没带回来"。真实 deals 站把"更新频率"当卖点挂首屏，没有人会自己算"我的更新里 98.6% 是重复读取"——因为这个数字一出来，频率这个卖点就变成了浪费的证据。更没人会主动说"我有一天跑了 12 次，结果和跑 1 次一样" |
| A2 | **8 个受检 URL 的可读性，75 次扫描零翻转**。逐条追每个 URL 的 `readable` 布尔值：Hostinger `/vps-hosting`、Hetzner `/hosting/`、DigitalOcean `/pricing/droplets` **恒为 True（75/75）**；Vultr `/products/cloud-compute/`、Linode `/pricing/`、Contabo `/en/`、`/en/server-outlet/`、`/en-us/pricing/` **恒为 False（75/75）**——8 条全部 `present=75/75`、`flip=False`。整个 `source_checks` 在 75 次扫描里**只有 1 种签名** | 必须把"来源可读性"和"offer 列表"分开存、并对每个 URL 单独追 75 次，才看得出这不是抖动而是**结构性失败**：一个页面要么永远读得到，要么永远读不到，从来没有中间态。这直接否掉了"再试一次就好了"的直觉。而外部对照是：B7 显示英文雷达里唯一敢提成功率的是 vpsticker，写的是 `15/15 providers returning data`（**15 家全部成功**）——**没有任何一家英文站公开承认自己读不到某些厂商**，因为那等于承认自己的覆盖有洞。我们愿意写 5/8 恒不可读 |
| A3 | **我们管自己叫 VPS deals radar，但受检的 8 个 URL 里，没有一个是促销页/优惠页**。逐个拆路径：`/vps-hosting`（产品落地页）、`/hosting/`（产品大类页）、`/pricing/droplets`（定价页）、`/products/cloud-compute/`（产品页）、`/pricing`（定价页）、`/en`（**Contabo 首页**）、`/en/server-outlet/`（**唯一接近"清仓便宜货"的一页**）、`/en-us/pricing/`（定价页）。**促销/优惠/deals/offers/promo 类路径命中数 = 0**；8 条里 5 条是"定价页或产品页"、1 条是首页。而唯一那个真正卖便宜货的 `/en/server-outlet/`，恰好在 A2 里是**永久不可读**的三条之一 | 必须愿意把自己"检查了哪些 URL"这个清单原样摊开，并按路径语义给每一条分类。写"我们监控 N 个来源"很容易，写"我们监控的 N 个页面里没有一个促销页"是自砸招牌——但它正好解释了一切：为什么产出这么少、为什么数字全是常规价。**没有竞争对手会公布自己的受检清单**，因为一公布，读者就能自己判断这份清单配不配得上"deals"这个名字 |
| A4 | **我们的库存里，最新的一件货也是 8 天 6 小时前进的**。对 6 条 offer 追"首次出现时刻"：`Student discount` 与四条 `70% / 67% / 63% / 65% off` **在场 11 天 18 小时**（自 `2026-10-04T23:49:08Z`，即第一次扫描就在场）；Hetzner 那条**在场 8 天 6 小时**（自 `2026-10-08T12:37:03Z`）。**最后一件"进货"距今 8 天 6 小时 9 分**，之后 42 次扫描再没有新增过任何一条 | 必须把每条 deal 的"首次出现时刻"单独记下来，才能算出库存年龄——只存当前快照的站永远答不出"你最老的一条挂了多久"。而 deals 站的默认叙事是"每天都有新货"，公开"我最新的一件也是 8 天前的"等于承认自己没有新增能力。配合 A1 看更狠：**75 次扫描里唯一一次进货是第 42 次之前，之后 33 次扫描全是空转** |
| A5 | **我们唯一那条非 Hostinger 的 deal，指向的页面每一条 listing 都挂着一个正在走字的倒计时，而我们对它的记录 8 天没动过**。抓 `https://www.hetzner.com/sb`（我们的 `offer_url`）：页面逐条显示 `06:39:23left`、`17:41:42left`、`20:39:04left`、`22:25:45left`——**`left` 前面是一个实时减少的 HH:MM:SS 时钟**；另有 `max. per month` / `per hour`、`Server AuctionID: 3091544`、`Traffic: unlimited`、`Location #FSN1-DC8`。而这条 offer 在我们库里的 title 是 `Server Auction Save money and do good for the planet with refurbished servers from`——**截断在介词 `from` 上，8 天 6 小时一字未变** | 必须真的去打开自己存的那个 `offer_url`、看一眼页面现在长什么样，再回来和自己的记录对照。这一步没有人做：deals 站存了链接就当存了内容。而一旦做了，就会撞见最尴尬的对照——**一个自带倒计时、每小时都在变的拍卖页，被我们记成了一句永远不会变的静态文案**。要写出这个，还得愿意把自己 title 里那个断在 `from` 上的毛边原样摆出来 |
| A6 | **"每天更新"没说是按谁的表：我们对德国厂商只有 26.7% 的扫描落在当地白天**。75 次扫描的 UTC 小时分布：0 点×14、1 点×4、2 点×8、6 点×13、8 点×1、12 点×12、13 点×1、15 点×6、17 点×2、18 点×12、23 点×2。按厂商所在时区换算（10 月仍为夏令时：柏林 CEST=UTC+2、美东 EDT=UTC-4），落在当地 **9:00–18:00** 的扫描只占 **柏林 20/75 = 26.7%**、**美东 21/75 = 28.0%**（北京 26/75 = 34.7%）；三个时区各有 **13 个当地小时从未被扫过**。另外时间戳口径本身就是错位的：最后一次扫描 `2026-10-16T18:46:03Z` = **北京时间 2026-10-17 02:46**，我们今天要用的"最新数据"，UTC 日期是昨天 | 必须同时持有"扫描时刻（UTC）"、"厂商所在时区"和"夏令时是否在生效"三样东西，才可能算出"我对这家厂商的白天覆盖率是多少"。只写 "Updated daily" 的站既不知道自己在别人的白天还是半夜出现过，也不会公布"我有 73% 的扫描发生在对方下班后"——因为促销往往就是在对方白天上线、夜里撤掉的。而 UTC 日期与北京日期差一天这件事，所有站都默认读者和它同一个时区 |

### B. 谷歌搜索查词（今天真跑过的）

| query | SERP 上看到了什么 | 判断 |
|---|---|--|
| `vps deals` | **核心词**。5 条：vpsticker.com（`15 providers tracked` / `29 live offers` / `15/15 providers returning data` / **`2026-10-02 last refresh`**，距今已 **15 天**）、vpsfilter.com（`Updated daily`）、rackbazaar.com（`3 providers, 9 plans` / `No dark patterns`）、vncoupon.com ×2（中文站） | 与前两天同面，英文位 3 条。**vpsticker"声称 15/15 全部返回数据、刷新日期却是 15 天前"的自相矛盾已连续第 4 天复现**，作为外部佐证非常稳定 |
| `vps deals page stale not updated same offers every day` | 5 条**全是厂商落地页/博客**：glesys.com/vps、dreamhost.com/promo/wbevps、`vpsdime.com/a/3365/windows-vps`、dreamhost.com/blog/best-vps-hosting、monovm.com/windows-vps | **英文位里"deals 站数据陈旧"这个话题命中数为 0**——没有一家英文站在写，也没有检索需求（要么没人关心，要么没人敢写）。**但顺带挖到硬证据：dreamhost.com/promo/wbevps 证明厂商确实存在 `/promo/` 专属落地页**，直接喂给 A3（我们 8 个受检 URL 里 0 个是这类页） |
| `vps provider official promotions offers page versus pricing page` | 5 条：bestvpsdeal.com（第 1，**文案已升级为 `Official offer pages are monitored for changes. Every listing shows its source and uses transparent affiliate disclosure.`**）、arubacloud.com/vps.aspx、**vpspromocodes.com（全新英文券站：`Verified codes` / `Updated daily` / `Expired deals get removed. Active ones stay easy to find.`）**、foxvalleywebdesign.com、digitalocean.com/resources/articles/vultr-alternatives | **今天最有价值的一条**。竞品 bestvpsdeal 公开宣称它监控的是"官方 offer 页"，vpspromocodes 公开宣称"过期的会被移除"——**这两句都和我们的现状正面相反**（我们监控的是定价页/产品页/首页；我们从没移除过任何一条）。vpspromocodes 是新英文源，一次出 10 条原生说法，进 C 栏 |
| `evergreen vps deal never expires listed for months` | 5 条**全部是零售优惠券站**：dontpayfull.com（`Evergreen Coupon Codes`）、360vouchercodes.co.uk（`Affiliate Evergreen Code`）、cloudnine.getrefe.com、tervis.couponforless.com（`Evergreen Bundles`），另加 vncoupon 1 条 | **重要修正（今日降级依据）**：`evergreen` 在英文里是**零售优惠券圈**的行话，VPS 语境 SERP 命中 **0 条**。Day10 候选 #3 标题里的 `Evergreen Listings` 没有检索需求 → **该候选今日降级**（racksniff 那个 `evergreen listings` 是它从零售圈借来的自用分类词，不是买家会搜的词） |
| `black friday 2026 vps hosting deals early bird` | 5 条全是通用零售/主机聚合：blackfridaydeals.co.uk、tryblackfriday.com、technoven.com（Kohl's）、**blackfriday.hosting（标题仍写 `[Nov. 2025]`）**、blackfriday.bloggingjoy.com | VPS 专用黑五位今天 **0 条**（Day10 还在的 vps.blackfriday 已掉出前五），黑五线**维持不开新题**。但 blackfriday.hosting 是全新英文源且 10 月仍挂着去年的 `[Nov. 2025]`，一次出十余条折扣写法，进 C 栏 |
| `YABS results how to read vps benchmark score` | 5 条：CSDN ×2、知乎 ×1、github.com/masonr/yet-another-bench-script、**yabsdb.com** | **英文"怎么读 YABS"教程位连续第 3 次为 0**（中文位被 CSDN/知乎占满，英文位只有工具仓库与跑分库）。Day4 候选 #3 **第 3 次确认不升级** |
| `vps pricing page blocks scrapers cloudflare bot cannot read prices` | 5 条：vpsticker.com（第 1，**`15/15 providers returning data`**）、urtech.ca（Cloudflare 拦 AI 爬虫教程）、github.com/VeNoMouS/cloudscraper、brightdata.com（`Top 7 Anti-Scraping Techniques and How to Bypass Them`）、cloudflare.com | **没有任何一个 VPS deals 站公开承认自己抓不到某些厂商**。唯一提到成功率的就是 vpsticker，写的是"15/15 全部成功"。我们 8 个里 5 个恒不可读（A2），这个数字在英文圈 **0 人说过**——这是 A2 最强的外部对照 |

### C. 老外怎么说（真在用的说法）

| phrase | 谁在用 / 什么意思 |
|---|---|
| "**Expired deals get removed. Active ones stay easy to find.**" | vpspromocodes.com 首页原文：**英文券站把"过期即下架"直接写成卖点**，放在 `Updated daily` 标题下。与我们"从没下架过一条"正面相反 |
| "**26,555** Active Deals" / "**5,121+** Providers" / "**Code-first** Sorting" / "**Daily** Updates" | 同上首页四格指标原文：`Active Deals` 是库存计数词，`Code-first Sorting` 指有码的排前面 |
| "**Verified codes** — Promo codes are prioritised and checked before generic offers." | 同上原文：`verified` 的官方定义是"优先且经过核对"，与 `generic offers`（无码的普通折扣）对立 |
| "**Clear categories reduce time wasted opening weak offers.**" | 同上原文：**`weak offers` 是"不值得点开的券"的说法** |
| "**Deal** WebHostMost Blazing Fast NVMe Hosting For $17.50/Mo" / "**Code** CentriXNodes Save 20% On Recurring VPS Plans" | 同上条目前缀原文：**`Deal`（套餐自带折扣）与 `Code`（需要输码）是两类，用前缀区分** |
| "**Save** 20% On Recurring VPS Plans" / "**Save** 15% On Lifetime Hosting Plans" / "**Unlock** 15% Lifetime Dedicated Server Discounts" / "**Deploy** High-Speed Arm64 VPS From $5.3/mo" / "**Get** Base Plan For $10/mo" / "**Lock In** Annual Plan For $84" / "**Unlock** Your Free Trial Today" | 同上标题原文：**券站标题的动词是固定的五个——Save / Unlock / Deploy / Get / Lock In** |
| "**Recurring VPS Plans**" / "**Lifetime Hosting Plans**" / "**Lifetime Dedicated Server Discounts**" | 同上原文：**`Recurring` 与 `Lifetime` 是英文券站区分折扣持续性的两个标准标签** |
| "**37 offers**" / "**22 offers**" | 同上 Top providers 区原文：厂商名下"在线条数"的写法，量词用 `offers` |
| "**Show Coupon**" / "**Redeem Offer**" | 同上按钮原文：有码用 `Show Coupon`，无码用 `Redeem Offer` |
| "**Every provider page keeps context close to checkout.**" | 同上原文：`keeps context close to checkout` 指厂商页把说明放在靠近下单的地方 |
| "**The Black Friday hosting deals are usually introductory prices for the first year or billing cycle. When it's time to renew, the regular/non-promotional pricing will apply.**" | blackfriday.hosting 官方 FAQ 原文：**英文站解释"黑五价"的标准完整句式**，`introductory prices` + `non-promotional pricing` 成对 |
| "**Prices go up on renewal**" / "**Higher pricing at renewal**" / "**Renewal prices can go up**" | 同上三家厂商 Con 栏原文：**同一件事的三种英文写法**，都放在缺点栏 |
| "**Flat** 50% Off" vs "**up to** 85% Off" | 同上定价卡原文：**`Flat`（全场统一折扣）与 `up to`（最高可达）是两种必须区分的标法** |
| "**For 48 Months**" / "**For 12 Months**" / "**For 36 Months**" / "**For 3 Months**" / "**4 Months Free**" | 同上原文：**折扣时长写成 `For N Months`，或等价地写成 `N Months Free`** |
| "**Early Bird Black Friday Deal**" / "**Early Black Friday Deal**" | 同上原文：`Early Bird` 与 `Early` 都是十月就开始的预热促销标签 |
| "**Black Friday Coupon Timing: November 25th, 2 PM CT to December 1st, 11:59 PM CT (new hosting orders only)**" | 同上（HostGator）原文：**促销窗口写到分钟 + 时区（CT）+ 限新单**，是英文站给促销期的标准精度 |
| "**Long commitment period for claiming the deal**" | 同上 Con 栏原文：`commitment period`（承诺期）是长周期折扣的负面说法 |
| "**This limited-time offer is available for LiquidWeb-managed hosting on Essential, Advanced, and Professional VPS subscriptions.**" | 同上原文：`limited-time offer` + 逐档列出适用套餐名 |
| "**they won't last long**" / "**be prepared to act quickly**" | 同上原文：催单的两句标准说法 |
| "**30 Days Money Back**" / "**Anytime Money Back**" | 同上原文：**退款窗的两种标法，`Anytime` 指随时可退** |
| "**Free Domain For 1 Year**" / "**Free domain for 1st year**" | 同上原文：赠品期限写 `For 1 Year` / `for 1st year` |
| "Hostinger 横幅 **For 48 Months** vs 表格 **For 3 Months**" / "Bluehost **up to 70%** vs **up to 75%** vs **Up tup to 75% off**（原文拼写错误）" / "第 13 节标题是 **A2 Hosting Black Friday Deals**，正文却以 **Hosting.com is offering...** 开头" | 同上页面内部自相矛盾原文：**英文黑五聚合页自己也填不准折扣时长与幅度**——与 Day8 的 "TBA until verified" 同类 |
| "**Top 13 Black Friday Web Hosting Deals [Nov. 2025]**" | 同上标题原文：**10 月中旬仍挂着去年的 `[Nov. 2025]`** |
| "**06:39:23left**" / "**17:41:42left**" / "**20:39:04left**" / "**22:25:45left**" | **hetzner.com/sb（我们唯一那条非 Hostinger deal 的 `offer_url`）页面原文**：**拍卖 listing 每条挂一个实时走字的 HH:MM:SS 倒计时，`left` 表示剩余时间** |
| "**max. per month**" / "**per hour**" | 同上原文：**拍卖价把"每月最高"与"每小时"两种计价单位并排显示** |
| "**Server AuctionID: 3091544**" | 同上原文：每台拍卖机有独立编号，`Server AuctionID` 是字段名 |
| "**Traffic: unlimited**" / "**Location #FSN1-DC8**" / "**#HEL1-DC2**" | 同上原文：流量与机房的写法，**机房用 `#` + 代号** |
| "**replacement of defective hardware**" / "**free email support**" / "**free phone support**" | 同上 Support services 区原文：拍卖机附带服务的三项列举 |
| "**iNIC**" / "**IPv4**" / "**2 x HDD SATA 2,0 TB**" | 同上 Information 区原文：`iNIC` 是 Hetzner 自有网卡标识；**注意德式小数逗号 `2,0 TB`** |
| "**D4 Networks \| 4GB KVM, 80-120GB NVMe \| $49/year, renews at $49 \| Dallas, Amsterdam, New York**" | LowEndTalk 首页原帖标题：**`renews at` 后面可以是同一个价**（`$49/year, renews at $49`），即"续费不涨价"也要写出来 |
| "**[Early Black Friday Sale] VPS & Dedicated Server Deals \| Starting at Just €18/Year!**" / "**Black Friday 2026 - Wishlist Thread**" | LET 原文：**`[Early Black Friday Sale]` 是十月预热帖的前缀标签**；`Wishlist Thread` 是社区征集心愿单的帖型 |
| "**TRENDING NOW: RackNerd's BLACK FRIDAY! NEW DEALS, NEW LOCATIONS, NEW HARDWARE + 100's of GIVEAWAYS!**" | LET 原文：`TRENDING NOW:` 是置顶热帖前缀，`100's of GIVEAWAYS` 是赠品数量的写法 |
| "**SmokyHosts - 3 Days Only \| Summer Storage VPS Sale \| 50% off \| 20GB SSD OR 50% addon HDD \| Unmetered**" | LET 原文：**`3 Days Only` 是最短期限的写法**，直接写进标题 |
| "**30% off recurring!**" / "**Recurring Discounts**" / "**25% Recurring OFF \| LET Exclusive**" | LET 原文：`Recurring` 三种位置（句中 / 名词 / 标签），**它与"首周期折扣"严格对立** |
| "**25% off: LET25**" / "**LET25**" | LET 原文：**优惠码直接写在标题末尾，用冒号引出** |
| "**[LIFETIME -60%][GIVEWAY]**" | LET 原文：`LIFETIME` + 百分比是"永久折扣"标签；**`GIVEWAY` 是原文拼写错误（正确为 GIVEAWAY），同页两种拼法并存** |
| "**Metanet.ch - Unreachable/Bankrupt**" | LET 原文：**厂商倒闭的写法是 `Unreachable/Bankrupt`，用斜杠并列"联系不上"与"破产"** |
| "**DeluxHost.net \| VPS Restock \| Improved Storage Servers!**" | LET 原文：`VPS Restock` 是补货帖固定前缀 |
| "**Offers**" / "**Service Transfers**" / "**Requests**" / "**Giveaways & Freebies**" / "**Outages**" / "**Industry News**" / "**Reviews**" / "**Providers**" | LET 分类标签原文：**英文社区把 `Offers`（厂商发帖）与 `Requests`（买家求购）分开，另有专门 `Outages` 区** |
| "**[WARNING]**" / "**[FREE]**" / "**[Transfer]**" / "**[Request]**" | LET 标题前缀原文：方括号标签体系 |
| "**Servarica down?**" / "**What has happend to verasel ?**" / "**VSYS Host: UA data centers. What happened and where recovery stands?**" | LET 原文：故障帖三种问法，`<host> down?` 最短，`where recovery stands` 问恢复进度 |
| "**Well, all 100 VPS instances have now been given away.**" / "**But apparently, 100 wasn't enough!**" | LowEndBox 首页原文：**`given away` 是赠品告罄的写法**，必须带数量 |
| "**This is Virtbase's first offer on LowEndBox...**" | LEB 原文：**`first offer on <站点>` 是介绍新厂商的固定句式** |
| "**Exclusive LowEndBox Pricing: 2GB KVM VPS for $1.83/Month First Year!**" | LEB 原文：`Exclusive <站点> Pricing` + `First Year` 限定 |
| "**Oct Promo \| Ryzen 9955HX & EPYC · Instant Setup**" | LEB 原文：**`Oct Promo` 是月份促销标签，`Instant Setup` 是即时开通** |
| "**This site is the largest collection of YABS (Yet Another Benchmark Script) benchmarks on the planet, with over 10,000 user-submitted reports in its database.**" | LEB 原文（介绍 yabsdb）：`user-submitted reports` 是"用户投稿"的说法 |
| "**ServerVerify is a member of the LowEnd family of sites**" | LEB 原文：`family of sites` 指同一旗下的站点群 |
| "**You'll need our special coupon code to get these deals!**" | LEB 原文：要码的提示句 |
| "**I guess Velohost has never heard of inflation.**" | LEB 原文：夸降价的反讽开场 |
| "**reliability, responsive support, and fair pricing**" | LEB 原文：厂商自述三件套的固定顺序 |

### 明日候选

1. **"Expired Deals Get Removed" — We've Never Removed One in 75 Scans** — A1（75 次扫描 / 13 个 UTC 日，**12 天零日内变化；74 次相邻扫描里 73 次字节级完全相同 = 98.6%**；10-05 一天跑了 12 次，结果和跑 1 次一样）+ A4（**最后一件"进货"距今 8 天 6 小时 9 分**，之后 42 次扫描零新增；5 条在场 11 天 18 小时）+ C 栏 vpspromocodes.com 原文（`Expired deals get removed. Active ones stay easy to find.` / `26,555 Active Deals` / `Daily Updates` / `weak offers`）+ B3（bestvpsdeal 宣称 `Official offer pages are monitored for changes`）。缝：**英文券站把"过期即下架"当卖点写进首页，我们从没下过架一条**——不是因为我们守规矩，而是我们的 schema 只有 5 个字段、**没有 expiry 列，结构上就无法表达"这条结束了"**。没人愿意写这个，因为它把"库存大"和"不会清理"两种完全不同的能力混成了一件事
2. **The Page We Link To Has a Countdown Clock. Our Record of It Hasn't Moved in 8 Days** — A5（打开我们自己的 `offer_url` = hetzner.com/sb，页面逐条显示 `06:39:23left` / `17:41:42left` / `20:39:04left` / `22:25:45left`，另有 `max. per month` / `per hour` / `Server AuctionID: 3091544`）+ A1（这条 title 在 75 次扫描里一字未变）+ A4（在场 8 天 6 小时）+ A5 的毛边（title 截断在介词 `from`）。缝：**一个自带倒计时、每小时都在变的拍卖页，被我们记成了一句永远不会变的静态文案**。所有 deals 站存了链接就当存了内容，没有人真的回去打开自己存的那个 URL 看一眼它现在长什么样——因为一打开就会发现自己的记录是冻的
3. **We Call It a VPS Deals Radar — None of the 8 Pages We Check Is a Deals Page** — A3（8 个受检 URL 逐个拆路径：产品落地页×2、定价页×3、产品页×1、首页×1、清仓页×1，**促销/优惠/deals/offers/promo 类路径命中 0**；唯一卖便宜货的 `/en/server-outlet/` 恰好永久不可读）+ A2（**8 个 URL 的 `readable` 在 75 次扫描里零翻转，3 恒 True / 5 恒 False，结构性失败而非抖动**）+ B2（dreamhost.com/promo/wbevps 证明厂商确实有 `/promo/` 专属落地页，只是我们一家都没检查）+ B3（竞品 bestvpsdeal 公开宣称 `Official offer pages are monitored for changes`）+ B7（vpsticker 声称 `15/15 providers returning data`，**没有任何英文站承认自己读不到厂商**）。缝：**英文竞品明确说"我们监控的是官方 offer 页"，而我们监控的是定价页、产品页和首页**——这就是为什么我们的产出这么少、数字这么常规。没有竞品会公布自己的受检清单，因为一公布，读者就能自己判断这份清单配不配得上 "deals" 这个名字

已用：`compare-vps-deals-total-cost`（10-07）、`vps-deals-renews-at-x`（10-08）、`vps-deals-refund-window`（10-09）、`vps-deals-cost-per-gb-ram`（10-09）、`vps-deals-who-collects-vat`（10-09）、`vps-deals-hourly-to-monthly`（10-10）、`vps-deals-cost-per-gb-disk`（10-11）、`vps-deals-auto-renewal-notice`（10-12）、`vps-deals-port-25-smtp-blocked`（10-13）、`vps-deals-sla-credit-how-to-claim`（10-14）、`vps-deals-payment-methods-accepted`（10-15）、**`vps-deals-identity-verification-kyc`（10-16，最后一篇已发布）**。

已降级/不再写第二篇：退款天数（已发）、每 GB 单价（已发）、renews at 换算（已发）、Hourly ×672/730（已消耗）、CPU steal 诊断（英文位占满）、过期 deal（pennyclouds 已占）、Unmetered Port Metered Reality（Day2）、Stuck in an AI Support Loop（Day3）、低价套餐断货/候补（Day6）、Hetzner 拍卖"怎么运作"（Day6）、黑五"预热期填不出价格"（Day8，已改写）、"deals 站都会撑满库存"（Day10 证伪）、**"Flash Deals vs Evergreen Listings"（Day10 候选 #3，今日降级：B4 实测 `evergreen` 在英文里是零售优惠券圈的行话，5 条结果全是 dontpayfull / 360vouchercodes / cloudnine / tervis 这类零售券站，VPS 语境 0 条——racksniff 的 `evergreen listings` 是它借来的自用分类词，不是买家会搜的词，该标题没有检索需求）**。

剩余候选（未被消耗）：YABS 怎么读结果（Day4 候选 #3，**连续第 3 次确认不升级**：B6 英文位仍只有 GitHub 仓库 + yabsdb 跑分库，教程位为 0，中文位被 CSDN/知乎占满）；"Automatically Reverts to Standard Pricing" 四种折扣结束方式（Day5 候选 #2，**今日拿到英文黑五聚合站的官方口径**：blackfriday.hosting FAQ `introductory prices for the first year or billing cycle. When it's time to renew, the regular/non-promotional pricing will apply.` + 三家 Con 栏 `Prices go up on renewal` / `Higher pricing at renewal` / `Renewal prices can go up`，证据已足——**但 `vps-deals-renews-at-x` 已于 10-08 发布，若开此题必须走"英文站把续费涨价写进缺点栏"这个不同切口**）；Hostinger 学生折扣/资格类折扣（Day8 候选 #3，维持池底）；**时区口径（A6，今日新进池备用：柏林 20/75=26.7%、美东 21/75=28.0% 落在当地 9–18 点；UTC 日期与北京日期差一天）——单独成题偏窄，适合并入"更新于到底指什么"类文章做一节**。

---

## 2026-10-18 (Day 12)

> 本次 scan 时间戳 `2026-10-17T18:39:31+00:00` = 北京 10-18 02:39，属当日 scan。fetch + pull --rebase 干净，rebase 到 17d58a4（远端 offer 刷新）。**今天最大外部事件：B1 核心词 SERP 冒出一个全新英文竞品 savecd.com，它做"source-listed + verified + scheduled"几乎和我们同路，但有价格、有 expiry、还查 promo 页——见 B1 与"今日修正"**。

### A. 原创内容邪修

| # | 邪修点 | 为什么别人抄不走 |
|---|---|---|
| A1 | **6 条 deal 去重后只指向 3 个目标页面，其中一个被列了 4 次（4:1 重复）**。逐条去重 `offer_url`：`hostinger.com/vps-hosting` ×4、`hostinger.com/student-discount` ×1、`hetzner.com/sb` ×1 → **distinct offer_url = 3**；去重 `source_url` 只剩 2 个（`/vps-hosting` ×5、`/hosting/` ×1）。**库存数 6 与"目标页面数 3"差 2 倍**——那 4 条全是从同一个 Hostinger VPS 定价页上切下来的 4 个折扣档（70/67/63/65%），不是 4 个独立 deal。80 次扫描里 distinct offer_url 分布恒为「2 ×28 次（只有 Hostinger 时）→ 3 ×52 次（加 Hetzner 后）」，**从来没有超过 3** | 必须肯把 `offer_url` 字段拉出来去重，并把"重复在同页切了几档"算出来。所有 deals 站都把"条数"当首屏卖点（vpsticker `29 live offers`、vpspromocodes `26,555 Active Deals`、今日新竞品 savecd 也只标 `5 providers tracked`）——**去重会把自家头条数字砍半，没人肯做**。顺带挖到硬外部对照：savecd 的 Hostinger listing 指向 `hostinger.com/black-friday-vps-deals`（一个**促销落地页**），我们的 4 条全指向 `/vps-hosting`（产品定价页）——**它查 promo 页、我们一家都没查**（Day11 A3 已记 0/8 受检URL是促销页）。这是我们的洞，不是我们的强项，但只有肯摊开 `offer_url` 清单的人才看得出这个洞 |
| A2 | **自指计数（offer_url == source_url）80 次扫描恒为 4，不管总库存是 5 还是 6**。逐条算 `offer_url == source_url`：4 条 `X% off — Hostinger VPS page` 全部自指（deal 就是它来源的那个产品页本身），`Student discount`（→ `/student-discount`，来自 `/vps-hosting`）与 Hetzner（→ `/sb`，来自 `/hosting/`）不自指。**self-ref 计数分布：4 ×80 次**——库存从 5 涨到 6 那次唯一增长事件，加进来的是一条**非自指** deal（Hetzner）；换句话说**我们加过的每一条新 deal 都是外跳的，原 4 条自指档一个没动** | Day5 A4 在单次扫描里写过"5 自指 vs 1 外跳"这个二分；今天的增量是**把它放到 80 次扫描里证明"4 是结构常数"**——只存当前快照的站（含今日新竞品 savecd，它也存 `[View offer]` + `[Source]` 两条链接，且它的 Hostinger/InMotion listing 两条链接全相同、比我们更彻底地自指）答不出"我的自指率历史上变过没有"。要写出"恒为 4"，必须持有逐条 `offer_url`/`source_url` 且有 80 次历史快照 |
| A3 | **title 字段三种异质写法并存，schema 没有 discount_type / discount_amount 列**。6 条 title 按句法分三类：①`70%/67%/63%/65% off — Hostinger VPS page` ×4（百分比 + em-dash + 来源标签）；②`Student discount` ×1（光杆名词短语，零数字）；③`Server Auction Save money and do good for the planet with refurbished servers from` ×1（被截断在介词 `from` 上的句子片段）。**一个字段里同时装着"百分比折扣""资格类折扣""拍卖描述"三种东西，且没有任何列能让你按折扣类型筛选或按折扣幅度排序** | 要露出这种"我的 title 字段没归一化"，必须敢把原始解析器输出原样贴出来。今日新竞品 savecd 的标题是干净的 `KVM 1` / `VPS 2 vCPU`（**它归一化了，还挂了价格**）——我们暴露的是带毛边的原始字符串。商业站不会把"句子断在 from 上"这种解析瑕疵亮出来，因为那等于承认管道糙。但正是这种糙，读者才能反推"这家是真从 HTML 里切的，不是人填的" |
| A4 | **Hostinger 四档百分比 {63, 65, 67, 70} 的集合与存储顺序，80 次扫描一字未变——它们是价格档，不是促销**。对 80 次独立扫描逐次抽 Hostinger 的百分比：sorted set 只有一种 `(63, 65, 67, 70)`、出现 80 次；as-stored order 也只有一种 `(70, 67, 63, 65)`、出现 80 次。**集合冻结 + 顺序冻结 = 13 天里这四个数字一个没动过**。Day5 A3 早就注意到顺序不单调（70→67→63→65，第三个 63 比第四个 65 小），Day10 A1 又做过 title 断档校验（n == expected）；今天的新结论是**集合本身也冻结**——这四个数字是 Hostinger 长期挂着的四档常规定价，不是任何限时促销 | 必须把百分比抽出来、再对 80 次扫描做集合去重，才说得出"这四档从没变过"。只截一次图的人会以为 70% 是"今天的促销"，而它其实是常驻档。**B4 给了外部佐证**：英文圈对"不结束的折扣"是有命名的——FastComet 条款叫 `Same Renewal Price (Fixed Price)`、vncoupon 转 RareCloud 写 `locked at the flash rate for every renewal, not just year one … The list price never returns`。**行业有词（Fixed Price / locked / flash rate），但没有任何 deals 站把自己的 listing 按"tier vs promo"分类**——我们能，因为 80 次扫描证明了我们的 4 条 100% 是 tier |
| A5 | **fetched_at 秒级聚类：6 条 deal 只落在 2 个秒点，反推只有 2 次 HTTP 读取，且一次读了 5 条、一次读了 1 条**。本次 6 条 offer 的 `fetched_at`：5 条 Hostinger 全在 `18:39:23`、1 条 Hetzner 在 `18:39:26` → distinct seconds = 2。**6 条 deal 实际只来自 2 次 HTTP 抓取**，3 秒间隔正好对应 source_checks 里 Hostinger 在前、Hetzner 在后的顺序。**5:1 的产量分裂**——一次抓取返回 5 条 deal，另一次只返回 1 条；返回 5 条的那一页（`/vps-hosting`）正是 A1 里被列 4 次自指、A2 里贡献全部 4 条自指的那一页 | Day5 A2 写过"8 秒 harvest"（总耗时），Day9 算过 harvest span 分布（0s×24/1s×7/2s×29/3s×1）；**今天的新切口是"单次抓取的产量分裂"**——把 6 条 deal 按秒聚类后得到 5:1，意味着一个源页的单位产出是另一个的 5 倍。这个比要靠逐条 `fetched_at`（秒级）才能算；今日新竞品 savecd 只在页脚挂 `6h check cadence`（节奏），不公布每条 deal 的抓取时刻——它有节奏、没有 per-deal 时间戳，所以算不出产量分裂 |

### B. 谷歌搜索查词（今天真跑过的）

| query | SERP 上看到了什么 | 判断 |
|---|---|--|
| `vps deals` | **核心词**。5 条：vpsticker.com（`15 providers tracked` / `29 live offers` / `15/15 providers returning data` / **`2026-10-02 last refresh`，距今已 16 天**）、vpsfilter.com（`Updated daily`）、rackbazaar.com（`3 providers, 9 plans` / `No dark patterns`）、**savecd.com（全新英文站：`Source-listed price` / `See the source.` / `Official-source VPS offers, checked on a schedule. We show only prices we can verify and link every listing to its source.` / `5 providers tracked` / `6h check cadence` / 每条挂 `Valid until 2027-10-16`）**、vncoupon.com（中文） | **今天最重的一条**。savecd 是本周期第一个在核心词 SERP 出现、且**和我们走同一条"source-listed + 定时 + 可验证"路线**的英文竞品。它把 Hostinger KVM1/2/4/8 挂成 4 张独立卡（有价 $6.49/$8.99/$12.99/$25.99），`[View offer]` 与 `[Source]` 都指向 `hostinger.com/black-friday-vps-deals`（**促销页**）。**vpsticker 的"15/15 全返回 + 刷新停在 16 天前"自相矛盾连续第 5 天复现** |
| `vps deals same plan listed multiple times one page` | 5 条**全部跑题**：hostigger.com（拼写错的 VPS 站）、smaato.com（广告技术 FLEDGE）、dreamhost.com（电商 VPS 优化）、清华 Liquid 去重文件系统论文、veritas.com（Enterprise Vault） | **"deal 重复列在同一页"这个话题英文 SERP 命中 0 条**——没有一家在写，也没有检索需求。但 A1 的去重结论照样成立：**没人写，恰好说明"6 条只来自 3 个页面"这个数没人替读者算过**。可做 |
| `hostinger vps student discount eligibility verification how to qualify` | 5 条：groupon.co.uk（Overclockers 学生 5%/10% off）、**interserver.net/webhosting/student-webhosting.html（`Verify student eligibility … qualifying school email address`）**、freevps.edu.pl、fasthosts.co.uk（VPS 落地页）、idcspy.com（中文，确认 Hostinger 走 Student Beans 验学生身份） | 印证 A1 的"3 种页面类型"：`/student-discount` 是**资格核验页**（要验学生身份才放行），不是 VPS 产品页。Interserver 把 `Verify student eligibility` 写成步骤标题。**1/6 的"deal"卖的不是 VPS，是资格检查**——这条缝没人写过 |
| `vps deal permanent discount tier not promotion renewal price same every month` | 5 条：**vncoupon.com（RareCloud 圣诞文：`locked at the flash rate for every renewal, not just year one. The lock-in is the point. … The list price never returns`）**、52pchome.cn（中文）、**savecd.com（`Source-listed price`）**、**fastcomet.com/terms/promotions（`Same Renewal Price (Fixed Price)`）** | **今天最有价值的一条**。英文圈对"不结束的折扣"是有官方命名的：FastComet 条款叫 `Same Renewal Price (Fixed Price)`、RareCloud 叫 `locked at the flash rate` / `The list price never returns`。**行业有词，但 deals 站不分类**——A4 的"我们的 4 条 80 次扫描没动 = tier"正好补上这个空缺 |
| `vps offers point to product pricing page not dedicated promo landing page` | 5 条：vncoupon.com（RackNerd）、vncoupon.com（Bandwagon Host promo）、**hostcomparehub.com（`These offers are written as editorial deal notes, not blind promo-code dumping`）**、tilda.cc（落地页建站器）、voymedia.com（创业） | hostcomparehub 是新竞品定位语（`editorial deal notes` vs `blind promo-code dumping`），其余 0 条 VPS 专用。**"deal 链接到底指向产品页还是 promo 页"英文 SERP 0 条**——A1 的对照（我们指产品页、savecd 指 promo 页）没人替读者做过 |
| `vps provider official offer page versus pricing page monitored deals radar` | 5 条：bestvpsdeal.com（第 1，文案仍 `Official offer pages are monitored for changes. Every listing shows its source`）、arubacloud.com、vpspromocodes.com、foxvalleywebdesign.com、digitalocean.com/resources/articles/vultr-alternatives | bestvpsdeal 仍宣称监控"official offer pages"，vpspromocodes 仍宣称 `Expired deals get removed`。**加上今天新出现的 savecd（`Source-listed price` + `[Source]` 链接 + `Valid until`），本周期核心词周边已有 3 家英文竞品明确把"挂来源"当卖点**——Day11"没有英文站挂来源"的前提**今日作废，见"今日修正" |

### C. 老外怎么说（真在用的说法）

| phrase | 谁在用 / 什么意思 |
|---|---|
| "**02:06:45 left**" / "**03:28:31 left**" / "**04:33:20 left**" / "**06:44:02 left**" / "**10:40:11 left**" / "**11:40:54 left**" / "**20:13:58 left**" / "**23:25:21 left**" / "**23:42:06 left**" / "**24:06:58 left**" | **hetzner.com/sb（我们唯一那条非 Hostinger deal 的 `offer_url`）页面原文，今日复抓**：拍卖 listing 每条挂一个实时走字的 HH:MM:SS 倒计时，`left` 前面是剩余时间。**全部 10 个值都与 Day11 抓到的 `06:39:23 / 17:41:42 / 20:39:04 / 22:25:45` 不同 → 页面每小时都在变，而我们对它的 title 80 次扫描一字未变** |
| "**don't wait too long—someone else might snatch up your offer**" | 同上 hetzner.com/sb 原文（今日新出现）：拍卖页的催单句，`snatch up` = 抢走 |
| "**Show 132 results**" / "**132 results**" | 同上原文：拍卖页今日在架 132 台二手机（Day11 未抓此计数） |
| "**Server AuctionID: 3095297**" / "**3095088**" / "**3095016**" / "**3094958**" / "**3095093**" | 同上原文：每台拍卖机唯一编号。**与 Day11 的 `3091544` 全不同 → 库存已轮换** |
| "**Prices are dropping on our Server Auction.**" | 同上页头原文：荷兰式拍卖的总标题 |
| "**Enable IPv6 only**" / "**only auctions**" / "**sort by:**" / "**Filter (0)**" / "**Copy link**" | 同上筛选区原文：拍卖页的过滤标签 |
| "**max. per month**" / "**per hour**" | 同上原文：拍卖价把"每月最高"与"每小时"两种计价单位并排 |
| "**Traffic: unlimited**" / "**Location #FSN1-DC13**" / "**#FSN1-DC8**" / "**#FSN1-DC17**" | 同上原文：流量与机房写法，**机房用 `#` + 代号** |
| "**replacement of defective hardware**" / "**free email support**" / "**free phone support**" / "**24/7 Monitoring**" / "**24h Reset Service via Web Interface**" / "**Full Root Access**" | 同上 Support services 区原文：拍卖机附带服务的列举 |
| "**ECC**" / "**NIC 1 Gbit - Intel I219-LM**" / "**2 x 4.0 TB Enterprise HDD**" / "**2 x SSD M.2 NVMe 512 GB**" / "**2 x RAM 32768 MB DDR4**" | 同上 Information 区原文：硬件规格字段名；**德式小数逗号 `4,0 TB` 与点号 `4.0 TB` 同页并存** |
| "**Source-listed price. Billing period, upfront payment and renewal terms must be checked with the provider.**" | **savecd.com（今日 B1 新发现的英文竞品）每条 deal 卡片原文**：把"价格来自源页、续费要自己去问厂商"写成标准免责句。**与我们"没有价格列"正面相邻**——它有价但甩锅续费，我们连价都没有 |
| "**See the source.**" / "**Official-source VPS offers, checked on a schedule. We show only prices we can verify and link every listing to its source.**" | 同上 savecd 首屏原文：**和我们几乎同路的定位语**（挂来源 + 定时 + 可验证） |
| "**5 providers tracked**" / "**6h check cadence**" / "**Valid until 2027-10-16**" | 同上 savecd 指标区原文：跟踪 5 家、6 小时一刷、**每条带有效期**。**它有 expiry，我们没有**（Day8 A3：schema 无 expiry 列） |
| "**[View offer ↗]**" / "**[Source]**" | 同上按钮原文：每条 deal 挂两条链接（去向 + 来源）。**与我们 `offer_url` + `source_url` 双字段同构**，但它的 Hostinger listing 两条都指向 `/black-friday-vps-deals`（自指且指向 promo 页） |
| "**locked at the flash rate for every renewal, not just year one. The lock-in is the point. Sign up at the flash rate, and that is the price paid in year two, year three, and year five. The list price never returns**" | vncoupon.com 转 RareCloud 圣诞文原文：**英文圈对"不结束的折扣"的完整定义句**，`locked` / `flash rate` / `lock-in` / `list price never returns` 四个词成套 |
| "**Same Renewal Price (Fixed Price)**" | FastComet 条款页 SERP 摘要原文：**厂商官方对"续费不涨价"的命名**，`Fixed Price` 是正式术语 |
| "**Verify student eligibility** … **qualifying school email address**" | interserver.net 学生免费主机页原文：学生资格核验的标准步骤句，`qualifying` 限定词 |
| "**Early Bird discounts available for 12 months on our 1U, 2U, and 4U plans.**" | LowEndBox 原文（raindog308，Cloudnium 托管帖，10-17）：`Early Bird` + 限定 12 个月 + 按机架规格（1U/2U/4U） |
| "**No tricks here, just a wonderful treat: $500 in cold hard cash!**" | LEB 原文（raindog308，ServerHost 赠品帖，10-15）：赠品开场句，`cold hard cash` = 现金 |
| "**FREE for an entire year**" | LEB 原文（raindog308，RackNerd/AdminBolt 赠品帖，10-09）：免费一年的写法 |
| "**a chance for qualifying VPS winners to pick up one of 20 lifetime AdminBolt licenses!**" | 同上 LEB 原文：`qualifying … winners` = 资格赛赠品的限定写法 |
| "**Awesome Deals for EU Customers Only!**" | LEB 原文（Virtbase 帖标题，10-16）：**地理资格限制直接写进标题** |
| "**Godlike.Host is Back!**" / "**Velohost Returns With Even Cheaper Prices!**" | LEB 帖标题原文：厂商消失后回归的两种宣告句式（`is Back!` / `Returns With …`） |
| "**they were selling a 4GB VPS … for 3.00€/month. Now they're selling that same package for only 2.60€/month!**" | LEB 原文（raindog308，Velohost 帖）：**同套餐降价的对照写法**，`same package` 强调是同一货 |
| "**If you didn't read carefully, you may not be aware your service is being downgraded.**" | LEB 原文（raindog308，Microsoft 365 砍存储帖）：**静默降级的提醒句**，`downgraded` 是买家最怕的词 |
| "**Yet Another cPanel and WHMCS Price Increase.**" | LEB 帖标题原文：`Yet Another` 是社区对涨价的固定反讽前缀 |
| "**25% Recurring OFF \| LET Exclusive**" / "**Recurring Discounts**" | LowEndTalk 帖标题原文（NameBig / tanek）：`Recurring` 在标题里既可作后缀形容词也可作名词标签，**与"首周期折扣"严格对立** |
| "**LIFETIME -60%**" / "**LIFETIME LICENSES**" / "**Lifetime Web Hosting**" | LET 帖标题原文（AirnodeHosting / RackNerd / 买家 ouzm、greeneyed）：`LIFETIME` + 百分比是永久折扣标签，**与 `Recurring` 又是对立的另一极** |
| "**VPS Restock**" / "**our popular plans are back!**" | LET 帖标题原文（DeluxHost / serverpoint）：补货/重新上架的固定写法 |
| "**Servarica down?**" / "**What has happend to verasel ?**" / "**What happened and where recovery stands?**" | LET 帖标题原文：故障帖三种问法，`<host> down?` 最短，`where recovery stands` 问恢复进度（`happend` 是原帖拼写错） |
| "**unusable IPv4 (broadcast address), no ticket reply in 5 days**" / "**lost my entire virtual disk during maintenance – no backups available**" / "**Assigned a non-routable IANA documentation IP**" | LET 帖标题原文：买家控诉厂商的三种写法（IP 给错 / 维修丢盘 / 工单 5 天不回） |
| "**1Gbps Unmetered**" / "**UNMETERED BW**" / "**330T traffic**" / "**100TB**" / "**10G bandwidth**" | LET 帖标题原文：带宽的三种标法（速率不限流量 / 不限流量缩写 / 流量配额数字） |
| "**LET YABS Thread**" / "**archive for your YABS & bench runs**" | LET 帖标题原文（Astro / DejavuMoe）：YABS 跑分的汇总帖与归档站 |
| "**WTB:**" / "**LF:**" / "**[Request]**" / "**[WARNING]**" / "**[Transfer]**" / "**LET Exclusive**" | LET 标题前缀原文：买卖/求购/警告/转让/独家 的方括号标签体系 |
| "**100% price increase**" / "**12M expiry 22/06/27 transfer**" | LET 帖标题原文（bobert / Samoht999）：涨价倍数写法 / 二手服转让的"剩余 12 个月 + 到期日"写法 |
| "**DMCA Ignored VPS needed!**" / "**seedboxes**" / "**VPS for torrenting**" | LET 求购帖原文：离岸/种子盒/PT 用途的求购黑话 |

### 明日候选

1. **"6 Deals, 3 Pages": Why a VPS Deal Count Is Always Inflated 2:1** — A1（去重 `offer_url` 6→3，`/vps-hosting` 被列 4 次 = 4:1 重复；3 种页面类型：产品定价页 / 学生资格核验页 / 二手拍卖页）+ A2（自指计数 80 次恒为 4，库存 5→6 增长事件加的是非自指 deal）+ B2（"deal 重复列在同页"英文 SERP 0 条 = 没人写）+ B1（新竞品 savecd 也只标 `5 providers tracked`，不公布去重后页面数）。缝：**所有 deals 站都把"条数"当首屏卖点（29 live offers / 26,555 Active Deals / 5 providers），没一家公布"去重后只剩几个页面"**。我们能，因为逐条存了 `offer_url`。6 条只来自 3 个页面、其中一页被切了 4 档折扣——"deal 数"和"页面数"差 2 倍，这个差没人替读者算过
2. **"Same Renewal Price (Fixed Price)": The VPS Discounts That Never Expire — and Why 80 Scans Proved Ours Are Tiers, Not Promos** — A4（Hostinger {63,65,67,70} 集合与顺序 80 次扫描一字未变 = 常驻档不是限时促销）+ B4（FastComet 条款 `Same Renewal Price (Fixed Price)`、RareCloud `locked at the flash rate for every renewal … The list price never returns`）+ C 栏（`Fixed Price` / `locked` / `flash rate` / `list price never returns` 四词成套）。缝：**行业对"不结束的折扣"是有官方命名的（Fixed Price / locked / flash rate），但没有任何 deals 站把自己的 listing 按"tier vs promo"分类**——我们能，因为 80 次扫描证明我们的 4 条百分比 13 天没动过。**与 10-08 `vps-deals-renews-at-x` 不重复**：那篇讲续费涨价公式（renewal increase = d/(1-d)），这篇讲"不涨价的折扣"——方向相反
3. **"Source-Listed Price": Two VPS Deal Radars That Refuse to Guess — and the Opposite Tradeoffs They Made** — A3（我们暴露原始 title 字符串、无 price/expiry 列）+ A5（我们逐条 `fetched_at` 秒级、可算 5:1 产量分裂）+ B1/B6（本周核心词 SERP 新出现的英文竞品做 `Source-listed price` / `See the source` / `5 providers tracked` / `6h check cadence` / `Valid until 2027-10-16`，几乎同路但有价、有 expiry、还查 promo 页）+ C 栏（savecd 的免责句 `Billing period, upfront payment and renewal terms must be checked with the provider`）。缝：**一个和我们走同一条"挂来源 + 定时 + 可验证"路线的英文站本周冒出来了，但它做了相反的取舍（有价有 expiry、无 80 次历史、无 per-deal 时间戳、不公开 readable:false）**。没人会写"这里有个同路竞品、它哪里比我们强、我们哪里比它强"——但这种对照对正在选雷达的买家最有用。标题不点名竞品，用"two radars"

已用：`compare-vps-deals-total-cost`（10-07）、`vps-deals-renews-at-x`（10-08）、`vps-deals-refund-window`（10-09）、`vps-deals-cost-per-gb-ram`（10-09）、`vps-deals-who-collects-vat`（10-09）、`vps-deals-hourly-to-monthly`（10-10）、`vps-deals-cost-per-gb-disk`（10-11）、`vps-deals-auto-renewal-notice`（10-12）、`vps-deals-port-25-smtp-blocked`（10-13）、`vps-deals-sla-credit-how-to-claim`（10-14）、`vps-deals-payment-methods-accepted`（10-15）、`vps-deals-identity-verification-kyc`（10-16）、**`vps-deals-nonpayment-suspension-deletion`（10-17，最后一篇已发布，取自 gap-ledger #10 而非 line3 候选）**。

已降级/不再写第二篇：退款天数（已发）、每 GB 单价（已发）、renews at 换算（已发）、Hourly ×672/730（已消耗）、CPU steal 诊断（英文位占满）、过期 deal（pennyclouds 已占）、Unmetered Port Metered Reality（Day2）、Stuck in an AI Support Loop（Day3）、低价套餐断货/候补（Day6）、Hetzner 拍卖"怎么运作"（Day6）、黑五"预热期填不出价格"（Day8，已改写）、"deals 站都会撑满库存"（Day10 证伪）、"Flash Deals vs Evergreen Listings"（Day10 候选 #3，Day11 降级）。

**今日修正（重要）**：Day11 B7 / Day9 写过"没有任何英文站公开承认自己读不到厂商 / 没有英文站挂来源"——**今日 B1 出现的 savecd.com 直接打脸**：它挂 `[Source]` 链接、写 `See the source`、`link every listing to its source`，且跟踪 5 家（少于我们 8 家，等于隐含承认覆盖不全）。**"挂来源"不再是我们独有**；我们仍独有的是 80 次 `source_scan_at` 历史 + 逐条 `fetched_at` 秒级 + `source_checks` readable:false 公开 + 无 price/expiry 列的原始 schema。**Day11 候选 #3"我们叫 deals radar 却 0 受检URL是促销页"今日被 savecd 进一步坐实为弱点**：savecd 的 Hostinger listing 指向 `/black-friday-vps-deals` 促销页，我们 4 条全指向 `/vps-hosting` 产品页——它查 promo 页、我们没查。该候选若开必须走"我们承认漏了 promo 页"的自曝切口，不能当强项写。

剩余候选（未被消耗）：**Day11 三条候选全部未被 10-17 文章消耗**（10-17 取的是 gap-ledger #10 欠费停删机，非 line3 候选），但需逐条复检：①"Expired Deals Get Removed"（Day11 #1）——savecd 有 `Valid until 2027-10-16` expiry 字段 → 它能下架、我们不能（schema 无 expiry），缝仍在但对照对象变了；②"倒计时 vs 静态 title"（Day11 #2）——今日 hetzner.com/sb 复抓拿到 10 个全新倒计时值 + 全新 AuctionID（3095297 等）+ `Show 132 results` + `don't wait too long—someone else might snatch up your offer`，证据比 Day11 更硬，**可直接开**；③"deals radar 命名"（Day11 #3）——见上"今日修正"，降为弱点自曝口径，能开但须承认漏 promo 页。YABS 怎么读（Day4 #3，连续第 4 次不升级）；"Automatically Reverts to Standard Pricing"四种折扣结束方式（Day5 #2，证据足，须避开 renews-at-x）；Hostinger 学生折扣（Day8 #3，池底）；时区口径（A6，并入"更新于指什么"做一节）。**gap-ledger 提醒：可用未写只剩 #11/#12/#13 三条，BENCH 第三轮已到期（原定不晚于 10-19），line3 候选是 gap-ledger 写完后的回退池，不是当前取题源**。

---

## 2026-10-19 (Day 13)

> 本次 scan 时间戳 `2026-10-18T18:40:00+00:00` = 北京 10-19 02:40，属当日 scan。fetch + pull --rebase 干净，fast-forward 到 e08667b（远端 offer 刷新）。**85 次独立扫描**（115 个提交按 `source_scan_at` 去重后），跨度 `2026-10-04T23:49:08Z → 2026-10-18T18:40:00Z` = **13 天 18 小时 50 分**。**今天最大外部事件：B2 冒出一个全新英文竞品 cloudhostdeals.com，它把「每个受检 URL 的抓取状态」做成公开表格，并区分 4 种失败态——而我们只有 1 个布尔值 `readable`。同一天它还从 DigitalOcean 拿到 2 条 listing，我们对 DigitalOcean 85 次扫描 0 条。见 A1 / B2 /「今日修正」。**

### A. 原创内容邪修

| # | 邪修点 | 为什么别人抄不走 |
|---|---|---|
| A1 | **8 个受检 URL → 3 个可读 → 2 家产出 → 其中一家占 83.3%：一个没人愿意公布的漏斗**。本次 `source_checks` 8 条里 `readable: true` 只有 3 条（Hostinger `/vps-hosting`、Hetzner `/hosting/`、DigitalOcean `/pricing/droplets`）；但**真正产出 offer 的只有 2 家**——Hostinger 5 条、Hetzner 1 条，**DigitalOcean 全程可读却 0 条**。也就是 **8 个受检页里有 6 个，在 85 次扫描里一条 deal 都没产出过**（DigitalOcean / Vultr / Linode(Akamai) / Contabo×3）。单厂商集中度：**top-1 = 5/6 = 83.3%**；放到历史上，产出厂商数分布是「1 家 ×28 次扫描 → 2 家 ×57 次」，top-1 占比分布是「**100.0% ×28 次 → 83.3% ×57 次**」——即使" diversify "过一次，83.3% 的库存仍来自一家、一个页面 | 必须持有逐条 `readable` 且愿意把"8 家只产出 2 家"这个漏斗摊开。**英文圈把"provider 数"当标准卖点**：vpsticker 标 `15 providers tracked`、savecd 标 `5 providers tracked`、今日新站 cloudhostdeals 标 `3 providers tracked`——**但没有一家公布"跟踪 N 家 / 实际产出几家 / 最大一家占多少"**。因为一公布，读者就会发现 "15 providers tracked" 和"其实只有 2 家在供货"是两件事。我们能算，因为 85 次快照里每一条 `readable` 都在 |
| A2 | **库存里最年轻的一条 deal 已经 10 天 6 小时了**。逐条追"首次出现在第几次扫描"：Hostinger 5 条全部 **85/85 次扫描在场、年龄 13 天 18:50:52**；Hetzner 一条 **57 次扫描在场、年龄 10 天 6:02:57**。**没有任何一条 deal 的年龄低于 10 天**。总数序列只取过两个值 {5, 6}、**85 次扫描里从未下降过**；唯一一次增长事件可精确到第 28 次扫描、`2026-10-08T12:37:03Z`（5→6），此后 57 次扫描零新增、零下架 | 要说出"最年轻的一条 10 天"，必须给每条 deal 建"首见扫描序号"，也就是必须存 85 次快照而不是当前快照。**没有一家 deals 站公布自己 listing 的年龄**：它们公布的是"更新于"（cloudhostdeals `Updated 2026-10-18 19:50`、vpsticker `every 6 hours`），那是**页面刷新时间**，不是**listing 在场时间**。这两个数可以差 10 天——因为页面每小时刷一次，但里面躺着的还是 10 天前那批货。肯把这两个时间分开算的站，等于承认自己的"live deals"其实不 live |
| A3 | **我们的列表 85 次扫描只有 2 种排列，而这两种排列无法按折扣力度排序——因为折扣幅度只存在于 title 字符串里**。对 85 次扫描做排列去重：只有 2 种（57 次带 Hetzner、28 次不带，两者只在末尾差一条）。实际顺序恒为 `Student discount → 70% → 67% → 63% → 65% → Server Auction…`，**百分比段是 70,67,63,65——既不降序也不升序**（63 出现在 65 前面）；也不是字母序；也不是按 provider 分组后排的（Hostinger 内部先掺一条资格类折扣，再排 4 档百分比）。**这是 HTML DOM 顺序**。根因：schema 只有 5 个字段，**既没有 price 列也没有 discount 数值列**，折扣幅度被锁在 `70% off — Hostinger VPS page` 这种字符串里，**结构上无法排序、无法筛选、无法算"最大折扣"** | 必须敢说"我的列表排不了序"。**英文竞品之所以能排序，是因为它们有价**：cloudcuttersdeals 每条挂 `Regular $59.00/mo / Sale Price $29.99/mo / Discount 49% / Term 12mo / Savings $348.12` 五列，有价才有 `Savings`；savecd 明写 `A listed price alone does not establish a discount`。**我们连"折扣力度"这个数字都没有，所以顺序只能是抓下来的 DOM 序**。B5 实测"listing 排序/排名"这个话题英文 SERP 0 条 VPS 专用命中——没人写，因为能排序的站觉得理所当然，不能排序的站不会自曝 |
| A4 | **title 字符串 85 次扫描只有 2 种长度组合，Hetzner 那条全历史只有 1 个字符串、82 字符、永远断在 `servers from` 上——解析后零清洗**。对每次扫描取 6 条 title 的长度元组：只有 2 种 `(16,28,28,28,28,82)` ×57 次、`(16,28,28,28,28)` ×28 次。再把 Hetzner 那条单独去重：**85 次扫描里它的 title 字符串只有 1 个版本、长度恒为 82、结尾恒为 `servers from`**（句子被截断在介词上）。**从 10-08 加入至今，没有任何一次后处理去修这个截断、去补全省略号、去统一大小写** | Day12 A3 讲的是"title 字段里混装三种异质写法"，**今天的增量是"这种混装在 85 次扫描里字节级恒定"**——等于证明管道里**根本没有清洗/归一化这一步**，原件什么样就存什么样。商业站会把字符串洗干净再展示（savecd 的标题是 `KVM 1` / `VPS 2 vCPU` 这种干净规格名）；**把"断在介词上"原样挂出去，等于把解析器的毛边亮给读者看**。没人肯，因为那等于承认管道糙——但正是这种糙，读者才能反推"这家是真从 HTML 里切的，不是人填的表" |
| A5 | **482 条 offer 链接，0 条带查询串、0 条带 utm/ref/affiliate 参数、100% https、路径深度全为 1**。把 85 次扫描的全部 482 行 offer 拿出来扫 URL：含 `?` 的 **0 条**；含 `utm` / `ref=` / `aff` / `affiliate` 任一标记的 **0 条**；`http://` 明文 **0 条**（全 https）；路径段数全部为 1。distinct offer_url 全历史只有 3 个。**我们发出去的每一个链接都是裸的官方 URL，没有一个追踪参数、没有一个佣金 ID** | 这个数要逐条扫 482 个 URL 才说得出来，而且**说出来是在跟整个行业的商业模型作对**。B3 实测英文站的佣金披露是标配：vpsticker FAQ 字面就挂着 `Do you earn…`、codeless 写 `When you acquire products through affiliate links on our site, we earn a commission`、今日新站 cloudhostdeals 也写 `Some links may be affiliate links, which means a commission may be earned at no extra cost to you`。**所有人都在声明"我有佣金"，没有一个人在声明"我一个参数都没有"**——因为前者是免责，后者是自断收入。而读者只要看一眼地址栏就能验证我们说的是不是真的，这种可自证的事实，反而是最难抄的 |

### B. 谷歌搜索查词（今天真跑过的）

| query | SERP 上看到了什么 | 判断 |
|---|---|--|
| `vps deals` | **核心词**。5 条：vncoupon.com（中文）、**vpsticker.com（`15 providers tracked` / `29 live offers` / `refreshed every 6 hours` / `no estimated numbers`）**、vpsfilter.com（`Updated daily`）、rackbazaar.com（`3 providers, 9 plans` / `No dark patterns`）、vpsbenchmarks.com/vps_coupons（`Current offers 23` / `Black November`）。**savecd.com 今天掉出前五**（Day12 时排第 4） | **核心词英文位波动仍然大**：Day12 新出现的 savecd 一天就掉出前五，说明这条 SERP 每天在洗牌，**任何"我们在第几位"的判断都不能沿用昨天**。vpsticker 的 `refreshed every 6 hours` 与 `2026-10-02 last refresh`（距今 16 天）自相矛盾**连续第 6 天复现** |
| `vps deals site how many providers tracked provider count` | **今天最重的一条**。5 条：savecd.com（第 1）、vpsticker.com（`15 providers tracked` / `29 live offers` / `15/15 providers returning data` / **`2026-10-02 last refresh`**）、**cloudhostdeals.com（全新英文站，见下）**、vncoupon.com、nodecompass.com（新英文站，`Cheap VPS deals & promo offers directory`） | **新竞品 cloudhostdeals.com 是本周期信息量最大的一家**：`7 live listings` / `3 providers tracked` / `Updated 2026-10-18 19:50`（**今天**），且它把"每个受检 URL 的抓取结果"做成公开表，区分 4 种失败态。**它还跟踪 DigitalOcean 并拿到 2 条 listing**——我们同样跟踪 DigitalOcean，85 次扫描 `readable` 恒 True、0 条 offer。同一厂商、不同页面、相反结果。**这是今天 A1 最硬的外部对照** |
| `vps deals site affiliate links commission disclosure we earn` | 5 条：vpsticker.com（FAQ 字面挂着 **`Do you earn`** 这个截断问句）、webhosting1st.com/affiliate.html（`you will earn 70% commission`）、codeless.co（`When you acquire products through affiliate links on our site, we earn a commission`）、dreamhost.com/blog/best-vps-hosting/、crazydomains.com/affiliates/ | **佣金披露是英文 deals 站的行业标配，5 条里 3 条是明写"我赚佣金"**。**没有任何一家声明"我的链接不带追踪参数"** → A5 的缝成立：所有人声明的是"我有佣金"，没人声明"我零参数"。两者方向相反，且后者可被读者用地址栏自行验证 |
| `hostinger vps 70% off discount permanent tier always available not limited time` | 5 条：hostinger.com.hk/vps-hosting（`最高立减 70%` 与 **`以¥87.99/月 的价格续订 2 年`** 同页并列）、vps.me（`up to 70% off`）、hostigger.com、hostripples.co.uk、edealsfollow.com（零售券站） | 官方页自证：**70% 与"续订价"是同页并列的两个数**，`up to` 是关键限定词（英文站一律写 `up to 70%`，中文站写"最高立减"）。**这坐实 A4 的判断：我们 title 里那个 70% 是页面上的常驻档位上限，不是一笔限时交易** |
| `vps deals listing order sorted by price or discount how offers are ranked` | 5 条：**savecd.com（`We extract named prices from official structured data. A listed price alone does not establish a discount or include all billing conditions; use the source link to check them.`）**、vncoupon.com/tag/racknerd/、blog.naibabiji.com（中文）、newcoupons.info、**cloudcuttersdeals.com（`Regular $59.00/mo / Sale Price $29.99/mo / Discount 49% / Term 12mo / Savings $348.12`）** | **"listing 怎么排序"英文 SERP 0 条 VPS 专用命中**——没人写，因为能排序的站觉得理所当然。但 cloudcuttersdeals 暴露了前提：**要算出 `Savings` 这一列，你必须同时有 Regular 价和 Sale 价**；savecd 更直接：`A listed price alone does not establish a discount`。**我们没有 price 列 → 我们既算不出 Savings，也排不了序**（A3）。这是结构限制，不是偷懒 |
| `vps deal no end date offer stays listed forever never expires` | 5 条：vncoupon.com/vps-hosting/（Noble VPS `25% Off … from $7.70/mo`，dated Sep 29）、vncoupon.com/tag/racknerd/、dreamhost.com/promo/wbevps/、groupon.com.au（零售券，**完全跑题**）、vpsfreehosting.com | **"不结束的折扣"英文 SERP 0 条直接命中**，5 条里 1 条零售券站彻底跑题 → 这个角度**没有检索需求**，不宜做标题。但 A2 换个说法就有货：**不是"折扣不结束"，而是"我的列表里最年轻的一条已经 10 天"**——前者没人搜，后者是可自曝的硬事实 |

### C. 老外怎么说（真在用的说法）

| phrase | 谁在用 / 什么意思 |
|---|---|
| "**page read, no price published in the HTML - not listed**" | **cloudhostdeals.com（今日 B2 新发现的英文站）"Where these numbers come from" 表内原文**：**失败态之一**——页面读到了，但价格不在 HTML 里（JS 渲染），所以不收录。这是全行业最精确的一次失败自述 |
| "**page read, nothing usable found**" | 同上原文：**失败态之二**——读到了但没解析出可用内容。与上面那条是两种不同的失败 |
| "**blocked by the provider's robots.txt - not fetched**" | 同上原文：**失败态之三**——被 robots.txt 挡住，明确写"没有抓取"（遵守规则，不是抓不到） |
| "**blocked by the provider (HTTP Error 403: Forbidden)**" | 同上原文：**失败态之四**——被厂商主动拒绝，连 HTTP 状态码都写出来。**一家站用 4 个不同句子描述"我没读到"，我们只用 `readable: false` 一个布尔值**（A1） |
| "**When a page cannot be read, we say so instead of filling in a guess.**" | 同上原文（首屏）：把"读不到就说读不到、不猜一个数"写成卖点 |
| "**Some providers render prices with JavaScript or block automated readers. When this site cannot read a number it leaves the field empty instead of estimating one.**" | 同上 FAQ 原文：`leaves the field empty instead of estimating one` = 宁可留空也不估算。**这是英文圈对"数据缺失"最完整的处理声明** |
| "**Every six hours, and the timestamp at the bottom of the page shows the last successful read.**" | 同上 FAQ 原文：`last successful read` —— 强调"成功"那一次，与 vpsticker 挂在首屏却停在 `2026-10-02` 形成对照 |
| "**Prices and promo codes read straight from each provider's own public pricing or promo page. Every number on this site links back to where it came from.**" | 同上首屏原文。`read straight from` = 直接读自；`links back to where it came from` = 回填来源 |
| "**7 live listings**" / "**3 providers tracked**" / "**Updated 2026-10-18 19:50**" | 同上指标区原文：**它把"条数 / 厂商数 / 更新时间"三个数并排挂在首屏**——和我们 A1 的漏斗是同一组指标，但它只报前两个 |
| "**2 listingsfrom 3.0**" / "**3 listingsfrom 6.6**" / "**from 2.89**" | 同上 "Providers we track" 区原文：每家挂"几条 listing + 起价"，`from` 是起价的标准写法 |
| "**Do you sell these plans? No. This site lists offers and links to the provider. Some links may be affiliate links, which means a commission may be earned at no extra cost to you.**" | 同上 FAQ 原文：佣金披露的标准三段式（否认直销 → 承认联盟 → `at no extra cost to you` 免责）。**与 A5 的"零参数"正面相反** |
| "**We extract named prices from official structured data. A listed price alone does not establish a discount or include all billing conditions; use the source link to check them.**" | savecd.com 原文（今日 B5 复抓）：`named prices` / `official structured data`；`A listed price alone does not establish a discount` = 光有挂牌价不构成折扣 |
| "**Source-listed price. Billing period, upfront payment and renewal terms must be checked with the provider.**" | savecd.com 每条 deal 卡片原文（与 Day12 一致，未变）：标准免责句 |
| "**Valid until 2027-10-16**" / "**5 providers tracked**" / "**6h check cadence**" | savecd.com 指标区（今日复抓，**与 Day12 完全一致，未滚动**）：每条带有效期。今日新增 InMotion Hosting 5 张卡（VPS 2/4/8/12/16 vCPU，$7.99/$9.99/$19.99/$31.99/$39.99），**清单从 4 条扩到 9 条** |
| "**[View offer ↗]**" / "**[Source]**" | savecd.com 按钮原文：每条挂"去向 + 来源"两条链接，与我们 `offer_url` + `source_url` 双字段同构 |
| "**PERPETUAL $1/Year VPS GIVEWAY !!**" | LowEndTalk 帖标题原文（Netfront AS4658，原帖拼错 `GIVEWAY`）：`PERPETUAL` 是与 `LIFETIME` / `Recurring` 并列的第三种"长期"标签 |
| "**$12/y Recurring**" / "**25% Recurring OFF \| LET Exclusive**" | LET 帖标题原文：`Recurring` = 每个周期都续的折扣，与"仅首期"严格对立；`LET Exclusive` = 论坛专属 |
| "**[WANTED] Hetzner Cloud Server on Legacy Pricing – EU Location Preferred**" | LET 帖标题原文（今日新收）：**`Legacy Pricing` = 已下架的老价格档**，买家求转让。这是"老客户锁价"的社区说法 |
| "**RackNerd halved my VPS cores with no warning. Got them back, but my one question went unanswered**" | LET 帖标题原文：`halved my VPS cores` = 把核数砍半；`with no warning` = 无预告 |
| "**NetDynamics24: Order Canceled and Client Account Flagged as FRAUD – My Experience with Support**" | LET 帖标题原文：`Flagged as FRAUD` = 账户被打上欺诈标记 |
| "**Metanet.ch - Unreachable/Bankrupt**" / "**tarisu.com down?**" / "**VSYS Host: UA data centers. What happened and where recovery stands?**" | LET 帖标题原文：厂商出事的三种标题写法（破产 / 挂了 / 问恢复进度） |
| "**Urgent: Netcup Support Unresponsive - Paid Server Blocked by Duplicate Invoice Glitch**" | LET 帖标题原文：`Paid Server Blocked` = 已付款却被停机；`Duplicate Invoice Glitch` = 重复账单故障 |
| "**xTom VPS lost my entire virtual disk during maintenance – no backups available**" | LET 帖标题原文：维护丢盘的控诉句式（Day11 已收，今日复现） |
| "**[TRANSFER] 8 vCPU 8 GB RAM 200 GB SSD SVR4U MY REGION**" | LET 帖标题原文：二手转让帖的标准格式（规格串 + 机房地区） |
| "**Only 6: UK Ryzen 5900X 4GB/100GB NVMe £6/mo**" | LET 帖标题原文：**`Only 6:` 把剩余库存数直接写进标题开头** |
| "**DartNode - Countdown to Black Friday - Dedicated Server Deals and Giveaway! Live now!**" | LET 帖标题原文：`Countdown to Black Friday` = 黑五倒计时；`Live now!` = 已开跑 |
| "**TRENDING NOW: RackNerd's BLACK FRIDAY! NEW DEALS, NEW LOCATIONS, NEW HARDWARE + 100's of GIVEAWAYS!**" | LET 帖标题原文：黑五旺季的三段式呐喊（`NEW DEALS / NEW LOCATIONS / NEW HARDWARE`） |
| "**[Early Black Friday Sale] VPS & Dedicated Server Deals \| Starting at Just €18/Year!**" | LET 帖标题原文：`Early Black Friday Sale` 方括号标签 + `Starting at Just` 起价句式 |
| "**[WTB] Dedicated server — 384GB DDR4, NVMe + bulk HDD, US, BAA required — up to $450/mo**" | LET 求购帖原文：`WTB` = want to buy；`BAA required` = 要求签 BAA 协议 |
| "**Is the IPv4 Shortage Finally Over?**" | LET 帖标题原文：IPv4 枯竭是社区长期议题 |
| "**Upto 50% off**" / "**1Gbps Unmetered**" / "**Since 2017**" | LET 帖标题原文：促销/带宽/资历的三种简写（`Upto` 是连写，非标准拼写） |
| "**LET YABS Thread**" / "**VPS Restock**" | LET 帖标题原文：跑分汇总帖 / 补货帖的固定写法 |
| "**Early Bird discounts available for 12 months on our 1U, 2U, and 4U plans.**" | LowEndBox 原文（raindog308，Cloudnium 托管帖）：`Early Bird` + 限定 12 个月 + 按机架规格（1U/2U/4U） |
| "**Exclusive LowEndBox Pricing: 2GB KVM VPS for $1.83/Month First Year! Godlike.Host is Back!**" | LEB 帖标题原文：**`First Year!` 是限定首年的标准后缀**；`Godlike.Host is Back!` 是厂商回归宣告句式 |
| "**I guess Velohost has never heard of inflation.**" | LEB 原文：夸降价的反讽开场 |
| "**Eight months ago, they were selling a 4GB VPS with 25GB of disk and 1TB of bandwidth for 3.00€/month. Now they're selling that same package for only 2.60€/month!**" | LEB 原文：**同套餐跨期降价的对照写法**，`that same package` 强调是同一货 |
| "**Well, all 100 VPS instances have now been given away. But apparently, 100 wasn't enough!**" | LEB 原文（RackNerd/AdminBolt 赠品帖）：赠品发完再加码的写法 |
| "**We love cheap VPSes around here. But FREE? That gets our attention!**" | LEB 原文：免费赠品的开场句 |
| "**A VPS for UNDER $10/YEAR!**" / "**1GB VPSes in Los Angeles starting at only $9.95/year!**" | LEB 原文：年付低价的两种标题写法（`UNDER $X/YEAR` / `starting at only`） |
| "**Those are IPv6-only, but they have IPv4 as well for only $17.95 a year!**" | LEB 原文：`IPv6-only` + 加购 IPv4 的写法 |
| "**Yet Another cPanel and WHMCS Price Increase. But You're Getting More Value. Right? (Right?)**" | LEB 帖标题原文：`Yet Another` 是社区对涨价的固定反讽前缀，句尾 `(Right?)` 是反讽追问 |
| "**Low prices...high RAM...generous bandwidth...must be AffordableBytes!**" | LEB 原文：厂商三件套的排比开场 |
| "**ServerHost Ryzen/i9 VPS from $22.99/year - October Haunt**" | LET offer 标题原文（10-16）：季节促销名直接挂标题尾（`- October Haunt`） |
| "**up to 70% off**" | vps.me 原文（今日 B4）：**`up to` 是英文站写折扣上限的强制限定词**，中文站对应"最高立减" |
| "**Regular $59.00/mo / Sale Price $29.99/mo / Discount 49% / Term 12mo / Savings $348.12**" | cloudcuttersdeals.com 原文（今日 B5）：**有 Regular 与 Sale 两个价才能算出 `Savings` 这一列**——A3 的结构限制由此坐实 |
| "**When you acquire products through affiliate links on our site, we earn a commission**" | codeless.co 原文（今日 B3）：英文站佣金披露的标准句 |

### 明日候选

1. **"Page Read, Nothing Usable Found": The Four Different Ways Reading a Provider Fails — We Only Record One of Them** — A1（8 个受检 URL → 3 可读 → 2 产出；**6 个页面 85 次扫描一条 deal 都没产出过**，含 DigitalOcean 全程可读却 0 条）+ B2（今日新英文站 cloudhostdeals.com 把每个受检 URL 的抓取结果做成公开表，区分 **4 种失败态**：`page read, no price published in the HTML - not listed` / `page read, nothing usable found` / `blocked by the provider's robots.txt - not fetched` / `blocked by the provider (HTTP Error 403: Forbidden)`，并写 `leaves the field empty instead of estimating one`）+ C 栏（同上 4 句原文）+ A1 的漏斗（top-1 83.3%，历史 100%→83.3%）。缝：**一家英文站用 4 个句子描述"我没读到"，我们只有 `readable: false` 一个布尔值**。布尔值能告诉你"读没读到"，说不出"是被 robots 挡的、被 403 拒的、还是读到了但价格藏在 JS 里"——而这三件事对读者的意义完全不同（前两个是厂商不让你看，第三个是你自己技术不行）。**把 8 个 URL 摊开、承认我们只记了一个 bit，是别人不肯做的自曝**；但它顺带给出了一个没人算过的漏斗：跟踪 8 家、产出 2 家、其中一家占 83.3%
2. **No utm, No ref, No "?": 482 Offer Links and Zero Tracking Parameters** — A5（482 行 offer 链接逐条扫：**含 `?` 0 条、含 utm/ref/aff/affiliate 0 条、`http://` 0 条、路径深度全为 1**；distinct offer_url 全历史只有 3 个）+ B3（英文站佣金披露是行业标配：vpsticker FAQ 字面 `Do you earn`、codeless `we earn a commission`、cloudhostdeals `Some links may be affiliate links, which means a commission may be earned at no extra cost to you`）+ C 栏（cloudhostdeals 的 `Do you sell these plans? No. … at no extra cost to you.` 三段式）。缝：**所有人都在声明"我有佣金"，没有一个人声明"我一个追踪参数都没有"**。前者是免责（法律需要），后者是自断收入（没人自愿）。而这一条**读者看一眼地址栏就能自己验证**——可自证的事实最难抄，因为抄的人得真的把参数删干净。**与"我们没价格 / 没 expiry"是同一条诚信线**：我们公布不了的东西，一个也没编；我们本可以偷偷加的参数，一个也没加
3. **The Youngest Deal in Our Index Is 10 Days Old** — A2（Hostinger 5 条 **85/85 次扫描在场、13 天 18:50:52**；Hetzner **57 次、10 天 6:02:57**；**没有任何一条低于 10 天**；总数只取 {5,6}、**85 次从未下降**；唯一增长事件精确到 `2026-10-08T12:37:03Z`）+ B6（"折扣不结束"英文 SERP 0 条直接命中、1 条零售券站跑题 → 该措辞无检索需求，**必须换成"最年轻的一条 10 天"这个可自曝的说法**）+ B2（cloudhostdeals `Updated 2026-10-18 19:50` 是**今天**）+ C 栏（LET `PERPETUAL` / `LIFETIME` / `Recurring` / `Legacy Pricing` 四种"长期"标签）。缝：**所有 deals 站公布的是"页面更新于"，不是"listing 在场多久"**——这两个数在我们这里差了 10 天，因为页面一天刷 5 次，里面躺着的还是 10 天前那批货。**把"刷新时间"和"货物年龄"分开算，需要 85 次快照**；而一旦算了，就得承认自己的 "live deals" 一点都不 live

已用：`compare-vps-deals-total-cost`（10-07）、`vps-deals-renews-at-x`（10-08）、`vps-deals-refund-window`（10-09）、`vps-deals-cost-per-gb-ram`（10-09）、`vps-deals-who-collects-vat`（10-09）、`vps-deals-hourly-to-monthly`（10-10）、`vps-deals-cost-per-gb-disk`（10-11）、`vps-deals-auto-renewal-notice`（10-12）、`vps-deals-port-25-smtp-blocked`（10-13）、`vps-deals-sla-credit-how-to-claim`（10-14）、`vps-deals-payment-methods-accepted`（10-15）、`vps-deals-identity-verification-kyc`（10-16）、`vps-deals-nonpayment-suspension-deletion`（10-17）、**`vps-deals-data-kept-after-cancel`（10-18，最后一篇已发布，取自 gap-ledger #11 而非 line3 候选）**。

已降级/不再写第二篇：退款天数（已发）、每 GB 单价（已发）、renews at 换算（已发）、Hourly ×672/730（已消耗）、CPU steal 诊断（英文位占满）、过期 deal（pennyclouds 已占）、Unmetered Port Metered Reality（Day2）、Stuck in an AI Support Loop（Day3）、低价套餐断货/候补（Day6）、Hetzner 拍卖"怎么运作"（Day6）、黑五"预热期填不出价格"（Day8，已改写）、"deals 站都会撑满库存"（Day10 证伪）、"Flash Deals vs Evergreen Listings"（Day10 候选 #3，Day11 降级：`evergreen` 是零售券圈行话）、**"折扣不结束"这个措辞本身（Day13 降级：B6 实测 `vps deal no end date … never expires` 英文 SERP **0 条直接命中**，5 条里 groupon.com.au 零售券站彻底跑题 → 该说法无检索需求，若写必须换成 A2 候选 #3 的"最年轻的一条 10 天"）**。

**今日修正（重要）**：Day12 记过 savecd.com 是"第一个和我们同路（source-listed + 定时 + 可验证）的英文站"。**今天 B2 出现的 cloudhostdeals.com 比它更近**：它同样挂 `[View offer]` + `[Source]` 双链接、同样 `every six hours`、**同样公开承认自己读不到某些 URL**，而且更进一步——**它把每个受检 URL 的抓取状态逐条列成表**（A1 的 4 种失败态），还明写 `leaves the field empty instead of estimating one`。**"公开抓取状态"这条路已经挤了 3 家（savecd / cloudhostdeals / bestvpsdeal），不能再当卖点写**。今天我们仍独有的是：**85 次 `source_scan_at` 历史**（可算 listing 在场年龄、可算 8→3→2 漏斗、可算 top-1 83.3%）、**逐条 `fetched_at` 秒级时间戳**、**482 条链接零追踪参数**（A5，方向与全行业相反）、**无 price / 无 expiry 的原始 schema 原样公开**。**另一处修正**：Day12 判断 savecd `Valid until 2027-10-16` —— 今日复抓**该日期未滚动**，但清单从 4 条扩到 9 条（新增 InMotion Hosting 5 张卡），说明它在扩覆盖但没更新有效期，可作为"expiry 字段是否真在维护"的观察点，下轮继续盯。

剩余候选（未被消耗）：Day12 三条候选**全部未被 10-18 文章消耗**（10-18 取的是 gap-ledger #11），逐条复检：①"6 Deals, 3 Pages"库存通胀 2:1（Day12 #1）——仍成立，但今日 A1 的漏斗角度更硬，可让位；②"Same Renewal Price (Fixed Price)"不结束的折扣（Day12 #2）——**今日 B6 显示该措辞无检索需求，但 B4 拿到 Hostinger 官方页 `最高立减 70%` 与 `以¥87.99/月 的价格续订 2 年` 同页并列的新证据，若要开必须走"官方页把首期价与续订价并排写"这个切口**，避开 10-08 `vps-deals-renews-at-x`；③"两个雷达的相反取舍"（Day12 #3）——**今日因 cloudhostdeals 出现而降级**："挂来源 + 定时 + 承认读不到"已有 3 家在做，不再是差异化，若开必须改为"三家的取舍对比"，但点名竞品有风险，暂挂。Day11 #1 "Expired Deals Get Removed"——缝仍在（我们有 85 次快照证明从没下过架），但对照对象从 vpspromocodes 换成 cloudhostdeals（后者明写 `leaves the field empty`，也没说会下架）。YABS 怎么读（Day4 #3，**连续第 5 次不升级**，建议正式移出候选池）。Hostinger 学生折扣（Day8 #3，池底）。时区口径（并入"更新于指什么"做一节）。**gap-ledger 提醒：可用未写只剩 #12/#13 两条，BENCH 第三轮已到期（原定不晚于 10-19，今天就是 10-19），line3 候选是 gap-ledger 写完后的回退池，不是当前取题源——两套不要混。**

## 2026-10-20 (Day 14)

> 本次 scan 时间戳 `2026-10-19T18:49:51+00:00` = 北京 10-20 02:49，属当日 scan。fetch + pull --rebase 干净，fast-forward 到 ecb7b74（远端 offer 刷新 + gap #12 文章已发布）。**90 次独立扫描**（120 个提交按 `source_scan_at` 去重后），跨度 `2026-10-04T23:49:08Z → 2026-10-19T18:49:51Z` = **14 天 19 小时 0 分 43 秒**。**今天是全项目最重要的一天：库存发生了 90 次扫描里的第二次突变，而且是有史以来第一次「title 字符串的值」发生变化——`63%` 变成了 `64%`（scan #89 / `2026-10-19T12:51:50Z`），同时总数 6→7，多出一条叫 `Claim deal` 的新条目。我打开官方页核对：页面上真的写着 `Special offer • 64% off`，而且 `Claim deal` 是页面上那个按钮的锚文本，href 是 `#pricing`——一个指向本页锚点、没有百分比、没有价格、没有套餐名的按钮。见 A1 / A2 / A5 与「今日修正」。**

### A. 原创内容邪修

| # | 邪修点 | 为什么别人抄不走 |
|---|---|---|
| A1 | **90 次扫描里唯一一次「数值」变化：`63%` → `64%`，发生在 scan #89 / `2026-10-19T12:51:50Z`，而 `63%` 在此之前整整存活了 14 天 7 小时 5 分 59 秒**（`2026-10-04T23:49:08Z` 首见 → `2026-10-19T06:55:07Z` 末见）。全历史只有 2 次突变事件：#29（`2026-10-08T12:37:03Z`，5→6）与 #89（6→7 + 63→64），**平均 45 次扫描才动一次**。而且这次只动了四档里的**一档**：`(70, 67, 63, 65)` ×88 次 → `(70, 67, 64, 65)` ×2 次，**70 / 67 / 65 三档横跨 14 天 19 小时一个字没变**，唯一变化是 +1 个百分点 | 必须持有 90 次快照才能说出"63 这个值活了 14 天 7 小时"和"只动了一档"。**任何只发布当前状态的站，根本不存在"变化"这个概念**——它今天显示 64%，明天显示 65%，读者永远看不出它变了、更看不出它是 14 天来第一次变。而且 **+1 个百分点这个幅度小到没有任何第三方会报道**：B2 实测 `hostinger vps hosting discount 64% off pricing`，5 条结果里 vps.me 仍写 `up to 70% off`、券站 hostinger.dataprot.net 写 `10% Off All Items`、**没有任何一家英文站出现 64 这个数**。我们抓到了整个券圈生态都还没反映的 1 点变化 |
| A2 | **我们新增的第 7 条 deal，标题叫 `Claim deal`——它是官方页上一个按钮的锚文本，不是一笔折扣**。打开我们自己存的 `offer_url` 核对：`https://www.hostinger.com/vps-hosting#pricing`，而官方页上确实有一个 `[Claim deal](https://www.hostinger.com/vps-hosting#pricing)` 按钮，**href 是 `#pricing`，指向同一份文档的一个锚点**。这条"deal"**没有百分比、没有价格、没有套餐名**，长度 10 字符，是全库最短的一条 title，也是**唯一一条不含任何数字**的 deal。同时它把 distinct offer_url 从 3 个推到 4 个（`vps-hosting` 与 `vps-hosting#pricing`），但 **distinct 页面数仍然是 3**——两个 URL 是同一个文档。**于是我们现在的 7 条 deal 来自 3 个页面，其中 5 条指向同一个文档** | 要说出"我的第 7 条 deal 其实是个按钮"，必须真的打开自己存的 URL 去看一眼，而且要发现 href 里的 `#` 意味着同页锚点。**没有一家 deals 站会公布"我的清单里混进了 CTA 按钮"**——那是自曝解析器分不清折扣和按钮。而这个错误的根因是可公开的：**schema 里没有 `type` 列**，所以"一笔折扣"和"一个按钮上的文字"在我们的表里长得一模一样。顺带算出 7 条 / 3 页 / 5 条同文档这个比例，需要逐条 `offer_url` 去重 + 识别 fragment，也是快照级的能力 |
| A3 | **这次"扩容"让我们的集中度更高了，不是更低**。top-1（Hostinger）占比的历史分布是 `100.0% ×28 次 → 83.3% ×60 次 → 85.7% ×2 次`。**新增的第 7 条 deal 同样是 Hostinger 的**，于是占比从 83.3% 升到 85.7%——一次"多元化事件"反而把最大来源的份额抬高了 2.4 个百分点。放到 14 天 19 小时的全窗口看，**我们从来没有真正分散过**：Hostinger 占比只取过 {100%, 83.3%, 85.7%} 三个值，最低点 83.3% 出现在 10-08 那次 5→6 之后，此后一路没有再降 | 要证明"扩容反而更集中"必须有占比的时间序列，而**英文圈的惯例是把"覆盖多少家"当成正面卖点挂在首屏**（B1 实测 vpsticker `15 providers tracked`、savecd `5 providers tracked`、rackbazaar `3 providers, 9 plans`、今日新站 bestvpsproviders `Compare 1961 Plans`），**没有一家公布"最大一家占多少"**。原因很简单：一公布，"15 providers tracked" 和"85% 的货来自 1 家"就同时成立，前者立刻贬值。我们能算，是因为 90 次快照里每一次的 provider 字段都在 |
| A4 | **两个不变量在突变中活了下来：自指数恒为 4（90/90 次扫描），单次采集仍是 2 个秒点**。库存从 6 变 7、URL 从 3 个变 4 个，但**`offer_url == source_url` 的条数在 90 次扫描里每一次都恰好是 4**（新加的 `Claim deal` 不是自指：`#pricing` ≠ `vps-hosting`）；同时最新一次扫描的 7 条 deal 仍只落在 2 个 `fetched_at` 秒点上——**6 条 Hostinger 全部 `18:49:43`、Hetzner `18:49:45`**，与 6 条时代完全同构。**也就是说：多抓一条 deal 没有多花一次 HTTP 请求，也没有多花一秒**——新条目来自一个我们本来就在读的页面 | 这两个数分别从"逐条比对 offer_url 与 source_url"和"秒级 `fetched_at` 聚类"里来，都需要 90 次全量快照。**自指数 4 是一个跨突变的常数**——它说明自指的 4 条是页面结构决定的，与新不新增 deal 无关；而"采集耗时不变"说明我们的成本与库存条数无关，只与被读页面数有关。**没有任何 deals 站公布"抓一次要几秒 / 发几个请求"**，因为那是基础设施开销，说了不涨销量；但它恰恰是读者判断"这个站到底有多频繁去真看页面"的唯一硬指标 |
| A5 | **外部交叉验证：官方页确认 `64%`，但顺序与我们存的不一样，而且同页上的续订价我们一条都没存**。打开 `https://www.hostinger.com/vps-hosting`，页面按套餐顺序给出 `67% off`（KVM 1）、**`Special offer • 64% off`**（KVM 2，标 `MOST POPULAR`）、`70% off`（KVM 4）、`65% off`（KVM 8）——四个数字与我们库里的 `(70, 67, 64, 65)` **数值完全吻合，但排列不同**（页面是 67/64/70/65，我们存 70/67/64/65）。**同一页还逐档写着 `Renews at $11.99/mo` / `$14.99/mo` / `$28.99/mo` / `$49.99/mo for 2 years`，我们一条都没存**（schema 无 price 列）。也就是说：我们这次**抓对了数字、抓错了顺序、漏掉了同一页上最重要的四个价格** | 要做出这个判断，必须同时持有"90 次快照的 title 序列"和"此刻官方页的真实 DOM 顺序"并逐项对照——单看任何一边都得不出的结论。**B3 实测"listing 是否过期 / 多久变一次"英文 SERP 0 条 VPS 专用命中**（只有 savecd 一家在描述自己的刷新机制，DreamHost 两篇是买前清单不是库存话题），**B4 实测"同一家多条 listing 重复计数"英文 SERP 同样 0 条命中**。这两件事没人写，因为做了的站觉得理所当然、没做的站不会自曝。**而我们敢同时承认"数字对了、顺序错了、续订价漏了"这三件事**——这三句话合起来比任何"我们最准"的声明都可信，也更难抄：抄的人得先有一个 90 次的历史库，再肯把"我漏了同页上的续订价"写出来 |

### B. 谷歌搜索查词（今天真跑过的）

| query | SERP 上看到了什么 | 判断 |
|---|---|--|
| `vps deals` | **核心词**。5 条：vpsticker.com（`15 providers tracked` / `29 live offers` / `15/15 providers returning data` / **`2026-10-02 last refresh`**）、vpsfilter.com（`Updated daily`）、rackbazaar.com（`3 providers, 9 plans` / `No dark patterns`）、**savecd.com（Day13 掉出前五，今天又回来了）**、vncoupon.com（中文，RackNerd 法国机房） | **核心词 SERP 继续每日洗牌，第 7 天复现**：savecd 一天掉出、一天回来；vpsticker `refreshed every 6 hours` 与 `2026-10-02 last refresh`（距今 17 天）自相矛盾**连续第 7 天**。任何"竞品在不在前五"的判断都不能沿用昨天 |
| `hostinger vps hosting discount 64% off pricing` | **今天最关键的一条验证**。5 条：hostinger.dataprot.net（`10% Off All Items` / `Save 10% on All Hosting Plans`，**Updated last week**）、**vps.me（`AI-managed KVM VPS hosting with up to 70% off`）**、fasthosts.co.uk 条款页（`Up to 40% off … for the first six months`）、rpayu.com、neaplagia.com（`plans start from $2.99`） | **没有任何一家英文站出现 64 这个数**——券站还在发 `10% Off`，vps.me 仍是 `up to 70% off`，厂商条款页只有自己的 `Up to 40%`。**A1 的缝因此成立：我们抓到的 `63%→64%` 是 1 个百分点的变化，小到整个券圈生态都还没反映**。同时复证 `up to` 是英文站写折扣上限的强制限定词（中文站对应"最高立减"） |
| `vps deals site how often listings change stale outdated offers` | 5 条：savecd.com（`Prices are shown only when verifiable`）、dreamhost.com/blog/best-vps-hosting/（**买前清单，非库存话题**）、foxvalleywebdesign.com（**建站公司页，完全跑题**）、domainhostcoupon.com（SterkHost 券页）、dreamhost.com/blog/vps-upgrade/（升级信号） | **"listing 多久变一次 / 会不会过期"英文 SERP 0 条 VPS 专用命中**，5 条里 1 条彻底跑题、2 条是 DreamHost 买前指南。**没人写"我的清单会不会变"** → A1/A5 的"第一次变化"是无人区，可放心开题 |
| `vps deals same provider multiple listings one page duplicate plans` | 5 条：serverwala.com（日本 VPS 产品页）、findmeavps.com（`Top VPS Providers will compete for your business`）、**bestvpsproviders.com（新英文站，`Compare 1961 Plans from $0.11/mo`，列 `Price/mo` / `$/GB` / `$/Core` / `Payment Info`）**、dreamhost.com/blog/best-vps-hosting/、dreamhost.com/hosting/vps/ | **"同一家被重复计为多条 listing"英文 SERP 0 条命中**——所有人都在**增加**条数（bestvpsproviders 直接把 1961 当卖点），没有一个人讨论"这 1961 条里有多少是同一页的重复计数"。**A2 的 7 条 / 3 页正是反着来的角度**：别人以条数多为荣，我们以"条数除以页数"自曝 |
| `vps deals black friday 2026 early sale` | 5 条：contabo.com/en-us/black-friday/（`Even our regular prices offer better value than most deals you'll find elsewhere` / `$5.28 for the first 24 months`）、blackfriday.bloggingjoy.com、theblackfriday.com.ng、**vps.blackfriday（标题竟是 `VPS BLACK FRIDAY 2024`，见 C 栏）**、blackfridayvault.com | **旺季线今天拿到最硬的一条外部证据**：`vps.blackfriday` 这个专门的 VPS 黑五站，页面标题**至今写着 2024**，而现在是 2026 年 10 月——**整整晚了两年**，正文 `Flash Deals` 后面跟了一串 `0 0 0 0 0`。**Contabo 黑五页连续第 8 天仍是常规价**。`vps.blackfriday` 是"deals 站有多不更新"的免费外部佐证，直接喂给候选 #3 |
| `cheap vps hosting deal price changed increase 2026` | 5 条：cheapvps.store（`Compare 1,257+ VPS plans from 12 providers`）、vncoupon.com/namecheap-coupons、whatsthehost.com、pdqserver.com（`Starter Plan $4.95 /Month`）、vncoupon.com/reseller-hosting | **"价格变动"在英文 SERP 里被"价格比较"完全吃掉**：5 条里 4 条是对比表/券页，0 条讨论"价格什么时候变、变了多少"。**印证 A1：大家只发布当前值，不发布变化** |

### C. 老外怎么说（真在用的说法）

| phrase | 谁在用 / 什么意思 |
|---|---|
| "**Special offer • 64% off**" | **hostinger.com/vps-hosting 官方页原文**（今日 A5 核到）：厂商在套餐卡上标注"特价"的标准写法，`•` 分隔标签与折扣，仅 KVM 2 一档有此标签 |
| "**MOST POPULAR**" | 同上官方页原文：套餐卡上的常驻标签。**我们的 title 里完全没有承载这个标签的字段** |
| "**Renews at $11.99/mo for 2 years. Cancel anytime.**" | 同上原文，四档各一句（`$14.99` / `$28.99` / `$49.99`）：**`renews at` 的头号出处就是厂商自己的定价卡**，且带期限（`for 2 years`）与解约条件（`Cancel anytime`）。**我们同页抓取却一条都没存**（无 price 列） |
| "**Claim deal**" | 同上原文：页面 CTA 按钮锚文本，`href = /vps-hosting#pricing`。**我们把它当成了一条 deal**（A2） |
| "**Choose plan**" | 同上原文：套餐卡上的另一个按钮文本，与 `Claim deal` 是同一层的 UI 元素 |
| "**From $19.49 $6.49/mo**" | 同上原文：划原价 + 现价的写法，`From` 是起价前缀 |
| "**Up to 70% off**" / "**this Black Friday**" | 同上首屏原文：`up to` 是折扣上限的强制限定词；`this Black Friday` 说明页面已进入黑五话术 |
| "**All plans are paid upfront. The monthly rate reflects the total plan price divided by the number of months in your plan.**" | 同上页脚原文：**厂商自己解释"月单价 = 总价 ÷ 月数"**，是理解 VPS 报价最关键的一句免责 |
| "**Secure your deal before it's gone**" | 同上原文： urgency 文案，`before it's gone` 是标准催单句 |
| "**30-day money-back guarantee**" | 同上原文：退款窗口的标准写法 |
| "**Find a VPS plan. _See the source._**" | savecd.com 首屏原文（今日复抓）：把"看来源"做成标题的一部分 |
| "**Official-source VPS offers, checked on a schedule. We show only prices we can verify and link every listing to its source.**" | 同上首屏原文：`checked on a schedule` / `only prices we can verify` / `link every listing to its source` |
| "**5 providers tracked**" / "**6h check cadence**" | 同上指标区：`check cadence` 是"检查节奏"的说法，比 `refreshed every` 更准确 |
| "**Source-listed price. Billing period, upfront payment and renewal terms must be checked with the provider.**" | 同上每条卡片原文（与 Day12/13 一致）：标准免责句 |
| "**Valid until 2027-10-19**" | 同上（**今日重大变化：Day12/Day13 连续两天都是 `2027-10-16`，今天滚动到了 `2027-10-19`**）→ **该 expiry 字段确实在维护，Day12/13"没滚动"的判断今日作废**。见「今日修正」 |
| "**[View offer ↗]**" / "**[Source]**" | 同上按钮原文：去向 + 来源双链接，与我们 `offer_url` + `source_url` 同构 |
| "**Cloud hosting and VPS deals, refreshed every 6 hours**" | cloudhostdeals.com 标题原文（今日复抓）：`refreshed every 6 hours` |
| "**7 live listings**" / "**3 providers tracked**" / "**Updated 2026-10-19 21:51**" | 同上首屏指标区（今日复抓，**更新时间是今天**）：三数并排 |
| "**2 listingsfrom 3.0**" / "**3 listingsfrom 11.0**" | 同上 "Providers we track" 原文：每家挂"几条 listing + 起价" |
| "**blocked by the provider (HTTP Error 403: Forbidden)**" | 同上状态表原文：**失败态之一**，连 HTTP 状态码都写出来 |
| "**blocked by the provider's robots.txt - not fetched**" | 同上：**失败态之二**，明确写"没有抓取"（守规则，不是抓不到） |
| "**page read, no price published in the HTML - not listed**" | 同上：**失败态之三**（今日该状态扩到 4 行：DO `/pricing/agent-droplets`、`/pricing/backups`、A2 Hosting） |
| "**page read, nothing usable found**" | 同上：**失败态之四**（今日新增 A2 Hosting 与 Vultr `/pricing/`） |
| "**read**" | 同上状态表：最简单的成功态（今日出现于 `digitalocean.com/pricing/`、`sitemaps/pricing-0.xml.gz`、Cloudways sitemap 等） |
| "**We show only prices we can verify**" / "**When a page cannot be read, we say so instead of filling in a guess.**" | 同上首屏原文（与 Day13 一致）：不猜数的承诺 |
| "**When this site cannot read a number it leaves the field empty instead of estimating one.**" | 同上 FAQ 原文：`leaves the field empty instead of estimating one` |
| "**Every six hours, and the timestamp at the bottom of the page shows the last successful read.**" | 同上 FAQ 原文：`last successful read` = 最后一次**成功**读取 |
| "**Some links may be affiliate links, which means a commission may be earned at no extra cost to you.**" | 同上 FAQ 原文：佣金披露三段式的末句 |
| "**VPS BLACK FRIDAY 2024**" | **vps.blackfriday 页面标题原文（今日 B5 发现）**：2026 年 10 月，一个专门的 VPS 黑五站标题仍写着 **2024** |
| "**Flash Deals**" + "**0 0 0 0 0 0 0 0 0 0 …**" | 同上原文：闪购区挂着 30 个 `0` 的计数器，一个 deal 都没有 |
| "**VirMach's rotating VPS offers are back for Black Friday. Don't blink or you might miss it.**" | 同上原文（B5 摘要）：`rotating VPS offers` = 轮换上下的 offers；`Don't blink or you might miss it` = 转瞬即逝 |
| "**Best VPS Hosting: Compare 1961 Plans from $0.11/mo**" | bestvpsproviders.com 标题原文（今日 B4 发现）：把条数当卖点的极致 |
| "**Price/mo**" / "**$/GB**" / "**$/Core**" / "**Payment Info**" | 同上表头原文：三档单位价列。**`$/GB` 与 `$/Core` 是英文圈比价的标准化指标**（我们 10-09 / 10-11 已发过同题文章，此处仅作对照） |
| "**No plans found**" | 同上表格空态原文 |
| "**1 mo.**" | 同上账单周期写法：极简期限标注 |
| "**~$0.46**" | 同上价格写法：**波浪号前缀 = 约数/起价**，英文站用 `~` 表示不承诺精确值 |
| "**Compare 1,257+ VPS plans from 12 providers.**" | cheapvps.store 原文（今日 B6）：`data-driven comparison tool` 也是同类说法 |
| "**Up to 40% off (depending on the product) will be discounted from the full product standard price for the first six months.**" | fasthosts.co.uk 官方条款页原文（今日 B2）：**厂商条款里限定折扣期限的标准句法**（`for the first six months`） |
| "**Up to 70% off**" | vps.me 原文（B2 复抓）：第三方仍沿用厂商首屏的上限值，**不反映 64% 这个变动** |
| "**$12/y Recurring**" / "**25% Recurring OFF**" / "**30% lifetime discount**" | LowEndTalk 帖标题原文：`Recurring`（每周期都续）与 `lifetime discount`（永久）是两种严格对立的"长期"标签 |
| "**Upto 50% off**" / "**Up to 55% Off**" / "**Upto 60% discount**" | LET 标题原文：`Upto` 连写是非标准拼写，社区里高频出现 |
| "**$5 for 5 Years?!**" | LET 帖标题原文：多年付的惊叹式写法 |
| "**From £3.37/yr**" / "**Under $150/Year**" / "**for 212 USD/year**" | LET 标题原文：年付价的三种写法（起价 / 上限 / 总额） |
| "**[VPS Restock]**" / "**Improved Storage Servers!**" | LET 帖标题原文（DeluxHost）：`Restock` = 补货，是 `out of stock` 的对应动作 |
| "**DeluxHost.net \| VPS Restock \| Improved Storage Servers!**" | 同上完整标题 |
| "**Countdown to Black Friday - Dedicated Server Deals and Giveaway! Live now!**" | LET 原文（DartNode）：`Countdown to` + `Live now!` |
| "**$500 Halloween Giveaway Has Begun!**" | LET 原文（ServerHost）：`Has Begun!` 是活动开启的固定句式 |
| "**heartbeat-it SE down?**" / "**Servarica down?**" / "**VirMach LA outage**" | LET 原文：三种"出事了"的标题写法（厂商名 + `down?` / 地区 + 故障类型） |
| "**Metanet.ch - Unreachable/Bankrupt**" | LET 原文（今日复现）：`Unreachable/Bankrupt` 是社区对厂商关门的浓缩写法 |
| "**Does anyone know what is the situation with rarecloud?**" | LET 原文：询问厂商状况的标准问句 |
| "**IP unreachable after about 10 days**" | LET 原文：故障持续时间的写法 |
| "**DartNode Unauthorized SSH Access**" | LET 原文：安全事件的标题写法 |
| "**RackNerd halved my VPS cores with no warning. Got them back, but my one question went unanswered**" | LET 原文（今日复现）：`halved my VPS cores` = 核数砍半；`with no warning` = 无预告 |
| "**Suspended again for high CPU usage**" | LET 原文：因 CPU 使用被停机的写法（`Suspended again` 强调反复） |
| "**$3 replacement fee, no refund**" | LET 原文：`replacement fee` = 换机费 |
| "**MXRoute bulk closing support tickets**" | LET 原文：`bulk closing` = 批量关闭工单 |
| "**vps[dot]gripe: A simple archive for your YABS & bench runs**" | LET 原文（DejavuMoe）：`bench runs` = 跑分；社区为规避过滤把域名写成 `vps[dot]gripe` |
| "**LET YABS Thread**" | LET 原文（134.9K views）：跑分汇总固定帖名。`YABS` = Yet Another Benchmark Script |
| "**[WTB] … IPv6 /64**" / "**REQ: Cheapest 8+ core and 16gb+ ram VPS\|VDS**" / "**LF Storage server deals**" | LET 求购帖三种前缀：`WTB` = want to buy、`REQ` = request、`LF` = looking for |
| "**I want a 512mb ram VM/box**" | LET 原文：`box` 是小机口语说法 |
| "**nano VPS in Miami (~$1/month)**" | LET 原文：`nano VPS` = 极小配置档 |
| "**ServerHost Ryzen/i9 VPS from $22.99/year - October Haunt**" | LET offer 标题原文（今日复现）：季节促销名挂标题尾 |
| "**transferring 4tb storage server for costco hotdog**" | LET 原文：社区黑话式标题（用物价打比方） |
| "**This is the largest collection of YABS (Yet Another Benchmark Script) benchmarks on the planet, with over 10,000 user-submitted reports in its database.**" | LowEndBox 原文（ServerVerify 访谈）：`YABS` 全称首次出现 |
| "**Exclusive LowEndBox Pricing: 2GB KVM VPS for $1.83/Month First Year! Godlike.Host is Back!**" | LEB 原文（今日复现）：`First Year!` 限定首年；`is Back!` 厂商回归宣告 |
| "**You'll need our special coupon code to get these deals!**" | LEB 原文：`special coupon code` = 专属优惠码 |
| "**Early Bird Discounts on Cheap Colocation!**" / "**with Early Bird discounts available for 12 months**" | LEB 原文（Cloudnium，今日复现）：`Early Bird` + 明确期限 |
| "**Velohost Returns With Even Cheaper Prices!**" / "**I guess Velohost has never heard of inflation.**" | LEB 原文（今日复现）：降价报道的反讽开场 |
| "**Eight months ago, they were selling a 4GB VPS … for 3.00€/month. Now they're selling that same package for only 2.60€/month!**" | LEB 原文（今日复现）：跨期同套餐降价的对照写法 |
| "**Well, all 100 VPS instances have now been given away. But apparently, 100 wasn't enough!**" | LEB 原文（今日复现）：赠品发完再加码 |
| "**More of RackNerd & AdminBolt! Here's 50 More FREE VPS + 10 Lifetime Licenses!**" | LEB 原文：`Lifetime Licenses` = 永久授权 |
| "**A VPS for UNDER $10/YEAR!**" / "**1GB VPSes in Los Angeles starting at only $9.95/year!**" | LEB 原文：年付低价的两种标题写法 |
| "**Those are IPv6-only, but they have IPv4 as well for only $17.95 a year!**" | LEB 原文：`IPv6-only` + 加购 IPv4 |
| "**Yet Another cPanel and WHMCS Price Increase. But You're Getting More Value. Right? (Right?)**" | LEB 原文（今日复现）：`Yet Another` 是涨价反讽固定前缀 |
| "**38:05:57left**" / "**06:21:09left**" | **hetzner.com/sb 官方拍卖页原文（今日复抓，全新技术）**：倒计时写法，`left` 紧挨时间无空格。**AuctionID 3095118 / 3095150，与 Day12 的 3095297、Day11 的 3091544 全不相同** —— 页面每次都在变，而我们对它的 title 90 次扫描一字未变 |

### 明日候选

1. **"63% Became 64% Today": The First Time Our Index Ever Changed a Number** — A1（`63%` 存活 **14 天 7 小时 5 分 59 秒**后于 scan #89 / `2026-10-19T12:51:50Z` 变为 `64%`；90 次扫描仅 2 次突变，平均 45 次才动一次；**四档里只动了一档**，70/67/65 横跨 14 天 19 小时未变）+ A5（打开官方页核对，页面确实写着 **`Special offer • 64% off`**，四档数值 `67/64/70/65` 与我们库完全吻合）+ B2（**`hostinger vps hosting discount 64% off pricing` 5 条结果里没有任何一家英文站出现 64**：vps.me 仍 `up to 70% off`、券站还在发 `10% Off All Items`）+ B3（"listing 多久变一次 / 会不会过期"英文 SERP **0 条 VPS 专用命中**）+ C 栏（`Special offer • 64% off` / `MOST POPULAR` / `Renews at $11.99/mo for 2 years`）。缝：**只发布当前状态的站，根本不存在"变化"这个概念**——它今天 64、明天 65，读者永远看不出它变了，更看不出这是 14 天来第一次变。**+1 个百分点小到整个券圈生态都还没反映**，而我们有精确到秒的首次出现/最后一次出现时间。这条 hardest 的部分是我们同时要承认 A5 的"顺序错了、续订价漏了"
2. **"Claim Deal" Is a Button, Not a Discount: 7 Deals, 3 Pages, and One of Them Is an Anchor** — A2（新增第 7 条 title `Claim deal`，`offer_url = https://www.hostinger.com/vps-hosting#pricing`；打开官方页确认它是 **CTA 按钮锚文本**，href 是同页锚点；**10 字符、全库最短、唯一不含任何数字**；distinct offer_url 3→4 但 **distinct 页面数仍是 3**，**7 条 deal 来自 3 个页面，其中 5 条指向同一个文档**）+ A5（同页逐档写着 `Renews at $11.99/$14.99/$28.99/$49.99/mo for 2 years`，我们一条没存）+ B4（"同一家多条 listing 重复计数"英文 SERP **0 条命中**，所有人都在增加条数——bestvpsproviders 直接把 `Compare 1961 Plans` 当卖点）+ C 栏（`Claim deal` / `Choose plan` / `Renews at … for 2 years` / `All plans are paid upfront…`）。缝：**别人以条数多为荣，我们以"条数 ÷ 页数"自曝**。承认"我的第 7 条 deal 其实是个按钮"是自曝解析器缺陷，没人肯——但根因可公开：**schema 没有 `type` 列**，所以一笔折扣和一个按钮上的文字在我们的表里长得一模一样
3. **A VPS Black Friday Site Still Says "2024": What "Updated" Means When Nothing Ever Moves** — A1（我们 14 天 19 小时才动一次、且只动 1 个百分点）+ B5（**`vps.blackfriday` 这个专门的 VPS 黑五站，2026 年 10 月页面标题仍写着 `VPS BLACK FRIDAY 2024`，晚两年；`Flash Deals` 后面挂 30 个 `0`**；Contabo 黑五页连续第 8 天只有常规价）+ A5/今日修正（**savecd `Valid until` 今日从 `2027-10-16` 滚动到 `2027-10-19`，确属在维护**——所以"不更新"不是全行业通病，是有站做得到）+ B1（vpsticker `refreshed every 6 hours` 与 `2026-10-02 last refresh` 自相矛盾**连续第 7 天**）+ C 栏（`VPS BLACK FRIDAY 2024` / `Flash Deals` / `rotating VPS offers` / `Don't blink or you might miss it` / `6h check cadence` / `last successful read`）。缝：**"更新于"这个词被四种完全不同的口径共用**——页面刷新时间（cloudhostdeals `Updated 2026-10-19 21:51`，是真的今天）、声明的节奏（vpsticker `every 6 hours`，实际停在 17 天前）、listing 的有效期（savecd `Valid until`，真在滚）、以及标题年份（vps.blackfriday 停在 2024）。**把这四种摆在一起对照，需要一个 90 次快照的库 + 每天真跑 6 条 SERP**

已用：`compare-vps-deals-total-cost`（10-07）、`vps-deals-renews-at-x`（10-08）、`vps-deals-refund-window`（10-09）、`vps-deals-cost-per-gb-ram`（10-09）、`vps-deals-who-collects-vat`（10-09）、`vps-deals-hourly-to-monthly`（10-10）、`vps-deals-cost-per-gb-disk`（10-11）、`vps-deals-auto-renewal-notice`（10-12）、`vps-deals-port-25-smtp-blocked`（10-13）、`vps-deals-sla-credit-how-to-claim`（10-14）、`vps-deals-payment-methods-accepted`（10-15）、`vps-deals-identity-verification-kyc`（10-16）、`vps-deals-nonpayment-suspension-deletion`（10-17）、`vps-deals-data-kept-after-cancel`（10-18）、**`vps-deals-wrong-datacenter-move`（10-19，最后一篇已发布，取自 gap-ledger #12 而非 line3 候选）**。

已降级/不再写第二篇：退款天数（已发）、每 GB 单价（已发）、renews at 换算（已发）、Hourly ×672/730（已消耗）、CPU steal 诊断（英文位占满）、过期 deal（pennyclouds 已占）、Unmetered Port Metered Reality（Day2）、Stuck in an AI Support Loop（Day3）、低价套餐断货/候补（Day6）、Hetzner 拍卖"怎么运作"（Day6）、黑五"预热期填不出价格"（Day8，已改写）、"deals 站都会撑满库存"（Day10 证伪）、"Flash Deals vs Evergreen Listings"（Day10 候选 #3，Day11 降级）、"折扣不结束"措辞（Day13 降级）、**"挂来源 + 定时 + 承认读不到"作为差异化卖点（Day13 已降级，今日再确认：savecd / cloudhostdeals / bestvpsdeal 三家都在做，cloudhostdeals 今日状态表已扩到 14 行）**。

**今日修正（重要，两条）**：① **savecd.com 的 `Valid until` 今日从 `2027-10-16` 滚动到 `2027-10-19`**——Day12 与 Day13 连续两天记录的"未滚动/没在维护"结论**今日作废**，该字段确实在维护（且恰好是"今天 +1 年"）。**教训：expiry 字段是否维护，不能靠两次观察下结论，要盯到它动为止。** ② **"只有 1 个布尔值 `readable`"这个自我批评需要微调**：我们确实只有 `readable`，但 cloudhostdeals 今日的状态表**新增了 `read` 这个成功态**，其 4 种失败态（403 / robots.txt / 价格不在 HTML / 读不到可用内容）与我们今日确认的"8 个受检 URL 里 6 个 90 次零产出"仍是两套不同口径——**它记的是"为什么读不到"，我们记的是"读没读到"，而我们还额外记了"读到了但没产出"**。这个区分（可读 ≠ 有 deal）仍然是我们的独家口径。**另一处修正**：Day13 A4 说"Hetzner title 全历史只有 1 个字符串、恒断在 `from`"——今日复抓 hetzner.com/sb，拿到**全新倒计时 `38:05:57left` / `06:21:09left` 与全新 AuctionID 3095118 / 3095150**（Day12 是 3095297、Day11 是 3091544），**页面每次都在变而我们 title 90 次一字未变**，该判断继续成立且证据更硬。

剩余候选（未被消耗）：Day13 三条候选**全部未被 10-19 文章消耗**（10-19 取的是 gap-ledger #12），逐条复检：①"Page Read, Nothing Usable Found" 四种失败态（Day13 #1）——缝仍在，但今日新增证据显示 cloudhostdeals 已把状态表扩到 **14 行**（新增 A2 Hosting、Vultr 三行、DO sitemap 等），**它记失败原因的粒度比我们细，若开必须改为"它记为什么失败、我们记读到了但没产出"这个不同口径**；②"No utm, No ref, No '?'" 零追踪参数（Day13 #2）——**仍是最稳的一条**，今日未复验但 482→ 应重算为 547 行（90 次扫描含 7 条期）；③"The Youngest Deal in Our Index Is 10 Days Old"（Day13 #3）——**今日作废**：新增的 `Claim deal` 使最年轻的一条变为 **2 次扫描 / 约 6 小时**，该候选的事实基础已经改变，若要写必须改成"最老的一条 14 天 19 小时"。Day12 #1 "6 Deals, 3 Pages"——**今日被 A2 吸收并升级**（7 条 / 3 页 / 5 条同文档 + 新增锚点 URL）。Day12 #2 "Same Renewal Price"—**今日拿到最强证据**：官方页四档 `Renews at $11.99/$14.99/$28.99/$49.99/mo for 2 years`，但要避开 10-08 `vps-deals-renews-at-x`，须走"厂商把首期价与续订价并排印在同一张卡上"这个切口。YABS 怎么读（Day4 #3，**连续第 6 次不升级，正式移出候选池**——B3/B4/B6 三条 query 均显示英文教程位为 0）。**gap-ledger 提醒：可用未写只剩 #13 一条；BENCH 第三轮已过期（原定不晚于 10-19），line3 候选是 gap-ledger 写完后的回退池，不是当前取题源——两套不要混。**

---

## 2026-10-21 (Day 15)

### A. 原创内容邪修

| # | 邪修点 | 为什么别人抄不走 |
|---|---|---|
| A1 | **全库 97 次已提交扫描里，只有 2 次出现过任何货币金额，而且都是同一处**：Hetzner 拍卖标题在 `2026-10-20T12:51:51Z` 从 **82 字符、止于 `from`** 变成 **111 字符、带出 `€ 67.70 per month, excl. VAT`**——此前 67 次一字未变；今日 07:06（`2026-10-20T23:06:41Z`）复扫仍是 111 字符，连续第 3 次 | 要证明"这个价是 10-20 才出现的"，必须先有 10-04 到 10-20、平均 3.95 小时一次的 97 次独立快照。**只发布当前状态的站，无论今天抓到什么，都答不出"它以前是什么、多久没变"** |
| A2 | **双层零产出账**：8 个受检官方 URL 里 **5 个 97/97 不可读**（contabo ×3、vultr、linode），第 6 个 DigitalOcean **97/97 可读但 0 条 offer**——即 **6/8 = 75% 的受检页面 16 天零产出**，我们照记、从不把这些 URL 从受检表里删掉 | 竞品全在比条数：vpsticker `15 providers tracked 29 live offers`、cheapvps.store `Compare 1,257+ VPS plans from 12 providers`、rackbazaar `6 providers, 269 plans, stock checked daily`。**没有一家公开"我查了 8 个页面、6 个一条都没出"**——这个数字只会让自己难看 |
| A3 | **把"排序键缺失"当资产公开**：库里四档顺序是 `70, 67, 64, 65`，官方页上的实际顺序是 KVM1=67 / KVM2=64 / KVM4=70 / KVM8=65，**两个顺序都不单调**；我们没有 price/discount 数值列，所以库内顺序就是抓取顺序，不是价格顺序。今日新证：官方页 hero 写着 `Up to 70% off`，**正好等于四档最大值** | 需要把自己的 schema 缺陷（无数值列）与官方页逐档真相并排印出来。而"最高 70% = 四档里最大的那一档、不是额外优惠"这个换算，**第三方站把它当独立卖点**（vps.me 至今 `up to 70% off`） |
| A4 | **"突变间隔"是只有快照库才有的时序量**：4 次突变存活 **3d12h47m55s / 11d0h14m47s / 1d0h0m1s / 5h54m43s（进行中）**，97 次里平均每 24.25 次才动一次；且 **#89 与 #96 两次突变落在同一天同一分钟（`12:51:50` 与 `12:51:51`，相隔 24 小时零 1 秒）** | 必须**公开自己的采样时钟**并承认：固定时点采样只能给出变化的**下界**，我们观察到的节奏里有一部分是我们自己的时钟定义的。没人愿意把自己的采样偏误差一起印出来 |
| A5 | **打开自己存的 offer_url 逐字核对，并公开"有什么我没存下来"**：hostinger.com/vps-hosting 四档 `67% off` / `Special offer • 64% off` / `70% off` / `65% off` 与库完全吻合；**一条都没存**的有：四档 `Renews at $11.99 / $14.99 / $28.99 / $49.99/mo for 2 years. Cancel anytime.`、`30-day money-back guarantee`、`All plans are paid upfront. The monthly rate reflects the total plan price divided by the number of months in your plan.`、hero `Up to 70% off` + `this Black Friday` + `From $19.49$6.49/mo`、`Secure your deal before it's gone`。hetzner.com/hosting/ 上 **7 行产品里 6 行都印着 `Starting at € X per month, excl. VAT`（67.70 / 59.00 / 5.99 / 34.00 / 1.60 / 4.29 / 3.20）**，而我们只存了拍卖那 1 条 | **公开"页面上有什么我没存下来"是纯自曝**——别人只会挑对自己有利的字段。且这条每天可复现：今天它让我们承认 16 天里只存下 1 行价格，另外 6 行一直在页面上 |

### B. 谷歌搜索查词（今天真跑过的）

| query | SERP 上看到了什么 | 判断 |
|---|---|---|
| `vps deals` | **核心词**。前五：vpsticker（`15 providers tracked` / `29 live offers` / `15/15 providers returning data` / **`2026-10-02 last refresh`**——今天 10-21，已 19 天未动）、**vpsfilter.com（`Updated daily`，今日首次进入前五）**、**rackbazaar.com（`6 providers, 269 plans, stock checked daily`，今日首次进入前五）**、savecd（`Prices are shown only when verifiable.`）、vncoupon（越南/中文券站 `CloudCone – Lunar New Year VPS Deals from $9.99/Year`） | **锁死不动**。核心词 SERP **每天在洗牌**：Day13 首次出现的 savecd 还在，vpsfilter / rackbazaar 是全新面孔；vpsticker 的 `last refresh` 停在 10-02 是**连续第 9 天**自相矛盾 |
| `Hetzner server auction "starting at" price per month excl VAT` | 官方 hetzner.com 首页、hetzner.com/sb?search=gpu（片段里出现 **`€0.0748 per hour`** / **`65:15:22 left`** / **`€46.70`** / `excl. VAT`）、**hostnotify.com（`Get a Telegram, email or Discord ping the moment a Hetzner Server Auction listing matches your criteria, or a Cloud server type is back in stock` + `$2.99/month, 7-day free trial`）**、hostaan、nodereef（中文） | **可做**。**拍卖提醒已经有人做成付费订阅产品（hostnotify $2.99/mo）**，但**没有任何一个页面在做"起拍价随时间的序列"**——他们只做"匹配就推送"。切口是价格时序，不是推送 |
| `VPS hosting price "excl. VAT" vs "incl. VAT" what buyers pay` | 5 条里 **2 条是中文问答**（百度文库 / 百度知道）、1 条南非采购 PDF（sansa.org.za）、1 条 myhostingpartner（`monthly Excl. VAT`）、1 条 firstheberg（`+20% of the VPS price excl VAT/month`） | **可做，英文位几乎全空**。"买 VPS 时 excl. VAT 意味着实际要多付多少"这个真问题，英文 SERP **没有一篇正面回答**。而我们今天刚拿到 6 条 `Starting at € X per month, excl. VAT` 的一手样本 |
| `"renews at" VPS recurring same price promo renewal` | onebesthost（**`Promotional price applies to the first billing period. Renewal is charged at the regular price.`**）、DreamHost ×2（`Auto-renews at $16.99 /mo after 3 years` / `First 3 years at $10 /mo` / `SAVE 73%` / `Auto-renews at $24.99 /mo after 3 years`）、InMotion（`Renews at $59.99 /mo` / `You Save 54%` / `Starting at $39.99 /mo` / `Renews at $86.99 /mo`） | **可做但要换切口**。**"renews at"是厂商自己印在价卡上的标准字段，不是社区黑话**。要避开 10-08 已发 `vps-deals-renews-at-x`：那篇讲"renews at 是什么意思"，新切口是"**同一张卡上首期价与续订价并排印**"与"**renews at 与原价相同 = 真 recurring**"（LET 今日 `$49/year, renews at $49`） |
| `vps price comparison site "last updated" stale listings how often` | **0 条 VPS 专用命中**（第 5 次跑仍是 0）。沾边的只有 Zyte 讲房地产爬虫（`Price and status are typically delivered daily or several times a day; full listing attributes are usually re-crawled weekly`）、DreamHost 泛文、cheapvps.store（`Compare 1,257+ VPS plans from 12 providers`，**仍无时间戳**）、**domainhostcoupon（`⏱️ Expires December 6, 2025 ➕ Last verified November 25, 2025`——2026 年 10 月还挂着 2025-11-25 核过的券）** | **降级为佐证素材，不单独立题**（Day13 B3 也是 0 条）。但**旁证今天反而变硬了**：domainhostcoupon 的过期券是最便宜的免费佐证 |
| `vps black friday 2026 deals early` | theblackfriday.com.ng、contabo.com/en-us/black-friday（**`Contabo Black Friday Deals Coming Soon!`** / `Even our regular prices offer better value than most deals you'll find elsewhere` / `from $6.60` / **`$5.28 for the first 24 months`**）、blackfridayvault、bloggingjoy、vps.blackfriday（`rotating VPS offers are back` / `Don't blink or you might miss it` / **`Offer may expire or change at any time.`**） | **观察，今天不取**。**Contabo 黑五页连续第 9 天仍只有常规价**（`$6.60` / `$5.28 for the first 24 months`，无黑五价）。**重要更正：vps.blackfriday 正文已从 `Black Friday 2024` 滚动到 `Black Friday 2025`**（见今日修正 ①） |

### C. 老外怎么说（真在用的说法）

| phrase | 谁在用 / 什么意思 |
|---|---|
| **"Starting at € 67.70 per month, excl. VAT"** | **hetzner.com/hosting/ 官方产品行原文（今日复抓，7 行里 6 行同格式）**：€67.70 拍卖 / €59.00 独服 / €5.99 Cloud / €34.00 托管 / €1.60 虚拟主机 / €4.29 Storage Share / €3.20 Storage Box，另 1 行写 `on demand`。**欧洲厂商的"起价 + 不含税"标准句法**，看到 `excl. VAT` 就得自己加税 |
| **"Reduction in:"** + `00:23:30`（下方 `Intel XEON E-2276G`） | 同上官方页拍卖区原文：**降价倒计时**，比拍卖卡上的 `left` 更正式 |
| **"Snap up your offer."** / **"Keep an eye on price changes."** / **"Compare offers."** / **"Enter your desired hardware specification."** | 同上拍卖四步说明原文。`Snap up` = 抢到手，比 buy 更口语；`Keep an eye on` = 盯住 |
| **"max. per month"** + **"per hour"** + `06:45:27left` | **hetzner.com/sb 拍卖卡原文（今日新抓，倒计时 `06:45:27left` / `16:34:11left` / `33:52:11left` / `42:24:26left` / `42:26:57left`）**：`max. per month` = **封顶月价**（不是固定价），`left` 紧挨时间无空格 |
| **"Server AuctionID: 3095549"** | 同上原文（今日新抓 **3095549 / 3096433 / 3095702**，Day14 是 3095118 / 3095150，Day12 是 3095297，Day11 是 3091544）：**拍卖机唯一编号**，社区报价时的身份凭证 |
| **"Traffic: unlimited"** / **"NIC 1 Gbit - Intel I219-LM"** / **"replacement of defective hardware"** / **"free email support"** / **"free phone support"** | 同上拍卖卡详情原文：`replacement of defective hardware` = 坏件更换（拍卖机最关键的售后条款） |
| **"€0.0748 per hour"** | hetzner.com/sb?search=gpu 原文：**按小时计价**是拍卖 / 裸机圈的常态单位，与 `max. per month` 并存 |
| **"Up to 70% off"** + **"this Black Friday"** + **"From $19.49$6.49/mo"** | **hostinger.com/vps-hosting hero 原文（今日复抓）**：**划价与现价紧连无空格**是促销排版固定写法；`this Black Friday` = 旺季口径首次出现在该页 |
| **"Renews at $11.99/mo for 2 years. Cancel anytime."** | 同上四档原句（另三档 $14.99 / $28.99 / $49.99）：`for 2 years` 限定续订价适用时长，`Cancel anytime` 紧跟其后 |
| **"All plans are paid upfront. The monthly rate reflects the total plan price divided by the number of months in your plan."** | 同上官方原句：**"月价"是总额除以月数**，不是每月扣这些钱 |
| **"Secure your deal before it's gone"** / **"30-day money-back guarantee"** / **"MOST POPULAR"** / **"Choose plan"** / **"24/7 support"** | 同上原文：`MOST POPULAR` 压在 KVM 2 卡上方；`Choose plan` 是四档卡的 CTA（与 hero 的 `Claim deal` 是**两个不同按钮**） |
| **"$49/year, renews at $49"** | **LowEndTalk 今日帖标题原文（D4 Networks）**：**renews at 与原价相同 = 真 recurring**，与 Hostinger 的 `Renews at $28.99`（高于促销价）是两种截然相反的机制 |
| **"$12/y Recurring"** / **"25% Recurring OFF"** | LET 原文（今日复现，systemfreaks / NameBig）：`Recurring` = 每个周期都按此价 |
| **"25 x PERPETUAL $1/Year VPS GIVEWAY"** | LET 原文：**`perpetual` 比 `lifetime` 更强的永久说法** |
| **"VPS Restock"** / **"our popular plans are back"** | LET 原文（DeluxHost / Serverpoint）：`Restock` = 补货，`are back` = 重新上架 |
| **"UptimeRobot Raised Pricing by ~62% Any one got Email?"** / **"Kimsufi/Soyoustart/OVH Rise New Price"** | LET 原文：涨价帖的两种标题写法，`Raised Pricing by ~X%` 是母语写法，`Rise New Price` 是非母语写法 |
| **"Order Canceled and Client Account Flagged as FRAUD"** | LET 原文：`Flagged as FRAUD` = 被标欺诈，风控拒单的写法 |
| **"VSYS Host: UA data centers. What happened and where recovery stands?"** | LET 原文：**厂商自己发事故说明的标准问句**（`What happened` + `where recovery stands`） |
| **"Crunchbits is moving services into Synteq client area"** | LET 原文：`moving services into … client area` = 被迁移 / 并入另一家的后台 |
| **"[Early Black Friday Sale] VPS & Dedicated Server Deals \| Starting at Just €18/Year!"** | LET 原文（HostDZire）：**方括号前缀 = 活动类型标签**，`Just` 强调低价 |
| **"6 providers, 269 plans, stock checked daily"** | **rackbazaar.com 原文（今日 B1 新发现的竞品）**：把"每天查库存"直接当卖点；另有 `Sort: Price ↑ Price ↓ Best $/GB RAM Best $/GB disk Newest Featured` 与 `JSON API` |
| **"In stock · 12 left"** / **"Sold out"** / **"—"** | 同上库存三态原文：`12 left` = 库存计数；**`—` = 未知（比瞎填诚实）** |
| **"$0.48 /annual"** 与 **"$5.35 /monthly"** 混在同一个 `Price ↑` 里 | 同上原文：**周期后缀写在价格后面**，年付与月付混排会让"最便宜"失真 |
| **"Prices are shown only when verifiable."** | savecd.com 原文（今日 B1 复现）：与我们的"读不到就不写"同一口径，已挤第 4 家 |
| **"real prices from public sources updated every 6 hours"** / **"15/15 providers returning data"** / **"2026-10-02 last refresh"** | vpsticker.com 原文：`last refresh` 停在 10-02 已 19 天，与 `every 6 hours` 自相矛盾**连续第 9 天** |
| **"Contabo Black Friday Deals Coming Soon!"** / **"Even our regular prices offer better value than most deals you'll find elsewhere"** / **"$5.28 for the first 24 months"** | contabo.com/en-us/black-friday/ 原文：`for the first 24 months` = 折扣期限；黑五页连续第 9 天只有常规价 |
| **"Offer may expire or change at any time."** | vps.blackfriday 原文：免责声明固定句 |
| **"⏱️ Expires December 6, 2025 ➕ Last verified November 25, 2025"** | domainhostcoupon.com 原文（`Last verified` = 最后核验日，券站标准字段）：**2026 年 10 月仍在挂** |
| **"Promotional price applies to the first billing period. Renewal is charged at the regular price."** | onebesthost.com 原文：**"促销价只适用于首个账单周期"最完整的一句厂商自述** |
| **"Auto-renews at $16.99 /mo after 3 years"** / **"First 3 years at $10 /mo"** / **"SAVE 73%"** | DreamHost 官方原文：`Auto-renews at … after N years` 是长周期促销的标准句法 |
| **"You Save 54%"** / **"Renews at $59.99 /mo"** / **"Renews at $86.99 /mo"** | InMotion 官方原文：省多少钱与续订价并排印 |
| **"+20% of the VPS price excl VAT/month"** | firstheberg.com 原文：加购项按 **VPS 价的百分比**计价，且明确 `excl VAT` |
| **"Get a Telegram, email or Discord ping the moment a Hetzner Server Auction listing matches your criteria"** / **"$2.99/month, 7-day free trial"** | **hostnotify.com 原文（今日 B2 发现）**：**拍卖 / 库存提醒已经有人做成付费订阅**，这是"变化"这件事第一次出现明码标价 |

### 明日候选

1. **"€67.70 excl. VAT": The First Price Our Index Ever Caught, After 97 Scans** — A1（97 次已提交扫描里只有 2 次出现货币金额，且都在 `2026-10-20T12:51:51Z` 之后；此前 67 次 Hetzner 标题恒为 82 字符、止于 `from`；今日 07:06 复扫仍 111 字符）+ A5（打开 hetzner.com/hosting/ 逐行核对：**7 行产品里 6 行都印着 `Starting at € X per month, excl. VAT`，我们 16 天只存下拍卖那 1 条**；hostinger 侧同样漏掉四档 `Renews at` 全句）+ B2（**拍卖提醒已被 hostnotify 做成 `$2.99/month` 的付费订阅，但没有任何一个页面在做"起拍价随时间的序列"**——他们只做"匹配就推送"）+ B3（`"excl. VAT" vs "incl. VAT"` 英文 SERP 5 条里 2 条中文问答、1 条南非采购 PDF，**英文位几乎全空**）+ C 栏（`Starting at € 67.70 per month, excl. VAT` / `max. per month` / `per hour` / `Reduction in:` / `Snap up your offer` / `Server AuctionID` / `€0.0748 per hour` / `replacement of defective hardware`）。**缝：要说出"这个价是 10-20 才出现的"，必须先有 10-04 到 10-20 的 97 次快照；只发布当前状态的站无论今天抓到什么都答不出"它以前是什么"。** hardest 的部分是同时承认：**我们的库 16 天里只装下 1 行价格，另外 6 行一直在页面上而我们没存。**
2. **We Check 8 Official Pages Every 4 Hours. Six Have Never Produced a Single Deal.** — A2（5 个 URL **97/97 不可读** + DigitalOcean **97/97 可读但 0 条 offer** = **6/8 页面 16 天零产出**，我们照记、从不删表）+ B5（"deals 站多久更新一次"英文 SERP **第 5 次跑仍是 0 条直接命中**，唯一沾边的是 Zyte 讲房地产爬虫）+ B1（**所有竞品都在比条数**：vpsticker `15 providers tracked 29 live offers`、cheapvps.store `Compare 1,257+ VPS plans`、rackbazaar `6 providers, 269 plans, stock checked daily`——**没有一家公开"我查了几个页面、几个没出东西"**）+ C 栏（`15/15 providers returning data` / `2026-10-02 last refresh` / `Prices are shown only when verifiable.` / `In stock · 12 left` / `Sold out` / `—`）。**缝："覆盖了多少家"是能吹的数字，"我查了 8 个、6 个白查"是只能自曝的数字——正因如此没人肯做。** 今日新增旁证：rackbazaar 的 `Price ↑` 把 `$0.48 /annual` 与 `$5.35 /monthly` 混排，说明"条数多"与"可比"根本是两回事。
3. **"Up to 70% Off" Is Just the Biggest of Four Badges: How to Read One VPS Pricing Card** — A3（库内顺序 `70, 67, 64, 65` vs 页面顺序 `67, 64, 70, 65`，**两个都不单调**；我们没有数值列，所以库里那个顺序只是抓取顺序）+ A5（逐档核对：hero `Up to 70% off` **正好等于四档最大值，不是额外优惠**；四档续订句 `Renews at $11.99 / $14.99 / $28.99 / $49.99/mo for 2 years. Cancel anytime.`；`All plans are paid upfront. The monthly rate reflects the total plan price divided by the number of months in your plan.`）+ B4（**"renews at"是厂商自己印在价卡上的字段，不是社区黑话**：DreamHost `Auto-renews at $16.99 /mo after 3 years`、InMotion `Renews at $59.99 /mo`、onebesthost `Promotional price applies to the first billing period. Renewal is charged at the regular price.`）+ C 栏（`Renews at … for 2 years` / `All plans are paid upfront…` / `30-day money-back guarantee` / `MOST POPULAR` / `Choose plan` vs `Claim deal` / `You Save 54%` / `$49/year, renews at $49`）。**缝：避开 10-08 已发 `vps-deals-renews-at-x` 的办法是换切口**——那篇讲"renews at 是什么意思"，这篇讲"**一张卡上四个字段的阅读顺序**"：先看 `Up to X%`（= 四档最大值，不是第五个优惠）→ 找到自己那一档的 badge → 读同档的 `Renews at`（并判断它是高于促销价还是与原价相同）→ 最后读 `paid upfront` 那句才知道"月价"是怎么除出来的。

已用：`compare-vps-deals-total-cost`（10-07）、`vps-deals-renews-at-x`（10-08）、`vps-deals-refund-window`（10-09）、`vps-deals-cost-per-gb-ram`（10-09）、`vps-deals-who-collects-vat`（10-09）、`vps-deals-hourly-to-monthly`（10-10）、`vps-deals-cost-per-gb-disk`（10-11）、`vps-deals-auto-renewal-notice`（10-12）、`vps-deals-port-25-smtp-blocked`（10-13）、`vps-deals-sla-credit-how-to-claim`（10-14）、`vps-deals-payment-methods-accepted`（10-15）、`vps-deals-identity-verification-kyc`（10-16）、`vps-deals-nonpayment-suspension-deletion`（10-17）、`vps-deals-data-kept-after-cancel`（10-18）、`vps-deals-wrong-datacenter-move`（10-19）、**`vps-deals-bandwidth-overage-throttled-or-billed`（10-20，最后一篇已发布，取自 gap-ledger #13 而非 line3 候选）**。

已降级/不再写第二篇：退款天数（已发）、每 GB 单价（已发）、renews at 换算（已发）、Hourly ×672/730（已消耗）、CPU steal 诊断（英文位占满）、过期 deal（pennyclouds 已占）、Unmetered Port Metered Reality（Day2）、Stuck in an AI Support Loop（Day3）、低价套餐断货/候补（Day6）、Hetzner 拍卖"怎么运作"（Day6）、黑五"预热期填不出价格"（Day8，已改写）、"deals 站都会撑满库存"（Day10 证伪）、"Flash Deals vs Evergreen Listings"（Day10 候选 #3，Day11 降级）、"折扣不结束"措辞（Day13 降级）、"挂来源 + 定时 + 承认读不到"作为差异化卖点（Day13 已降级，Day14 再确认：savecd / cloudhostdeals / bestvpsdeal 三家都在做）、**"deals 站多久更新一次"单独成题（Day13 B3 / Day15 B5 两次 0 条直接命中，今日正式降级为佐证素材）**、**"A VPS Black Friday Site Still Says 2024"（Day14 #3，今日作废）**。

**今日修正（重要，三条）**：① **vps.blackfriday 的年份从 `Black Friday 2024` 滚动到了 `Black Friday 2025`** —— Day14 记录的"停在 2024"**今日作废**（正文已动，但仍比当前年份晚一年）。教训与 savecd expiry 同一条：**"没在更新"不能靠一次观察下结论**；但"更新了却仍晚一年"依旧是可用事实。② **Day13 A4 与 Day14 据以立论的"Hetzner title 全历史只有 1 个字符串、82 字符、恒断在 `from`"今日作废**——该字符串在 `2026-10-20T12:51:51Z` 变为 111 字符并**首次带出价格**。这是**连续第二天**出现"前一天立论的事实基础第二天就变了"（昨天是 savecd expiry）。**新判断：我们只在页面把价格写进链接文本的那一天才拿得到价格**——这不是"页面每次都在变而我们没变"，而是"我们的抽取口径决定了我们看不看得到变化"。③ **"Hetzner 页面每次都在变（倒计时 / AuctionID）而 title 一字未变"这个对照今日被打破**：title 现在也变了。Day14 的对照写法需要改成"**同一个页面上，倒计时和 AuctionID 每次刷新都变，而我们存下来的字段要 67 次才变一次**"。

**Day14 三条候选复检（全部未被 10-20 文章消耗，10-20 取的是 gap-ledger #13）**：①「63% Became 64%」（Day14 #1）——**事实基础仍在**（今日页面仍 `Special offer • 64% off`，四档 67/64/70/65 与库吻合），但今日 A1 的"97 次才等到第一个价格"是同一枚硬币的另一面且更新鲜，**两条只能取一条，建议先取 A1**；②「"Claim Deal" Is a Button」（Day14 #2）——**仍在，且今日证据变强**：核对发现 hero 区的 `Claim deal` 与四档卡的 `Choose plan` 是**两个不同的 CTA**，distinct offer_url 4 个、distinct 页面仍 3 个，建议合并进候选 #3；③「A VPS Black Friday Site Still Says 2024」（Day14 #3）——**今日作废**，年份已滚到 2025。Day13 #2「No utm, No ref, No "?"」——**仍是最稳的一条**，行基数应重算为 **97×7 = 679 行**（97 次扫描，其中 9 次为 7 条期），下轮复算。YABS 怎么读（Day4 #3）**维持移出候选池**。**gap-ledger 提醒：可用未写剩 7 条（#14–#20），下一步取 #14「删机 / 换机 / 换机房后能不能留住 IP」；line3 候选是 gap-ledger 写完后的回退池，不是当前取题源——两套不要混。**

---

## 2026-10-22 (Day 16)

### A. 原创内容邪修

| # | 邪修点 | 为什么别人抄不走 |
|---|---|---|
| A1 | **全库第一次出现"价格变化"**：Hetzner 拍卖行在 scan #100 / `2026-10-21T06:51:23Z` 从 **`€ 67.70`** 变成 **`€ 58.70`**，跌 €9.00（13.3%）。`€ 67.70` 存活 **17 小时 59 分 32 秒**、只被 5 次扫描拍到（#95–#99）；`€ 58.70` 至今 3 次扫描 / 11h56m。此前 scan #0–#94 共 **15 天 13 小时 2 分 43 秒**该字段没有任何数字 | 必须同时持有 #95（首次出现价）与 #100（首次变化）两次快照才能说出"降了 9 欧"。B5 实测英文 SERP **0 条**在做这条 `Starting at` 线的时序——hostnotify 只数逐台 listing 的 `Price cuts 472`（24h 全站聚合），vpsbenchmarks / gauraxtiwari 只写"typical €29/€39/€49"这类静态快照。**没有人把这一行当时间序列** |
| A2 | **605 行里只有 8 行含货币符号（1.32%），且全历史只出现过 2 个不同的价**：`€ 67.70`（5 行）×5、`€ 58.70`（3 行）×3，全部来自同一条 Hetzner 记录；其余 **597 行一个数字都没有**。今日复抓官方页核对，`€ 58.70` 确实印在 `Starting at € 58.70 per month, excl. VAT` | 要算出"605 行里 8 行有钱"必须先有 103 次快照的行级累加。**只发布当前状态的站，一行里永远只有 1 个价格，不存在分母**。这条同时自曝：我们的抽取口径只有 1.32% 的行能碰到钱 |
| A3 | **把全库突变做成一张只有 4 行的完整账本**：103 次独立扫描、102 次转换，**98 次一字未变**；4 次突变分别是 #28（5→6 条，Hetzner 行出现）、#88（6→7 条，`63%`→`64%` + `Claim deal`）、#95（**史上第一个价格**）、#100（**史上第一次价格变化**）。**最后两次突变只隔 5 次扫描**——前 94 次一动不动，之后 8 次扫描里连爆两次 | 4 行账本每一行的成立都依赖 103 次逐字节快照。**"98/102 零变化"这个分母本身就是资产**：竞品只发布当前状态，它的世界永远是 0/0，既没有分母也没有分子 |
| A4 | **我们索引里有一行根本不是 VPS deal，而且它的 CTA 跳出了厂商域名**：`Student discount`（`https://www.hostinger.com/student-discount`）从 scan #0（10-04）起 **103/103 次在场**，17 天没变过；它的 `offer_url` ≠ `source_url`（源页是 `/vps-hosting`），**title 里一个数字都没有**。打开核对：真身是 **`Get online for less with 25% student discount`**，需经 **Student Beans** 验证、`Available to new users only`，按钮 `Claim discount` 直接跳到 **studentbeans.com**（第三方域） | **公开"我的 VPS 报价索引里有一行是学生认证页"是纯自曝**。而 25% 这个真实数字我们 103 次扫描一次都没存——因为 schema 没有 percent 列，title 又只有两个单词。**承认"我有一行 deal 的折扣率是 0（因为我没存）"没人肯写** |
| A5 | **打开自己存的 offer_url 逐字核对，并公开"页面变了几次、我们变了几次"**：hetzner.com/hosting/ 今日新增标语 **`Prices drop & excitement mounts. Place bids in our Server Auction!`**（Day15 无此句）+ `Reduction in: 00:02:45 AMD Ryzen 5 3600`；hetzner.com/sb 拿到**全新倒计时 `19:24:08left` / `21:42:40left` / `23:33:01left` / `26:54:07left` 与全新 AuctionID `3097455` / `3097151` / `3097146`**（Day15 是 3095549 / 3096433 / 3095702，Day14 是 3095118 / 3095150，Day12 是 3095297，Day11 是 3091544） | **同一页面上，倒计时与 AuctionID 每次刷新都变，而我们存下来的字段 103 次只变了 4 次**。这个比值只有"既抓了页面、又存了 103 次快照"才说得出来。今日新增：`Prices drop` 是厂商自己印的，**我们的价格方向（67.70→58.70）第一次与厂商自述同向** |

### B. 谷歌搜索查词（今天真跑过的）

| query | SERP 上看到了什么 | 判断 |
|---|---|---|
| `vps deals` | **核心词**。前五：vpsticker（`15 providers tracked 29 live offers` / `15/15 providers returning data` / **`2026-10-02 last refresh`**，今天 10-21 已 19 天未动）、vpsfilter（`Updated daily`）、**rackbazaar（今日从 `6 providers, 269 plans, stock checked daily` 缩到 `3 providers, 9 plans. Updated daily. No dark patterns.`——公开缩水）**、savecd（`Prices are shown only when verifiable.`）、vncoupon（越南/中文券站） | **锁死不动**。核心词 SERP 连续第 3 天洗牌。**今日最大变化是 rackbazaar 主动缩到 1/30 规模并打出 `No dark patterns.`**——"条数少但诚实"第一次被当成卖点 |
| `VPS plan price history over time tracker "price change"` | MonoVM（Forex VPS 泛文）、**VPSBenchmarks `/plans`（`Managed VPS Only` / `Hyperscaler Only` 筛选，3 天前更新，无价格时序）**、vpsticker（`29 live offers, no estimated numbers`，仍无时间戳）、VPS Depot（`STARTING AT $19.95 / MONTH`）、**vpspricetracker.com（新站，`rank and compare VPS by price, CPU, storage and network`，仍是当前态排序）** | **可做，空位确认**。5 条里 **0 条提供"某个价格随时间的序列"**；连名字叫 Price Tracker 的站都只是排序器 |
| `Hostinger student discount VPS 25% Student Beans verify` | ee.co.uk（Student Beans 通用说明）、**idcspy（中文，2022 年写 Hostinger × Student Beans"全场九折"——即当年是 10%，今日页上是 25%）**、**studentbeans.com/hk（原文 `entertainment 25% student discount hostinger 只適用於學生 在線`）**、oneplus（`/discount` 页说明可用 Studentbeans / Gocertify.me / SheerID 验证） | **可做但要换切口**。"学生折扣"在英文 SERP 里是**零售圈内容**（手机运营商 / 鞋服 / 数码），VPS 语境 0 条。但**"同一家厂商的学生折扣率从 10% 变成 25%"这个跨年事实**是可写的一手对照——我们有 103 次在场记录，却一次都没存下那个数字 |
| `Hetzner server auction "prices drop" bidding starting price how it works` | hetzner.com/?country=en（`Server Auction Prices drop & excitement mounts. Place bids in our Server Auction!`）、hetzner.com/（`The clock is ticking!` + 四步 `1. Enter your desired hardware specification. 2. Compare offers. 3. Keep an eye on price changes. 4. Snap up your offer.`）、**hostnotify.com（`Listings change constantly and prices drop over time, so the best deals disappear within minutes.`）**、serverbidding.com（`Prices are dropping on our Server Auction.`）、HostFoundry（性能评测） | **观察，不单独立题**。"拍卖怎么运作"Day6 已降级。但**今日拿到关键外部互证**：厂商自己写 `Prices drop`、第三方写 `prices drop over time`、我们的库记到 `67.70→58.70`——**三方第一次同向** |
| `hetzner auction "starting at" lowest price over time history chart` | hetzner.com（首页，无时序）、hostnotify（`#3078774 · ex. VAT`、`$168 (€151)`、`$2.63`、**逐台 listing 级，非 `Starting at` 行**）、百度百科（中文）、NodeReef（中文）、VPSBenchmarks Hetzner 页（`Base price of 6.49€/mo`） | **可做，英文位 0 条**。**这条 query 直接验证 A1 的独占性**：英文 SERP 里没有任何一页在记录 `Starting at € X` 这一行的历史值。hostnotify 的 133 台清单是 listing 级聚合，口径与我们不同 |
| `cheap vps "out of stock" "back in stock" restock providers 2026` | vncoupon（RackNerd 年付促销）、**vpsticker（`TransIP … $12.99 EUR /mo in stock checked 2026-10-02`、`GreenGeeks 4 GB VPS $69.95 USD /mo in stock checked 2026-10-02`——`checked` 日期与 `last refresh` 同为 10-02）**、**topvpslist.com（新站，`compares affordable VPS hosting by renewal pricing`，明写按续订价比）**、pdqserver、rdp.sh | **降级为佐证**。"out of stock / back in stock"英文位被零售与电商内容占满（Day6 `waitlist` 同理）。**新收获：`renewal pricing` 这个词被第三方站当卖点**——与我们 10-08 已发 `renews-at-x` 不同层，可留作旁证 |
| `rackbazaar vps deals providers plans updated daily no dark patterns` | rackbazaar.com（`Find a VPS by spec, location, or price — 3 providers, 9 plans, updated daily` + 筛选器 `Price (USD/mo) / RAM (GB) / Storage type Any NVMe SSD HDD / Virtualization Any KVM OpenVZ LXC Dedicated / Location / Apply filters Reset 3 providers`）、vncoupon、newcoupons、racknerd.com、rackdc.com | **观察**。**rackbazaar 从 269 plans 掉到 9 plans**，且新增 `No dark patterns.` 自我标榜。它是第一个"缩减规模并公开承认"的英文竞品 |

### C. 老外怎么说（真在用的说法）

| phrase | 谁在用 / 什么意思 |
|---|---|
| **"Prices drop & excitement mounts. Place bids in our Server Auction!"** | **hetzner.com/hosting/ 官方原文（今日新增，Day15 该页无此句）**：厂商自述"价格在降"。今日我们库里 `67.70→58.70` 首次与厂商自述同向 |
| **"Starting at € 58.70 per month, excl. VAT"** | 同上官方拍卖行原文（今日核对，**Day15 此处为 `€ 67.70`**）。同页另 6 行：独服 `€ 59.00` / Cloud `€ 5.99` / 托管 `€ 34.00` / 虚拟主机 `€ 1.60` / Storage Share `€ 4.29` / Storage Box `€ 3.20`，另 1 行写 `on demand` |
| **"Reduction in:"** + `00:02:45`（下方 `AMD Ryzen 5 3600`） | 同上官方页拍卖区原文：**降价倒计时**（Day15 是 `00:23:30` / Intel XEON E-2276G），每次刷新都在走 |
| **"1. Enter your desired hardware specification. 2. Compare offers. 3. Keep an eye on price changes. 4. Snap up your offer."** | 同上官方四步说明原文（hetzner.com/ 版本前有 `The clock is ticking!`）。`Keep an eye on price changes` = 盯价格变化，是厂商教买家的原话 |
| **"19:24:08left"** / **"21:42:40left"** / **"23:33:01left"** / **"26:54:07left"** | **hetzner.com/sb 官方拍卖页原文（今日复抓，全部全新）**：倒计时写法，`left` 紧挨时间无空格 |
| **"Server AuctionID: 3097455"** / `3097151` / `3097146` | 同上原文（今日新抓；Day15 = 3095549 / 3096433 / 3095702，Day14 = 3095118 / 3095150，Day12 = 3095297，Day11 = 3091544）：**拍卖机唯一编号**，社区报价时的身份凭证 |
| **"max. per month"** + **"per hour"** + **"Location #FSN1-DC4"** | 同上拍卖卡原文：`max. per month` = **封顶月价**（不是固定价）；`#FSN1-DC4` = 机房代号写法（另见 `#FSN1-DC1` / `#FSN1-DC15` / `#FSN1-DC8`） |
| **"Traffic: unlimited"** / **"NIC 1 Gbit - Intel I219-LM"** / **"replacement of defective hardware"** / **"free email support"** / **"free phone support"** | 同上拍卖卡详情原文：`replacement of defective hardware` = 坏件更换，拍卖机最关键的售后条款 |
| **"Get online for less with 25% student discount"** | **hostinger.com/student-discount 官方原文（今日首次打开核对）**：这就是我们索引里 `Student discount` 那行的真身——**折扣率是 25%，我们 103 次扫描一次都没存** |
| **"Verify your student status through Student Beans to unlock an exclusive 25% discount on hosting. Available to new users only."** | 同上原文。`Available to new users only` = 仅限新用户；`unlock` = 解锁（需先验证） |
| **"Student Beans is the world's leading student verification platform"** / **[Claim discount](https://www.studentbeans.com/student-discount/us/hostinger)** | 同上原文：**CTA 跳出厂商域名**到第三方验证平台。认证方三选一的说法见 oneplus.com/ie/discount（`verify with Studentbeans or Gocertify.me or SheerID`） |
| **"Stop refreshing the Hetzner auction"** | **hostnotify.com 首页大标题原文（今日首抓）**：把"别再手动刷新"当产品定位 |
| **"Auction prices fall over time. Get pinged again when a match drops 5% or more, with a cooldown you set."** | 同上 `Price-drop re-alerts` 段原文：`drops 5% or more` = 跌 5% 再推一次；`cooldown` = 冷却期 |
| **"New 266 / Gone 285 / Price cuts 472"** | 同上 `What the auction did in the last 24 hours` 原文（下方 `Cheapest per TB that vanished in 24h`）：**全站 24h 聚合计数**。它数的是逐台 listing，不是 `Starting at` 那一行 |
| **"visible 12h"** / **"visible 5h"** / **"visible 88 min"** / **"visible 49 min"** + **"Counted from our snapshots, so a listing may have been up longer before we first saw it."** | 同上原文：`visible` = 上架可见时长；**末句是快照测量的标准免责声明——和我们"固定时点采样只能给出下界"同一困境** |
| **"$148/mo (€133) · $2.31/TB · #3082997 · ex. VAT"** | 同上推送样例原文：**`ex. VAT` 缩写**，与 Hetzner 官方的 `excl. VAT` 是两种写法；`$2.31/TB` = 每 TB 单价 |
| **"prices ex. VAT"** / **"7-day trial · no card · $4.99 $2.99/mo after"** / **"Applied at checkout, no code needed"** | 同上定价区原文。**今日涨价信号**：Day15 记的是 `$2.99/month`，今日已变成 **`$4.99` 划线价 + `$2.99/mo after`**（`Launch offer`）。`no code needed` = 无需优惠码 |
| **"Good listings do not wait"** / **"Cheap storage does not sit around."** | 同上原文：稀缺感的母语写法 |
| **"Popular server types like CX22 or CAX11 sell out in some locations for days"** | 同上原文：`sell out` = 卖光（stock 圈最常用动词），`for days` = 连续数天 |
| **"a price that falls until someone takes it"** / **"Every listing has a countdown. When it expires and the machine is still unsold, the price drops and the clock restarts."** | 同上 guides 原文（`/guides/hetzner-server-auction`、`/guides/price-drops`）：**拍卖降价机制最完整的一句英文解释** |
| **"We only read what Hetzner publishes: the auction feed, the dedicated server catalogue and Cloud stock."** / **"HostNotify is an independent service and is not affiliated with or endorsed by Hetzner"** | 同上 FAQ 原文：**第三方挂来源 + 声明非官方**的标准句法 |
| **"no noisy neighbors"** | **bex.co 英文评测文原文（`The Hetzner auction box at ~$51 is the floor for a real dedicated machine with no noisy neighbors.`）**：`noisy neighbors` = 邻居抢资源，本次首次在英文评测站原文里抓到（此前几轮只在 LET 语境推测） |
| **"After Hetzner's Price Hike"** / **"raised its shared and dedicated x86 lines by 110 to 175 percent and more"** | 同上原文（2026-09-18）：**`Price Hike` 是涨价的标准母语说法**（LET 侧对应 `Raised Pricing by ~62%` / `Rise New Price` / `Pricing Update`） |
| **"auction prices are dynamic and demand-based"** / **"Dynamic auction pricing"** | webhostingservices.co 原文：**第三方描述拍卖价的标准措辞是"动态"，但没人给数字序列** |
| **"Hetzner Price Adjustment 15 June 2026"** | 同上引用 Hetzner Docs 的篇名：**厂商官方文档的涨价公告命名法**（`Price Adjustment`，不用 increase/hike） |
| **"compares affordable VPS hosting by renewal pricing"** | topvpslist.com 原文（今日 B6 发现的新英文站）：**`renewal pricing` 被第三方当比较维度** |
| **"3 providers, 9 plans. Updated daily. No dark patterns."** | **rackbazaar.com 原文（今日复抓）**：**从 Day15 的 `6 providers, 269 plans, stock checked daily` 缩到 `3 providers, 9 plans`**，并新增 `No dark patterns.`（无暗黑模式）。筛选器原文 `Storage type Any NVMe SSD HDD` / `Virtualization Any KVM OpenVZ LXC Dedicated` / `Apply filters Reset` |
| **"in stock checked 2026-10-02"** | **vpsticker.com 原文（今日 B6 复抓）**：`TransIP … $12.99 EUR /mo in stock checked 2026-10-02`、`GreenGeeks 4 GB VPS $69.95 USD /mo in stock checked 2026-10-02`。**`checked` 日期与首页 `last refresh` 同为 10-02，已 19 天** |
| **"real prices from public sources updated every 6 hours"** / **"15/15 providers returning data"** / **"2026-10-02 last refresh"** | 同上首页原文：`every 6 hours` 与 `2026-10-02` 自相矛盾**连续第 10 天** |
| **"Prices are shown only when verifiable."** | savecd.com 原文（今日 B1 复现）：与我们的"读不到就不写"同一口径，已挤第 5 家 |
| **"Fourplex VPS Pricing Update Effective November 1, 2026"** | **LowEndTalk 今日帖标题原文**：**涨价预告的标准句法**（`Pricing Update Effective <date>`），比 `price hike` 正式 |
| **"Black Friday 2026 - Wishlist Thread"** / **"TRENDING NOW: RackNerd's BLACK FRIDAY! NEW DEALS, NEW LOCATIONS, NEW HARDWARE + 100's of GIVEAWAYS!"** / **"DartNode - Countdown to Black Friday"** | LET 原文（今日复现）：`Wishlist Thread` = 社区许愿帖；`TRENDING NOW:` 是论坛置顶前缀；`Countdown to` = 倒计时预告 |
| **"DeluxHost.net \| VPS Restock \| Improved Storage Servers! \| Z / T / Q \| Highly DDoS Protected \| NL"** | LET 原文（今日复现）：`Restock` = 补货；`Z / T / Q` = 机房区段代号；`Highly DDoS Protected` = 高防 |
| **"$12/y Recurring"** / **"25 x PERPETUAL $1/Year VPS GIVEWAY !! Netfront AS4658"** | LET 原文：`Recurring` = 每周期同价；`PERPETUAL` 比 `lifetime` 更强的永久说法；`GIVEWAY` 是社区惯用拼错 |
| **"UptimeRobot Raised Pricing by ~62% Any one got Email?"** / **"Kimsufi/Soyoustart/OVH Rise New Price"** | LET 原文（今日复现）：涨价的两种写法——母语 `Raised Pricing by ~X%` 与非母语 `Rise New Price` |
| **"CloudCone VPS: 2 Reinstalls, 4 Support Reps, 9 Hours Waiting for an IPv4 Change"** | LET 原文：**用计数控诉工单处理的标题写法** |
| **"AxusHost Outage? All of My Servers Are Down"** | LET 原文：`Outage` 是故障帖固定词；`All of My Servers Are Down` = 全挂 |
| **"WTB: Maltese VPS with BGP/BYIOP -- Budget 50-60EU/Month"** / **"REQ Austria"** / **"Bring Your Own Server"** | LET 原文：`WTB` = want to buy（求购）、`REQ` = request（求资源）、`BYIOP` / `Bring Your Own Server` = 自带 IP / 自带服务器 |
| **"25G Unmetered 30% lifetime discount - Dedicated Servers"** / **"The Eternal Väinämöinen -- Seedboxes Starting From 1.99€/Month or 6.99€/Year -- 700 Years Give Away"** | LET 原文：`Unmetered` = 不限量（端口不限）；`lifetime discount` = 终身折扣 |
| **"DataPasa Is Scam - Avoid"** | LET 原文：**`Is Scam - Avoid` 是社区点名跑路/欺诈的固定标题格式** |
| **"Exclusive LowEndBox Pricing: 2GB KVM VPS for $1.83/Month First Year! Godlike.Host is Back!"** | **LowEndBox 原文（今日复现）**：`Exclusive LowEndBox Pricing` = 本站专属价；`First Year!` 限定首年；`is Back!` = 厂商回归 |
| **"Velohost Returns With Even Cheaper Prices!"** / **"Eight months ago, they were selling a 4GB VPS … for 3.00€/month. Now they're selling that same package for only 2.60€/month!"** | LEB 原文（今日复现）：**跨期同套餐降价的对照写法**——我们要写"价格随时间变化"，LEB 的写法是"人工挑两次对比"，我们是"103 次自动快照" |
| **"Early Bird Discounts on Cheap Colocation!"** / **"with Early Bird discounts available for 12 months"** | LEB 原文（今日复现）：`Early Bird` = 早鸟价，且明确期限 |
| **"A VPS for UNDER $10/YEAR!"** / **"Those are IPv6-only, but they have IPv4 as well for only $17.95 a year!"** | LEB 原文（今日复现）：`IPv6-only` + IPv4 加购的说法 |
| **"all 100 VPS instances have now been given away"** / **"FlipperHost is back"** | LEB 原文：`be given away` = 送完；`is back` = 重新上架 |
| **"10,000 Benchmarks! … YABS (Yet Another Benchmark Script)"** | LEB 原文（ServerVerify 访谈）：`YABS` 全称出处。注意：YABS 怎么读（Day4 #3）**维持移出候选池** |

### 明日候选

1. **"€67.70 Became €58.70": The First Time a Price Moved Inside Our Index** — A1（103 次独立扫描里**第一次价格变化**，发生在 `2026-10-21T06:51:23Z`；`€ 67.70` 存活 **17h59m32s**、只被 5 次扫描拍到；此前 15 天 13 小时 2 分 43 秒该字段没有数字）+ A2（**605 行里只有 8 行含货币符号 = 1.32%**，全历史只出现过 2 个不同的价）+ A5（打开 hetzner.com/hosting/ 核对，页面确实印着 `Starting at € 58.70 per month, excl. VAT`，且新增标语 **`Prices drop & excitement mounts.`**——**厂商自述、第三方 hostnotify `prices drop over time`、我们的 67.70→58.70，三方第一次同向**）+ B5（`hetzner auction "starting at" lowest price over time history chart` **英文 SERP 0 条**：hostnotify 数是逐台 listing 的 `Price cuts 472`，不是这一行）+ C 栏（`Prices drop & excitement mounts` / `Reduction in:` / `ex. VAT` / `Price-drop re-alerts` / `drops 5% or more` / `a price that falls until someone takes it`）。**缝：要说出"降了 9 欧、上一个价活了 18 小时"，必须同时持有 #95 与 #100 两次快照；只发布当前状态的站，它的世界里这一行永远只有一个值。** hardest 的部分是同时承认 A2：**我们有 597 行一个数字都没有。**
2. **7 Deals, 4 Discounts: Three Rows in Our Index Aren't What They Look Like** — A4（`Student discount` 从 scan #0 起 **103/103 在场**，offer_url 是 `/student-discount` ≠ source_url `/vps-hosting`，**title 里零数字**；打开核对真身是 `25% student discount`、需 Student Beans 验证、`Available to new users only`、CTA 跳到 **studentbeans.com 第三方域**）+ Day14 #2 遗留（`Claim deal` 是 `#pricing` 锚点按钮，不是折扣）+ A5（Hetzner 那行是**产品线的起价行**，不是促销）。**合计：7 行里只有 4 行是真正的 VPS 折扣徽章，另外 3 行分别是同页锚点按钮、跨文档的学生计划入口、厂商产品线起价** + B3（"学生折扣"英文 SERP 被零售圈占满，VPS 语境 0 条；但 **idcspy 2022 年记的是 10%，今日官方页是 25%**）+ C 栏（`Get online for less with 25% student discount` / `Available to new users only` / `Claim discount` / `world's leading student verification platform`）。**缝：把"我的索引里有什么不是 deal"逐条列出来是纯自曝**——尤其"这一行的折扣率是 25%，而我存了 103 次都没存下那个数字"。根因可公开：**schema 没有 type 列，也没有 percent 列**，所以一笔折扣、一个按钮文字、一个计划入口在我们的表里长得一模一样。
3. **Our Blind Window Is 6 Hours. The First Price We Ever Timed Lived 18.** — A3（**103 次扫描 / 102 次转换，98 次零变化**；完整突变账本只有 4 行：#28 / #88 / #95 / #100，**最后两次只隔 5 次扫描**）+ 采样时钟自曝（间隔 min **1.1 分钟** / median 277.8 分钟 / max **374.5 分钟 = 6.24 小时** / mean 3.95 小时；**24 个 UTC 小时里只覆盖 11 个，13 个小时从未被扫过**）+ A1（**今天第一次有了"外部变化速度"的实测值：€67.70 活了 17h59m32s，我们拍到 5 次**）+ C 栏（hostnotify `Counted from our snapshots, so a listing may have been up longer before we first saw it.`——**同为快照测量的第三方也在同一困境里**；`visible 12h / 88 min / 49 min`）。**缝：过去我们只能说"我们多久扫一次"，今天第一次能拿一个实测的外部变化时长去量自己的盲窗**——18 小时的价我们抓到 5 次，若它只活 4 小时，我们有 6.24 小时的盲窗就可能整段错过。**把"我的采样时钟"和"被测对象的变化速度"并排放，需要 103 次快照 + 至少一次真实的外部变化，缺一不可。**

已用：`compare-vps-deals-total-cost`（10-07）、`vps-deals-renews-at-x`（10-08）、`vps-deals-refund-window`（10-09）、`vps-deals-cost-per-gb-ram`（10-09）、`vps-deals-who-collects-vat`（10-09）、`vps-deals-hourly-to-monthly`（10-10）、`vps-deals-cost-per-gb-disk`（10-11）、`vps-deals-auto-renewal-notice`（10-12）、`vps-deals-port-25-smtp-blocked`（10-13）、`vps-deals-sla-credit-how-to-claim`（10-14）、`vps-deals-payment-methods-accepted`（10-15）、`vps-deals-identity-verification-kyc`（10-16）、`vps-deals-nonpayment-suspension-deletion`（10-17）、`vps-deals-data-kept-after-cancel`（10-18）、`vps-deals-wrong-datacenter-move`（10-19）、`vps-deals-bandwidth-overage-throttled-or-billed`（10-20）、**`vps-deals-can-you-keep-your-ip-after-delete`（10-21，最后一篇已发布，取自 gap-ledger #14 而非 line3 候选）**。

已降级/不再写第二篇：退款天数（已发）、每 GB 单价（已发）、renews at 换算（已发）、Hourly ×672/730（已消耗）、CPU steal 诊断（英文位占满）、过期 deal（pennyclouds 已占）、Unmetered Port Metered Reality（Day2）、Stuck in an AI Support Loop（Day3）、低价套餐断货/候补（Day6）、Hetzner 拍卖"怎么运作"（Day6，**今日 B4 再确认：厂商 + hostnotify + HostFoundry 三方都在讲，不立题**）、黑五"预热期填不出价格"（Day8，已改写）、"deals 站都会撑满库存"（Day10 证伪）、"Flash Deals vs Evergreen Listings"（Day10 #3，Day11 降级）、"折扣不结束"措辞（Day13 降级）、"挂来源 + 定时 + 承认读不到"作为差异化卖点（Day13 已降，Day14 再确认）、"deals 站多久更新一次"单独成题（Day13/Day15 两次 0 条，降级为佐证）、"A VPS Black Friday Site Still Says 2024"（Day14 #3，已作废）、**"out of stock / back in stock" 单独成题（Day16 B6 降级，英文位被零售电商占满，与 Day6 `waitlist` 同一原因）**。

**今日修正（重要，三条）**：① **Day15 A1"97 次扫描里只有 2 次出现货币金额"的口径必须升级**——今日 €67.70→€58.70，说明那不是"罕见地出现价格"，而是**我们已经进入了一条价格序列**：10-20 12:51:51 首次出现、10-21 06:51:23 首次变化，两次只隔 5 次扫描。**"只有 2 次"的说法今日作废，正确说法是"103 次里 8 行有钱、2 个不同的值、1 次变化"。** ② **Day15 候选 #1「"€67.70 excl. VAT": The First Price Our Index Ever Caught」今日事实基础已变**——它强调"第一次抓到价格"，而今天有了第二次（更低）。**必须升级为"第一次价格变化"，否则文章见光当天就过期。** ③ **rackbazaar 从 `6 providers, 269 plans, stock checked daily` 缩到 `3 providers, 9 plans`**——Day15 B1 把它当"条数多但不可比"的样本，**该判断今日失效**（它已主动缩到 1/30 并打出 `No dark patterns.`）。**教训：竞品的规模数字每天都在变，任何以"某某有多少条"为前提的论证都必须当天复抓。**

**Day15 三条候选复检（全部未被 10-21 文章消耗，10-21 取的是 gap-ledger #14）**：①「"€67.70 excl. VAT": The First Price Our Index Ever Caught」（Day15 #1）——**事实基础已变但方向有利**，今日升级为「€67.70 Became €58.70」（本轮候选 #1），**建议先取这条**；②「We Check 8 Official Pages Every 4 Hours. Six Have Never Produced a Single Deal.」（Day15 #2）——**仍在，今日未复验**，下轮需重算为 103 次基准；③「"Up to 70% Off" Is Just the Biggest of Four Badges」（Day15 #3）——**仍在**，但本轮候选 #2 的"7 行里只有 4 行是折扣"是同族且更狠，两者只能取一。Day14 #2「"Claim Deal" Is a Button」——**按 Day15 建议合并进本轮候选 #2**。Day13 #2「No utm, No ref, No "?"」——**仍是最稳的一条**，行基数应重算为 **103×7 = 721 行**（103 次扫描，其中 15 次为 7 条期）。YABS 怎么读（Day4 #3）**维持移出候选池**。**gap-ledger 提醒：可用未写剩 6 条（#15–#20），下一步取 #15；line3 候选是 gap-ledger 写完后的回退池，不是当前取题源——两套不要混。**

---

## 2026-10-23 (Day 17)

### A. 原创内容邪修

| # | 邪修点 | 为什么别人抄不走 |
|---|---|---|
| A1 | **折扣徽章是个被算出来的数，而我们从来没存过算出它的两个输入**。scan #88 / `2026-10-19T12:51:50Z` 那次 `63%`→`64%`，我们的库只记下"+1 个百分点"。今日逐档反推：**徽章 = round((原价 − 售价) / 原价 × 100)**。US 页 KVM 1 `(19.49 − 6.49) / 19.49 = 66.70% → 67%`；KVM 2 `(24.49 − 8.79) / 24.49 = 64.11% → 64%`；KVM 4 `(42.99 − 12.99) / 42.99 = 69.78% → 70%`；KVM 8 `(73.99 − 25.99) / 73.99 = 64.87% → 65%`。四档全部对上。**所以 63→64 可能是售价降了，也可能是原价抬了，我们无法分辨** | 要说出这句话必须同时具备三样东西：① **108 次快照**才能知道 `63%` 活了 88 次扫描、死在 #87；② **我们自己的 schema 没有 price 列**（这是自曝，没人肯写）；③ **同一厂商的区域页对照**——今日 B3 抓到 `hostinger.com/ae/vps-hosting` 上 KVM 1 是 **`68% off US$19.99 US$6.49/mo`**，而 US 页是 **`67% off $19.49 $6.49/mo`**。**售价完全相同（$6.49）、原价不同（19.99 vs 19.49）、徽章就差 1pp。** 只发布当前状态的站，看到哪个数就报哪个数，永远看不到"同一个售价有两个徽章" |
| A2 | **今天"deals 页"上 7 条 deal 的中位年龄是 108 次扫描 / 17 天 18 小时 58 分**。逐条在场计数：`Student discount` **108/108**、`70% off` **108/108**、`67% off` **108/108**、`65% off` **108/108**（四条都生于我们第一次扫描之前）、`64% off` **20/108**（3 天 5 小时 55 分）、`Claim deal` **20/108**、Hetzner 价格行 **8/108**（1 天 11 小时 56 分）。中位 108、均值 68.6、最小 8、最大 108 | **"这条 deal 挂了多久"是一个只能靠历史算出来的量，而它恰好是 deals 站最不愿意让人问的问题**——因为答案永远是"很久"。今天第一次把它做成单一数字：**中位 17 天 18 小时**。更狠的是：**全库最新的一条（8 次扫描 / 36 小时）同时也是唯一带过钱的那一条**——新鲜度和"有没有价"在我们库里是同一件事。竞品卖"每天刷新"，刷新不改变年龄 |
| A3 | **突变速率换了一个数量级，然后又停了**。108 次扫描 / 107 次转换 / **103 次零变化**；4 次突变落在 #28、#88、#95、#100。分段看：**前 88 次扫描只有 1 次突变，后 12 次扫描有 3 次**——速率约 ×20。然后自 #100 起 **7 次连续扫描、1 天 11 小时 56 分 17 秒零变化**，是价格出现以来最长的一段静默 | "突变账本"本身需要 108 次逐字节快照，但**今天新的是"分段速率"**：同一个索引在 10-19 前后表现完全不同。这个结论每一次都必须重算——Day16 写的是"4 行账本"，今天它是"1 次 / 3 次 / 停"。只发布当前状态的站既没有分子也没有分母，更没有"分段"这个概念 |
| A4 | **把每一条 title 的长度排成一个元组，108 次扫描只产生过 4 种元组**：`(16,28,28,28,28)`×28、`(16,28,28,28,28,82)`×60、`(10,16,28,28,28,28,82)`×7、`(10,16,28,28,28,28,111)`×13。**四个百分比徽章永远是精确的 28 个字符**——它是 `NN% off — Hostinger VPS page` 这个模板的产出；`Student discount` 恒为 16、`Claim deal` 恒为 10，是手写的标签 | **同一张表里混着三种不同的字符串生成器**（一个模板吐 4 行 + 两个手写标签），而我们的 schema **没有 type 列**，所以模板产出、按钮文案、计划入口在我们的表里长得一模一样。28 这个常数只有逐次量长度才看得到，而且它顺带解释了为什么"四个徽章长度相同"不等于"四个徽章同龄"（见 A2：其中一个是 20 次，另外三个是 108 次） |
| A5 | **8 个受检 URL、108/108 次在场、readable 翻转次数全为 0**（Hostinger/Hetzner/DigitalOcean 恒 True，Vultr/Linode/Contabo×3 恒 False）。**但今日 B1 出现的新竞品 vpsdealswire.com 已经在公开同样的事**：逐厂商挂 `HostHatch 0 offers listed`、`A2 Hosting 0 offers listed`、`Bitlaunch 0 offers listed`、`InterServer unreachable (HTTP 403)` | **"公开读不到"这条路今天挤进第 4 家，不能再当卖点**（已降级，见文末）。仍独有的是**时间维度**：vpsdealswire 的 `0 offers listed` 是**一次快照的状态**，我们的 `flip = 0 / 108` 是**结构性证明**——失败不是抖动。而且我们连 `Hetzner Cloud` 的对位也做得更细：它在本次会话内从 `0 offers listed` 变成 `from €5.99/mo · 4 offers`，**总条数 214 → 222**，而我们的库 108 次只动过 4 次 |

### B. 谷歌搜索查词（今天真跑过的）

| query | SERP 上看到了什么 | 判断 |
|---|---|---|
| `vps deals` | **核心词**。前五：**saver.com**（券站，`DEAL VERIFIED` / `Monovm 20% OFF … Expires Nov 13, 2026` / `Rockhoster 25% Off First Month on Managed VPS`）、**gxcom.net/latest-vps-hosting-deals**（`*Current reference pricing at the time of update` / `Low Monthly Equivalent ≠ Month-to-Month Billing` / `$5 Unmanaged VPS ≠ $5 Managed VPS`）、**vpsdealswire.com（今日首次进入核心词前五的新竞品）**、gxcom.net/top-vps-deals、**gb.hostadvice.com**（`The average VPS price is $10 for a yearly or multi-year subscription`） | **锁死不动，但今日最大事件是新竞品 vpsdealswire 直接冲进核心词第 3 位**。它公开 `32 Providers` / `222 Offers listed` / `€0.01 From / mo` / `Oct 2026 Updated`，并逐厂商公布 `0 offers listed` 与 `unreachable (HTTP 403)`。**这条直接改写了我们的差异化清单**（见文末降级） |
| `vpsdealswire VPS Hosting Deals Public Promotions providers offers listed` | **savecd.com**（`Prices are shown only when verifiable.`）、ovh.com/sg/deals、colocrossing（中文站，`55%VPS折扣`）、**cloudhostdeals.com（`7 live offers from 3 providers, read from their own public pricing pages and refreshed every six hours.`）**、**vpsticker.com（`Independent VPS price radar. Lowest published monthly price from 15 hosting providers, refreshed every 6 hours. 29 live offers, no estimated numbers.`）** | **观察，竞品口径盘点**。五家英文站口径全部公开：cloudhostdeals `7 offers / 3 providers`、vpsticker `29 offers / 15 providers`、vpsdealswire `222 offers / 32 providers`、savecd `5 providers`、我们 `7 rows / 3 pages / 8 URLs checked`。**没有一家公布"每一行挂了多久"**——这正是 A2 的空位 |
| `hostinger vps hosting discount 70% 67% 65% 64% off badges plans` | **厂商自己就有 5 个近乎相同的页面**：`/black-friday-vps-deals`（**67 / 64 / 70 / 65**，`$19.49→$6.49`，`Secure your deal before it's gone`）、`/au/vps-hosting`（67 / 64 / 70 / 65，**A\$28.19→A\$9.39**）、**`/ae/vps-hosting`（68 / 64 / 70 / 65，`US$19.99→US$6.49`）**、`/docker-hosting`（67 / 64 / 70 / 65）、`/recommended/panduan-coding-vps`（67 / 64 / 70 / 65） | **今日最大发现，直接可做**。**KVM 1 在 AE 页是 `68% off`、在 US 页是 `67% off`，而两边售价都是 `$6.49 / US$6.49`**——差的那 1pp 来自原价（19.99 vs 19.49）。**同一个售价、两个徽章** = 徽章是算出来的，不是写死的 |
| `hetzner server auction "starting at" price lowest today october 2026` | hetzner.com（`1. September 2026 The new GEX45 GPU server: AI power at an entry-level price`）、**百度百科（中文，占第 2 位）**、**hetzner.com/sb（`SERVER AUCTION Prices are dropping on our Server Auction.` / `The Smart Way to Start Self-Hosting`）**、hostnotify（`$2.99/month, 7-day free trial`）、VPSBenchmarks（`Base price of 6.49€/mo for 1TB with 1.5GB traffic/hr`） | **可做，英文位仍是 0 条时序**。5 条里 0 条在记录 `Starting at € X` 这一行的历史值；**中文位被百度百科占掉第 2 名**（且它写"2026 年 Hetzner 宣布了多次服务提价"）。厂商自己的说法今日换了措辞：Day16 是 `Prices drop & excitement mounts.`，今天 `/sb` 上是 **`Prices are dropping on our Server Auction.`** |
| `vps deal "last checked" "last verified" timestamp how old is this offer` | domainhostcoupon（**`⏱️ Expires No expiry listed` / `➕ Last verified May 2, 2026`**、HostDare 页 `Last verified May 2, 2026`）、Justhost.asia（`2026年7月18日verified saving`）、DreamHost 十点清单、VPSDime、DigitalOcean rkhunter 教程 | **英文位第 6 次 0 条直接命中**，维持"降级为佐证"。**但今天拿到了两句硬货**：**`No expiry listed`**（券站承认没有到期日的写法）与 **`Last verified <date>`**（核验日字段）。前者正好是我们"schema 无 expiry 列"的母语对照说法 |
| `black friday 2026 vps hosting deals early november countdown` | **5 条全是零售**：Currys Ireland（`Black Friday 2025 might be over, but it's never too soon to start thinking about 2026`）、TechRadar AU、**tryblackfriday（Friday falls on November 27, 2026）**、blackfriday.com（`Black Friday 2026 is on Friday, November 27, 2026`）、Argos（`The countdown to Black Friday 2026 is on!`） | **VPS 语境 0 条**——"黑五"这个词在英文里被零售完全占满，不要单独成题。**但拿到确定日期：Black Friday 2026 = 11 月 27 日**（TechRadar / blackfriday.com / tryblackfriday 三方一致），Cyber Monday 11 月 30 日，且 TechRadar 明写 `early Black Friday deals can kick of in early November`。**距今天 35 天**，是我们 108 次快照布局的旺季窗口 |
| `vps price drop history tracker archive "was" "now" changed discount percentage` | **comparedge/price-watch-mcp（GitHub，`product_changes returns dated rows for one slug` / `last verified July 4` / `The human-readable trail is its price history page`）**、xbxprices（Xbox 价格追踪）、domainhostcoupon（**`1 expired archive entry kept for price reference`**）、keepa（Amazon）、struggleville（Home Depot） | **VPS 语境 0 条，但拿到了最重要的旁证**：**"价格变更历史"这个品类在 SaaS 侧已经存在且有成熟说法**（`dated rows`、`price history page`、`last verified`），在游戏/零售侧更是标配（keepa / xbxprices）。**唯独 VPS 侧空白**——A1/A2/A3 的空位由此坐实 |

### C. 老外怎么说（真在用的说法）

| phrase | 谁在用 / 什么意思 |
|---|---|
| **"68% off"** vs **"67% off"** | **hostinger.com/ae/vps-hosting 与 US 页的同一档 KVM 1 原文对照（今日首次抓到）**：AE 页 `68% off KVM 1 US$19.99 US$6.49/mo`，US 页 `67% off KVM 1 $19.49 $6.49/mo`。**售价同为 6.49，徽章差 1pp**——徽章由原价算出，不是写死的 |
| **"Special offer • 64% off"** + **"MOST POPULAR"** | 同上价卡原文：`Special offer •` 是**仅此一档才有的前缀**（其余三档只有裸百分比）；`MOST POPULAR` 是主推档标记 |
| **"Renews at US$11.99/mo for 2 years. Cancel anytime."** | 同上原文（四档分别 `US$11.99 / US$14.99 / US$28.99 / US$49.99`）。AE 页用 `US$` 前缀区分币种，US 页直接 `$` |
| **"From US$19.99US$6.49/mo"** | 同上 hero 区原文：**原价与促销价之间无空格连写**，是厂商页的标准排版（`/mo` 后缀） |
| **"All plans are paid upfront. The monthly rate reflects the total plan price divided by the number of months in your plan."** | 同上原文：**"月价"是怎么除出来的**唯一权威句。另见同页 FAQ `Our KVM VPS hosting plans range from US$6.49–US$25.99/month` |
| **"Up to 70% off VPS hosting this Black Friday"** / **"Secure your deal before it's gone"** | 同上原文。今日确认：**黑五文案已经挂到常规 VPS 页与 Docker 页上**，不再是单独的 `/black-friday-vps-deals` 页 |
| **"Choose plan"** vs **"Claim deal"** | 同上原文：**价卡上的 CTA 是 `Choose plan`，hero 区的 CTA 是 `Claim deal`**——我们库里 `Claim deal` 那一行来自后者 |
| **"SERVER AUCTION Prices are dropping on our Server Auction."** / **"The Smart Way to Start Self-Hosting"** | **hetzner.com/sb 官方原文（今日复抓）**：Day16 在 `/hosting/` 上抓到的是 `Prices drop & excitement mounts.`，今天 `/sb` 上是这句。**同一件事、两个页面、两种措辞** |
| **"04:51:29left"** / **"07:26:11left"** / **"07:33:02left"** / **"13:25:06left"** / **"13:29:57left"** | 同上官方拍卖页原文（**今日全新，全不同于 Day16 的 19:24:08/21:42:40/23:33:01/26:54:07**）：倒计时紧挨 `left` 无空格 |
| **"Server AuctionID: 3098065"** / `3098482` / `3098397` | 同上原文（今日新抓；Day16 = 3097455/3097151/3097146，Day15 = 3095549/3096433/3095702，Day12 = 3095297，Day11 = 3091544）：拍卖机唯一编号 |
| **"Location #HEL1-DC2"** / **"#HEL1-DC9"** | 同上原文（**今日机房从 `#FSN1-*` 换成了 `#HEL1-*`**——Falkenstein → Helsinki）。`#` + 城市代码 + `-DC` + 编号是 Hetzner 的机房写法 |
| **"max. per month"** / **"per hour"** / **"Traffic: unlimited"** / **"iNIC"** / **"IPv4"** | 同上拍卖卡原文：`max. per month` = **封顶月价**（不是固定价）；`iNIC` = 内网网卡；`Traffic: unlimited` = 流量不限 |
| **"2 x SSD M.2 NVMe 512 GB"** / **"2 x HDD SATA 2,0 TB Enterprise"** / **"4 x RAM 16384 MB DDR4"** | 同上原文：**`N x` 前缀表示数量**；注意 `2,0 TB` 用**欧式逗号小数** |
| **"replacement of defective hardware"** / **"free email support"** / **"free phone support"** | 同上 `Support services` 原文：**拍卖机的售后三件套**，逐台不同（有的只有电话支持） |
| **"Prices are shown only when verifiable."** | savecd.com 原文（今日 B2 复现）：与我们的"读不到就不写"同一口径，已挤第 6 家 |
| **"7 live offers from 3 providers, read from their own public pricing pages and refreshed every six hours."** | **cloudhostdeals.com 原文（今日 B2 复抓）**：`live offers` + `read from their own public pricing pages` + `refreshed every six hours`，三件套齐全 |
| **"Independent VPS price radar. Lowest published monthly price from 15 hosting providers, refreshed every 6 hours. 29 live offers, no estimated numbers."** | **vpsticker.com 原文（今日 B2 复抓）**：`price radar` 是这类站给自己取的品类名；`no estimated numbers` = 不填估算值 |
| **"Live pricing pulled straight from 32 hosting providers' own public pages. Nothing here is invented; sponsored placements are labeled as such."** | **vpsdealswire.com 原文（今日 B1 首次进入核心词 SERP 的新竞品）**：`pulled straight from … own public pages` + **`Nothing here is invented`** —— 与我们"绝不编造"同一口径，措辞最狠的一家 |
| **"32 Providers"** / **"222 Offers listed"** / **"€0.01 From / mo"** / **"Oct 2026 Updated"** | 同上首页统计条原文。**本次会话内实测：先是 `214 Offers listed` + `Hetzner Cloud 0 offers listed`，几分钟后变 `222` + `Hetzner Cloud from €5.99/mo · 4 offers`**——**它的数字以分钟为单位在动，我们的以"次突变 / 108 次"为单位** |
| **"HostHatch 0 offers listed"** / **"A2 Hosting 0 offers listed"** / **"Bitlaunch 0 offers listed"** / **"InterServer unreachable (HTTP 403)"** | 同上逐厂商状态原文：**公开"0 条"与"403 不可达"**——Day15 候选 #2 的差异化前提今日作废 |
| **"12+ offers"** | 同上原文：**条数封顶写法**（超过 12 只写 `12+`），与 `3 offers` / `5 offers` 精确值混用 |
| **"⏱️ Expires No expiry listed"** / **"➕ Last verified May 2, 2026"** | **domainhostcoupon.com 原文（今日 B5）**：`No expiry listed` = 承认没有到期日；`Last verified` = 最后核验日。**2026 年 10 月仍挂着 5 月的核验日** |
| **"1 expired archive entry kept for price reference"** | 同上原文（今日 B7）：`expired archive entry` = 过期归档条目，`kept for price reference` = 留作价格参考——**券站已经开始为"历史价"留档** |
| **"product_changes returns dated rows for one slug"** / **"last verified July 4"** / **"The human-readable trail is its price history page"** | **comparedge/price-watch-mcp（GitHub）原文（今日 B7）**：SaaS 侧"价格变更历史"的成熟说法。`dated rows` = 带日期的行；**VPS 侧无对应物** |
| **"Expires Nov 13, 2026"** / **"DEAL VERIFIED"** / **"SHOW DEAL"** / **"Buy 1 Year, Get 2 Months Free"** / **"25% Off First Month on Managed VPS"** / **"Free Setup on All New Server Orders"** | **saver.com 原文（今日 B1 核心词第 1 位）**：券站标准四件套。`Expires <date>` / `DEAL VERIFIED` / `SHOW DEAL`；`Buy 1 Year, Get 2 Months Free` = 买一年送两月；`Free Setup` = 免安装费 |
| **"Base price of 6.49€/mo for 1TB with 1.5GB traffic/hr"** | **VPSBenchmarks 原文（今日 B2）**：`Base price of` 是跑分库标起价的说法；`traffic/hr` = 每小时流量配额 |
| **"*Current reference pricing at the time of update. Promotions, locations, billing terms, and configurations can change."** | **gxcom.net 原文（今日 B1 第 2 位）**：`reference pricing at the time of update` = 更新当时的参考价。**它明写了"会变"，但没给上一次的值** |
| **"Low Monthly Equivalent ≠ Month-to-Month Billing"** / **"$5 Unmanaged VPS ≠ $5 Managed VPS"** | 同上原文：**用 `≠` 做标题的写法**，把两个易混概念并排否定 |
| **"The average VPS price is $10 for a yearly or multi-year subscription."** | gb.hostadvice.com 原文（今日 B1 第 5 位）：`yearly or multi-year subscription` = 年付/多年付 |
| **"Black Friday 2026 - Wishlist Thread"** | **LowEndTalk 原文（今日复现）**：`Wishlist Thread` = 社区许愿帖，每年旺季固定格式 |
| **"Fourplex VPS Pricing Update Effective November 1, 2026"** | LET 原文（今日复现）：**涨价预告标准句法** `Pricing Update Effective <date>`（比 `price hike` 正式） |
| **"[Early Black Friday Sale] VPS & Dedicated Server Deals \| Starting at Just €18/Year!"** | LET 原文（今日复现）：方括号 = 活动类型标签；`Just` = 强调低价 |
| **"TRENDING NOW: RackNerd's BLACK FRIDAY! NEW DEALS, NEW LOCATIONS, NEW HARDWARE + 100's of GIVEAWAYS!"** / **"DartNode - Countdown to Black Friday"** | LET 原文（今日复现）：`TRENDING NOW:` 是置顶前缀；`Countdown to` = 倒计时预告 |
| **"LET YABS Thread"** | LET 原文（今日复现）：社区跑分集中帖。**注意：YABS 怎么读（Day4 #3）维持移出候选池** |
| **"25 x PERPETUAL $1/Year VPS GIVEWAY !! Netfront AS4658"** | LET 原文（今日复现）：`PERPETUAL` = 永久；`GIVEWAY` 是社区惯用拼错；`AS4658` = ASN 号 |
| **"$12/y Recurring"** / **"25% Recurring OFF \| LET Exclusive"** / **"Recurring Discounts"** | LET 原文（今日复现）：**`Recurring` 有两种用法**——跟在价格后表示"每周期同价"，跟在折扣后表示"每周期都打折" |
| **"Unmetered 1 Gbps"** / **"30% lifetime discount"** | LET 原文（今日复现）：`Unmetered` = 端口不限量；`lifetime discount` = 终身折扣 |
| **"VPS Restock \| Improved Storage Servers! \| Z / T / Q \| Highly DDoS Protected \| NL"** | LET 原文（今日复现）：`Restock` = 补货；`Z / T / Q` = 机房区段代号；`Highly DDoS Protected` = 高防 |
| **"DataPasa Is Scam - Avoid"** / **"Chunkserve is fraud !"** | LET 原文（今日复现）：**`Is Scam - Avoid` / `is fraud !` 是点名跑路的固定标题格式** |
| **"AxusHost Outage? All of My Servers Are Down"** / **"Incognet Kansas City Outage and WHMCS 403"** | LET 原文（今日复现）：`Outage` = 故障；**`WHMCS 403` 把具体的 403 写进标题**（与 vpsdealswire 的 `unreachable (HTTP 403)` 是同一事实的两种写法） |
| **"Should I be seeing other servers on the same "LAN" as my VPS?"** | LET 原文（今日复现）：**`noisy neighbors` 的民间问法**——不识术语的买家用"同一 LAN 里看到别人的机器"描述同一件事 |
| **"[WTB] Affordable VPS in UAE (Dubai) or Turkey - Hourly/Monthly"** / **"REQ Austria"** | LET 原文（今日复现）：`WTB` = want to buy；`REQ` = request；`Hourly/Monthly` = 计费周期诉求 |
| **"PHP security advisory: Critical remote code execution vulnerabilities, update now (21 Oct 2026)"** | LET 原文（今日新出）：`security advisory` + **`update now (<date>)`** 是社区安全帖的固定格式 |
| **"Exclusive LowEndBox Pricing: 2GB KVM VPS for $1.83/Month First Year! Godlike.Host is Back!"** | **LowEndBox 原文（今日复现）**：`Exclusive LowEndBox Pricing` = 本站专属价；`First Year!` = 限定首年；`is Back!` = 厂商回归 |
| **"Velohost Returns With Even Cheaper Prices!"** / **"Get a 4GB VPS for Only 2.60€/month!"** | LEB 原文（今日复现）：**跨期同套餐降价的对照写法**——我们要写"价格随时间变化"，LEB 是人工挑两次对比，我们是 108 次自动快照 |
| **"Early Bird Discounts on Cheap Colocation! $29/Month in Phoenix from Cloudnium!"** | LEB 原文（今日复现）：`Early Bird` = 早鸟价 |
| **"A VPS for UNDER $10/YEAR!"** / **"all 100 VPS instances have now been given away"** | LEB 原文（今日复现）：`UNDER $X/YEAR` 强调句式；`be given away` = 送完 |
| **"10,000 YABS! New Features!"** / **"the largest collection of YABS (Yet Another Benchmark Script) benchmarks on the planet, with over 10,000 user-submitted reports"** | LEB 原文（今日复现）：YABS 全称出处；`user-submitted` = 用户提交 |
| **"ServersCamp: new Simple VPS, starting €1/month"** / **"Infrawire - VPS now in Turkey \| 10 Gbps \| Linux & Windows \| Starting at $9.30/mo"** | LEB 侧栏原文（今日复现）：`Starting at` 是**起价行**的标准前缀（正是我们 A1 追踪的那一行） |
| **"Instant setup, automatic RPKI ROA, rDNS, and WHOIS changes - Free /48 IPv6 for everyone - IPYE.com"** | LEB 侧栏原文（今日复现）：`Instant setup` / `RPKI ROA` / `rDNS` / `/48 IPv6` 是运维买家的硬需求词 |

### 明日候选

1. **"68% Off" and "67% Off" Are the Same $6.49: A VPS Discount Badge Is Calculated, Not Written** — A1（徽章 = `round((原价 − 售价) / 原价 × 100)`，四档反推全部对上：67 / 64 / 70 / 65；**63→64 那次我们只看到 +1pp，无法分辨是售价降了还是原价抬了**）+ A5 + B3（**AE 页 `68% off US$19.99 US$6.49/mo` vs US 页 `67% off $19.49 $6.49/mo`——售价相同、原价差 0.50、徽章差 1pp**；厂商另有 `/au/`（A\$）、`/docker-hosting`、`/recommended/panduan-coding-vps` 等多个同构页）+ C 栏（`Special offer • 64% off` / `MOST POPULAR` / `Renews at … for 2 years` / `From US$19.99US$6.49/mo` / `All plans are paid upfront…`）。**缝：要说出"同一个售价有两个徽章"，必须同时打开两个区域页；要说出"63% 活了 88 次扫描才变"，必须有 108 次快照；要说出"我们分不清是哪个输入动了"，必须先承认自己没有 price 列。三条缺一不可，而且第三条是自曝。**  hardest 的部分是明说：**我们的库把"算出来的结果"当成"事实"存了 108 次。**
2. **The Median Deal on Our Index Is 17 Days Old** — A2（**7 条 deal 的中位在场年龄 = 108 次扫描 / 17 天 18 小时 58 分**；四条生于我们第一次扫描之前，`64%` 与 `Claim deal` 各 20 次 / 3 天 5 小时 55 分，Hetzner 价格行 8 次 / 1 天 11 小时 56 分；均值 68.6）+ A3（**前 88 次扫描只有 1 次突变，后 12 次有 3 次**，然后 7 次连续静默 1 天 11 小时 56 分）+ B2（五家英文竞品口径全部公开——cloudhostdeals `7 offers / 3 providers`、vpsticker `29 / 15`、vpsdealswire `222 / 32`、savecd `5 providers`——**没有一家公布"每一行挂了多久"**）+ C 栏（`live offers` / `refreshed every six hours` / `no estimated numbers` / `Oct 2026 Updated` / `reference pricing at the time of update`）。**缝："我多久扫一次"大家都在说，"我这一行挂了多久"没人说——因为答案永远是"很久"。** 可复用的写法：把 7 行按年龄排成一列，配 `Oct 2026 Updated` 这种月份级口径对照。
3. **28 Characters, 88 Scans: Three Different String Generators Feed One Table** — A4（**108 次扫描只产生 4 种 title 长度元组**；四个百分比徽章恒为 **28 字符** = `NN% off — Hostinger VPS page` 模板的产出；`Student discount` 恒 16、`Claim deal` 恒 10 = 手写标签；四个 28 字符的行里，三个是 108 次、一个是 20 次，**长度相同 ≠ 同龄**）+ A2（中位年龄）+ C 栏（`Choose plan` vs `Claim deal` / `Secure your deal before it's gone` / `Special offer •`）。**缝：公开"我的表里混着三种字符串生成器、而且没有 type 列区分它们"是纯自曝**——它等于承认我们无法程序化判断哪一行是折扣。可复用的写法：给出 4 个元组 × 出现次数（×28 / ×60 / ×7 / ×13），让读者自己看出"我们的表只变过 3 次形状"。

已用：`compare-vps-deals-total-cost`（10-07）、`vps-deals-renews-at-x`（10-08）、`vps-deals-refund-window`（10-09）、`vps-deals-cost-per-gb-ram`（10-09）、`vps-deals-who-collects-vat`（10-09）、`vps-deals-hourly-to-monthly`（10-10）、`vps-deals-cost-per-gb-disk`（10-11）、`vps-deals-auto-renewal-notice`（10-12）、`vps-deals-port-25-smtp-blocked`（10-13）、`vps-deals-sla-credit-how-to-claim`（10-14）、`vps-deals-payment-methods-accepted`（10-15）、`vps-deals-identity-verification-kyc`（10-16）、`vps-deals-nonpayment-suspension-deletion`（10-17）、`vps-deals-data-kept-after-cancel`（10-18）、`vps-deals-wrong-datacenter-move`（10-19）、`vps-deals-bandwidth-overage-throttled-or-billed`（10-20）、`vps-deals-can-you-keep-your-ip-after-delete`（10-21）、**`vps-deals-block-storage-price-per-gb`（10-22，最后一篇已发布，取自 gap-ledger #15 而非 line3 候选）**。

已降级/不再写第二篇：退款天数（已发）、每 GB 单价（已发）、renews at 换算（已发）、Hourly ×672/730（已消耗）、CPU steal 诊断（英文位占满）、过期 deal（pennyclouds 已占）、Unmetered Port Metered Reality（Day2）、Stuck in an AI Support Loop（Day3）、低价套餐断货/候补（Day6）、Hetzner 拍卖"怎么运作"（Day6）、黑五"预热期填不出价格"（Day8，已改写）、"deals 站都会撑满库存"（Day10 证伪）、"Flash Deals vs Evergreen Listings"（Day10 #3，Day11 降级）、"折扣不结束"措辞（Day13 降级）、"挂来源 + 定时 + 承认读不到"作为差异化卖点（Day13 已降，Day14 再确认）、"deals 站多久更新一次"单独成题（Day13/Day15 两次 0 条，降级为佐证）、"A VPS Black Friday Site Still Says 2024"（Day14 #3，已作废）、"out of stock / back in stock" 单独成题（Day16 B6 降级）、**「We Check 8 Official Pages Every 4 Hours. Six Have Never Produced a Single Deal.」（Day15 #2，今日正式降级——B1 新竞品 vpsdealswire.com 已公开逐厂商的 `HostHatch 0 offers listed` / `A2 Hosting 0 offers listed` / `Bitlaunch 0 offers listed` / `InterServer unreachable (HTTP 403)`，"公开读不到"这条路挤进第 4 家，不再是我们的独家）**。

**今日修正（重要，三条）**：① **"公开 0 条 / 不可达"不再是差异化卖点**，必须用时间维度重述：vpsdealswire 的 `0 offers listed` 是一次快照的状态，我们的 `readable 翻转 = 0 / 108 次` 是结构性证明。② **徽章不是常量而是算式**——Day14 把 `63% → 64%` 当作"页面上真的改了折扣"来写（A1「63% Became 64%」），今天证明**它可能只是原价从 19.49 挪到 19.99 一类的输入变化**：同一售价 `$6.49` 在 AE 页就是 68%。**任何"折扣变了"的立论，动笔前先确认是售价动了还是原价动了**——而我们没有 price 列，恰恰无法确认。③ **本次会话内实测竞品数字以分钟为单位在动**：vpsdealswire 从 `214 Offers listed` + `Hetzner Cloud 0 offers listed` 变为 `222` + `from €5.99/mo · 4 offers`，相隔仅几分钟。**"某某有多少条"这类数字连一个会话都撑不过，绝不能作为论证前提。**

**Day16 三条候选复检（全部未被 10-22 文章消耗，10-22 取的是 gap-ledger #15）**：①「"€67.70 Became €58.70": The First Time a Price Moved Inside Our Index」（Day16 #1）——**仍是最强的一条，但今日必须换分母口径**：`€ 58.70` 已被 **8 次**扫描拍到，超过 `€ 67.70` 的 5 次，**全库含钱行从 8 行增至 13 行 / 640 行 = 2.03%**；且自 #100 起已 7 次连续零变化，需补进"静默期"这个新事实；②「7 Deals, 4 Discounts: Three Rows in Our Index Aren't What They Look Like」（Day16 #2）——**仍在**，且今日 A4 的"三种字符串生成器"是同族但更硬的版本（能给出 28/16/10 三个常数 + 4 种元组），**两条只能取一条，建议取 A4 版本**；③「Our Blind Window Is 6 Hours. The First Price We Ever Timed Lived 18.」（Day16 #3）——**仍在**，采样时钟今日重算：间隔 min **1.1 分钟** / median 277.8 分钟 / max **374.5 分钟 = 6.24 小时** / mean **3.99 小时**，**24 个 UTC 小时里只覆盖 11 个**（新增 weekday 分布：Mon 22 / Thu 21 / Tue 17 / Wed 15 / Sat 12 / Sun 11 / Fri 10）。Day15 #2 已降级（见上）。Day13 #2「No utm, No ref, No "?"」——**仍是最稳的一条**，行基数应重算为 **640 行**（原 721 是按 103×7 估算，实际为 108 次扫描逐次累加）。YABS 怎么读（Day4 #3）**维持移出候选池**。**gap-ledger 提醒：可用未写剩 5 条（#16–#20），下一步取 #16；line3 候选是 gap-ledger 写完后的回退池，不是当前取题源——两套不要混。**

---

## 2026-10-24 (Day 18)

### A. 原创内容邪修

| # | 邪修点 | 为什么别人抄不走 |
|---|---|---|
| A1 | **第二次价格变化是往上涨的，而所有英文资料都说它只会跌**。scan #110 / `2026-10-23T06:50:54Z`：Hetzner 那行从 **`€ 58.70` → `€ 65.70`，+7.00**。这是 113 次扫描里**第一次观测到价格上升**。今天 B7 抓到的五份英文资料口径完全一致地只讲"降"：baremetalindex FAQ `listed prices fall automatically over time until a server is taken`、thetruestack `The price drops steadily every few hours until someone buys it`、achromatic `descending-price (Dutch) auction mechanism … prices progressively decrease over time`、topsitehosters `prices start at a set level and drop over time until someone claims the server`、valebyte `the price for a lot gradually decreases until someone buys it`。**更狠的是厂商自己**：我们存的 source_url `hetzner.com/hosting/` 上那句标语今天仍是 **`Prices drop & excitement mounts.`**，而同一页面此刻印的数字是 `€ 65.70`——**比它两天前的 `€ 58.70` 高 7 欧**。标语说跌、数字涨了，两者在同一页同一分钟里并存 | 要说出这句话必须同时持有三样东西：① **113 次快照**才能知道 `58.70` 活了 10 次扫描 / 1 天 23 小时 59 分 31 秒，且这是"第二次"变化而不是第一次；② **必须同时记录两个方向**——baremetalindex 的 `Was / Now / Drop` 表只显示下跌（`-23% / -12% / -6% / -6% / -5%`），它的数据结构里没有"涨"这个位置；③ **厂商标语与厂商数字取自同一次 HTTP 读取**（`fetched_at 2026-10-23T18:47:53Z`），所以矛盾是同一时刻的，不是跨日拼出来的。只发布当前状态的站，它的世界里 `Starting at` 这一行永远只有一个值，永远不会有"方向"这个概念 |
| A2 | **第一次出现了真正做价格历史的竞品，而它的粒度和我们完全不同——这个差异本身就是新选题**。B3/B7 挖出 **baremetalindex.com/deals**（`Updated 2026-10-23`）：`computed from our daily price history, each plan's latest price versus its 30-day high`、`Real movements, not marketing`、FAQ 原文 `We capture a daily snapshot of every tracked dedicated-server plan's price into a time-series database`。它做的是**逐台机器**（`Hetzner Intel Xeon E5-1650V3 · 128 GB RAM · 512 GB FSN1-DC13 $195 $151/mo -23%`）。我们做的是**一整页上的那一行聚合值**（`Starting at € X per month`），113 次扫描、中位间隔 **278.6 分钟**、且**涨跌都记** | **两家都在存时间序列，但存的是两个不同的对象**：它存"每一台机器的价"，我们存"整个拍卖场地的下界"。它需要在库里为每台机器建一条序列（所以要 `time-series database`），我们只需要在 675 行里数出 **18 行含货币符号 = 2.67%**。更关键的是口径差：它 `daily snapshot` + `vs 30-day high` + **只算跌幅**；我们 4.64 小时中位间隔 + **绝对值序列** + **两个方向**。这个"同一厂商、同一拍卖、两种完全不同的序列化对象"的对照，需要同时读过它的 methodology 页和我们 113 次快照才写得出来 |
| A3 | **今天拍卖场的起价比同页"全新服务器"的起价还贵**。同一次抓取（`fetched_at 2026-10-23T18:47:53Z`）的 `hetzner.com/hosting/` 上有 7 行 `Starting at`：**Server Auction `€ 65.70`**、**Dedicated Server `€ 59.00`**、Cloud `€ 5.99`、Managed Servers `€ 34.00`、Web hosting `€ 1.60`、Storage Share `€ 4.29`、Storage Boxes `€ 3.20`。**翻新的拍卖机（65.70）比全新独服（59.00）贵 `€ 6.70` = +11.4%**；而我们 18 天只存了这 7 行里的 1 行 | **这是一个必须"同一分钟读同一页的两行"才看得见的反转**，而 deals 站的默认动作就是把每个产品单独成条、打散排序——打散之后这个关系就消失了。更自曝的是后半句：**那 7 行一直在那一页上，我们 113 次扫描只存下 1 行**，另外 6 行连"见过"的记录都没有。这个"我漏了同页 6 行"的事实只有靠打开自己的 source_url 逐行对照才拿得到，无从编造 |
| A4 | **毛波动 16.00、净变化 −2.00，87.5% 的波动互相抵消了**。三次取值 `67.70 → 58.70 → 65.70`：单步 `−9.00`、`+7.00`，**绝对波动之和 16.00**，而**首尾净变化只有 −2.00**（3 天 5 小时 56 分 5 秒）。当前值 `65.70` 比观测最低值 `58.70` 高 **11.9%**。另有一处小常数：三个值的**角分位全是 `.70`** | **"毛/净"这个比值至少需要 3 个值才存在**，而全库只有这一条线有 3 个值（全历史也只有 3 个不同的价）。只发布当前状态的站永远拿不到分子：它看到的是"现在 65.70"，看不到"这条线上下走过 16 欧，最后只留下 2 欧"。**这条同时是给 A1 加码**：如果只报净变化（−2.00），读者会以为"跌了 2 欧"；实际它先跌 9 再涨 7 |
| A5 | **这条 111 字符的 title 里，全历史只有 5 个字符变过**。Hetzner 那行 113 次扫描只产生 **4 个不同的字符串**：无数字版 `…servers from`（82 字符，67 次）+ 三个带价版（各 111 字符，5 / 10 / 3 次）。结构恒为 **85 字符前缀（`Server Auction … from € `）+ 5 个字符的金额 + 21 字符后缀（` per month, excl. VAT`）**。**前缀自 scan #28 起 85 次扫描 / 12 天 0 小时 14 分 48 秒一字未变**，后缀同样。变过的只有中间那 5 个字符 = 整串的 **4.5%** | **"哪个字符在动"是逐字符 diff 才有的结论**，而 deals 站的 schema 里 title 是一个整字段——它只会"整条变了/没变"，不会告诉你"111 个字符里只有 5 个在动"。而且这条顺带把 A1 的因果坐实：**动的正好是金额，而金额由页面上最便宜的那台机器决定**——所以"涨价"不是厂商改价，是**最便宜的那台被买走或下架了**。这个机制推断需要"85 字符恒定 + 5 字符在动 + 拍卖页是荷兰式降价"三件事拼起来 |

### B. 谷歌搜索查词（今天真跑过的）

| query | SERP 上看到了什么 | 判断 |
|---|---|---|
| `vps deals` | **核心词**。前五：**vncoupon.com/vps-hosting（`RAVNIX VPS Deals: Atlanta KVM Servers From $14/Year October 12, 2026` / `RAVNIX is back with fresh VPS deals after moving its infrastructure to a new data center in Atlanta`）**、vncoupon.com 首页、**vpsticker.com（`29 live offers, no estimated numbers` / `15 hosting providers, refreshed every 6 hours`）**、**savecd.com（`Prices are shown only when verifiable.`）**、**lowendstock.com（VPSFILTER，`Updated daily`）** | **锁死不动，但今天英文位换了一半**：Day17 的 saver.com / gxcom.net / vpsdealswire / gb.hostadvice 全部掉出前五，**vncoupon 首次登顶、lowendstock 首次进前五**。vpsdealswire 只撑了一天（Day17 第 3 → 今日 0），**再次印证"核心词牌每天洗"**。**值得做**：前五里没有任何一家给出"这一行挂了多久"或"上次的值是多少"，A2/A4 的空位完好 |
| `hetzner server auction "starting at" price went up history chart` | hetzner.com 首页（`The new GEX45 GPU server`）、**hetzner.com/sb?search=gpu（`BID ON SERVERS AND SAVE! NO MINIMUM CONTRACT PERIOD AND NO SETUP FEES` / `or somebody else might beat you to the bargain`）**、cloud.hetzner.com、**frankly.hostingpost.com（HostFoundry，`it operates on a Dutch-style model where prices start at a set point and gradually decrease over time until a user claims the server`）**、hostnotify（`$2.99/month, 7-day free trial`） | **可做，且是今天最值钱的一条**。5 条里 **0 条在记录 `Starting at € X` 这一行的历史值**，更没有一条提过"它可能涨"。**全部 5 条都在复述"荷兰式降价"这一个说法**——我们对它的第一次反证（A1）因此坐实 |
| `vps price history "price change" tracker archive was now per month` | pricehistory.app（Google Play，`Stores change prices constantly, and change them again during sales. A product marked 60% off can be more expensive than it`）、**vpspricetracker.com（`over 250,000 VPSs from nearly a hundred providers`）**、pricebark.com（Amazon UAE，6 个月历史）、crucial.com.au、plaspy.com/ChangeLog | **VPS 侧第一次出现"价格历史"品类的雏形**——vpspricetracker 首次进 SERP。**但它没有历史**：页面自述 `compiling statistics every 24 hours`，**没有 `last updated` 时间戳、没有 `was/now`**。零售侧（pricehistory.app / pricebark / keepa）早已成熟。**"品类在别处成熟、在 VPS 侧空白"这个对照今天是第 2 次拿到，可作 A2 的背景** |
| `hostinger vps hosting 70% 67% 65% 64% off black friday pricing page` | **hostinger.com.hk/vps-hosting（又一个区域页，人民币：`142.99 47.99 以¥87.99/月 的价格续订 2 年`）**、hostinger.com（`VPS hosting Save on VPS this Black Friday`）、**idcspy（2025-11 记 `官网目前为67%的折扣,使用本站专属优惠码BLACKFRIDAY即可叠加优惠至70%`）**、**Rakuten（`Up to 67% off Node.js VPS Hosting 21.5% Cash Back was 7.5%`）**、host114.org | **观察，区域页清单再 +1**。今天新增 **HK 页（¥）**，与 Day17 已记录的 US（`$`）/ AE（`US$`）/ AU（`A$`）合计 **4 个币种区**。Rakuten 的 **`was 7.5%`**（返现已涨）是"was/now"写法第一次出现在 VPS 相关页上。**未升级**：徽章算术 Day17 候选 #1 已覆盖，本轮不重复开题 |
| `vpspricetracker VPS price history compare rank` | **vpspricetracker.com（`The Largest VPS Directory and Comparator` / `over 250,000 VPSs from nearly a hundred providers` / 同页另一处 `circa 300,000 server configurations`、`120 VPS service providers`，**自曝同页两处规模数字不一致**）、vpsticker、webhostingbreak（`39 Compared`）、panel.dreamhost.com、cloudcostly.com | **观察。今天最有用的一句是它自曝的归一化口径**：`prices are obtained by dividing the annual prices by 12` 与 `Discounts on yearly payment terms are incorporated in the price if available.` ——**它发布的"价"是算出来的，不是页面上的价**。这正是我们"绝不推算"的反面样本，可作 A2/A3 的对照。**不单独成题**（英文位已被 vpsticker / savecd / vpspricetracker 三家占住） |
| `lowendtalk "price increase" renewal "went up" provider announced` | **5 条里 4 条中文**：微信公众号（CenturyLink 涨价和解）、cn.investing.com、百家号（Three/Vodafone 涨价）、**bilibili（`raising prices / raise prices / a price increase` / `across the board` / `went up across the board`）**、微博 | **英文位 0 条，VPS 语境 0 条**，维持不单独成题。**但收获一句母语搭配：`went up across the board`**（全线涨价），可作 C 栏素材。教训同 Day11：**C 栏收来的词必须单独跑 query 验检索需求** |
| `hetzner server auction dutch auction prices decrease over time until someone buys` | **topsitehosters.com/providers/hetzner（`The prices start at a set level and drop over time until someone claims the server`）**、**thetruestack.com/tools/hetzner（`"Dutch Auction." … The price drops steadily every few hours until someone buys it`）**、**achromatic.dev（`a descending-price (Dutch) auction mechanism … prices progressively decrease over time`）**、**baremetalindex.com/deals（今日最大发现）**、valebyte.com | **今日最大发现，直接改写差异化清单**。见文末「今日修正」①。**四份独立英文资料口径 100% 一致地只讲"降"**，为 A1 提供了四个外部对照点 |
| `vps deals site "last checked" timestamp how old is this offer verified date` | **savecd.com（`Source-listed price. Billing period, upfront payment and renewal terms must be checked with the provider.`）**、domainhostcoupon（`⏱️ Expires No expiry listed` / `➕ Last verified April 29, 2026`）、domainhostcoupon HostDare（`Last verified May 2, 2026`）、vpsdime.com、**vpsticker.com（`How often is this updated? The scraper and the site rebuild run on a schedule, every 6 hours. Every page carries the exact UTC timestamp of the fetch it was built from`）** | **英文位第 7 次 0 条直接命中**，维持"降级为佐证"。**新收获**（首次拿到完整句）：vpsticker 的 **`Every page carries the exact UTC timestamp of the fetch it was built from, so you can always tell how fresh what you are reading is.`** —— 它解释了"我何时抓的"，但**没解释"我抓到的这个东西本身多旧"**。这正是 A2「中位在场年龄 113 次扫描」要补的那一格 |

### C. 老外怎么说（真在用的说法）

| phrase | 谁在用 / 什么意思 |
|---|---|
| **"Prices drop & excitement mounts."** | **hetzner.com/hosting/ 官方原文（今日复抓，我们的 source_url）**：厂商对拍卖的标语。**今日矛盾点：同一页此刻印 `Starting at € 65.70`，比 10-21 的 `€ 58.70` 高 7 欧** |
| **"Starting at € 65.70 per month, excl. VAT"** | 同上原文（**今日新值**，前值 58.70 / 67.70）。同页另有 Dedicated `€ 59.00`、Cloud `€ 5.99`、Managed `€ 34.00`、Web hosting `€ 1.60`、Storage Share `€ 4.29`、Storage Box `€ 3.20`、Custom Solutions **`on demand`** |
| **"Keep an eye on price changes."** | 同上官方四步操作原文（`1. Enter your desired hardware specification. 2. Compare offers. 3. Keep an eye on price changes. 4. Snap up your offer.`）。**厂商自己用的是中性词 `price changes`，不是 `price drops`**——与同页标语 `Prices drop` 内部不一致 |
| **"Reduction in: 00:26:17"** / **"AMD Ryzen 9 3900"** | 同上官方拍卖区原文（今日复抓）：下一次降价的倒计时 + 机型 |
| **"01:30:45left"** / **"03:49:24left"** / **"04:51:29left"** / **"07:43:27left"** | **hetzner.com/sb 官方拍卖页原文（今日全新，与 Day17 的 04:51:29/07:26:11/07:33:02/13:25:06/13:29:57 不同）**：倒计时紧挨 `left` 无空格 |
| **"Server AuctionID: 3098517"** / `3099325` / `3099242` | 同上原文（今日新抓；Day17 = 3098065/3098482/3098397，Day16 = 3097455，Day15 = 3095549）：拍卖机唯一编号 |
| **"#FSN1-DC14"** / **"#HEL1-DC12"** / **"#FSN1-DC13"** | 同上原文：机房写法 `#` + 城市代码 + `-DC` + 编号（FSN1 = Falkenstein，HEL1 = Helsinki） |
| **"max. per month"** / **"per hour"** / **"Traffic: unlimited"** / **"iNIC"** | 同上拍卖卡原文：`max. per month` = 封顶月价；`iNIC` = 内网网卡 |
| **"2 x 512 GB SSD"** / **"2 x SSD SATA 480 GB Datacenter"** / **"2 x HDD SATA 4,0 TB Enterprise"** / **"4 x RAM 16384 MB DDR4"** | 同上原文：**`N x` 前缀表示数量**；`4,0 TB` 用欧式逗号小数；`Datacenter` / `Enterprise` 是磁盘等级词 |
| **"replacement of defective hardware"** / **"free email support"** / **"free phone support"** | 同上 `Support services` 原文：拍卖机售后三件套，逐台不同 |
| **"The biggest current discounts on dedicated servers — computed from our daily price history, each plan's latest price versus its 30-day high. Real movements, not marketing. Updated 2026-10-23."** | **baremetalindex.com/deals 原文（今日 B7 首次发现的新竞品）**：`computed from our daily price history` / `latest price versus its 30-day high` / **`Real movements, not marketing`** |
| **"Was"** / **"Now"** / **"Drop"** / **"$195 $151/mo -23%"** | 同上表格栏位原文：**降价表的三栏标准写法**（`Was` = 原值，`Now` = 现值，`Drop` = 跌幅） |
| **"Latest price vs 30-day high, from daily snapshots. Auction & promo prices change fast — confirm at checkout."** | 同上原文：`from daily snapshots` 是口径自述；**注意它写的是 `change fast`（会变），不是 `drop`** |
| **"We capture a daily snapshot of every tracked dedicated-server plan's price into a time-series database, then compare each plan's latest price against its highest price over the last 30 days."** | 同上 FAQ 原文：**`time-series database` / `highest price over the last 30 days`**——**只跟 30 天最高价比，所以它只能显示跌，不能显示涨** |
| **"Why are most drops on Hetzner? Hetzner runs a server auction where listed prices fall automatically over time until a server is taken"** | 同上 FAQ 原文：**`fall automatically over time`** —— 今日 A1 的头号外部对照句 |
| **"Are these prices guaranteed? No. Auction and promotional prices change continuously and can sell out. Always confirm the live price on the provider's checkout page before buying."** | 同上 FAQ 原文：`can sell out` / `Always confirm the live price … before buying` |
| **"score = 0.40 × price + 0.30 × specs + 0.20 × benchmark + 0.10 × support"** / **"The formula is public on purpose"** / **"Missing components are renormalized, not zero-filled"** / **"No score yet"** | **baremetalindex.com/methodology 原文**：公开打分公式；`renormalized, not zero-filled` = 缺失项重新归一化而非填零；`No score yet` = 只读目录不实时抓取的厂商标记 |
| **"Provider public payload"** / **"Provider page snapshot"** / **"Provider catalog / public page"** / **"Source type reflects the current ingestion path"** | 同上数据源透明度表原文：**四种来源类型**（API / payload / snapshot / catalog）。**Hetzner 与 Vultr 标的是 `API`** |
| **"The Largest VPS Directory and Comparator"** / **"The reference point for all your VPS needs"** | **vpspricetracker.com 原文（今日 B3/B5 新站）**：同类站给自己取的品类名 |
| **"over 250,000 VPSs from nearly a hundred providers"** / **"circa 300,000 server configurations"** / **"120 VPS service providers"** | 同上原文（**同页两处规模数字不一致**：250,000 vs 300,000）。教训同 Day17：**竞品的规模数字不能当论证前提** |
| **"compiling statistics every 24 hours"** / **"prices are obtained by dividing the annual prices by 12"** / **"Discounts on yearly payment terms are incorporated in the price if available."** | 同上原文：**归一化口径自曝**——它发布的"价"是年价除以 12 算出来的，不是页面上印的价 |
| **"shared tenancy"** vs **"dedicated tenancy"** / **"1 Intel Cores (shared)"** / **"BYOL"**（Bring Your Own License）/ **"free evaluation for 180 days"** / **"IPv6 Only"** | 同上原文：买家硬需求词。`shared` 标注在核心数后表示共享核；`BYOL` = 自带授权 |
| **"in_stock=true"** / **"reliable=false"** / **"period=prefer_year"** / **"virtualization_type=kvm hv"** | 同上 URL 参数原文：**英文站把筛选条件写进 query string** 的标准做法（与我们库里 0 个 `?` 形成对照） |
| **"Kimsufi/Soyoustart/OVH Rise New Price"** | **LowEndTalk 原文（今日新增，本轮唯一一条讲"涨"的社区标题）**：`Rise New Price` 是社区涨价帖的固定简写 |
| **"Black Friday 2026 - Wishlist Thread"** / **"[Early Black Friday Sale] VPS & Dedicated Server Deals \| Starting at Just €18/Year!"** | LET 原文（今日复现）：`Wishlist Thread` = 旺季固定格式；方括号 = 活动类型标签 |
| **"DeluxHost.net \| VPS Restock \| Improved Storage Servers! \| Z / T / Q \| Highly DDoS Protected \| NL"** | LET 原文（今日复现）：`Restock` = 补货；`Z / T / Q` = 机房区段代号 |
| **"25G Unmetered 30% lifetime discount - Dedicated Servers"** / **"[UK] VirexNode Halloween Sale … £1.25/mo recurring"** | LET 原文（今日复现）：`Unmetered` = 端口不限量；`recurring` 跟在价格后 = 每周期同价 |
| **"25 x PERPETUAL $1/Year VPS GIVEWAY !! Netfront AS4658"** / **"GIVEAWAY by AdminBolt & RackNerd! 100x FREE VPS FOR A YEAR + 20x LIFETIME LICENSES."** | LET 原文（今日复现）：`PERPETUAL` = 永久；`GIVEWAY` 是社区惯用拼错 |
| **"AxusHost Outage? All of My Servers Are Down"** / **"Incognet Kansas City Outage and WHMCS 403"** / **"DartNode Unauthorized SSH Access"** / **"DataPasa Is Scam - Avoid"** | LET 原文（今日复现）：故障 / 安全 / 跑路三类帖的固定标题格式 |
| **"PSA: RackNerd ctrl Firewall is stateless and may block outbound UDP replies"** | LET 原文（**今日新增**）：`PSA:` = 公告前缀；`stateless` = 无状态防火墙 |
| **"Introducing ServerVerify: built with the LowEndTalk community in mind"** | LET 原文（**今日新增**）：厂商/社区共建工具的发布句式 |
| **"AIO IP-Related (IPv4/IPv6/ASN) Thread. Only Providers/LIRs are allowed to post offers."** / **"[WTB] 32GB RAM, 512GB NVMe, 10Gbps Port (VPS / VDS / Dedic)"** | LET 原文（今日复现）：`LIRs` = 本地互联网注册机构；`WTB` = want to buy；`VDS` = 虚拟独立服务器 |
| **"PHP security advisory: Critical remote code execution vulnerabilities, update now (21 Oct 2026)"** | LET 原文（今日复现）：`security advisory` + `update now (<date>)` 固定格式 |
| **"Velohost Returns With Even Cheaper Prices! Get a 4GB VPS for Only 2.60€/month!"** | **LowEndBox 原文（今日复现）**：原文自曝跨期对照 `they were selling that same package for 3.00€/month. Now they're selling that same package for only 2.60€/month` —— **LEB 是人工挑两次比，我们是 113 次自动快照** |
| **"More of RackNerd & AdminBolt! Here's 50 More FREE VPS + 10 Lifetime Licenses!"** / **"all 100 VPS instances have now been given away. But apparently, 100 wasn't enough!"** | LEB 原文（今日复现）：`be given away` = 送完 |
| **"Exclusive LowEndBox Pricing: 2GB KVM VPS for $1.83/Month First Year! Godlike.Host is Back!"** | LEB 原文（今日复现）：`Exclusive <site> Pricing` = 本站专属价；`is Back!` = 厂商回归 |
| **"Early Bird Discounts on Cheap Colocation! $29/Month in Phoenix from Cloudnium!"** | LEB 原文（今日复现）：`Early Bird` = 早鸟价 |
| **"Halloween VPS @ Frankfurt Equinix \| from €7.26/mo \| IPv6 EPYC €31/year and more"** | **LEB 侧栏 LET 最新 offer 原文（今日新出，Oct 23, 2026）**：`@ <机房>` 是机房标注写法；`from` = 起价 |
| **"Instant setup, automatic RPKI ROA, rDNS, and WHOIS changes - Free /48 IPv6 for everyone - IPYE.com"** | LEB 侧栏原文（今日复现）：`Instant setup` / `RPKI ROA` / `rDNS` / `/48 IPv6` |
| **"Stores change prices constantly, and change them again during sales. A product marked 60% off can be more expensive than it"** | **pricehistory.app（Google Play）原文（今日 B3）**：零售侧"价格历史"品类的成熟说理。**VPS 侧无对应物**，是 A2 的背景句 |
| **"How often is this updated? The scraper and the site rebuild run on a schedule, every 6 hours. Every page carries the exact UTC timestamp of the fetch it was built from"** | **vpsticker.com 原文（今日 B8，首次拿到完整句）**：解释"我何时抓的"，**没解释"我抓到的东西本身多旧"**——A2 的对照句 |
| **"No expiry listed"** / **"Last verified April 29, 2026"** / **"Last verified May 2, 2026"** | domainhostcoupon 原文（今日 B8 复现）：券站承认无到期日的写法；**2026 年 10 月仍挂着 4/5 月的核验日** |
| **"went up across the board"** / **"raising prices / raise prices / a price increase"** | **bilibili 英文学习页原文（今日 B6）**：母语涨价搭配。**注意：B6 实测 VPS 语境英文位 0 条，此词只作 C 栏素材，不作标题** |

### 明日候选

1. **"€58.70 Became €65.70": The Second Time a VPS Price Moved, It Went Up** — A1（113 次扫描里**第一次观测到价格上升**：`2026-10-23T06:50:54Z`、`€ 58.70 → € 65.70`、**+7.00**；`58.70` 活了 **10 次扫描 / 1 天 23 小时 59 分 31 秒**）+ A4（**毛波动 16.00、净变化 −2.00，87.5% 互相抵消**；当前值比观测最低值高 **11.9%**）+ A5（**111 字符里只有 5 个字符变过**，前缀 85 字符自 scan #28 起 **12 天 0 小时 14 分 48 秒**一字未变 → 动的是金额，而金额由"场上最便宜的那台"决定 → **涨价不是厂商改价，是最便宜的那台被买走或下架了**）+ 外部对照（**五份英文资料口径 100% 一致只讲"降"**：baremetalindex `fall automatically over time`、thetruestack `drops steadily every few hours`、achromatic `descending-price (Dutch) auction`、topsitehosters `drop over time until someone claims`、valebyte `gradually decreases`）+ **厂商自相矛盾**：同页标语 `Prices drop & excitement mounts.` 与同页数字 `€ 65.70` 并存，而同页四步操作写的是 `Keep an eye on price changes.`（中性）+ C 栏（baremetalindex `Was / Now / Drop` / `Real movements, not marketing` / `Latest price vs 30-day high, from daily snapshots`）。**缝：要说"它涨了"，必须先有第二个方向可比较——即至少 3 个值、2 次变化；只发布当前状态的站永远只有 1 个值、0 个方向。要说"标语与数字打架"，必须标语和数字来自同一次 HTTP 读取（我们 `fetched_at` 秒级，标语与数字同一秒）。** hardest 的部分是同时承认：**我们 113 次扫描里只有 18 行有钱（2.67%），这条"涨了"的结论建立在 3 个数字上。**
2. **Two Sites, One Auction, Two Different Time Series** — A2（**第一次出现真正做价格历史的竞品 baremetalindex.com/deals**，它 `capture a daily snapshot of every tracked dedicated-server plan's price into a time-series database`、`latest price versus its 30-day high`、**只有 `Drop` 一栏（−23%/−12%/−6%/−6%/−5%），数据结构里没有"涨"的位置**）+ 粒度对照（**它逐台机器**：`Hetzner Intel Xeon E5-1650V3 · 128 GB RAM · 512 GB FSN1-DC13 $195 $151/mo -23%`；**我们逐页聚合行**：`Starting at € 65.70 per month, excl. VAT`，113 次扫描、中位间隔 278.6 分钟）+ A4（我们两个方向都记，毛 16.00 / 净 −2.00）+ B5（vpspricetracker 自曝 `prices are obtained by dividing the annual prices by 12`——**它的"价"是算出来的**；同页规模数字 250,000 vs 300,000 自相矛盾）+ B3（零售侧 pricehistory.app `Stores change prices constantly… A product marked 60% off can be more expensive than it` 已成成熟品类，**VPS 侧空白**）。**缝：把"同一厂商、同一拍卖、两种序列化对象"并排写出来，需要同时读过对方 methodology 页与我们 113 次快照。更难的是它逼我们自曝粒度劣势——我们只有 1 行，它有 250,000 行；我们的补偿是 4.64 小时中位间隔 vs 它的 daily，以及两个方向 vs 它只有跌。** 这一点必须明写，不能绕。
3. **The Refurbished Auction Floor Is Now €6.70 Above the New-Server Floor** — A3（同次抓取 `hetzner.com/hosting/` 上 7 行 `Starting at`：**Server Auction `€ 65.70`** vs **Dedicated Server `€ 59.00`**，翻新比全新贵 **+6.70 = +11.4%**；另有 Cloud 5.99 / Managed 34.00 / Web hosting 1.60 / Storage Share 4.29 / Storage Box 3.20 / Custom Solutions `on demand`）+ A5（**我们 18 天 113 次扫描只存了这 7 行里的 1 行**——另外 6 行连"见过"的记录都没有，因为 schema 只有 provider/title/offer_url/source_url/fetched_at 五列，且抽取只取匹配拍卖模式的那一句）+ A4（当前值比 10-21 观测最低值 `58.70` 高 **11.9%**）+ C 栏（hetzner.com/hosting/ 七行原文 + `on demand` + `Reduction in: 00:26:17`）。**缝：这是一个必须"同一分钟读同一页的两行"才看得见的反转**，而 deals 站的默认动作就是把每个产品单独成条、按价格排序——一旦打散，这个关系就消失了。**自曝点最硬：那 6 行一直在那一页上，我们一次都没存。** 可复用的写法：把同页 7 行原样排成一列，标出我们存的那一行，其余 6 行留白。

已用：`compare-vps-deals-total-cost`（10-07）、`vps-deals-renews-at-x`（10-08）、`vps-deals-refund-window`（10-09）、`vps-deals-cost-per-gb-ram`（10-09）、`vps-deals-who-collects-vat`（10-09）、`vps-deals-hourly-to-monthly`（10-10）、`vps-deals-cost-per-gb-disk`（10-11）、`vps-deals-auto-renewal-notice`（10-12）、`vps-deals-port-25-smtp-blocked`（10-13）、`vps-deals-sla-credit-how-to-claim`（10-14）、`vps-deals-payment-methods-accepted`（10-15）、`vps-deals-identity-verification-kyc`（10-16）、`vps-deals-nonpayment-suspension-deletion`（10-17）、`vps-deals-data-kept-after-cancel`（10-18）、`vps-deals-wrong-datacenter-move`（10-19）、`vps-deals-bandwidth-overage-throttled-or-billed`（10-20）、`vps-deals-can-you-keep-your-ip-after-delete`（10-21）、`vps-deals-block-storage-price-per-gb`（10-22）、**`vps-deals-snapshot-cross-region`（10-23，最后一篇已发布，取自 gap-ledger #16 而非 line3 候选）**。

已降级/不再写第二篇：退款天数（已发）、每 GB 单价（已发）、renews at 换算（已发）、Hourly ×672/730（已消耗）、CPU steal 诊断（英文位占满）、过期 deal（pennyclouds 已占）、Unmetered Port Metered Reality（Day2）、Stuck in an AI Support Loop（Day3）、低价套餐断货/候补（Day6）、Hetzner 拍卖"怎么运作"（Day6）、黑五"预热期填不出价格"（Day8，已改写）、"deals 站都会撑满库存"（Day10 证伪）、"Flash Deals vs Evergreen Listings"（Day10 #3，Day11 降级）、"折扣不结束"措辞（Day13 降级）、"挂来源 + 定时 + 承认读不到"作为差异化卖点（Day13 已降，Day14 再确认）、"deals 站多久更新一次"单独成题（Day13/Day15 两次 0 条，降级为佐证）、"A VPS Black Friday Site Still Says 2024"（Day14 #3，已作废）、"out of stock / back in stock" 单独成题（Day16 B6 降级）、「We Check 8 Official Pages Every 4 Hours…」（Day15 #2，Day17 降级）。

**今日修正（重要，三条）**：① **Day17 A1/B4 隐含的"没人把 `Starting at` 这一行当时间序列"今日必须改写**——**baremetalindex.com/deals 已经在做真正的价格历史**（`time-series database`、`daily snapshot`、`vs 30-day high`、`Updated 2026-10-23`）。**正确说法改为：已有竞品在做价格历史，但它是逐台机器 + daily + 只显示跌；我们是逐页聚合行 + 4.64 小时中位 + 两个方向。差异在对象与口径，不在"有没有人做"。** ② **Day16 #1「€67.70 Became €58.70」与 Day17 #1 的事实基础都已被第二次变化覆盖**：现在是 `67.70 → 58.70 → 65.70`。**任何只讲"第一次变化"的标题今天起都过期**，必须改成"第二次变化，而且方向相反"。③ **"荷兰式降价"这个说法今天被五份英文资料 100% 一致地复述**（baremetalindex FAQ / thetruestack / achromatic / topsitehosters / valebyte），**它不是我们的发现，是行业共识**。我们的独家只能是**对它的第一次反证**（涨了），不能是"我来告诉你它是荷兰式拍卖"。

**Day17 三条候选复检（全部未被 10-23 文章消耗，10-23 取的是 gap-ledger #16）**：①「"68% Off" and "67% Off" Are the Same $6.49」（Day17 #1）——**仍在**，今日 B4 新增 **HK 页（¥）** 使区域页达 **4 个币种区**（US `$` / AE `US$` / AU `A$` / HK `¥`），证据可再加一层；但本轮候选 #1 更硬（有真实价格变化），**建议先取 #1，此条留作次日**；②「The Median Deal on Our Index Is 17 Days Old」（Day17 #2）——**数字必须重算为 113 次扫描 / 18 天 18 小时 58 分**（当前 7 行：四条 113、`Claim deal` 25、`64%` 25、Hetzner 行按 offer_url 计 85；**中位 113、均值 83.9**）；③「28 Characters, 88 Scans: Three Different String Generators Feed One Table」（Day17 #3）——**仍在**，元组重算为 **4 种**：`(16,28,28,28,28)`×28、`(16,28,28,28,28,82)`×60、`(10,16,28,28,28,28,111)`×18、`(10,16,28,28,28,28,82)`×7（**注意 82 与 111 两组今日互换了次数**：带价版从 13 增至 18）。Day13 #2「No utm, No ref, No "?"」——**仍是最稳的一条**，行基数应重算为 **675 行**（113 次扫描逐次累加）。YABS 怎么读（Day4 #3）**维持移出候选池**。**gap-ledger 提醒：可用未写剩 4 条（#17–#20），下一步取 #17；line3 候选是 gap-ledger 写完后的回退池，不是当前取题源——两套不要混。**
