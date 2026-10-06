# 第 8 步对标记录（第 10 步 28 天周期内锁定）

记录日期：2026-10-06
锁定周期：第 10 步 28 天日更周期内不更换

## 锁定项

| 项目 | 值 | 状态 |
|---|---|---|
| 核心词 | `vps deals`（英文，美区） | 锁定，一个字不改 |
| 对标一 | lowendbox.com | 锁定 |
| 对标二 | namecheap.com | 锁定 |
| 对标三 | liquidweb.com | 锁定 |

## 选型理由

- **lowendbox.com**：本次抓取中唯一有两条自然结果进首页的站（首页 + Best Cheap VPS Hosting 榜单文），必须拆。
- **namecheap.com**：代表厂商页写法，学它怎么在第一屏给答案。
- **liquidweb.com**：榜单型文章（The 7 Cheapest VPS Hosting Providers for 2026），和「每天一篇」的主线形态最接近。

## 明确排除

| 域名 | 排除原因 |
|---|---|
| reddit.com | 论坛，不是站 |
| godaddy.com | 巨头大厂，量级不对等 |
| contabo.com | 本站已有 `/contabo-coupon-code` 落地页，属自家页 |
| us.ovhcloud.com | 品牌自家页 |
| digitalocean.com / hostinger.com | 品牌自家页 |

## 数据出处

- 抓取时间：2026-10-06
- 抓取方式：本机 Chrome（独立 profile）经 CDP 读取 `google.com/search?q=vps+deals&hl=en&gl=us&pws=0` 自然结果
- 结果：第一页真实自然结果 9 条（广告、视频、People also ask 不计）

| 名次 | 域名 | 页面标题 |
|---|---|---|
| 1 | lowendbox.com | LowEndBox - Cheap VPS, Dedicated Servers and Hosting ... |
| 2 | reddit.com | Virtual Private Server (VPS) Discussions |
| 3 | us.ovhcloud.com | VPS - Your virtual private server in the cloud |
| 4 | contabo.com | The Best Value Cloud VPS On Earth |
| 5 | namecheap.com | Cheap VPS Hosting Services - Managed Virtual Servers at ... |
| 6 | netcup.com | Permanently Affordable VPS Offers |
| 7 | liquidweb.com | The 7 Cheapest VPS Hosting Providers for 2026 [Updated] |
| 8 | godaddy.com | VPS Hosting \| A Managed Virtual Server Solution for Pros |
| 9 | lowendbox.com | Best Cheap VPS Hosting - Updated September 2026 |

## 附带结论

- 本站 PROVIDERS 清单里的 Hostinger / Hetzner / DigitalOcean / Vultr / Linode 无一家进入该核心词前十，硬碰不现实，对标须避开自家 provider。
- reddit 为论坛，按 NON_GOALS 不计入对标候选。
