---
interest: medium
link: https://arxiv.org/abs/2610.24233
next_step: skim
priority: medium
slack_ts: '1792556394.372709'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: Censored Flow Matching for Synthetic Time-to-Event Generation
---
# Censored Flow Matching for Synthetic Time-to-Event Generation
> 原文: [https://arxiv.org/abs/2610.24233](https://arxiv.org/abs/2610.24233)

arXiv:2610.24233v1 Announce Type: new
Abstract: Generating time-to-event data is increasingly important in survival analysis, but it remains statistically challenging because event times are often censored and thus prevent flexible generative modeling. To fill this gap, we propose a novel method called censored flow matching (CFM), aiming at providing a flexible flow-based generative mechanism for synthesizing time-to-event data as well as learning their corresponding probabilistic densities. Unlike existing methods, CFM does not rely on survival likelihoods to handle censoring, but instead exploits the monotonicity property of differential flows to address censoring via pullback sampling. Under this framework, we implement an alternating procedure between pullback sampling and CFM steps, leading to a flow-based expectation--maximization (EM) algorithm tailored for time-to-event inference. Under mild distributional conditions, we establish the convergence of CFM to the true event-time distribution as the EM iterations proceed. We then apply CFM to generate time-to-event data and estimate their probabilistic densities, where the observed censoring time can be incorporated to provide truncated sampling or truncated density estimation for survival inference. Through extensive simulation studies, we demonstrate the benefits of CFM for complex and large-scale data generation. Finally, we apply CFM to analyze data from the Organ Procurement and Transplantation Network (OPTN) and the Medical Information Mart for Intensive Care IV (MIMIC-IV), showcasing its benefits for synthetic and predictive survival analyses in terms of data fidelity, predictive performance, and empirical privacy characteristics.
