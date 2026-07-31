---
interest: medium
link: https://arxiv.org/abs/2607.26099
next_step: skim
priority: low
slack_ts: '1785469018.433159'
source: cs.CR - Cryptography and Security
status: unread
title: 'Lilith: Backdoor Generalization under Training-Inference Trigger Shift'
---
# Lilith: Backdoor Generalization under Training-Inference Trigger Shift
> 原文: [https://arxiv.org/abs/2607.26099](https://arxiv.org/abs/2607.26099)

arXiv:2607.26099v1 Announce Type: new
Abstract: Machine-learning services increasingly rely on public data, third-party providers, and outsourced training, creating opportunities for data-poisoning attacks that implant persistent malicious behavior while preserving benign utility. However, existing backdoor studies largely evaluate exact trigger reuse, training-exposed trigger diversity, or variations along predefined transformation axes. They therefore leave a critical blind spot: whether a backdoor learned from one training-time trigger can generalize to an inference-time trigger family absent from victim training. We formulate this problem as backdoor generalization under training--inference trigger shift and introduce Lilith, a black-box anchor-to-family framework. Using only disjoint surrogate resources, Lilith first induces a compact target-side vulnerability with a single training anchor, then constructs a bounded inference-only family that preserves the anchor-induced representation geometry. We characterize this mechanism through anchor clearance and family reach, deriving sufficient conditions for family-wise target preservation under local regularity and bounded surrogate--victim discrepancy. Experiments across datasets, architectures, poisoning rates, and defenses show that Lilith achieves high family-wise attack success with limited utility degradation and a small trigger generalization gap. Additional analyses show that family activation depends on representation alignment rather than the proposal mechanism, exposing a broader threat overlooked by exact-trigger evaluation.
