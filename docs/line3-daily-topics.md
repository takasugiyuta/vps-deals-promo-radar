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
