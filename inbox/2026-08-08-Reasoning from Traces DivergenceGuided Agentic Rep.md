---
interest: medium
link: https://arxiv.org/abs/2608.05521
next_step: skim
priority: low
slack_ts: '1786154734.386859'
source: cs.SE - Software Engineering
status: unread
title: 'Reasoning from Traces: Divergence-Guided Agentic Repair of WebAssembly Discrepancies'
---
# Reasoning from Traces: Divergence-Guided Agentic Repair of WebAssembly Discrepancies
> 原文: [https://arxiv.org/abs/2608.05521](https://arxiv.org/abs/2608.05521)

arXiv:2608.05521v1 Announce Type: new
Abstract: WebAssembly (Wasm) promises seamless reuse of C/C++ codebases as portable, fast, sandboxed binaries. In practice, however, this promise often falls short: recent studies show that cross-compiling the same C/C++ source to Wasm and native binaries frequently leads to runtime discrepancies, owing to library implementation differences or compiler bugs. Since the root causes lie in the platform-level runtime and are hidden beneath the source code, even state-of-the-art LLM-based repair agents often fail to fix these discrepancies. In this paper, we present WasmMend, the first system to automatically repair Native-Wasm functional discrepancies. WasmMend converts the undirected exploration to a focused reasoning task in two stages: First, a novel differential trace analysis approach localizes the function where Wasm and native executions initially diverge; guided by this localization, LLM agents then reason about the root causes and generate patches that eliminate the divergent behavior. Experiments on real-world C/C++ projects show that WasmMend achieves a fix rate of 70.0%, compared to 50.2% for the agentic baseline and 54.5\% for the approach augmented with repair-time LLM-based instrumentation, demonstrating the value of divergence-guided reasoning for cross-platform repair.
