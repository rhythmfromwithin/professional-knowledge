---
title: "Pre-training, Reasoning, Benchmarking: X-ray Report Generation on CheXpert Plus Dataset"
source: "cs.CV - Computer Vision"
link: https://arxiv.org/abs/2610.08813
priority: medium
status: unread
interest: medium
next_step: skim
---
# Pre-training, Reasoning, Benchmarking: X-ray Report Generation on CheXpert Plus Dataset
> 原文: [https://arxiv.org/abs/2610.08813](https://arxiv.org/abs/2610.08813)

arXiv:2610.08813v1 Announce Type: new
Abstract: X-ray image-based Radiology Report Generation (RRG) constitutes a critical research direction within medical artificial intelligence, with great potential to alleviate clinicians' diagnostic workload and shorten patient waiting periods. Despite substantial advances over recent years, the field faces evident bottlenecks stemming from insufficient standardized benchmarks and inadequate domain adaptation of generic large models. Notably, the newly released CheXpert Plus dataset is provided without accompanying baseline implementations and evaluation results, which impedes standardized training, quantitative evaluation and fair comparison among follow-up algorithms. To mitigate this limitation, we establish a comprehensive benchmark encompassing prevailing X-ray report generation models and Large Language Models on CheXpert Plus. This benchmark delivers a reliable comparative foundation for upcoming methods and enables researchers to rapidly identify state-of-the-art approaches within this domain. Beyond benchmark construction, we rethink X-ray RRG under the paradigm of large models and propose a novel framework termed MambaXray-PRB. Our framework improves report generation performance and enhances model interpretability via multi-stage large-model pre-training and multi-modal Chain-of-Thought reasoning. The pipeline consists of three successive phases: self-supervised auto-regressive modeling, X-ray-report contrastive learning, and post-training optimization for reasoning and report generation. Extensive experiments on IU X-ray, MIMIC-CXR, and CheXpert Plus datasets validate the effectiveness of MambaXray-PRB for radiology report generation. The source code of this paper is available on https://github.com/Event-AHU/Medical\_Image\_Analysis
