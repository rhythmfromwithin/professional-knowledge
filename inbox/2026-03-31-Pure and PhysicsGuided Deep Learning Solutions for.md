---
title: "Pure and Physics-Guided Deep Learning Solutions for Spatio-Temporal Groundwater Level Prediction at Arbitrary Locations"
source: "cs.LG - Machine Learning"
link: https://arxiv.org/abs/2603.25779
priority: high
status: unread
interest: medium
next_step: skim
---
# Pure and Physics-Guided Deep Learning Solutions for Spatio-Temporal Groundwater Level Prediction at Arbitrary Locations
> 原文: [https://arxiv.org/abs/2603.25779](https://arxiv.org/abs/2603.25779)

arXiv:2603.25779v1 Announce Type: new
Abstract: Groundwater represents a key element of the water cycle, yet it exhibits intricate and context-dependent relationships that make its modeling a challenging task. Theory-based models have been the cornerstone of scientific understanding. However, their computational demands, simplifying assumptions, and calibration requirements limit their use. In recent years, data-driven models have emerged as powerful alternatives. In particular, deep learning has proven to be a leading approach for its design flexibility and ability to learn complex relationships.
We proposed an attention-based pure deep learning model, named STAINet, to predict weekly groundwater levels at an arbitrary and variable number of locations, leveraging both spatially sparse groundwater measurements and spatially dense weather information. Then, to enhance the model's trustworthiness and generalization ability, we considered different physics-guided strategies to inject the groundwater flow equation into the model. Firstly, in the STAINet-IB, by introducing an inductive bias, we also estimated the governing equation components. Then, by adopting a learning bias strategy, we proposed the STAINet-ILB, trained with additional loss terms adding supervision on the estimated equation components. Lastly, we developed the STAINet-ILRB, leveraging the groundwater body recharge zone information estimated by domain experts.
The STAINet-ILB performed the best, achieving overwhelming test performances in a rollout setting (median MAPE 0.16%, KGE 0.58). Furthermore, it predicted sensible equation components, providing insights into the model's physical soundness. Physics-guided approaches represent a promising opportunity to enhance both the generalization ability and the trustworthiness, thereby paving the way to a new generation of disruptive hybrid deep learning Earth system models.
