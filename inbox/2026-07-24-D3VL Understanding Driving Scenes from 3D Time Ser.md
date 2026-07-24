---
title: "D3VL: Understanding Driving Scenes from 3D Time Series Data and Video with Language Models"
source: "cs.CV - Computer Vision"
link: https://arxiv.org/abs/2607.19528
priority: medium
status: unread
interest: medium
next_step: skim
---
# D3VL: Understanding Driving Scenes from 3D Time Series Data and Video with Language Models
> 原文: [https://arxiv.org/abs/2607.19528](https://arxiv.org/abs/2607.19528)

arXiv:2607.19528v1 Announce Type: new
Abstract: Recent advances in Multimodal Large Language Models (MLLMs) have triggered the development of end-to-end MLLMs for autonomous driving. However, the main emphasis to date has been for MLLMs using 2D images and videos. In contrast, this paper considers MLLM effectiveness using 3D sensors, particularly LiDAR and stereo cameras. LiDAR presents unique challenges to integration within an MLLM, largely because of data sparsity and lack of a grid structure for the data. For similar reasons, fusion of camera and LiDAR data within an MLLM pipeline is also uncommon. However, most autonomous systems rely on LiDAR-based sensing, and incorporating 3D data has been proven to improve performance in traditional 3D scene perception tasks. This paper presents D3VL, a novel MLLM framework that integrates 2D and 3D time-series data in a single but simple architecture. The model aims to answer questions involving traffic scene understanding and safety. D3VL shows an 11% improvement in the KITTI Question-Answering (QA) dataset compared to baseline methods in processing 2D and 3D time-series data. This paper further introduces the Waymo QA dataset extension, which assesses models' capabilities in processing 3D and time-series data under diverse driving conditions. D3VL implementation code and WaymoQA extension can be found on our supplemental website: https://automotivesafety-lvlm.github.io
