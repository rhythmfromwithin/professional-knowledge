---
interest: medium
link: https://arxiv.org/abs/2607.16612
next_step: skim
priority: medium
slack_ts: '1784777491.234499'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: Backpropagation-Free Trunk Training via the Split Forward Gradients
---
# Backpropagation-Free Trunk Training via the Split Forward Gradients
> 原文: [https://arxiv.org/abs/2607.16612](https://arxiv.org/abs/2607.16612)

arXiv:2607.16612v1 Announce Type: new
Abstract: Backpropagation makes training deep networks memory intensive because it must store intermediate activations. Forward-mode methods avoid this cost, but their gradient estimates become increasingly noisy as the number of trained parameters grows. We introduce Split Forward Gradient (Split-FG), which splits a network at an intermediate representation: it computes the output head gradient exactly and estimates only the trunk gradient with a Jacobian--vector product. This reduces estimator variance and requires no backward pass through the trunk, while retaining an Adam-style convergence guarantee. Our experiments reveal an important practical failure mode. On WikiText-103, naive forward-gradient training of the trunk performs worse than leaving a randomly initialized trunk frozen, likely because Adam updates every noisy, under-determined trunk coordinate too aggressively. Simply using a much smaller learning rate for the trunk reverses this result: a $16$M-parameter GPT-2-style model reaches validation perplexity $387$, compared with $668$ for the frozen-trunk control and $2{,}885$ for a matched pure forward-gradient baseline (backpropagation reaches $150$). Split-FG also produces the strongest backprop-free results on our tabular benchmarks and reaches $60.5\%$ on CIFAR-10 and $35.2\%$ on CIFAR-100 with a heavy-head design. It reduces peak memory by up to $35\%$ relative to matched backpropagation, although the performance gap widens as the forward-mode trunk grows.
