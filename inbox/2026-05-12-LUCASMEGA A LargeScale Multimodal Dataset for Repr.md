---
interest: medium
link: https://arxiv.org/abs/2605.04323
next_step: skim
priority: low
slack_ts: '1778644944.340349'
source: cs.DB - Databases
status: unread
title: 'LUCAS-MEGA: A Large-Scale Multimodal Dataset for Representation Learning in
  Soil-Environment Systems'
---
# LUCAS-MEGA: A Large-Scale Multimodal Dataset for Representation Learning in Soil-Environment Systems
> 原文: [https://arxiv.org/abs/2605.04323](https://arxiv.org/abs/2605.04323)

arXiv:2605.04323v2 Announce Type: replace-cross
Abstract: Understanding soil is fundamental to agriculture, carbon cycling, and environmental sustainability, yet progress is limited by fragmented and heterogeneous datasets that constrain modeling to small-scale predictive settings rather than high-dimensional representation learning. We introduce LUCAS-MEGA, a large-scale multimodal dataset constructed through systematic data fusion of European soil-environment observations, with the LUCAS survey as its backbone. The fused dataset comprises over 70,000 samples and more than 1,000 features spanning physical, chemical, environmental, biological, and visual attributes, aggregated from 68 source datasets. To enable integration at scale, we develop SoilFuser, a multi-agent, human-in-the-loop data fusion pipeline that standardizes heterogeneous data formats and measurement protocols, resolves inconsistencies and invalid entries (e.g., unit inconsistencies, codebook mismatches, and erroneous values), incorporates natural language annotations, and harmonizes multimodal attributes and metadata into a unified, machine learning-ready feature space. The resulting dataset captures key characteristics of real-world soil observations, including multimodality, uneven feature coverage, and heterogeneous uncertainty. To demonstrate the usability of LUCAS-MEGA for data-driven modeling, we pretrain a multimodal tabular transformer (SoilFormer) using a self-supervised objective based on feature masking, achieving stable training, strong predictive performance, and representations that support uncertainty-aware prediction. We further show that the learned representations recover relationships consistent with established soil processes. LUCAS-MEGA is released with open access and is accompanied by composable, agent-friendly APIs that support structured querying and data-driven workflows.
