---
interest: medium
link: https://arxiv.org/abs/2606.24898
next_step: skim
priority: high
slack_ts: '1782360758.502279'
source: cs.LG - Machine Learning
status: unread
title: 'Dense Supervision Is Not Enough: The Readout Blind Spot in Looped Language
  Models'
---
# Dense Supervision Is Not Enough: The Readout Blind Spot in Looped Language Models
> 原文: [https://arxiv.org/abs/2606.24898](https://arxiv.org/abs/2606.24898)

arXiv:2606.24898v1 Announce Type: new
Abstract: Looped language models turn hidden states into runtime state: each state is decoded for prediction and fed back into future computation. This creates a basic supervision question: which state variables does cross-entropy actually control? We show that dense per-loop cross-entropy controls the variables exposed by the readout, not every variable active in the recurrent transition. Hidden-state scale gives a concrete failure mode. Scale-invariant readouts such as RMSNorm and LayerNorm hide radial scale from the immediate cross-entropy loss, while pre-norm residual recurrence continues to carry and update that same scale. Thus per-loop loss can make early exits usable without controlling recurrent scale. In 44M and 129M looped transformers without inter-loop normalization, per-loop cross-entropy through RMSNorm readouts still drives final hidden-state norms into the thousands or tens of thousands. Scale-visible readouts and explicit norm penalties keep norms in the tens, and scale-removing recurrence is the complementary architectural fix. The resulting design rule is simple: dense supervision trains exits; recurrent scale control requires either making scale visible to a loss or removing it from the loop. Consistent with this rule, scale-controlled variants achieve lower perplexity at matched inference-depth operating points in our variable-depth benchmarks.
