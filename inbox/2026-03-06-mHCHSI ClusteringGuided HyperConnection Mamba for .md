---
interest: medium
link: https://arxiv.org/abs/2603.03418
next_step: skim
priority: medium
slack_ts: '1773544809.239319'
source: cs.CV - Computer Vision
status: unread
title: 'mHC-HSI: Clustering-Guided Hyper-Connection Mamba for Hyperspectral Image
  Classification'
---
# mHC-HSI: Clustering-Guided Hyper-Connection Mamba for Hyperspectral Image Classification
> 原文: [https://arxiv.org/abs/2603.03418](https://arxiv.org/abs/2603.03418)

arXiv:2603.03418v1 Announce Type: new
Abstract: Recently, DeepSeek has invented the manifold-constrained hyper-connection (mHC) approach which has demonstrated significant improvements over the traditional residual connection in deep learning models \cite{xie2026mhc}. Nevertheless, this approach has not been tailor-designed for improving hyperspectral image (HSI) classification. This paper presents a clustering-guided mHC Mamba model (mHC-HSI) for enhanced HSI classification, with the following contributions. First, to improve spatial-spectral feature learning, we design a novel clustering-guided Mamba module, based on the mHC framework, that explicitly learns both spatial and spectral information in HSI. Second, to decompose the complex and heterogeneous HSI into smaller clusters, we design a new implementation of the residual matrix in mHC, which can be treated as soft cluster membership maps, leading to improved explainability of the mHC approach. Third, to leverage the physical spectral knowledge, we divide the spectral bands into physically-meaningful groups and use them as the "parallel streams" in mHC, leading to a physically-meaningful approach with enhanced interpretability. The proposed approach is tested on benchmark datasets in comparison with the state-of-the-art methods, and the results suggest that the proposed model not only improves the accuracy but also enhances the model explainability. Code is available here: https://github.com/GSIL-UCalgary/mHC\_HyperSpectral
