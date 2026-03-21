---
interest: medium
link: https://arxiv.org/abs/2603.13231
next_step: skim
priority: high
slack_ts: '1774060654.343959'
source: cs.LG - Machine Learning
status: unread
title: 'Translational Gaps in Graph Transformers for Longitudinal EHR Prediction:
  A Critical Appraisal of GT-BEHRT'
---
# Translational Gaps in Graph Transformers for Longitudinal EHR Prediction: A Critical Appraisal of GT-BEHRT
> 原文: [https://arxiv.org/abs/2603.13231](https://arxiv.org/abs/2603.13231)

arXiv:2603.13231v1 Announce Type: new
Abstract: Transformer-based models have improved predictive modeling on longitudinal electronic health records through large-scale self-supervised pretraining. However, most EHR transformer architectures treat each clinical encounter as an unordered collection of codes, which limits their ability to capture meaningful relationships within a visit. Graph-transformer approaches aim to address this limitation by modeling visit-level structure while retaining the ability to learn long-term temporal patterns. This paper provides a critical review of GT-BEHRT, a graph-transformer architecture evaluated on MIMIC-IV intensive care outcomes and heart failure prediction in the All of Us Research Program. We examine whether the reported performance gains reflect genuine architectural benefits and whether the evaluation methodology supports claims of robustness and clinical relevance. We analyze GT-BEHRT across seven dimensions relevant to modern machine learning systems, including representation design, pretraining strategy, cohort construction transparency, evaluation beyond discrimination, fairness assessment, reproducibility, and deployment feasibility. GT-BEHRT reports strong discrimination for heart failure prediction within 365 days, with AUROC 94.37 +/- 0.20, AUPRC 73.96 +/- 0.83, and F1 64.70 +/- 0.85. Despite these results, we identify several important gaps, including the lack of calibration analysis, incomplete fairness evaluation, sensitivity to cohort selection, limited analysis across phenotypes and prediction horizons, and limited discussion of practical deployment considerations. Overall, GT-BEHRT represents a meaningful architectural advance in EHR representation learning, but more rigorous evaluation focused on calibration, fairness, and deployment is needed before such models can reliably support clinical decision-making.
