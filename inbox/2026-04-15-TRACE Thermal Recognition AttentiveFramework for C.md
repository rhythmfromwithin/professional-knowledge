---
interest: medium
link: https://arxiv.org/abs/2604.09648
next_step: skim
priority: medium
slack_ts: '1776310487.023189'
source: cs.CV - Computer Vision
status: unread
title: 'TRACE: Thermal Recognition Attentive-Framework for CO2 Emissions from Livestock'
---
# TRACE: Thermal Recognition Attentive-Framework for CO2 Emissions from Livestock
> 原文: [https://arxiv.org/abs/2604.09648](https://arxiv.org/abs/2604.09648)

arXiv:2604.09648v1 Announce Type: new
Abstract: Quantifying exhaled CO2 from free-roaming cattle is both a direct indicator of rumen metabolic state and a prerequisite for farm-scale carbon accounting, yet no existing system can deliver continuous, spatially resolved measurements without physical confinement or contact. We present TRACE (Thermal Recognition Attentive-Framework for CO2 Emissions from Livestock), the first unified framework to jointly address per-frame CO2 plume segmentation and clip-level emission flux classification from mid-wave infrared (MWIR) thermal video. TRACE contributes three domain-specific advances: a Thermal Gas-Aware Attention (TGAA) encoder that incorporates per-pixel gas intensity as a spatial supervisory signal to direct self-attention toward high-emission regions at each encoder stage; an Attention-based Temporal Fusion (ATF) module that captures breath-cycle dynamics through structured cross-frame attention for sequence-level flux classification; and a four-stage progressive training curriculum that couples both objectives while preventing gradient interference. Benchmarked against fifteen state-of-the-art models on the CO2 Farm Thermal Gas Dataset, TRACE achieves an mIoU of 0.998 and the best result on every segmentation and classification metric simultaneously, outperforming domain-specific gas segmenters with several times more parameters and surpassing all baselines in flux classification. Ablation studies confirm that each component is individually essential: gas-conditioned attention alone determines precise plume boundary localization, and temporal reasoning is indispensable for flux-level discrimination. TRACE establishes a practical path toward non-invasive, continuous, per-animal CO2 monitoring from overhead thermal cameras at commercial scale. Codes are available at https://github.com/taminulislam/trace.
