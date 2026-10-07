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

已用：`compare-vps-deals-total-cost`（总持有成本对比法，2026-10-07 已发布；本站当前唯一已发布文章 slug）
