---
title: "Topology-Constrained Quantized nnUNet for Efficient and Anatomically Accurate 3D Tooth Segmentation"
source: "cs.CV - Computer Vision"
link: https://arxiv.org/abs/2605.04201
priority: medium
status: unread
interest: medium
next_step: skim
---
# Topology-Constrained Quantized nnUNet for Efficient and Anatomically Accurate 3D Tooth Segmentation
> 原文: [https://arxiv.org/abs/2605.04201](https://arxiv.org/abs/2605.04201)

arXiv:2605.04201v1 Announce Type: new
Abstract: We propose a topology-constrained quantized nnUNet framework for efficient and anatomically accurate 3D tooth segmentation, addressing the challenges of spatial distortion introduced by quantization in deep learning models. The proposed method integrates a novel tooth-specific topological loss into quantization-aware training, preserving critical anatomical structures such as tooth count, adjacency relationships, and cavity integrity while maintaining computational efficiency. The system employs an 8-bit quantized nnUNet backbone, where weights and activations are dynamically calibrated to minimize precision loss during inference. Furthermore, the topological loss combines connected-component analysis, adjacency consistency, and hole detection penalties, ensuring anatomical fidelity without modifying the underlying network architecture. The joint optimization objective harmonizes cross-entropy loss, quantization regularization, and topological constraints, enabling end-to-end training with gradient approximations for persistent homology terms. Experiments demonstrate that our approach significantly reduces topological errors compared to conventional quantized models, achieving clinically plausible segmentations on dental CBCT scans. The method retains the hardware efficiency of integer-only inference, making it suitable for deployment in resource-constrained clinical environments. This work bridges the gap between computational efficiency and anatomical precision in medical image segmentation, offering a practical solution for real-world dental applications.
