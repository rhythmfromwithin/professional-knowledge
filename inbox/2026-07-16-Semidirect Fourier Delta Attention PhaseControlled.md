---
interest: medium
link: https://arxiv.org/abs/2607.11897
next_step: skim
priority: high
slack_ts: '1784344393.583879'
source: cs.LG - Machine Learning
status: unread
title: 'Semidirect Fourier Delta Attention: Phase-Controlled Delta Memory with Constructive
  Chunk-WY Kernels'
---
# Semidirect Fourier Delta Attention: Phase-Controlled Delta Memory with Constructive Chunk-WY Kernels
> 原文: [https://arxiv.org/abs/2607.11897](https://arxiv.org/abs/2607.11897)

arXiv:2607.11897v1 Announce Type: new
Abstract: Linear attention replaces softmax attention's growing KV cache with a fixed recurrent state, but this compression limits exact state tracking and long-context memory. We introduce \emph{Semidirect Fourier Delta Attention} (SFDA), a phase-controlled generalization of Kimi Delta Attention that replaces real diagonal decay with block-rotational Fourier control: \[ S\_t=(I-\beta\_t k\_tk\_t^\*)\Lambda\_tS\_{t-1}+\beta\_tk\_tv\_t^\*, \qquad \Lambda\_t=\diag(\alpha\_t\odot e^{i\theta\_t}). \] Our main result is a constructive chunk-WY factorization for products \(A\_t=\Lambda\_t-u\_tr\_t^\*\), giving \[ A\_t\cdots A\_1=\Gamma\_t-Y\_tM\_tW\_t^\* \] with rank growth bounded inside fixed chunks. This yields an exact affine chunk transfer, formal stability and complexity bounds, and a compact characterization of phase-plus-low-rank memory. We verify the algebra numerically and show in toy state-tracking experiments that SFDA learns cyclic memory where the phase-disabled KDA baseline remains near chance. Fused kernels and large-scale language-model comparisons are left to future work.
