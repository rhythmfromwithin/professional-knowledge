---
title: "Feature Visualization Recovers Known Cortical Selectivity from TRIBE v2"
source: "q-bio.NC - Neurons and Cognition"
link: https://arxiv.org/abs/2605.13904
priority: low
status: unread
interest: medium
next_step: skim
---
# Feature Visualization Recovers Known Cortical Selectivity from TRIBE v2
> 原文: [https://arxiv.org/abs/2605.13904](https://arxiv.org/abs/2605.13904)

arXiv:2605.13904v1 Announce Type: new
Abstract: Brain encoder models predict cortical fMRI responses from the internal activations of pretrained vision and language networks, and are typically evaluated by held-out prediction accuracy. This is a useful signal for training but a poor one for interpretation: it tells us an encoder fits the data without telling us whether it has internalized the functional organization of the brain. We propose feature visualization -- gradient ascent on the encoder's predicted activation for a target region of interest (ROI) -- as a complementary interpretability technique, and apply it to TRIBE v2 composed with V-JEPA 2 (ViT-G, 40 layers), holding both frozen and synthesizing still images for seven regions spanning the ventral and dorsal visual hierarchies. Under identical hyperparameters, the probe recovers a visible progression of increasing spatial scale and feature complexity across V1 to V4, matching the ventral-stream hierarchy. It also produces three distinctive downstream regimes: radial "frozen-motion" streaks for the middle temporal area (MT) despite static-only optimization, face-like features for the fusiform face area (FFA), and consistent rectilinear line patterns for the parahippocampal place area (PPA). Optimized FFA stimuli drive the predicted region ~4x as much as a natural face photograph, consistent with feature visualization producing adversarial super-stimuli rather than canonical exemplars. The probe is simple, differentiable, and applicable to any brain encoder with a differentiable backbone, allowing for qualitative evaluation of brain encoders.
