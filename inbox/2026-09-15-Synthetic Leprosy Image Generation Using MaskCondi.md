---
title: "Synthetic Leprosy Image Generation Using Mask-Conditioned Latent Diffusion and Transfer Learning from Large Chronic Wound Datasets"
source: "cs.CV - Computer Vision"
link: https://arxiv.org/abs/2609.13226
priority: medium
status: unread
interest: medium
next_step: skim
---
# Synthetic Leprosy Image Generation Using Mask-Conditioned Latent Diffusion and Transfer Learning from Large Chronic Wound Datasets
> 原文: [https://arxiv.org/abs/2609.13226](https://arxiv.org/abs/2609.13226)

arXiv:2609.13226v1 Announce Type: new
Abstract: Machine learning for neglected tropical diseases is limited by data, not algorithms: public annotated image sets for leprosy (Hansen's disease) number in the hundreds, orders of magnitude below what generative models require. We ask whether a model trained on abundant chronic wound photography transfers to this low-data regime. We build a three-stage pipeline. First, a DeepLabV3-ResNet50 segmentation network (validation Dice 0.876, IoU 0.799) supplies lesion masks for two wound datasets that ship without them. Second, we assemble a mask-conditioned latent diffusion model from Stable Diffusion 1.5 components and train it on 3,280 region-of-interest wound crops, widening the UNet input convolution from 4 to 11 channels to admit three mask feature maps and a blurred low-frequency context latent. Third, we fine-tune this model on 708 leprosy image-mask pairs drawn from 764 images of approximately 150 patients. We evaluate with LPIPS perceptual distance, anchored by a real-versus-real baseline computed on the same 242 anchor images as the cross-set comparisons; without that reference the cross-set distances cannot be interpreted. The generated set shows no mode collapse: its internal perceptual diversity (0.662) is statistically indistinguishable from that of the real leprosy set (0.672, 95% CI [0.664, 0.680]). Generated images sit 0.044 LPIPS outside the real distribution - measurably apart, but under half of one standard deviation. Fine-tuning shifted the output distribution only marginally, which we trace to lesion geometry reaching the network through input concatenation alone. Chronic wound photography is therefore a viable donor domain for leprosy lesion synthesis: low-level appearance transfers well, and the remaining barrier is semantic control rather than image quality.
