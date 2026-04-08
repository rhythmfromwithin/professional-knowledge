---
interest: medium
link: https://arxiv.org/abs/2604.03267
next_step: skim
priority: medium
slack_ts: '1775618432.194469'
source: cs.CV - Computer Vision
status: unread
title: A reconfigurable smart camera implementation for jet flames characterization
  based on an optimized segmentation model
---
# A reconfigurable smart camera implementation for jet flames characterization based on an optimized segmentation model
> 原文: [https://arxiv.org/abs/2604.03267](https://arxiv.org/abs/2604.03267)

arXiv:2604.03267v1 Announce Type: new
Abstract: In this work we present a novel framework for fire safety management in industrial settings through the implementation of a smart camera platform for jet flames characterization. The approach seeks to alleviate the lack of real-time solutions for industrial early fire segmentation and characterization. As a case study, we demonstrate how a SoC FPGA, running optimized Artificial Intelligence (AI) models can be leveraged to implement a full edge processing pipeline for jet flames analysis. In this paper we extend previous work on computer-vision jet fire segmentation by creating a novel experimental set-up and system implementation for addressing this issue, which can be replicated to other fire safety applications. The proposed platform is designed to carry out image processing tasks in real-time and on device, reducing video processing overheads, and thus the overall latency. This is achieved by optimizing a UNet segmentation model to make it amenable for an SoC FPGAs implementation; the optimized model can then be efficiently mapped onto the SoC reconfigurable logic for massively parallel execution. For our experiments, we have chosen the Ultra96 platform, as it also provides the means for implementing full-fledged intelligent systems using the SoC peripherals, as well as other Operating System (OS) capabilities (i.e., multi-threading) for systems management. For optimizing the model we made use of the Vitis (Xilinx) framework, which enabled us to optimize the full precision model from 7.5 million parameters to 59,095 parameters (125x less), which translated into a reduction of the processing latency of 2.9x. Further optimization (multi-threading and batch normalization) led to an improvement of 7.5x in terms of latency, yielding a performance of 30 Frames Per Second (FPS) without sacrificing accuracy in terms of the evaluated metrics (Dice Score).
