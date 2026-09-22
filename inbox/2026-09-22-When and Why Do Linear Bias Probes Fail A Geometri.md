---
title: "When and Why Do Linear Bias Probes Fail? A Geometric and Statistical Theory of Bias Detectability in Large Language Model Representations"
source: "stat.ML - Machine Learning (Statistics)"
link: https://arxiv.org/abs/2609.22337
priority: medium
status: unread
interest: medium
next_step: skim
---
# When and Why Do Linear Bias Probes Fail? A Geometric and Statistical Theory of Bias Detectability in Large Language Model Representations
> 原文: [https://arxiv.org/abs/2609.22337](https://arxiv.org/abs/2609.22337)

arXiv:2609.22337v1 Announce Type: new
Abstract: Linear probing is the standard instrument for detecting social biases in the hidden representations of large language models. Yet reported probe accuracies come almost exclusively from \emph{counterfactual} evaluations in which every input carries an explicit demographic marker. Once only a fraction $\alpha$ of inputs carries demographic information, performance degrades sharply, and a weak probe may reflect either an unbiased model or an underpowered detector. We develop a theory that resolves this ambiguity. Modeling representations as two class-conditional clusters with Mahalanobis separation $s$ on a manifold of curvature $\kap$, we prove: (i) a finite-sample generalization bound governed by the manifold's extrinsic radius with a matching $\smash{\sqrt{\dB/n}}$ minimax lower bound; (ii) an exact purity law for the maximum linear-probe AUC, strictly increasing in $\alpha$; (iii) a curvature ceiling: ambient chordal separation on a space form cannot exceed $2/\sqrt{\kap}$; and (iv) a detectability threshold below which no audit can distinguish probe output from chance. Every theorem is validated on synthetic manifolds with known ground truth and on six open-weight models $\times$ four bias dimensions, where the purity law predicts entire AUC--$\alpha$ curves from a single cross-fitted $\hat s$ measured at $\alpha=1$, with no parameters fitted to those curves. The framework turns bias auditing into a power analysis: given a target purity and effect size, it prescribes the sample budget $n(\alpha)$ for a conclusive audit.
