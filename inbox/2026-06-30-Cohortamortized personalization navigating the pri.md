---
interest: medium
link: https://arxiv.org/abs/2606.30329
next_step: skim
priority: low
slack_ts: '1782792821.088109'
source: q-bio.NC - Neurons and Cognition
status: unread
title: 'Cohort-amortized personalization: navigating the privacy-utility frontier
  for virtual brain twins'
---
# Cohort-amortized personalization: navigating the privacy-utility frontier for virtual brain twins
> 原文: [https://arxiv.org/abs/2606.30329](https://arxiv.org/abs/2606.30329)

arXiv:2606.30329v1 Announce Type: new
Abstract: Personalized generative brain models require individual neuroimaging data that privacy constraints and re-identification risk make difficult to share, while per-subject fitting procedures cost hours of compute -- limiting clinical translation and multi-site collaboration. We introduce cohort-amortized personalization (CAP), which replaces data sharing with model sharing: a neural density estimator is trained on simulations from a mechanistic whole-brain model under a low-rank cohort prior, and only the compact estimator is distributed, so new subjects are personalized in seconds on their own data alone. To make this prior both compact and atlas-independent, a cross-atlas autoencoder (CrossCoder) maps connectomes from 20 anatomical atlases into a shared latent space, enabling deployment across sites with heterogeneous atlases. We validate CAP on two cohorts: 21 patients with drug-resistant epilepsy (epileptogenic-zone localization F1=0.56) and 832 subjects from the 1000BRAINS aging cohort (predicted age r=0.44); in both, CAP matches or exceeds per-subject inference with hours-to-seconds speed-up. Because the shared artifact couples a cohort prior to a mechanistic simulator, it can serve as a mechanistic surrogate supporting in-silico experimentation and synthetic-cohort generation without raw-data access -- a governance-audited alternative we term synthetic access, allowing for wider adoption of personalized modeling in more diverse settings.
