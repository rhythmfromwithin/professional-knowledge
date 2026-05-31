---
interest: medium
link: https://arxiv.org/abs/2605.29139
next_step: skim
priority: medium
slack_ts: '1780202382.882669'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: Anytime-Valid Federated Conformal RAG for LLM Swarms
---
# Anytime-Valid Federated Conformal RAG for LLM Swarms
> 原文: [https://arxiv.org/abs/2605.29139](https://arxiv.org/abs/2605.29139)

arXiv:2605.29139v1 Announce Type: new
Abstract: Federated Conformal RAG (FC-RAG) provides distribution-free coverage for a bandwidth-limited swarm of weak language models, but only at a fixed horizon. We extend it to anytime-valid sequential coverage: validity at every stopping time, preserved under predictable adaptive control (recalibration, per-node bandwidth escalation, distilled-student refresh), at no extra cost in assumptions over fixed-horizon FC-RAG. Naive composition fails because FC-RAG's marginal coverage bound makes the betting e-process a non-supermartingale on adverse calibration draws, and Ville's inequality cannot be invoked. We give Anytime-FC-RAG, a sequential extension built on a summable per-step calibration-deviation budget that converts the marginal bound into a strict conditional bound on a calibration-good event, paired with a truncated betting e-process that is a nonnegative supermartingale on the entire probability space. From these two ingredients, we obtain four guarantees: time-uniform alarm validity $\mathbb{P}(\sup\_t E\_t \ge 1/\delta\_e) \le \delta\_e + \delta\_{\mathrm{cal}}$, a Hoeffding-stitched cumulative-miscoverage envelope at the same total budget, safety under any predictable controller (recalibration, bandwidth escalation, student refresh), and training-side error propagation across an unbounded sequence of Federated Probe-Logit Distillation (FPLD) refreshes via a summable training budget. As a practical consequence, an adaptive controller that escalates retrieval bandwidth only when the e-process crosses a warning threshold matches the alarm rate of a fixed-high-bandwidth schedule at substantially lower communication cost. Experiments on a GPT-2-small + MiniLM swarm across MMLU, DBpedia, and AG News verify the predicted alarm rate, detection delay, envelope coverage, and $14$-$57\%$ bandwidth savings; the alarm fires when and only when coverage genuinely breaks.
