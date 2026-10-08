---
title: "Scaling subjects in cross-modal alignment: video decoding with EEG foundation model"
source: "q-bio.NC - Neurons and Cognition"
link: https://arxiv.org/abs/2610.09287
priority: low
status: unread
interest: medium
next_step: skim
---
# Scaling subjects in cross-modal alignment: video decoding with EEG foundation model
> 原文: [https://arxiv.org/abs/2610.09287](https://arxiv.org/abs/2610.09287)

arXiv:2610.09287v1 Announce Type: new
Abstract: Naturalistic visual decoding from EEG has long been constrained by cohort size: existing scaling literature caps out at a few dozen subjects, leading prior work to conclude that scaling subject cohorts yields minimal performance gains. Training a cross-modal EEG--video contrastive encoder on a cohort larger by more than an order of magnitude, we find the axis is productive but has an onset. Below $S\approx50$ --- the entirety of the range prior work occupies --- no model improves meaningfully over an untrained encoder; above it, decoding rises log-linearly in subject count with no saturation at the top of our ladder, on a fitted stimulus-feature probe and on fit-free movie-moment retrieval alike, and the gain transfers to a second, unseen film. How far the axis carries then depends on initialisation more than on capacity: an encoder initialised from an EEG foundation model scales ${\sim}1.6\times$ faster per doubling of the cohort than randomly initialised encoders at two depths, is the only one still converting subjects into retrieval accuracy at the top of the ladder, and converges on a fraction of the alignment compute. Subject scaling on shared naturalistic stimuli is thus an effective and currently unsaturated frontier for scaling EEG foundation models.
