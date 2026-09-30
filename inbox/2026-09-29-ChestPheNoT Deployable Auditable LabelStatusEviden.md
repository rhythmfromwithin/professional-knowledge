---
interest: medium
link: https://arxiv.org/abs/2609.31629
next_step: skim
priority: high
slack_ts: '1790745126.383159'
source: cs.CL - Computation and Language (NLP)
status: unread
title: 'ChestPheNoT: Deployable, Auditable Label-Status-Evidence Extraction from Radiology
  Reports'
---
# ChestPheNoT: Deployable, Auditable Label-Status-Evidence Extraction from Radiology Reports
> 原文: [https://arxiv.org/abs/2609.31629](https://arxiv.org/abs/2609.31629)

arXiv:2609.31629v1 Announce Type: new
Abstract: Structured phenotype extraction from radiology reports supports cohort construction, quality auditing, and clinical analytics, but practical deployment requires local inference and auditable predictions, while expert annotations remain scarce. Conventional labelers provide structured findings and assertion states but no supporting evidence, while API-hosted large language models may be unsuitable when clinical text cannot leave institutional infrastructure. We present CHESTPHENOT, a compact 0.5-3B language model that jointly extracts finding labels, three-class status (present/absent/uncertain), and verbatim supporting evidence spans. CHESTPHENOT is trained using hybrid CheXbert+72B silver supervision followed by supervised fine-tuning and lightweight GRPO refinement. Across three human-annotated gold sets spanning in-distribution, cross-taxonomy, and cross-institution evaluation, the 3B model remains below its CheXbert silver teacher in distribution but is competitive under distribution shift, significantly surpassing CheXbert on cross-institution detection (+2.0 F1). Task-specific training also enables the 3B model to match or exceed substantially larger prompted models on most detection and status comparisons. For evidence-grounded extraction, over 99% of final evidence spans are locatable in the source report, and the 3B model achieves 47.5 auditable-F1, outperforming Qwen2.5-7B one-shot prompting by 7.6 points and approaching Qwen2.5-72B. These results demonstrate that locally deployable models can provide competitive and directly auditable radiology-report extraction without relying on external inference APIs. Code and the full extraction/judge prompts will be made available at https://github.com/yukkai/ChestPheNoT.
