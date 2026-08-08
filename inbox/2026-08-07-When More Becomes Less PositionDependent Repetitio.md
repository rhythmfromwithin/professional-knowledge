---
interest: medium
link: https://arxiv.org/abs/2608.04021
next_step: skim
priority: high
slack_ts: '1786154718.258129'
source: cs.CL - Computation and Language (NLP)
status: unread
title: 'When More Becomes Less: Position-Dependent Repetition Effects in Language
  Models'
---
# When More Becomes Less: Position-Dependent Repetition Effects in Language Models
> 原文: [https://arxiv.org/abs/2608.04021](https://arxiv.org/abs/2608.04021)

arXiv:2608.04021v1 Announce Type: new
Abstract: Cloze-style probes that vary how often a target token appears implicitly assume that more copies of a target affect prediction the same way regardless of where the readout slot sits. We show this assumption fails. Our two-probe design holds a repeated-target prefix fixed and varies only the readout position: the adjacent probe places the slot immediately after the repeated block; the displaced probe places it inside a fresh sentence frame. Adjacent repetition behaves as priming intuition predicts: $P(\text{target})$ climbs with $N$ and plateaus. Displaced repetition produces an inverted-U: $P(\text{target})$ rises to an early peak and then declines as more copies are added. The displaced inverted-U shows a per-word drop with bootstrap CI excluding zero in all 13 open-access encoder and decoder models we test, and replicates across Spanish, Chinese, German, and French in 42 of 42 multilingual cells. A six-condition causal ablation isolates the effect to exact lexical repetition rather than length, generic redundancy, or semantic-neighbour exposure. A frame-pragmatics control rules out an artefact of the readout frame. Internally, per-target-token attention falls with $N$ while the total budget assigned to the repeated block grows in causal LMs but not in the masked LM we probe. Probes that vary repetition count cannot treat the readout position as orthogonal to what they measure.
