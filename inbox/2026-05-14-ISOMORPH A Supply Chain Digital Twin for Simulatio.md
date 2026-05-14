---
title: "ISOMORPH: A Supply Chain Digital Twin for Simulation, Dataset Generation, and Forecasting Benchmarks"
source: "stat.ML - Machine Learning (Statistics)"
link: https://arxiv.org/abs/2605.12768
priority: medium
status: unread
interest: medium
next_step: skim
---
# ISOMORPH: A Supply Chain Digital Twin for Simulation, Dataset Generation, and Forecasting Benchmarks
> 原文: [https://arxiv.org/abs/2605.12768](https://arxiv.org/abs/2605.12768)

arXiv:2605.12768v1 Announce Type: new
Abstract: Open time-series forecasting (TSF) benchmarks cover retail, energy, weather, and traffic, but supply-chain logistics remains underserved. We introduce ISOMORPH, the first public digital twin of a multi-echelon logistics network with fully interpretable, user-configurable parameters and modular topology, demand process, and control rules. The simulator advances a directed routing graph in discrete time: demand arrives at the destination, is served from stock or recorded as backlog, and triggers replenishment through the network. The state vector tracks per-node on-hand inventory with outstanding orders, in-transit shipments, and a smoothed demand estimate, so the dynamics close as a Markov chain on a tractable state space whose transition kernel acts linearly on the empirical distribution of the state. The released data reproduces the bullwhip effect at empirically consistent magnitudes, and three conservation laws encoded in the Markov chain serve as verification tools when users extend the simulator. We release datasets at two catalogue scales ($C=50$ and $C=200$) with six scenario sweeps producing 30 additional rollouts and 20 Latin-hypercube perturbations, exhibiting dynamics absent from fixed TSF benchmarks: variance amplification, cascading bottlenecks, regime shifts, and cross-channel coupling through shared macro shocks. Zero-shot evaluation of four foundation models (Chronos, Moirai, TimesFM, Lag-Llama) shows MASE values exceeding public GIFT-Eval references at low-to-moderate horizons, supporting incorporation into existing benchmarks. The same pairing produces forecast confidence bands via Latin-hypercube perturbation of demand-side knobs, forward UQ from parameter uncertainty unavailable on standard TSF datasets, demonstrating that foundation models can serve as fast surrogates for the digital twin's forward UQ. Code (MIT): https://github.com/tuhinsahai/ISOMORPH.
