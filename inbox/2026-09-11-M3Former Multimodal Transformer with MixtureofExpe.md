---
title: "M3-Former: Multimodal Transformer with Mixture-of-Experts for Long-Term Vessel Trajectory Prediction"
source: "cs.LG - Machine Learning"
link: https://arxiv.org/abs/2609.10559
priority: high
status: unread
interest: medium
next_step: skim
---
# M3-Former: Multimodal Transformer with Mixture-of-Experts for Long-Term Vessel Trajectory Prediction
> 原文: [https://arxiv.org/abs/2609.10559](https://arxiv.org/abs/2609.10559)

arXiv:2609.10559v1 Announce Type: new
Abstract: To address the challenges of behavioral multimodality, limited semantic utilization, and long-term error accumulation in vessel trajectory prediction, this paper proposes M3-Former, a multimodal trajectory prediction framework enhanced by large language models (LLMs). The proposed framework incorporates vessel static attributes and navigational intent as semantic priors for long-term trajectory modeling. Specifically, a unified multimodal representation space is constructed, in which static semantic information is encoded by a pre-trained LLM and aligned with dynamic trajectory features through self-attention. To jointly capture global route planning and local motion variations, a dual-granularity Mixture-of-Experts (MoE) architecture is introduced, where sequence-level experts model global navigation trends and token-level experts refine fine-grained maneuvering behaviors. In addition, a Steering-Weighted Cross-Entropy loss is designed to alleviate the long-tail distribution of sparse turning samples and improve prediction accuracy in critical maneuvering scenarios. Experiments on a real-world Danish AIS dataset demonstrate that M\textsuperscript{3}-Former consistently outperforms state-of-the-art baselines across prediction horizons from 1 to 4 hours. In the 4-hour prediction task, the proposed method reduces Average Displacement Error (ADE) and Final Displacement Error (FDE) by 4.4\% and 5.1\%, respectively, compared with the strongest baseline. Qualitative and ablation analyses further verify that semantic fusion effectively reduces long-term trajectory drift, while the dual-granularity MoE improves robustness in complex waterways and route-branching scenarios. The proposed framework establishes a semantic-guided hierarchical prediction paradigm, in which high-level navigational intent and local motion dynamics are jointly modeled for robust long-term vessel trajectory forecasting.
