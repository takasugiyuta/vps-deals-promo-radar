# 构建验收口径（2026-10-07 定稿）

## 为什么写这份文件

文章管线第一次空跑时，验收条件写的是「跑完 scraper.py + build.py 后，产物与 HEAD 逐字节一致（零副作用）」。
这个条件**永远不可能成立**：`scraper.py` 每次运行都会把 `source_scan_at` 推进到当前时间，
而所有页面的 `Source scan run` 时间戳和 sitemap 的 `lastmod` 都取自它，所以只要跑了抓取，产物必然变化。

那不是缺陷，是设计：这个站要向读者证明"数据是刚才核过的"。把时钟钉死反而会让页面显示过期时间。

## 定稿口径

**验收的是「构建确定性」，不是「时钟不变」。**

条件：

1. **固定输入**：不运行 `scraper.py`，只用已提交的 `data/offers.json`。
2. **跑一次** `python build.py`。
3. 产物与 HEAD 中的 `site/` 逐字节一致（Windows 工作区按行尾规范化后比对，CRLF/LF 差异不算）。
4. 三条硬指标同时成立：canonical 页面数不变（当前 11 条）、5 条 legacy `/deals/` 301 全在且锚点正确、
   sitemap 的 `lastmod` 与页面 `Source scan run` 一致。

加入文章后的增量验收：文章源放进 `content/articles/`、图片放进 `assets/` 再构建，
页面数 +N、sitemap +N、文章 URL 与 canonical 正确、`assets/` 被拷进 `site/assets/`、5 条 301 不受影响。

**不再要求**跑完 `scraper.py` 之后仍然零差异。`scraper.py` 保持现状，不为验收而改。

## 谁该读这个

任何改动 build.py / scraper.py / 文章管线的环节，验收都按这份口径来，不要再拿"抓取后 diff 非空"当失败。
