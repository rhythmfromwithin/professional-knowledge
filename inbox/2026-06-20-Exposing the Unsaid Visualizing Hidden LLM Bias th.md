---
interest: medium
link: https://arxiv.org/abs/2606.19344
next_step: skim
priority: high
slack_ts: '1781930800.253139'
source: cs.CL - Computation and Language (NLP)
status: unread
title: 'Exposing the Unsaid: Visualizing Hidden LLM Bias through Stochastic Path Aggregation'
---
# Exposing the Unsaid: Visualizing Hidden LLM Bias through Stochastic Path Aggregation
> 原文: [https://arxiv.org/abs/2606.19344](https://arxiv.org/abs/2606.19344)

arXiv:2606.19344v1 Announce Type: new
Abstract: Large Language Models (LLMs) exhibit representational and syntactic biases that are difficult to evaluate due to the stochastic nature of text generation. Standard auditing methods rely on a single output inspection or static automated metrics. These approaches obscure the underlying probability distributions and fail to capture biases hidden in lower-probability generation branches. This paper introduces TreeTracer, a visual analytics tool designed to evaluate LLM bias through aggregated comparison. Using a systematic perturbation analysis pipeline, the tool replaces ontology-defined terms in each input prompt, aggregates hundreds of stochastic generations into a syntax-aligned hierarchical structure, and then performs classification-aware node merging with an auxiliary language model. The resulting structure is visualized through a custom Sankey diagram. By juxtaposing two ontology-driven trees, the workspace enables direct comparison between semantic contexts and supports systematic bias detection. Because any visualization reflects only a subset of the model's learned behavior, the system further applies contrastive inference to compute and directly display counterfactual token probabilities across contexts, reducing the risk of misinterpreting the presence of bias. We validate the workspace through case studies comparing an unaligned baseline model GPT-2 XL against the constitutionally aligned Apertus models. The visual aggregation successfully exposes hidden representational harms, such as counterfactual pronoun suppression and conversational marginalization of individuals. A preliminary user study confirms that the aggregated comparative interface reduces cognitive load and effectively supports analysts in detecting systemic biases.
