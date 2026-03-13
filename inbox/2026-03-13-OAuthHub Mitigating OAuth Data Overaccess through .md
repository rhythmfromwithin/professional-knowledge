---
title: "OAuthHub: Mitigating OAuth Data Overaccess through a Local Data Hub"
source: "cs.CR - Cryptography and Security"
link: https://arxiv.org/abs/2603.10056
priority: low
status: unread
interest: medium
next_step: skim
---
# OAuthHub: Mitigating OAuth Data Overaccess through a Local Data Hub
> 原文: [https://arxiv.org/abs/2603.10056](https://arxiv.org/abs/2603.10056)

arXiv:2603.10056v1 Announce Type: new
Abstract: Most OAuth service providers, such as Google and Microsoft, offer only a limited range of coarse-grained data access. As a result, third-party OAuth applications often end up accessing more user data than necessary, even if their developers want to minimize data access. We present OAuthHub, a development framework that leverages users' personal devices as the intermediary controller for OAuth-based data sharing between cloud services. The key innovations of OAuthHub are: (1) the insight that discretionary data access is largely unnecessary for most OAuth apps, which typically only require access at three well-defined moments-during installation, in response to user actions, and at scheduled intervals; (2) a development framework that requires explicit declarations of intended data access and supports the three common access patterns through intermittently available personal devices; and (3) a centralized runtime permission model for managing OAuth access across providers. We evaluated OAuthHub with three real-world apps on both PCs and mobile phones and found that OAuthHub requires moderate changes to the application code and imposes insignificant performance overheads. Our study with 18 developers showed that participants completed programming tasks significantly faster (9.1 vs. 18.0 minutes) with less code (4.7 vs. 15.8 lines) using OAuthHub than conventional OAuth APIs.
