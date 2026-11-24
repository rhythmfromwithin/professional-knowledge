---
title: "torchtsetlin: Fast, Interpretable Tsetlin Machines for PyTorch"
source: "cs.AI - Artificial Intelligence"
link: https://arxiv.org/abs/2611.28195
priority: high
status: unread
interest: medium
next_step: skim
---
# torchtsetlin: Fast, Interpretable Tsetlin Machines for PyTorch
> 原文: [https://arxiv.org/abs/2611.28195](https://arxiv.org/abs/2611.28195)

arXiv:2611.28195v1 Announce Type: new
Abstract: The Tsetlin machine learns propositional rules with teams of Tsetlin automata that are driven by reward and penalty rather than gradients, so its models are interpretable by construction and cheap to evaluate. Its software, however, consists of C and CUDA kernels behind scikit-learn-style wrappers that sit outside the deep learning ecosystem. torchtsetlin implements the Tsetlin machine family as ordinary PyTorch modules: vanilla and weighted, coalesced, regression, convolutional over sequences, images and volumes, and dense per-pixel segmentation. The automata are a tensor buffer, so a model moves with .to(device), is saved with state\_dict() and learns from a mini-batch with one update(x,y) call. Its core technique is a batched formulation of Type I and Type II feedback, in which automaton transitions become event counts realised as binomial draws, with one commit per mini-batch. On ten benchmarks taken from the existing libraries, it matches their accuracy, and on all but the two smallest it trains 2.4-10.9X faster than PyTsetlinMachineCUDA and 10.3-81.2X faster than tmu on the same GPU. The package is pure Python, MIT-licensed and on PyPI; every number in this paper is reproduced by one script. Code: https://github.com/vlbthambawita/torchtsetlin; package: https://pypi.org/project/torchtsetlin/.
