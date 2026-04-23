---
title: "OmniMouse: Scaling properties of multi-modal, multi-task Brain Models on 150B Neural Tokens"
source: "q-bio.NC - Neurons and Cognition"
link: https://arxiv.org/abs/2604.18827
priority: low
status: unread
interest: medium
next_step: skim
---
# OmniMouse: Scaling properties of multi-modal, multi-task Brain Models on 150B Neural Tokens
> 原文: [https://arxiv.org/abs/2604.18827](https://arxiv.org/abs/2604.18827)

arXiv:2604.18827v1 Announce Type: new
Abstract: Scaling data and artificial neural networks has transformed AI, driving breakthroughs in language and vision. Whether similar principles apply to modeling brain activity remains unclear. Here we leveraged a dataset of 3.1 million neurons from the visual cortex of 73 mice across 323 sessions, totaling more than 150 billion neural tokens recorded during natural movies, images and parametric stimuli, and behavior. We train multi-modal, multi-task models that support three regimes flexibly at test time: neural prediction, behavioral decoding, neural forecasting, or any combination of the three. OmniMouse achieves state-of-the-art performance, outperforming specialized baselines across nearly all evaluation regimes. We find that performance scales reliably with more data, but gains from increasing model size saturate. This inverts the standard AI scaling story: in language and computer vision, massive datasets make parameter scaling the primary driver of progress, whereas in brain modeling -- even in the mouse visual cortex, a relatively simple system -- models remain data-limited despite vast recordings. The observation of systematic scaling raises the possibility of phase transitions in neural modeling, where larger and richer datasets might unlock qualitatively new capabilities, paralleling the emergent properties seen in large language models. Code available at https://github.com/enigma-brain/omnimouse.
