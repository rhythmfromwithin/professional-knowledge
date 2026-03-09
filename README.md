# professional-knowledge
personal knowledge base for professional knowledge to empower career growth

## Gmail 日报
- 每天 08:00 UTC 自动将 inbox 汇总发到 Gmail，Subject：`aI related blogs_researchs_VCNews`。
- 在仓库 **Settings → Secrets and variables → Actions** 中配置：
  - `GMAIL_USERNAME`：你的 Gmail 地址
  - `GMAIL_APP_PASSWORD`：Gmail 应用专用密码
  - `GMAIL_TO`：（可选）收件人，不设则发到 GMAIL_USERNAME
- 也可在 Actions 页手动运行 workflow「Send Inbox Digest Email」。

## 本地脚本
- **补全旧文章 frontmatter**（为缺少 `interest`/`next_step` 的 inbox 文章添加默认值）：
  ```bash
  python scripts/scripts/backfill_inbox_frontmatter.py
  ```
- **按 next_step 整理到精读/泛读 subbox**：
  ```bash
  python scripts/scripts/organize_inbox_by_next_step.py
  ```
  - `next_step: deep_read` → 移动到 `inbox/deep_reading/`
  - `next_step: skim` → 移动到 `inbox/skim_reading/`
