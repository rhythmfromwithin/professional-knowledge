---
interest: medium
link: https://arxiv.org/abs/2603.15644
next_step: skim
priority: high
slack_ts: '1773888856.507669'
source: cs.LG - Machine Learning
status: unread
title: Tokenization Tradeoffs in Structured EHR Foundation Models
---
# Tokenization Tradeoffs in Structured EHR Foundation Models
> 原文: [https://arxiv.org/abs/2603.15644](https://arxiv.org/abs/2603.15644)

arXiv:2603.15644v1 Announce Type: new
Abstract: Foundation models for structured electronic health records (EHRs) are pretrained on longitudinal sequences of timestamped clinical events to learn adaptable patient representations. Tokenization -- how these timelines are converted into discrete model inputs -- determines what information is preserved, how efficiently it is encoded, and which relationships must be learned versus precomputed. Yet the impact of tokenization design choices on downstream performance and computational efficiency remains largely unexplored. Here, we pretrained a transformer on pediatric EHR data under a factorial design, varying tokenization along event encoding, time encoding, and workflow annotation. We evaluated area-under-the-receiver-operating-characteristic curve across 74 clinical prediction tasks. Joint event encoding and positional time encoding outperformed their alternatives (73/74 and 71/74 tasks) while requiring 39.5% and 9.6% fewer pretraining floating-point operations, respectively. Targeted ablations traced the joint encoding advantage to local binding efficiency, that is, code-attribute pairs are combined into single tokens, rather than split across tokens that the model must learn to associate during pretraining. External evaluation on an adult intensive care unit cohort demonstrated that this advantage generalizes despite substantial vocabulary mismatch, while temporal and workflow effects remain institution-specific. These results establish tokenization as a tractable lever for improving both the performance and efficiency of EHR foundation models.
