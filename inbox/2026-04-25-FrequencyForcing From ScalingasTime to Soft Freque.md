---
interest: medium
link: https://arxiv.org/abs/2604.20902
next_step: skim
priority: high
slack_ts: '1777174931.301679'
source: cs.LG - Machine Learning
status: unread
title: 'Frequency-Forcing: From Scaling-as-Time to Soft Frequency Guidance'
---
# Frequency-Forcing: From Scaling-as-Time to Soft Frequency Guidance
> 原文: [https://arxiv.org/abs/2604.20902](https://arxiv.org/abs/2604.20902)

arXiv:2604.20902v1 Announce Type: new
Abstract: While standard flow-matching models transport noise to data uniformly, incorporating an explicit generation order - specifically, establishing coarse, low-frequency structure before fine detail - has proven highly effective for synthesizing natural images. Two recent works offer distinct paradigms for this. K-Flow imposes a hard frequency constraint by reinterpreting a frequency scaling variable as flow time, running the trajectory inside a transformed amplitude space. Latent Forcing provides a soft ordering mechanism by coupling the pixel flow with an auxiliary semantic latent flow via asynchronous time schedules, leaving the pixel interpolation path itself untouched. Viewed from the angle of improving pixel generation, we observe that forcing - guiding generation with an earlier-maturing auxiliary stream - offers a highly compatible route to scale-ordered generation without rewriting the core flow coordinate. Building on this, we propose Frequency-Forcing, which realizes K-Flow's frequency ordering through Latent Forcing's soft mechanism: a standard pixel flow is guided by an auxiliary low-frequency stream that matures earlier in time. Unlike Latent Forcing, whose scratchpad relies on a heavy pretrained encoder (e.g., DINO), our frequency scratchpad is derived from the data itself via a lightweight learnable wavelet packet transform. We term this a self-forcing signal, which avoids external dependencies while learning a basis better adapted to data statistics than the fixed bases used in hard frequency flows. On ImageNet-256, Frequency-Forcing consistently improves FID over strong pixel- and latent-space baselines, and naturally composes with a semantic stream to yield further gains. This illustrates that forcing-based scale ordering is a versatile, path-preserving alternative to hard frequency flows.
