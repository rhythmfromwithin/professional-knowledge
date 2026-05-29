---
interest: medium
link: https://arxiv.org/abs/2605.28962
next_step: skim
priority: medium
slack_ts: '1780028408.270069'
source: cs.CV - Computer Vision
status: unread
title: Resolving Endpoint Underfitting in Diffusion Bridges via Noise Alignment
---
# Resolving Endpoint Underfitting in Diffusion Bridges via Noise Alignment
> 原文: [https://arxiv.org/abs/2605.28962](https://arxiv.org/abs/2605.28962)

arXiv:2605.28962v1 Announce Type: new
Abstract: Diffusion bridge models offer a powerful framework for connecting two data distributions, such as in image restoration and translation. Many existing methods learn this bridge by mimicking the score-matching formulation of standard diffusion models. In this work, we find that this way leads to an anomalous underfitting phenomenon near the target endpoint, as the process approaches the target distribution ($t \to 0$). This underfitting, characterized by significant drift in the predicted variance and direction, results from an excessively large discrepancy in noise levels between the network's input and its regression target.To resolve this issue, we propose the Noise-Aligned Diffusion Bridge (NADB).Our approach reformulates the diffusion bridge by first employing a mean network to provide a cleaner conditional target, and then introducing a novel, noise-aligned mapping relationship. This new formulation resolves the noise mismatch and corrects the underfitting near the target endpoint. Experimental validation across multiple image restoration and image translation tasks demonstrates the effectiveness of our approach. Code is available at https://github.com/gyr02/NADB.
