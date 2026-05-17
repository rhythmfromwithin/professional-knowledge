---
interest: medium
link: https://arxiv.org/abs/2605.13930
next_step: skim
priority: high
slack_ts: '1778990759.916279'
source: cs.LG - Machine Learning
status: unread
title: Mechanistic Interpretability of EEG Foundation Models via Sparse Autoencoders
---
# Mechanistic Interpretability of EEG Foundation Models via Sparse Autoencoders
> 原文: [https://arxiv.org/abs/2605.13930](https://arxiv.org/abs/2605.13930)

arXiv:2605.13930v1 Announce Type: new
Abstract: EEG foundation models achieve state-of-the-art clinical performance, yet the internal computations driving their predictions remain opaque: a barrier to clinical trust. We apply TopK Sparse Autoencoders (SAEs) across three architecturally distinct EEG transformers: SleepFM, REVE, and LaBraM to extract sparse feature dictionaries from their embeddings. By grounding these features in a clinical taxonomy (abnormality, age, sex, and medication), we benchmark monosemanticity and entanglement across architectures. A single hyperparameter procedure, driven by an intrinsic dictionary health audit, transfers robustly across all three architectures. Via concept steering, we introduce a "target vs. off-target" probe area metric to quantify steering selectivity and reveal three operational regimes: selectively steerable, encoded but entangled, and non-encoded. This framework exposes critical representational failures: "wrecking-ball" interventions that collapse global model performance, and clinical entanglements, such as age-pathology confounding, where it is impossible to suppress one concept without corrupting the other. Finally, a spectral decoder maps these interventions back to the amplitude spectrum, translating latent manipulations into physiologically interpretable frequency signatures, such as pathological slow-wave suppression and $\alpha$-band restoration.
