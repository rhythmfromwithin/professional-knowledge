---
title: "vLLM Hook v0: A Plug-in for Programming Model Internals on vLLM"
source: "cs.LG - Machine Learning"
link: https://arxiv.org/abs/2603.06588
priority: high
status: unread
interest: medium
next_step: skim
---
# vLLM Hook v0: A Plug-in for Programming Model Internals on vLLM
> 原文: [https://arxiv.org/abs/2603.06588](https://arxiv.org/abs/2603.06588)

arXiv:2603.06588v1 Announce Type: new
Abstract: Modern artificial intelligence (AI) models are deployed on inference engines to optimize runtime efficiency and resource allocation, particularly for transformer-based large language models (LLMs). The vLLM project is a major open-source library to support model serving and inference. However, the current implementation of vLLM limits programmability of the internal states of deployed models. This prevents the use of popular test-time model alignment and enhancement methods. For example, it prevents the detection of adversarial prompts based on attention patterns or the adjustment of model responses based on activation steering. To bridge this critical gap, we present vLLM Hook, an opensource plug-in to enable the programming of internal states for vLLM models. Based on a configuration file specifying which internal states to capture, vLLM Hook provides seamless integration to vLLM and supports two essential features: passive programming and active programming. For passive programming, vLLM Hook probes the selected internal states for subsequent analysis, while keeping the model generation intact. For active programming, vLLM Hook enables efficient intervention of model generation by altering the selected internal states. In addition to presenting the core functions of vLLM Hook, in version 0, we demonstrate 3 use cases including prompt injection detection, enhanced retrieval-augmented retrieval (RAG), and activation steering. Finally, we welcome the community's contribution to improve vLLM Hook via https://github.com/ibm/vllm-hook.
