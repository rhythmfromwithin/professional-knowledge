---
title: "Stable and Faithful Explanations for Knowledge Tracing"
source: "cs.LG - Machine Learning"
link: https://arxiv.org/abs/2609.28502
priority: high
status: unread
interest: medium
next_step: skim
---
# Stable and Faithful Explanations for Knowledge Tracing
> 原文: [https://arxiv.org/abs/2609.28502](https://arxiv.org/abs/2609.28502)

arXiv:2609.28502v1 Announce Type: new
Abstract: Knowledge tracing (KT) models predict student performance opaquely, limiting pedagogical action. This study contributes a validation protocol testing predictive competitiveness (RQ1), explanation stability (RQ2) and retraining-based faithfulness (RQ3) together. Thirteen behavioral features across five pedagogical themes were engineered from ASSISTments 2009 and 2012, with history features computed from temporally preceding interactions and current response latency retained only for retrospective analysis. ASSISTments 2009 was rebuilt: the uncorrected skill-builder release duplicates each multi-skill interaction across one row per skill, and because those rows share one correctness label, they leak it into preceding-interaction features. Rebuilding lowered model AUC and reordered the explanation results. An Extreme Gradient Boosting (XGBoost) model explained with Tree SHapley Additive exPlanations (TreeSHAP) was compared against four deep baselines (DKT, SAKT, AKT and SimpleKT) under an information-matched protocol giving the deep models the same behavioral signals and restricting XGBoost to what is derivable from the identifier-and-correctness stream they consume. XGBoost reached an area under the curve (AUC) of 0.777 on 2012 and 0.786 on rebuilt 2009, with prediction-time AUCs of 0.771 and 0.775, respectively, after excluding current response latency; restricted to the baselines' information it performed as they did (0.697 against 0.700, and 0.717 against 0.720), locating the difference in information supplied, not model family. Rankings were consistent across folds, seeds and conditioning schemes (Spearman rho = 0.989-1.000), and removing top-ranked TreeSHAP features harmed AUC more than random removal, though split-gain and permutation rankings performed comparably. Student-level examples are illustrative interpretations, not validated recommendations.
