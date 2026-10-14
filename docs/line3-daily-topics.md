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
