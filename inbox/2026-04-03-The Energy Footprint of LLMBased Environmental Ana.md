---
interest: medium
link: https://arxiv.org/abs/2604.00053
next_step: skim
priority: low
slack_ts: '1775359522.204149'
source: cs.SE - Software Engineering
status: unread
title: 'The Energy Footprint of LLM-Based Environmental Analysis: LLMs and Domain
  Products'
---
# The Energy Footprint of LLM-Based Environmental Analysis: LLMs and Domain Products
> 原文: [https://arxiv.org/abs/2604.00053](https://arxiv.org/abs/2604.00053)

arXiv:2604.00053v1 Announce Type: new
Abstract: As large language models (LLMs) are increasingly used in domain-specific applications, including climate change and environmental research, understanding their energy footprint has become an important concern. The growing adoption of retrieval-augmented (RAG) systems for climate-domain specific analysis raises a key question: how does the energy consumption of domain-specific RAG workflows compare with that of direct generic LLM usage? Prior research has focused on standalone model calls or coarse token-based estimates, while leaving the energy implications of deployed application workflows insufficiently understood. In this paper, we assess the inference-time energy consumption of two LLM-based climate analysis chatbots (ChatNetZero and ChatNDC) compared to the generic GPT-4o-mini model. We estimate energy use under actual user queries by decomposing each workflow into retrieval, generation, and hallucination-checking components. We also test across different times of day and geographic access locations. Our results show that the energy consumption of domain-specific RAG systems depends strongly on their design. More agentic pipelines substantially increase inference-time energy use, particularly when used for additional accuracy or verification checks, although they may not yield proportional gains in response quality. While more research is needed to further test these initial findings more robustly across models, environments and prompting structures, this study provides a new understanding on how the design of domain-specific LLM products affects both the energy footprint and quality of output.
