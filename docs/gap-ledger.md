# 缺口台账（DAILY 取题的唯一来源）

> 缺口来自 `BENCH-对标表-vps-deals-2026-10-09.md`：TOP3 三站各读 10 篇共 30 篇实读后得出。
> 规则（对应 STEP:10 DAILY 模块 `[NEVER] 同一个缺口写两篇`）：
> 1. 每天只取**状态为「未写」且序号最小**的那一条。
> 2. 写完把状态改成「已写」，填上 slug、线上 URL、日期、commit。
> 3. 状态是「缺数据」的不许取——它需要先补抓取能力，取了就只能编数，违反永久边界。
> 4. 全部写完或可用条目耗尽时，回来重跑 BENCH 补新缺口，不许自己造词、不许自己估量。
> 5. 核心词 `vps deals` 和 TOP3（lowendbox / namecheap / liquidweb）本周期内锁定，不换。
>    换了对标，28 天后三个数没法跟上期比。
> 6. **28 天周期：2026-10-09（首篇）→ 2026-11-05（第 28 天），2026-11-06 出数**（索引数 / 点击 / 平均排名）。
>    每天至少一篇，断一天周期就白跑。取题顺序：本表 → 写完回跑 BENCH → 再不行才动 `docs/line3-daily-topics.md`。

---

## 方法铁律（2026-10-09 owner 拍板，照做，不要自作主张改）

1. **不换 UA、不绕反爬。** 遵守 `.ilang/site.ilang` 的 `::RULE{no login, bypass, or anti-bot evasion}`。遇到 Cloudflare 挑战 / 403 / 安全检查就停手，不要伪装成浏览器、不要换出口、不要用任何绕过手段。
2. **读不到就写 `not verifiable`。** 把"这家我核不到"如实写进文章，并说明原因（页面返回挑战 / 只返回导航壳 / 安全检查）。**这本身就是独家内容**——每篇榜单文都跳过这点，因为没数字就排不进表。绝对不许用记忆里的数、不许用别处看来的数、不许估算补位。
3. **不给 `scraper.py` 加字段。** 它源码注释写着 `no invented deal or price fields`，这是对的。加解析器 = 往库里塞推测值，撞 `::BOUNDARY{never:invent offers prices discounts expiration dates or commissions}`。
4. **独家数据走「人工读官方页 + 算」。** 除法、公式、横向对比，全部基于页面上明文印着的数字，算式写进文章里让读者能复算。已验证这条路走得通：单位价格、续费价两个缺口都是这么做出来的，不需要改一行抓取代码。
5. **每条数字挂真实可访问的官方链接**，至少 2 条。不抄对标站的说法。
6. **写完必须回填本文件**（状态 / slug / URL / 日期 / commit），否则第二天会重复写同一个缺口。
7. **发稿前先探源，不许先写再找来源。** 跑 `python C:\Users\y\WorkBuddy AI\Claw\scripts\probe_sources.py <url列表>` 直连试读：403 / 被反爬挡的官方页就写 `not verifiable`。
   **`r.jina.ai` 这类代理只能用于 BENCH 缺口分析（找题目），不许用来给文章取数**——拿代理绕过 Cloudflare 取来的价，本质上就是绕反爬，违反第 1 条。
8. **每篇至少 3 条「竞品 30 篇零命中」的独家事实。** 判法：把文章拆成可核对的事实条目，逐条到 BENCH 那 30 篇竞品正文里跑正则，零命中才算独家（命中在厂商自家页 / 评论区的，按口径 B 另算，不算竞品覆盖）。脚本在本机 workspace `scripts/exclusive_audit.py`，结果示例见 `outbox/独家清单与独家比例-2026-10-09.md`：2026-10-09 三篇实测 29/33 = 87.9%。**注意正则里的 `|` 必须用 `(?: )` 包住**，否则会把表达式拆开产生假阳性（我第一次跑成 45.5% 就是这么错的）。

---

## 可用（按顺序取，取完一条划一条）

> 这三条的写法：**人工逐家读官方页面，每条数字挂真实可访问的官方链接**。不许抄对标站的说法，不许从 `data/offers.json` 推——库里没有价格字段，推出来就是编。

| # | 缺口 | 依据（30 篇扫描） | 独家料来源 | 状态 | slug | 线上 URL | 日期 | commit |
|---|---|---|---|---|---|---|---|---|
| 1 | **退款天数**：每家到底几天包退，不是"各家不同" | Liquid Web 只写 "Money-back guarantee varies based on product"，没给任何一家具体天数 | 逐家读官方退款/条款页，挂真实链接 | 已写 | vps-deals-refund-window | https://lumafare.com/articles/vps-deals-refund-window/ | 2026-10-09 | 65118a5 |
| 2 | **VAT/GST 谁代收**：付款方式决定税由谁收 | 三站正文零覆盖；只有 RackNerd 的人在 LowEndBox 评论区答过一次：信用卡付款不代收，PayPal 由支付方代收代缴 | 逐家核官方结算/条款页 + 已抓到的评论区原话作旁证 | 已写 | vps-deals-who-collects-vat | https://lumafare.com/articles/vps-deals-who-collects-vat/ | 2026-10-09 | 9747359 |
| 3 | **按小时计费折月**：$0.007/hr 到底等于多少钱一个月 | Liquid Web 产品页给小时费率 $0.007–$0.245，不折算，也不和包月比。**2026-10-09 实测更正见下** | ⚠️ **别用 ×730**（原写法，错）。DO 官方 FAQ 原话：*"Bundled Plans have a monthly cap, so you'll never pay more than the flat monthly price for that plan. v5 Droplets are billed on actual hours used each month and are not capped at 672 hours."* 定价表 hourly×**672**=monthly（0.00595/$4、0.00893/$6、0.01786/$12、0.02679/$18、0.03571/$24、0.07143/$48、0.14286/$96，七档比值全为 672）。**×730 会高估 8.6%**。独家点：网上流传的折月口诀是错的，官方自己的封顶是 672 小时（28 天）；且 v5 Droplets **不封顶**，用满 730 小时的月份会超出月价。来源可读：DO pricing 页 200（小时价与月价同表）。Hetzner docs 客户端渲染抓不到数、Liquid Web / Vultr 均 403 → 一律写 not verifiable，不许用代理取来的数 | 已写 | vps-deals-hourly-to-monthly | https://lumafare.com/articles/vps-deals-hourly-to-monthly/ | 2026-10-10 | 7e2d180 |
| 4 | **存储单价 $/GB 磁盘**：NVMe 和 SSD 到底差多少钱 | 18 篇把 NVMe / SSD 当标签贴，**0 篇给任何 per-GB 价格**（`per/$ N per GB of disk/storage` 命中 0/30，与「单位价格」那篇的扫描一致） | 月价 ÷ 磁盘 GB，逐档算 $/GB 磁盘。**来源已探通**：DO pricing 页 200（磁盘 GiB 与月价同表）、Hostinger vps-hosting 200 | 未写 | | | | |
| 5 | **取消要不要提前通知 / 自动续费开关** | **0/30 篇提到**（`cancel + notice` / `notice of termination` 零命中） | 逐家核条款里的通知期 + 自动续费默认开还是关。**来源已探通**：DO ToS 200、Hostinger legal 200、Hetzner 条款页 200 | 未写 | | | | |
| 6 | **端口 25 / SMTP 能不能发信**：买了 VPS 能不能自己发邮件 | **0/30 篇提到**（`port 25` / `SMTP` 零命中）。自建邮局、WordPress 发信的真实卡点，三家完全空白 | 逐家核官方文档：默认封不封 25、能不能申请解封。**✅ 2026-10-10 解锁**：`docs.digitalocean.com/support/why-is-smtp-blocked/` **200**（Last verified 13 Jul 2026），官方原话 *"SMTP ports 25, 465, and 587 are blocked on Droplets... This block applies to all Droplets by default and includes traffic passing through a Reserved IP address."* 原记"两个 URL 都 404"已作废 | 未写 | | | | |
| 7 | **SLA 赔付怎么拿**：停机多久赔多少、要不要自己提工单 | 30 篇里 8 篇给 uptime 百分比（99.9% / 100%），**0 篇讲赔付规则**——`credit + downtime / outage` 组合命中 0/30 | 给「停机时长 → 赔付比例」表和申请时限。**✅ 2026-10-10 解锁**：`digitalocean.com/sla` **200**（从 billing docs 页导航里挖到的真地址，此前试的三个 `docs.digitalocean.com/*` 路径全是 404）。Hetzner SLA 仍 404，只有 hetzner.com/legal/terms-and-conditions 200 | 未写 | | | | |
| 8 | **付款方式矩阵**：每家到底收什么钱，加密货币能不能退 | 12 篇提到付款方式（PayPal / crypto / iDeal），**0 篇给清单或数字** | 逐家列官方结算页支持的付款方式 + 加密货币付款的退款后果。**注意别和 VAT 那篇重复**：那篇讲税由谁代收，这篇只讲方式与退款。**✅ 2026-10-10 部分解锁**：DO billing docs 200 给了清单原话 *"credit card, debit card, crypto wallet, third-party provider (like PayPal, Google Pay, or Apple Pay), or a bank account"*。Namecheap / Liquid Web / Vultr 仍 403 | 未写 | | | | |

> **排序理由（2026-10-09 调整）**：4、5 提到 3、4 前面，是因为它们的官方来源**今天实测直连 200**；6、7、8 的条款页今天全是 404 / 403，取题前必须先探源。见下面「来源可读性实测」。

### 来源可读性实测（2026-10-09 16:30 GMT+8，本机直连，未换 UA、未走代理）

| 官方页 | 状态 | 能取到什么 |
|---|---|---|
| `digitalocean.com/pricing/droplets` | **200** | 小时价 + 月价同表（七档），磁盘 GiB、vCPU、流量全有。**目前最好用的数据源** |
| `digitalocean.com/legal/terms-of-service-agreement` | **200** | 条款正文 |
| `hostinger.com/vps-hosting` | **200** | 套餐配置与价格 |
| `hostinger.com/legal/refund-policy` | **200** | 退款条款（带修订日期） |
| `hetzner.com/legal/terms-and-conditions/` | **200** | 条款正文 |
| `docs.hetzner.com/*` | 200 但**客户端渲染** | 抓不到数字，等于不可用 |
| `namecheap.com/*` | **403**（昨天还能读，今天被挡） | 不可用 |
| `liquidweb.com/*` | **403** | 不可用 |
| `vultr.com/pricing` | **403** | 不可用 |

**结论**：今天真正能喂文章的一手来源只有 DO（定价 + 条款）、Hostinger（定价 + 条款）、Hetzner（条款）三条线。
这直接决定了 28 天能写什么——**算得出来的（除法、换算、比值）优先，需要逐家条款的缺口排在后面且先探源**。
可读性会变（Namecheap 就是一天之内从能读到 403），每次取题前重新探，不要拿这张表当永久结论。

### 2026-10-10 复探（GMT+8 上午，本机直连，未换 UA、未走代理）

| 官方页 | 状态 | 变化 / 能取到什么 |
|---|---|---|
| `digitalocean.com/pricing/droplets` | **200** | 仍是最强数据源：`$/hr` + `$/mo` + 磁盘 GiB + vCPU + 流量同表，Shared 7 档 + CPU-Optimized 6 档 + General Purpose 6 档共 19 组 |
| `docs.digitalocean.com/platform/billing/` | **200** | **新增可用**：billing cycles 按 calendar month；付款方式清单；"Last verified 7 Oct 2026" |
| `docs.digitalocean.com/support/why-is-smtp-blocked/` | **200** ⬆️ | **昨天 404，今天通**。封 25/465/587，含 Reserved IP |
| `digitalocean.com/sla` | **200** ⬆️ | **昨天记 404，今天通**（真地址，从 billing docs 导航挖出） |
| `digitalocean.com/legal/terms-of-service-agreement` | **200** | 条款正文 |
| `hostinger.com/vps-hosting` | **200** | 套餐配置与价格（KVM 1/2/4，含磁盘 GB 与续费价） |
| `hostinger.com/legal/refund-policy` | **200** | 退款条款 |
| `hetzner.com/legal/terms-and-conditions/` | **200** | 条款正文 |
| `hetzner.com/cloud` | 200 但**客户端渲染** | 价格是占位符，抓不到数 |
| `namecheap.com` | 403（脚本）/ 可读（普通取回） | 首页 VPS 卡可读到 $3.88/mo、$46.56、续费 $58.56/yr |
| `liquidweb.com/vps-hosting/packages/` | **403** | 仍不可用 |
| `vultr.com/pricing` | **403** | 仍不可用 |
| `docs.digitalocean.com/platform/billing/payment-methods/` | **404** | 子路径不存在，付款方式看 billing 总页 |

**技巧（2026-10-10 发现）**：DigitalOcean 文档站每个页面都有 Markdown 镜像——把路径末尾换成 `index.html.md` 即可直取纯文本（实测 `docs.digitalocean.com/support/why-is-smtp-blocked/index.html.md` 200，2.3 KB），比正则剥 HTML 干净得多，后续取数优先用它。导航里的真实链接也可以从页面 `href` 里正则挖（SLA 地址就是这么找到的）。

---

## 缺数据（不许取，取了只能编数）

| # | 缺口 | 卡在哪 | 解锁条件 |
|---|---|---|---|
| A | ~~**单位价格**：$/GB 内存、$/vCPU~~ **已写，2026-10-09** | 原判断"必须等 scraper 加字段"是错的 | 走**人工读官方定价页 + 算除法**就够：slug `vps-deals-cost-per-gb-ram`，线上 URL https://lumafare.com/articles/vps-deals-cost-per-gb-ram/ ，日期 2026-10-09，commit 16f8d3b，线上 200。三站 30 篇零命中，这篇是全站第一个把这个数算出来的 |
| B | **续费价**：促销价到期后到底付多少 | **已被 2026-10-08 那篇覆盖**（`vps-deals-renews-at-x`）：人家是人工读官方 plan card + 算公式（`renewal increase = d/(1-d)`）做出来的，不靠抓取字段。证明这条路走得通，我原先标"缺数据"标错了 | 不要再写第二篇。要深挖就换角度（比如"同一张卡 12 个月后的实际账单"），别重复同一个公式 |
| C | **带日期的价格涨跌时间线** | `data/offers.json` 有 60 次提交的时间线，但每次只记链接存废，不记价格 | 同 A。这条是三家都没有的独家角度，价值最高，建议优先解锁 |
| D | **优惠码存废带日期**（原列在可用里，已撤下） | **实测证伪**：git 历史里唯一的"消失"事件是 2026-10-04 一次异常采集——4 条 `KVM 1/2/4/8 VPS — 67%/63%/70%/65% off` 出现一次后不见，但相邻两天的 `70%/67%/63%/65% off — Hostinger VPS page` **百分比完全相同**，是标题写法变了，不是码死了；同一天 `Student discount` 也短暂消失又回来，同一原因。**至今零个真实失效事件** | 要么等真的出现失效事件，要么先把 C 解锁（有价格才有得比） |
| E | **Windows 授权费含不含** / **自管 vs 托管溢价** | 样本不够：5 个 provider 里只有 Hostinger、Hetzner 抓得到（见下），DigitalOcean 能读但产出 0 条；Vultr / Linode / Contabo 全部抓不到 | 先把 provider 可读性修好（见下），至少要有 4–5 家同配置可比 |

---

## 数据底座现状（2026-10-09 实测，这条决定了上面能写什么）

- `data/offers.json` 最新一次扫描（2026-10-08T13:05:21Z）的 source_checks：
  - ✅ Hostinger、Hetzner、DigitalOcean（但 DO 产出 0 条 offer）
  - ❌ Vultr、Linode (Akamai)、Contabo（3 个 URL 全失败）
- 实际产出：**5–6 条 offer，全部来自 Hostinger，加 1 条 Hetzner（10-08 起）**。09-24 → 10-08 数量一直是 5，稳定得可疑。
- 本机实测原因：Linode 和 Contabo 的 robots.txt **允许**抓取，但页面返回 **403**——是服务端拦 bot（`VPSDealsRadarBot/1.0` 这个 UA 或机房 IP）。CI 上同样失败，不是本机个例。Vultr 在我这是 SSL 证书链问题（本机有拦截代理），CI 上也失败，原因待查。
- **修不修、怎么修，要你拍板**：换成浏览器 UA 有可能通，但 `.ilang/site.ilang` 里写着 `::RULE{check robots.txt; no login, bypass, or anti-bot evasion}`，伪装 UA 绕 403 算不算 evasion 是边界问题，我不替你决定。

---

## 变更记录

- 2026-10-09 建表。可用缺口来自 BENCH 30 篇实读扫描；缺数据条目单列，明确不许取。
- 2026-10-09 修订：#1 优惠码存废经实测证伪，从「可用」撤到「缺数据 D」；Windows 授权费、自管溢价两条因 provider 样本不足撤到「缺数据 E」。可用条目从 6 条减到 3 条。
- 2026-10-09 第二次修订：① 退款天数已发（`vps-deals-refund-window`，commit 65118a5，线上 200）；② B 号续费价改标为已被 10-08 那篇覆盖——人工读官方页 + 算公式就行，不需要抓取值段，我上一版标错了；③ 由此得出一条方法结论：**A / C 也可以走"人工读官方页 + 算"这条路，不必等 scraper 加字段**。
- 2026-10-09 第三次修订：A 号单位价格已发（`vps-deals-cost-per-gb-ram`，commit 16f8d3b，线上 200），方法证明确实不用改代码。
  - 算出来的硬事实（2026-10-09 读官方页）：入门档每 GB 价格 Hostinger 促销 $1.62 / Namecheap 年付折算 $3.88 / DigitalOcean $6.00，**差 3.7 倍**；
  - Hostinger 续费后单位价涨 1.67x–2.23x（KVM 4 最狠），入门档续费 $3.00/GB 已经逼近 Namecheap 年付价；
  - Hostinger KVM 4 和 KVM 8 促销期**单位价完全相同**（$0.81/GB、$3.25/vCPU），买大不打折；
  - **DigitalOcean 2GiB/2vCPU $18 是 $9.00/GB，比它正下方的 4GiB/2vCPU $24 的 $6.00/GB 还贵 50%**，同为 2 vCPU、内存翻倍、单价更低——这条是全篇最硬的"别买这个配置"。
  - Hetzner / Vultr / Linode / Contabo 定价页今日机器不可读，如实写"未核到"，没编数。
- 2026-10-09 第四次修订：2 号 VAT/GST 代收已发（`vps-deals-who-collects-vat`，commit 9747359，线上 200）。硬事实（2026-10-09 读官方页）：
  - **付款方式决定税，机制是"地址"不是"通道"**：DigitalOcean 官方写明 tax location "initially set to the payment address of your primary payment method"；Hostinger 把国家下拉框**放在付款方式那一步**（"Before submitting the payment, select your country"）。评论区流传的"信用卡不代收 / PayPal 代收"在所有读到的官方页里都找不到依据。
  - **代收方有四种**：厂商 / 市场卖方 / 你自己 / 无人代收。DigitalOcean Marketplace 的 Responsibility 表里 **20 个辖区中有 4 个（日本 JCT、沙特、瑞士、UAE）是 Vendor 收，不是 DigitalOcean**；坦桑尼亚 18% VAT 之外另有 **15% 预提**，由企业自己扣缴，"与 VAT 是两笔"。
  - **同一台 $6.00/mo Droplet，按 DO 自己公布的 39 个辖区税率折出来是 $6.30（UAE 5%）到 $7.62（匈牙利 27%），同一资源差 21%**；且 EU 有 VAT ID 就归零——27% 不是匈牙利的性质，是你有没有填那个表单的性质。
  - **两家同一天公布的 EU 税率互相打架**：爱沙尼亚 DO 24% / Hetzner 22%，卢森堡 16% / 17%，罗马尼亚 21% / 19%；南非 DO 15.5% / Hetzner 15%。都是官方页面原话，不判谁对，只提醒看账单不看表。
  - **Hostinger 的坑**："Due to taxes being forwarded automatically, the VAT already applied to an invoice cannot be refunded" + "Invoices already issued will remain unchanged"——VAT ID 必须在付款前填，买 24 个月促销再补，第一个月的税永久拿不回。
  - 三站实测零覆盖：LowEndBox 欧元价无任何税标注；Liquid Web 包月页只有 "predictable pricing" 这种空话；Namecheap 公开 KB 里**根本没有税率表**。
- **2026-10-10 第五次修订：3 号「按小时计费折月」已发**（`vps-deals-hourly-to-monthly`，commit 7e2d180，线上 200，Actions run 38016571718 两 job 全绿）。硬事实（2026-10-10 直读官方页）：
  - **19 组 DO 官方定价对全部整除 672**，不是 730。$/mo ÷ $/hr 在 Shared 七档、CPU-Optimized 六档、General Purpose 六档上全是 672.0（含 $1.87500/$1,260.00 这种大档），不是四舍五入巧合。
  - **×730 到底是错还是对，取决于有没有 cap**：DO 官方原话 *"Bundled Plans have a monthly cap... v5 Droplets are billed on actual hours used each month and are not capped at 672 hours"*。×730×12 = 8,760 = 365 天全年小时数，所以 **×730 对不封顶的 v5 是对的，对封顶的 Bundled 高估 8.63%**（730÷672−1，每档恒定）。此前台账只写「别用 ×730」，口径过粗，本条更正为按 cap 分岔。
  - **672 就是二月**：DO billing 文档写明 *"billing cycles are monthly... over the course of the calendar month"*，2026 非闰年 → 31 天月 744h、30 天月 720h、二月 672h。封顶套餐全年跑满实跑 8,760h 只计 8,064h，**白送 696 小时 = 29 天**；31 天月实际时薪 $4.00/744 = $0.005376，比页面标价 $0.00595 低 9.68%。**页面上的 $/hr 是二月价，也就是它一年中最贵的一档**。不封顶的 v5 拿不到这 696 小时。
  - 三家第一屏实测（2026-10-10）**都不做单位换算**：LowEndBox 把 `$12/Year` 和 `€3.49 / Month` 混排从不折算，"Hourly Billing" 只作为标题标签出现一次、无费率无换算；Namecheap 卡面 $3.88/mo「Billed yearly」+ $46.56 + 续费 $58.56/year，数字成对出现但从不写那句解释；Liquid Web 包月页三个档只有 /mo + 小字年续费，全程无小时价。
  - **没有小时价的套餐不该做小时换算**：Hostinger VPS 页（200）只给 KVM 1 $6.49/mo / KVM 2 $8.99/mo / KVM 4 $12.99/mo 与 2 年续费价，全文零小时费率。Liquid Web、Vultr 今日直连 403，Hetzner Cloud 价客户端渲染抓不到 → 一律 not verifiable，未用代理/缓存补数。
  - 独家闸门：28 条事实条目 / 26 条零命中 / **92.9% PASS**（要求 ≥3）。
- **2026-10-09 21:00 兜底核对**：今天实际发了 3 篇（#1 退款窗口 / A 单位价格 / #2 VAT 代收），三篇线上均 200，台账均已回填且三篇都过了独家闸门（3/5、28/32、23/28）。
  **2026-10-10 更新：#3 已写，可用条目还剩 5 条：#4 存储单价、#5 取消通知/自动续费、#6 端口 25、#7 SLA 赔付、#8 付款方式矩阵**（原"还剩 6 条"是 10-09 口径，以本行为准）。
  取题顺序仍是**序号最小优先**：下一步取 **#4 存储单价 $/GB 磁盘**（#4/#5 来源已探通 200；#6/#7/#8 取题前必须先跑 `probe_sources.py` 复探，404/403 就写 not verifiable）。
  **6 条写完才允许**回退到 `docs/line3-daily-topics.md` 的「明日候选」，并立刻重跑 BENCH 补缺口。
