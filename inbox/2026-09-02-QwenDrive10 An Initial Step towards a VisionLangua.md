---
title: "Qwen-Drive-1.0: An Initial Step towards a Vision-Language Foundation Model for Autonomous Driving"
source: "cs.CV - Computer Vision"
link: https://arxiv.org/abs/2609.00111
priority: medium
status: unread
interest: medium
next_step: skim
---
# Qwen-Drive-1.0: An Initial Step towards a Vision-Language Foundation Model for Autonomous Driving
> 原文: [https://arxiv.org/abs/2609.00111](https://arxiv.org/abs/2609.00111)

arXiv:2609.00111v1 Announce Type: new
Abstract: We present Qwen-Drive-1.0, an initial step towards a vision-language foundation model for autonomous driving. Qwen-Drive-1.0 retains the architecture of the pretrained vision-language model (VLM) and integrates 3D perception, visual question answering, and motion planning within a unified framework. An external bird's-eye-view (BEV) perception head jointly performs 3D object detection, semantic occupancy prediction, and BEV map segmentation. It serves as a probe of the 3D information accessible from the shared representations and provides an explicit, inspectable interface to 3D scene structure. A Planning Expert conditions on shared VLM representations to generate future ego trajectories. A staged training recipe combines driving supervision with general-purpose vision-language data to acquire driving-specific competence while helping preserve broad visual understanding and instruction-following capabilities. Experiments demonstrate strong 3D perception and driving scene understanding while largely preserving general vision-language capability. Comprehensive evaluations across open-loop, pseudo-closed-loop, and closed-loop settings further show highly competitive motion-planning performance.
