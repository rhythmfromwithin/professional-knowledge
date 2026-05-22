---
title: "Guiding Multi-Objective Genetic Programming with Description Length Improves Symbolic Regression Solutions"
source: "cs.NE - Neural and Evolutionary Computing"
link: https://arxiv.org/abs/2605.22374
priority: low
status: unread
interest: medium
next_step: skim
---
# Guiding Multi-Objective Genetic Programming with Description Length Improves Symbolic Regression Solutions
> 原文: [https://arxiv.org/abs/2605.22374](https://arxiv.org/abs/2605.22374)

arXiv:2605.22374v1 Announce Type: new
Abstract: Symbolic regression with genetic programming (GPSR) may suffer from overfitting and structural bloat, especially when noise is present. In this paper we evaluate description length (DL) and fractional Bayes factor (FBF) criteria as principled, data-efficient alternatives to heuristics for selecting compact expressions that generalise well. We implement DL using a Fisher-information-based parameter encoding and compare it to AIC and BIC across multiple datasets, including noisy synthetic benchmarks and real-world regression problems. We study three search/selection strategies: (i) multi-objective search for accuracy and program length followed by DL/FBF selection; (ii) multi-objective search using DL directly as an objective; and (iii) single-objective optimisation with DL/FBF as the fitness. Across datasets we find that DL/FBF post-selection improves test performance compared to AIC/BIC baseline and that BIC in combination with the same function complexity penalty from DL/FBF produces similar results. In contrast, using DL/FBF directly as a fitness function in single-objective GPSR frequently induces premature convergence to overly simple models. We conclude with practical guidance for using DL/FBF as robust model-selection tools in genetic programming workflows.
