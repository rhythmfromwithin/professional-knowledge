---
title: "A Hybrid Tsallis-Polarization Impurity Measure for Decision Trees: Theoretical Foundations and Empirical Evaluation"
source: "stat.ML - Machine Learning (Statistics)"
link: https://arxiv.org/abs/2603.13241
priority: medium
status: unread
interest: medium
next_step: skim
---
# A Hybrid Tsallis-Polarization Impurity Measure for Decision Trees: Theoretical Foundations and Empirical Evaluation
> 原文: [https://arxiv.org/abs/2603.13241](https://arxiv.org/abs/2603.13241)

arXiv:2603.13241v1 Announce Type: new
Abstract: We introduce the Integrated Tsallis Combination (ITC), a hybrid impurity measure for decision tree learning that combines normalized Tsallis entropy with an exponential polarization component. While many existing measures sacrifice theoretical soundness for computational efficiency or vice versa, ITC provides a mathematically principled framework that balances both aspects. The core innovation lies in the complementarity between Tsallis entropy's information-theoretic foundations and the polarization component's sensitivity to distributional asymmetry. We establish key theoretical properties-concavity under explicit parameter conditions, proper boundary conditions, and connections to classical measures-and provide a rigorous justification for the hybridization strategy. Through an extensive comparative evaluation on seven benchmark datasets comparing 23 impurity measures with five-fold repetition, we show that simple parametric measures (Tsallis $\alpha=0.5$) achieve the highest average accuracy ($91.17\%$), while ITC variants yield competitive results ($88.38-89.16\%$) with strong theoretical guarantees. Statistical analysis (Friedman test: $\chi^2=3.89$, $p=0.692$) reveals no significant global differences among top performers, indicating practical equivalence for many applications. ITC's value resides in its solid theoretical grounding-proven concavity under suitable conditions, flexible parameterization ($\alpha$, $\beta$, $\gamma$), and computational efficiency $O(K)$-making it a rigorous, generalizable alternative when theoretical guarantees are paramount. We provide guidelines for measure selection based on application priorities and release an open-source implementation to foster reproducibility and further research.
