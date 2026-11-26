---
title: "How Many Samples Is RL Worth? Best-of-N versus RL Post-Training for Text-to-Image Models"
source: "cs.CV - Computer Vision"
link: https://arxiv.org/abs/2611.33232
priority: medium
status: unread
interest: medium
next_step: skim
---
# How Many Samples Is RL Worth? Best-of-N versus RL Post-Training for Text-to-Image Models
> 原文: [https://arxiv.org/abs/2611.33232](https://arxiv.org/abs/2611.33232)

arXiv:2611.33232v1 Announce Type: new
Abstract: Reinforcement learning (RL) on a reward that can be checked automatically has become a common last step in the training of text-to-image models. A simpler way to get more correct images is best-of-N: draw N images from the base model and keep the one that a picker prefers. We ask how many base model samples one RL sample is worth, and call this number the exchange rate. We measure it for Stable Diffusion 3.5 Medium and its public Flow-GRPO checkpoint on 398 new prompts in the style of GenEval, the benchmark behind the RL reward, with human labels on every prompt and two automatic judges other than the reward. The answer depends on the prompt. Four fifths of the prompts do not ask for a position (for example, one object left of another). On these, the base model catches up: best-of-16 with an off-the-shelf vision-language model (VLM) as the picker is about as good as one RL image. A person who looks through up to 3 base images finds a correct one as often as one RL image is correct. On the prompts that ask for a position, RL is far ahead: a person finds a correct image among 8 base images for only 52% of the prompts, against 92% for one RL image. Over all prompts, our primary test, which we fixed in advance, finds best-of-16 with the VLM picker 9.3 points behind one RL image when both automatic judges must pass an image. People see a smaller gap, 5.5 and 6.5 points in two checks. FLUX.1-dev shows a similar gap in the same test. RL also solves 20 prompts that the base model misses in 128 tries, and 1,024 tries recover half of them. The automatic judges are wrong in opposite directions: a detector-based judge like the reward, as used in our primary test, reports a larger gap than people see, and VLM judges report little or none. Comparisons of RL with best-of-N should therefore check the selected images by hand.
