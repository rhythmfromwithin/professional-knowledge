---
interest: medium
link: https://arxiv.org/abs/2607.09833
next_step: skim
priority: low
slack_ts: '1784172048.320539'
source: cs.CR - Cryptography and Security
status: unread
title: Generative Testing of Automated Speech Recognition Systems
---
# Generative Testing of Automated Speech Recognition Systems
> 原文: [https://arxiv.org/abs/2607.09833](https://arxiv.org/abs/2607.09833)

arXiv:2607.09833v1 Announce Type: new
Abstract: Automatic speech recognition (ASR) systems have achieved high accuracy with transformer-based models, enabling deployment in critical applications. However, they remain vulnerable to adversarial manipulation, particularly in black-box settings where attacks must preserve perceptual naturalness. This work introduces GATAS, a black-box testing approach that generates failure inducing inputs by operating in the phoneme-level latent space of a text- to-speech model. Instead of perturbing waveforms directly, the approach interpolates latent representations to induce transcription errors while remaining within the manifold of natural speech. The attack is formulated as a multi-objective optimization problem balancing semantic divergence and perceptual quality. Our empirical evaluation against both white-box and black-box baselines shows that GATAS achieves a 98% success rate while producing lower distortion and higher perceptual quality, as confirmed by human studies. Despite operating without gradient access, GATAS remains competitive against white-box methods, highlighting that representation and perceptual alignment are more critical than access to model internals. Overall, our results demonstrate that untargeted latent-space optimization enables the efficient generation of realistic and effective test cases for ASR systems.
