---
title: "Context-aware Simopt-Power: Using structural data with simulation metadata to optimise FPGA designs"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2605.27446
priority: medium
status: unread
interest: medium
next_step: skim
---
# Context-aware Simopt-Power: Using structural data with simulation metadata to optimise FPGA designs
> 原文: [https://arxiv.org/abs/2605.27446](https://arxiv.org/abs/2605.27446)

arXiv:2605.27446v1 Announce Type: new
Abstract: Pre-implementation behavioural simulation routinely validates functional correctness, yet it also produces rich switching-activity traces that are typically discarded by FPGA computer-aided design (CAD) flows. Prior simulation-guided and power-aware FPGA optimisations demonstrate the promise of exploiting this metadata, but many rely on fixed thresholds, narrow decision heuristics, or limited design awareness, often incurring substantial area overhead. This paper presents Context-aware Simopt-Power, a simulator-guided optimisation framework that combines activity metadata with lightweight structural features (sequential proximity, logic-depth proxies, and fan-out estimates) to more precisely target high-impact regions of the netlist. We additionally remove empirically tuned constants, replacing them with architecture-aware parameters such as LUT size and mapping constraints, and evaluate trade-offs using power, delay, and a more useful metrics, area-delay product (AD) and power-delay product (PD). Implemented in an open-source Yosys/ABC flow and evaluated on the complex Koios deep-learning accelerator benchmarks, Context-aware Simopt-Power achieves an average 6.8% dynamic-power reduction while limiting LUT overhead to 11.2%, thus enabling a holistic design optimisation.
