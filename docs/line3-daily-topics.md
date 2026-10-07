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
