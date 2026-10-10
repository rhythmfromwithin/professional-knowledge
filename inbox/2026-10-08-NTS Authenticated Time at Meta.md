---
interest: medium
link: https://engineering.fb.com/2026/10/06/production-engineering/nts-authenticated-time-at-meta/
next_step: skim
priority: medium
slack_ts: '1791610127.128469'
source: Meta Engineering
status: unread
title: 'NTS: Authenticated Time at Meta'
---
# NTS: Authenticated Time at Meta
> 原文: [https://engineering.fb.com/2026/10/06/production-engineering/nts-authenticated-time-at-meta/](https://engineering.fb.com/2026/10/06/production-engineering/nts-authenticated-time-at-meta/)

Meta’s public time service now speaks NTS (Network Time Security, RFC 8915) at nts.meta.com. Packets are authenticated, so a device can verify the time came from us and was not modified on the way. Our NTS servers hold no per-client state. Cookie keys are derived, not stored and not replicated. We’ve open sourced everything, including [...]

[Read More...](https://engineering.fb.com/2026/10/06/production-engineering/nts-authenticated-time-at-meta/)

The post [NTS: Authenticated Time at Meta](https://engineering.fb.com/2026/10/06/production-engineering/nts-authenticated-time-at-meta/) appeared first on [Engineering at Meta](https://engineering.fb.com).
