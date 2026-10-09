# 缺口台账（DAILY 取题的唯一来源）

> 缺口来自 `BENCH-对标表-vps-deals-2026-10-09.md`：TOP3 三站各读 10 篇共 30 篇实读后得出。
> 规则（对应 STEP:10 DAILY 模块 `[NEVER] 同一个缺口写两篇`）：
> 1. 每天只取**状态为「未写」且序号最小**的那一条。
> 2. 写完把状态改成「已写」，填上 slug、线上 URL、日期、commit。
> 3. 状态是「缺数据」的不许取——它需要先补抓取能力，取了就只能编数，违反永久边界。
> 4. 全部写完或可用条目耗尽时，回来重跑 BENCH 补新缺口，不许自己造词、不许自己估量。
> 5. 核心词 `vps deals` 和 TOP3（lowendbox / namecheap / liquidweb）本周期内锁定，不换。
>    换了对标，28 天后三个数没法跟上期比。

---

## 方法铁律（2026-10-09 owner 拍板，照做，不要自作主张改）

1. **不换 UA、不绕反爬。** 遵守 `.ilang/site.ilang` 的 `::RULE{no login, bypass, or anti-bot evasion}`。遇到 Cloudflare 挑战 / 403 / 安全检查就停手，不要伪装成浏览器、不要换出口、不要用任何绕过手段。
2. **读不到就写 `not verifiable`。** 把"这家我核不到"如实写进文章，并说明原因（页面返回挑战 / 只返回导航壳 / 安全检查）。**这本身就是独家内容**——每篇榜单文都跳过这点，因为没数字就排不进表。绝对不许用记忆里的数、不许用别处看来的数、不许估算补位。
3. **不给 `scraper.py` 加字段。** 它源码注释写着 `no invented deal or price fields`，这是对的。加解析器 = 往库里塞推测值，撞 `::BOUNDARY{never:invent offers prices discounts expiration dates or commissions}`。
4. **独家数据走「人工读官方页 + 算」。** 除法、公式、横向对比，全部基于页面上明文印着的数字，算式写进文章里让读者能复算。已验证这条路走得通：单位价格、续费价两个缺口都是这么做出来的，不需要改一行抓取代码。
5. **每条数字挂真实可访问的官方链接**，至少 2 条。不抄对标站的说法。
6. **写完必须回填本文件**（状态 / slug / URL / 日期 / commit），否则第二天会重复写同一个缺口。

---

## 可用（按顺序取，取完一条划一条）

> 这三条的写法：**人工逐家读官方页面，每条数字挂真实可访问的官方链接**。不许抄对标站的说法，不许从 `data/offers.json` 推——库里没有价格字段，推出来就是编。

| # | 缺口 | 依据（30 篇扫描） | 独家料来源 | 状态 | slug | 线上 URL | 日期 | commit |
|---|---|---|---|---|---|---|---|---|
| 1 | **退款天数**：每家到底几天包退，不是"各家不同" | Liquid Web 只写 "Money-back guarantee varies based on product"，没给任何一家具体天数 | 逐家读官方退款/条款页，挂真实链接 | 已写 | vps-deals-refund-window | https://lumafare.com/articles/vps-deals-refund-window/ | 2026-10-09 | 65118a5 |
| 2 | **VAT/GST 谁代收**：付款方式决定税由谁收 | 三站正文零覆盖；只有 RackNerd 的人在 LowEndBox 评论区答过一次：信用卡付款不代收，PayPal 由支付方代收代缴 | 逐家核官方结算/条款页 + 已抓到的评论区原话作旁证 | 已写 | vps-deals-who-collects-vat | https://lumafare.com/articles/vps-deals-who-collects-vat/ | 2026-10-09 | 9747359 |
| 3 | **按小时计费折月**：$0.007/hr 到底等于多少钱一个月 | Liquid Web 产品页给小时费率 $0.007–$0.245，不折算，也不和包月比 | 拿官方页上写明的小时费率 × 730 折月，和同页包月价对比，算式写在文里 | 未写 | | | | |

---

## 缺数据（不许取，取了只能编数）

| # | 缺口 | 卡在哪 | 解锁条件 |
|---|---|---|---|
| A | ~~**单位价格**：$/GB 内存、$/vCPU~~ **已写，2026-10-09** | 原判断"必须等 scraper 加字段"是错的 | 走**人工读官方定价页 + 算除法**就够：`vps-deals-cost-per-gb-ram`，commit 16f8d3b，线上 200。三站 30 篇零命中，这篇是全站第一个把这个数算出来的 |
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
- **可用条目只剩 3 号（按小时计费折月）**。写完 3 号后，回退到 `docs/line3-daily-topics.md` 最新 block 的「明日候选」取题，并立刻重跑 BENCH 补缺口。
