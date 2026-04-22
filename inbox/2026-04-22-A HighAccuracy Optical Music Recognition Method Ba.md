---
interest: medium
link: https://arxiv.org/abs/2604.16446
next_step: skim
priority: medium
slack_ts: '1776828596.348839'
source: cs.CV - Computer Vision
status: unread
title: A High-Accuracy Optical Music Recognition Method Based on Bottleneck Residual
  Convolutions
---
# A High-Accuracy Optical Music Recognition Method Based on Bottleneck Residual Convolutions
> 原文: [https://arxiv.org/abs/2604.16446](https://arxiv.org/abs/2604.16446)

arXiv:2604.16446v1 Announce Type: new
Abstract: Optical Music Recognition (OMR) aims to convert printed or handwritten music score images into editable symbolic representations. This paper presents an end-to-end OMR framework that combines residual bottleneck convolutions with bidirectional gated recurrent unit (BiGRU)-based sequence modeling. A convolutional neural network with ResNet-v2-style residual bottleneck blocks and multi-scale dilated convolutions is used to extract features that encode both fine-grained symbol details and global staff-line structures. The extracted feature sequences are then fed into a BiGRU network to model temporal dependencies among musical symbols. The model is trained using the Connectionist Temporal Classification loss, enabling end-to-end prediction without explicit alignment annotations. Experimental results on the Camera-PrIMuS and PrIMuS datasets demonstrate the effectiveness of the proposed framework. On Camera-PrIMuS, the proposed method achieves a sequence error rate (SeER) of $7.52\%$ and a symbol error rate (SyER) of $0.45\%$, with pitch, type, and note accuracies of $99.33\%$, $99.60\%$, and $99.28\%$, respectively. The average training time is 1.74~s per epoch, demonstrating high computational efficiency while maintaining strong recognition performance. On PrIMuS, the method achieves a SeER of $8.11\%$ and a SyER of $0.49\%$, with pitch, type, and note accuracies of $99.27\%$, $99.58\%$, and $99.21\%$, respectively. A fine-grained error analysis further confirms the effectiveness of the proposed model.
