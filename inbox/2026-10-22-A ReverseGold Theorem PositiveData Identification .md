---
title: "A Reverse-Gold Theorem: Positive-Data Identification by Substrate-Bounded Contrastive Learners"
source: "stat.ML - Machine Learning (Statistics)"
link: https://arxiv.org/abs/2610.28747
priority: medium
status: unread
interest: medium
next_step: skim
---
# A Reverse-Gold Theorem: Positive-Data Identification by Substrate-Bounded Contrastive Learners
> 原文: [https://arxiv.org/abs/2610.28747](https://arxiv.org/abs/2610.28747)

arXiv:2610.28747v1 Announce Type: new
Abstract: Gold's theorem shows that no learner can identify an arbitrary language in a superfinite class from positive presentations alone. We prove a positive result of a different shape. Fix an innate \emph{recursive contrast operator} $R$ mapping any string to a finite set of structurally bounded perturbations of it, and a discriminative scorer of bounded capacity trained by InfoNCE-style contrastive estimation \citep{vandenoord2018,macollins2018} on self-generated perturbations. Under a faithfulness condition relating operator, scorer, and target, the trained scorer achieves \emph{PAC conditional identification} from positive data alone: with high probability it ranks all but an $\varepsilon$-fraction of positives above every out-of-language perturbation in their own orbit, with sample complexity polynomial in the capacity, the orbit size, the score bound, and $1/\varepsilon$. The negatives are constructed by the learner, not supplied by an oracle, and no global normalizing constant over strings is ever computed. The misranking bound follows from the geometry of the contrastive loss---per-example loss floors plus a definite loss increment under misranking---yielding an $\varepsilon^{-2}$ rate, together with an explicit approximation gap that quantifies the cost of in-language (``colliding'') perturbations and vanishes for orbit-pure operators. The ranking guarantee lifts to a global membership classifier under a margin condition, and the same operator composed with the learned scorer is a normalization-free Metropolis--Hastings generator. We instantiate the hypotheses for substitutable context-free languages \citep{clarkeyraud2007} and the subregular classes \citep{heinz2010,hayashikamigaito2025}, and state an open conjecture locating the construction in the mildly context-sensitive hierarchy.
