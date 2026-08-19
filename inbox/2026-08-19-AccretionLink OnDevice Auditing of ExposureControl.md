---
title: "AccretionLink: On-Device Auditing of Exposure-Control Attacks on Attribute Inference"
source: "cs.CR - Cryptography and Security"
link: https://arxiv.org/abs/2608.14735
priority: low
status: unread
interest: medium
next_step: skim
---
# AccretionLink: On-Device Auditing of Exposure-Control Attacks on Attribute Inference
> 原文: [https://arxiv.org/abs/2608.14735](https://arxiv.org/abs/2608.14735)

arXiv:2608.14735v1 Announce Type: new
Abstract: Exposure control lets an adversary rank authentic public posts to strengthen private-attribute inference without altering content. AccretionLink defines confidentiality and integrity games for this attack, models bounded selection odds through partial identification, and constructs dependence-aware time-uniform e-processes. On 52 held-out synthetic profiles, odds-four selection reduced aggregate negative log likelihood at every horizon. At eight posts the advantage was 0.01595 nats (95% CI [0.00890, 0.02336]), three of four target effects survived Holm adjustment, and label-blind model-guided selection caused 6/109 high-confidence false reversals. On 142 PAN15 test profiles, exploratory selection produced a 0.01227-nat advantage but no reversal. A separate TF-IDF selector retained a 0.01470-nat advantage against the unchanged G5 target, while matched identity shuffling did not reproduce it. Pixel 10 encoded all 1,622 held-out posts once with a fallback-free Tensor G5 graph. A P-256 checkpoint authenticated the selected-replay, actual-model, native-report, and operation digests; local KeyInfo identified the signing key as StrongBox-backed.
