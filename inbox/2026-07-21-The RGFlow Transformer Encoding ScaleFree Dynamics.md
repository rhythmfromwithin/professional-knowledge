---
interest: medium
link: https://arxiv.org/abs/2607.11950
next_step: skim
priority: low
slack_ts: '1784690755.663359'
source: q-bio.NC - Neurons and Cognition
status: unread
title: 'The RG-Flow Transformer: Encoding Scale-Free Dynamics in Scarce EEG'
---
# The RG-Flow Transformer: Encoding Scale-Free Dynamics in Scarce EEG
> 原文: [https://arxiv.org/abs/2607.11950](https://arxiv.org/abs/2607.11950)

arXiv:2607.11950v2 Announce Type: cross
Abstract: Brain field potentials are scale-free: their power spectra follow a $1/f^{\beta}$ law whose aperiodic exponent $\beta$ tracks cortical state, and sleep depth in particular is a shift in $\beta$. We ask whether a transformer endowed with an explicit renormalization-group (RG) inductive bias the RG-Flow Transformer, which couples ordinary self-attention to a scale-aware stream with a learnable anomalous dimension $\gamma$, block-spin coarse-graining, and an entropy-gated synchronization bridge has an advantage over a parameter-matched vanilla transformer on \emph{real, scarce} EEG. Using the PhysioNet Sleep-EDF corpus with a strict leakage-free by-subject hold-out, we (i) benchmark RG-Flow against a param-matched vanilla transformer and a hierarchy-only ablation on 5-class AASM sleep staging, (ii) sweep the per-subject data budget to look for the inductive-bias crossover predicted when data are scarce, and (iii) test whether RG-Flow's learned $\gamma$ tracks the measured spectral exponent $\beta$ out-of-sample a quantity the vanilla model does not possess. Across $5$ subjects and $5$ seeds under leave-one-subject-out cross-validation, RG-Flow and the vanilla transformer are statistically indistinguishable on 5-class staging (77.3\% vs 77.0\% accuracy; paired $p=0.294$), and the predicted scarce-data crossover does not appear: vanilla is numerically ahead at every data-limited budget. What does separate the models is interpretability RG-Flow recovers the continuous spectral exponent out-of-sample ($\beta$-recovery $R^2 = 0.416$), a capability the vanilla architecture has no analogue for.
