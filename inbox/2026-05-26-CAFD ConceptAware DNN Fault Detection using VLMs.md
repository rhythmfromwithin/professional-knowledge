---
title: "CAFD: Concept-Aware DNN Fault Detection using VLMs"
source: "cs.LG - Machine Learning"
link: https://arxiv.org/abs/2605.24008
priority: high
status: unread
interest: medium
next_step: skim
---
# CAFD: Concept-Aware DNN Fault Detection using VLMs
> 原文: [https://arxiv.org/abs/2605.24008](https://arxiv.org/abs/2605.24008)

arXiv:2605.24008v1 Announce Type: new
Abstract: Fault detection for Deep Neural Networks (DNNs) has received increasing attention in recent years. While more advanced hybrid approaches have been proposed to combine multiple sources of information and outperform earlier techniques, they often incur substantial computational overhead, limiting scalability and practicality in real-world settings. In this paper, we introduce Concept-Aware Fault Detection (CAFD), a learning-based approach that achieves superior fault detection performance by effectively integrating multiple information sources while maintaining practical efficiency. Specifically, CAFD is trained using a carefully selected set of informative features, including model-based signals derived from the DNN's outputs, distance-based features, and a novel concept-based feature, called Concept Failure Ratio (CFR). CFR leverages Vision-Language Models (VLMs) to extract textual concepts from images and quantify the likelihood that their presence is associated with DNN failures. By incorporating this feature, CAFD benefits from complementary semantic information, enabling more effective fault detection. Our results demonstrate that CFR serves as an effective indicator for DNN fault detection. We conduct an extensive empirical evaluation of CAFD, comparing it against five state-of-the-art baselines across three subject DNN models and datasets, including ImageNet. Across a wide range of constrained selection budgets, CAFD consistently outperforms all baselines in Fault Detection Rate (FDR), achieving average FDR improvements of 18.3% across all investigated subjects and budget sizes.
