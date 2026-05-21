---
interest: medium
link: https://arxiv.org/abs/2605.16353
next_step: skim
priority: medium
slack_ts: '1779337378.728629'
source: cs.CV - Computer Vision
status: unread
title: 'StrLoRA: Towards Streaming Continual Visual Instruction Tuning for MLLMs'
---
# StrLoRA: Towards Streaming Continual Visual Instruction Tuning for MLLMs
> 原文: [https://arxiv.org/abs/2605.16353](https://arxiv.org/abs/2605.16353)

arXiv:2605.16353v1 Announce Type: new
Abstract: Continual Visual Instruction Tuning (CVIT) enables Multimodal Large Language Models to incrementally acquire new abilities. However, existing CVIT methods operate under a restrictive task-incremental setting, where each training phase corresponds to a single, predefined task. This does not reflect real-world conditions, where data arrives as a continuous stream of interleaved and dynamically evolving tasks. To bridge this gap, we introduce Streaming CVIT (StrCVIT), a more general and realistic setting where models learn from a stream of data chunks containing a dynamic mixture of tasks. In StrCVIT, a model must simultaneously acquire new abilities, reinforce recurring abilities, and mitigate forgetting. Existing CVIT methods fail here as they cannot reliably distinguish or adapt to the heterogeneous task samples within each chunk. We therefore propose StrLoRA, a regularized two-stage expert routing framework. StrLoRA first performs task-aware expert selection using the textual instruction to activate a sparse subset of relevant experts, reducing cross-task interference. It then applies token-wise expert weighting within this subset, where contribution weights are computed via cross-modal attention between local visual tokens and the global instruction representation. To maintain stability across the non-stationary stream, a routing-stability regularization aligns current routing distributions with a historical exponential moving average reference. Extensive experiments on a newly developed StrCVIT benchmark show that StrLoRA substantially outperforms existing methods, effectively enhancing model's abilities from continuously evolving data streams.
