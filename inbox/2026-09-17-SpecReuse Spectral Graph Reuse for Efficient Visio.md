---
title: "SpecReuse: Spectral Graph Reuse for Efficient Vision GNN Inference on FPGAs"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2609.17718
priority: medium
status: unread
interest: medium
next_step: skim
---
# SpecReuse: Spectral Graph Reuse for Efficient Vision GNN Inference on FPGAs
> 原文: [https://arxiv.org/abs/2609.17718](https://arxiv.org/abs/2609.17718)

arXiv:2609.17718v1 Announce Type: new
Abstract: Dynamic Image Graph Construction (DIGC) is the primary performance bottleneck in FPGA acceleration of Vision Graph Neural Networks (ViGs), reconstructing graph connectivity at every layer through irregular, memory-intensive computation. Existing FPGA accelerators optimize DIGC but still execute it unconditionally, making repeated graph reconstruction a persistent source of latency and energy consumption. We propose the SpecReuse algorithm, which computes compact spectral descriptors of intermediate features and reuses previously constructed graphs when descriptor drift remains below a calibrated threshold. We further present the SpecReuse accelerator, an FPGA architecture that realizes graph reuse through lightweight hardware for spectral descriptor extraction and reuse control while remaining compatible with existing graph-construction accelerators. Experimental results demonstrate up to a $2.69\times$ speedup in end-to-end inference and approximately 58--65\% lower energy per inference with negligible FPGA resource overhead and minimal loss in classification accuracy.
