---
interest: medium
link: https://arxiv.org/abs/2605.30366
next_step: skim
priority: low
slack_ts: '1780462688.478859'
source: cs.CR - Cryptography and Security
status: unread
title: 'Escaping the Linearity Trap: Manifold Detours for Black-Box Adversarial Attacks
  on Singing Audio Deepfake Detection'
---
# Escaping the Linearity Trap: Manifold Detours for Black-Box Adversarial Attacks on Singing Audio Deepfake Detection
> 原文: [https://arxiv.org/abs/2605.30366](https://arxiv.org/abs/2605.30366)

arXiv:2605.30366v1 Announce Type: new
Abstract: Recent Singing Voice Synthesis (SVS) advances enable highly realistic but potentially malicious AI covers, making singing voice deepfake detection (SVDD) crucial. Self-Supervised Learning (SSL)-based detectors achieve state-of-the-art performance by fine-tuning speech SSL backbones to capture singing-specific spoof artifacts. Existing adversarial attacks often fail against SSL-SVDD, creating a false impression of inherent robustness. We reveal this stems from two challenges. First, at the objective level, attacks optimize cross-entropy on local surrogates, crossing surrogate-specific boundaries rather than suppressing shared spoof evidence. Second, at the method level, attacks follow the surrogate's dominant gradient direction. In SSL-SVDD, this aligns with fine-tuned artifact-sensitive directions, limiting transferability to unseen detectors - a geometric failure we term the Linearity Trap. To properly evaluate robustness, we propose MARS (Meta-Adversarial Regression of Semantics), a transfer-based black-box framework tailored to SSL-SVDD. Structurally, MARS shifts to hypothesis-evidence manipulation by constructing a natural semantic anchor from the pre-trained SSL space and an artifact anchor from the fine-tuned space. Algorithmically, MARS escapes the Linearity Trap via bi-level optimization: the inner stage induces tangential exploration, while the outer stage guides the audio toward the natural semantic manifold. Experiments on the CtrSVDD benchmark show MARS improves Attack Success Rate (ASR) in in-distribution transfer (13%), out-of-distribution transfer (10%), and cross-task evaluation (36%), highlighting the urgent need for robust SVDD systems.
