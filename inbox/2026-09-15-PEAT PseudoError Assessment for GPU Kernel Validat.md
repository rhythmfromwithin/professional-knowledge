---
title: "PEAT: Pseudo-Error Assessment for GPU Kernel Validation in DNN Training"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2609.13544
priority: medium
status: unread
interest: medium
next_step: skim
---
# PEAT: Pseudo-Error Assessment for GPU Kernel Validation in DNN Training
> 原文: [https://arxiv.org/abs/2609.13544](https://arxiv.org/abs/2609.13544)

arXiv:2609.13544v1 Announce Type: new
Abstract: Deep neural networks (DNNs) are widely adopted in various fields, driving an emerging trend in developing software stacks associated with DNN training systems. For example, many codes have been ported across different frameworks or developed to leverage the computing power of GPUs or domain-specific accelerators. However, validating a kernel implementation in DNN training is time-consuming and generally requires massive storage. Specifically, this poses a fundamental question: how to characterize the behavior of a new implementation when it is integrated into a DNN training flow. Unfortunately, this problem is not well investigated in the literature, to the best of our knowledge. To address this shortcoming, we present PEAT - a lightweight inspection framework for \underline{P}seudo-\underline{E}rror \underline{A}ssessment associated with GPU kernel validation in DNN \underline{T}raining. Firstly, inspired by conventional fault injection (FI), PEAT's Profiler invokes an operation-wise kernel in a training flow to collect a DNN model's states (e.g., checkpoints and activations). More importantly, the Profiler introduces two simple yet effective techniques, playback FI and frequency-based runtime FI, leveraging persistent kernel calling during the training process. Secondly, PEAT's Analyzer characterizes profiled errors, revealing some signatures from the error distribution of a kernel compared to the golden one. Lastly, PEAT's Detector provides some guidelines as a sufficient condition, which enables associating several well-known error models with signature patterns. We demonstrate the applicability of our approach by presenting the results and analysis using GPUs from the two most popular vendors, NVIDIA V100 and AMD MI250, on various AI models, from vision tasks to language models, for both pretraining and finetuning scenarios.
