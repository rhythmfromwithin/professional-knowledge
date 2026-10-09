---
title: "Large Language Model-Assisted Preparation of Transportation Management Plans: A Case Study with WisDOT WisTMP System"
source: "cs.CL - Computation and Language (NLP)"
link: https://arxiv.org/abs/2610.10650
priority: high
status: unread
interest: medium
next_step: skim
---
# Large Language Model-Assisted Preparation of Transportation Management Plans: A Case Study with WisDOT WisTMP System
> 原文: [https://arxiv.org/abs/2610.10650](https://arxiv.org/abs/2610.10650)

arXiv:2610.10650v1 Announce Type: new
Abstract: Work zones are critical yet hazardous components of transportation infrastructure, requiring carefully designed Transportation Management Plans (TMPs) to ensure safety and mobility. However, TMP preparation remains labor-intensive and heavily dependent on practitioner expertise. This paper proposes a Large Language Model (LLM)-assisted framework to automate TMP content generation, leveraging the WisDOT WisTMP system as the application context. The framework fine-tunes multiple open-source LLMs across different model scales and deploys them locally to ensure data security. To support model training, we construct a domain-specific dataset from historical WisTMP documents by converting PDF files into structured question-answer pairs in JSON format. Experimental results show that fine-tuning significantly improves performance across standard text generation metrics. Further section-wise and strategy-level analyses reveal that, while LLMs achieve strong overall performance, they tend to over-generate strategies and struggle to produce project-specific justifications and accurate cost estimates. In addition, scaling from 7B/8B to 14B yields limited gains. These findings demonstrate the potential of LLMs to improve TMP preparation efficiency while highlighting remaining challenges in LLM-assisted TMP development. The source code and demo videos will be publicly available at https://zihaosheng.github.io/TMP-LLM/.
