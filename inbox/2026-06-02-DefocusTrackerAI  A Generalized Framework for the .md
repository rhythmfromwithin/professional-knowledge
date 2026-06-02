---
title: "DefocusTrackerAI -- A Generalized Framework for the Automatic Detection of Defocused Particle Images"
source: "cs.CV - Computer Vision"
link: https://arxiv.org/abs/2606.00076
priority: medium
status: unread
interest: medium
next_step: skim
---
# DefocusTrackerAI -- A Generalized Framework for the Automatic Detection of Defocused Particle Images
> 原文: [https://arxiv.org/abs/2606.00076](https://arxiv.org/abs/2606.00076)

arXiv:2606.00076v1 Announce Type: new
Abstract: The present work introduces DefocusTrackerAI, a generalized deep-learning framework for the automatic detection and position estimation of defocused particle images from any kind of optical configuration without compromising uncertainty and recall, intended as a follow-up of the open-source project DefocusTracker. We selected the deep neural network architecture from the direct comparison of two well-known object detection models, Faster R-CNN and YOLOv9, trained on a diverse and feature-rich synthetic image set containing astigmatic and non-astigmatic defocused particle images of varying diameters. The model evaluation on synthetic data showed that, first, YOLOv9 outperforms Faster R-CNN, achieving higher recall and lower uncertainty, particularly at high particle image densities; and second, that YOLOv9 provides enhanced spatial resolution, with uncertainty values between 0.1 and 0.4 pixels for particle image densities N\_s up to 0.5, outperforming state-of-the-art algorithms. We demonstrated that our models are able to detect astigmatic and non-astigmatic defocused particle images in multiple optical setups with varying lighting conditions. In addition, we successfully applied our models on real DPT experiments, including fluorescence and shadowgraph data, showing that they can be used beyond conventional DPT applications, including the tracking of sprays and droplets. A pre-trained, ready-to-use version of DefocusTrackerAI based on YOLOv9 is available at https://gitlab.com/goncalo.coutinho/defocustrackerAI-main/-/tree/7e0f11f649ebad50e20dca5b9545f26ca303ebe0 and can be used for automatic detection of defocused particle images of any kind with high accuracy. In combination with a suitable calibration approach for the depth position, it can be used as an effective first step for three-dimensional defocusing particle tracking.
