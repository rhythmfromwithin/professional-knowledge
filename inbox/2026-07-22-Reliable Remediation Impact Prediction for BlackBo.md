---
interest: medium
link: https://arxiv.org/abs/2607.16357
next_step: skim
priority: low
slack_ts: '1784863623.526679'
source: cs.CR - Cryptography and Security
status: unread
title: Reliable Remediation Impact Prediction for Black-Box Security Ratings
---
# Reliable Remediation Impact Prediction for Black-Box Security Ratings
> 原文: [https://arxiv.org/abs/2607.16357](https://arxiv.org/abs/2607.16357)

arXiv:2607.16357v1 Announce Type: new
Abstract: Security rating platforms summarize externally observable cyber exposure and are expected to help organizations prioritize remediation. A platform may want to tell an organization how a candidate remediation action would affect its score, but repeatedly exposing exact score responses can reveal information about the hidden scoring engine. We propose a surrogate based approach for remediation score impact prediction that is designed to respect this opacity constraint. The surrogate predicts scores from organization configurations while explicitly representing checkpoint (i.e., a security check) applicability and the observed checkpoint set. A main challenge is that such predictions are not uniformly reliable: they depend on the amount and structure of the observable checkpoint evidence available for a given configuration. To address this, the approach combines applicability-aware surrogate construction, sensitivity analysis under controlled checkpoint restriction, a reliability layer for identifying unstable predictions, and score-impact prediction for supported remediation actions. Explicit modeling of checkpoint applicability is central throughout: it improves score prediction and provides the feature basis used by the reliability layer to identify unstable cases. We evaluate the approach on a real-world dataset of 5,188 organization configurations from a commercial security rating platform. The results show that the applicability-aware surrogate improves score prediction over simpler feature representations. For remediation, the surrogate predicts the score impact of supported actions, while the reliability layer helps identify cases in which these predicted impacts should be interpreted cautiously.
