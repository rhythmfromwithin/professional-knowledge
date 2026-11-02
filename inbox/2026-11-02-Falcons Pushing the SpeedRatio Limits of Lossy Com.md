---
interest: medium
link: https://arxiv.org/abs/2610.41209
next_step: skim
priority: medium
slack_ts: '1793597883.000789'
source: cs.DC - Distributed Computing
status: unread
title: 'Falcons: Pushing the Speed-Ratio Limits of Lossy Compression for Parallel
  Scientific Applications'
---
# Falcons: Pushing the Speed-Ratio Limits of Lossy Compression for Parallel Scientific Applications
> 原文: [https://arxiv.org/abs/2610.41209](https://arxiv.org/abs/2610.41209)

arXiv:2610.41209v1 Announce Type: new
Abstract: The extreme volume of scientific data has become a critical challenge for modern exa-scale scientific computing applications, and error-bounded lossy compression remains indispensable for scientific data management due to its high data reduction rate and controllable data fidelity. However, to ensure sufficient data reduction, existing compressors incur prohibitive computational overheads in real-world parallel scientific computing applications. To overcome the performance bottlenecks of error-bounded lossy compression, we present \textbf{Falcons}, a broadly deployable error-bounded lossy compressor that simultaneously achieves \textbf{high compression ratios with ultra-fast throughput, minimizing the overhead in parallel scientific applications}. Falcons integrates three key designs: memory-regularized interpolation with SIMD (Single Instruction Multiple Data) vectorization, distribution-adaptive lossless coding, and application-oriented optimizations for multiple parallelization schemes. Across our evaluations on cutting-edge supercomputers, Falcons clearly outperforms state-of-the-art compressors, simultaneously achieving up to 29\% compression ratio improvement and 255\% throughput improvement. In case studies of real-world applications, Falcons accelerates large-scale parallel data I/O and remote transfer by up to 44.6\% and 51.5\%, and provides 1.55$\times$ end-to-end speedup for the full WRF (Weather Research \& Forecasting) application workflow.
