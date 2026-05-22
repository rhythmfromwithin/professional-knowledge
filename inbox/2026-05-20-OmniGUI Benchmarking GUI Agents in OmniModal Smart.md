---
interest: medium
link: https://arxiv.org/abs/2605.18758
next_step: skim
priority: low
slack_ts: '1779423488.756019'
source: cs.HC - Human-Computer Interaction
status: unread
title: 'OmniGUI: Benchmarking GUI Agents in Omni-Modal Smartphone Environments'
---
# OmniGUI: Benchmarking GUI Agents in Omni-Modal Smartphone Environments
> 原文: [https://arxiv.org/abs/2605.18758](https://arxiv.org/abs/2605.18758)

arXiv:2605.18758v1 Announce Type: new
Abstract: Current benchmarks for graphical user interface (GUI) agents predominantly rely on static screenshots. However, real-world smartphone interaction routinely requires agents to process transient audio cues and temporal video dynamics that are tightly coupled with the moment of action. To bridge this gap, we introduce OmniGUI, the first step-level benchmark designed to evaluate GUI agents in omni-modal smartphone environments. OmniGUI provides continuous, interleaved multimodal inputs comprising static images, synchronous audio, and video clips at every action step. The dataset encompasses 709 expert-demonstrated episodes (2,579 action steps) across 29 applications, systematically annotated with objective multimodal dependency levels. Because dedicated omni-modal GUI agent frameworks are currently in their nascent stage, we select foundational omni-modal models capable of natively processing interleaved inputs to serve as agent proxies for our initial baselines. Our empirical evaluation reveals that while current models exhibit competency on visually static tasks, their action prediction performance degrades significantly in environments requiring synchronous temporal and auditory signals. Furthermore, ablation studies isolate specific operational bottlenecks, notably cross-modal interference when processing task-irrelevant environmental noise. The complete dataset, evaluation pipeline, and baseline prompts are provided in the supplementary material. Project page: https://omni-gui.github.io.
