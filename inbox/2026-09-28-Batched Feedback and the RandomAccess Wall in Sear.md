---
title: "Batched Feedback and the Random-Access Wall in Search-Based Graph Construction"
source: "cs.DB - Databases"
link: https://arxiv.org/abs/2609.30493
priority: low
status: unread
interest: medium
next_step: skim
---
# Batched Feedback and the Random-Access Wall in Search-Based Graph Construction
> 原文: [https://arxiv.org/abs/2609.30493](https://arxiv.org/abs/2609.30493)

arXiv:2609.30493v1 Announce Type: new
Abstract: Navigable graphs for nearest-neighbor search are built either incrementally, each inserted point searching a graph that mutates as construction proceeds, or in batch over a fixed substrate, which buys determinism and parallelism at a price in build time. We measure that price and find where it comes from. Instrumenting a tuned Vamana and PiPNN and building every system repeatedly in a paired design on one 64-thread machine, we separate build time into work (distance evaluations) and cost per evaluation. Letting the batch builder's substrate mutate in $B$ synchronous blocks recovers the feedback loop of incremental construction while the graph stays a function of (data, seed, parameters, $B$): eight trees with batched feedback match thirty-two frozen trees, and the build does $0.88\times$ Vamana's distance work. Yet it takes $1.55\times$ Vamana's wall-clock, because the mutating substrate costs more per evaluation.
Pushing further, we find a wall that no search-based builder crosses. Every one of them, incremental or batched, evaluates distances adaptively, one dependent random access at a time, and runs $20$-$27\times$ below a dense kernel on the same machine at $d \approx 100$, five to six times of it with the data resident in cache. The gap is not a low-dimension artifact: an adaptive evaluation costs $d^{1.04}$ and a blocked one $d^{0.63}$, so the wall grows as $d^{0.4}$ and is twice as high at $d = 960$ as at $d = 128$. PiPNN's order-of-magnitude build advantage is that kernel: it evaluates as many distances per point, but as fixed-in-advance dense blocks. We show the beam cannot be batched after the fact (the useful density of a lockstep block is 2-3%), state the wall as a two-ceiling roofline, and delimit it: it binds whenever the distance is a black box or the evaluation order is data-dependent.
