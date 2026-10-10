---
interest: medium
link: https://arxiv.org/abs/2610.08929
next_step: skim
priority: medium
slack_ts: '1791610128.034249'
source: cs.DC - Distributed Computing
status: unread
title: Part of the Strassen algorithm can speed up matrix multiplication in a parallel
  pebbling game
---
# Part of the Strassen algorithm can speed up matrix multiplication in a parallel pebbling game
> 原文: [https://arxiv.org/abs/2610.08929](https://arxiv.org/abs/2610.08929)

arXiv:2610.08929v1 Announce Type: new
Abstract: We present a novel variant of the Strassen algorithm called the Partial Strassen algorithm, which uses a fraction of the Strassen steps to perform matrix multiplication in less time than traditional implementations. The memory footprint required to implement this algorithm is provably small whether used with a single thread or in a multi-threaded context. Data comparing the Partial Strassen algorithm at depths one, two, and three with BLAS matrix multiplication show that the three-level Partial Strassen algorithm is able to perform matrix multiplication in $80\%$ the time of BLAS with $2.25$ times the memory requirement, with a theoretical improvement of $75\%$ for sufficiently large matrices. The Partial Strassen algorithm is also compared against an implementation of the traditional Strassen algorithm, and is shown to be more performant with increasing matrix size due to decreased memory consumption. An open source implementation of the Partial Strassen algorithm for arbitrary depth and rectangular matrix multiplication is also included.
