---
title: "Riding the Fixed-Point Curve: Image Classification in the Continuous Thought Machine"
source: "cs.NE - Neural and Evolutionary Computing"
link: https://arxiv.org/abs/2610.19220
priority: low
status: unread
interest: medium
next_step: skim
---
# Riding the Fixed-Point Curve: Image Classification in the Continuous Thought Machine
> 原文: [https://arxiv.org/abs/2610.19220](https://arxiv.org/abs/2610.19220)

arXiv:2610.19220v1 Announce Type: cross
Abstract: The Continuous Thought Machine (CTM) is a recurrent network that attends to inputs and makes predictions based on the synchronization between its neurons. On tasks spanning many domains, it displays emergent thought processes that have not been explained. We report a number of findings about how the CTM classifies images, focusing on ImageNet. Each thinking step is an attracting but strongly non-normal map exhibiting balanced amplification (Murphy and Miller, 2009); while attraction is already present at CTM initialization, training highly promotes non-normality. By Banach's theorem, the neural state has a locally unique attracting fixed point, which moves at every step, and the thought trajectory is the curve these fixed points trace, followed one tick behind. Most of that curve's motion is shared across images, and visible as a previously reported traveling wave of activity across neurons. The attention schedule along the thought is largely generic: shuffling queries across images at every tick costs only 7 percent of classification accuracy, while image-independent increments predict the next query with R^2 = 0.98 (held out). Our results suggest that the CTM has found a single strategy to process all ImageNet images.
