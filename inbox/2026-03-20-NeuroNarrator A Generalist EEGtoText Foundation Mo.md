---
title: "NeuroNarrator: A Generalist EEG-to-Text Foundation Model for Clinical Interpretation via Spectro-Spatial Grounding and Temporal State-Space Reasoning"
source: "q-bio.NC - Neurons and Cognition"
link: https://arxiv.org/abs/2603.16880
priority: low
status: unread
interest: medium
next_step: skim
---
# NeuroNarrator: A Generalist EEG-to-Text Foundation Model for Clinical Interpretation via Spectro-Spatial Grounding and Temporal State-Space Reasoning
> 原文: [https://arxiv.org/abs/2603.16880](https://arxiv.org/abs/2603.16880)

arXiv:2603.16880v1 Announce Type: cross
Abstract: Electroencephalography (EEG) provides a non-invasive window into neural dynamics at high temporal resolution and plays a pivotal role in clinical neuroscience research. Despite this potential, prevailing computational approaches to EEG analysis remain largely confined to task-specific classification objectives or coarse-grained pattern recognition, offering limited support for clinically meaningful interpretation. To address these limitations, we introduce NeuroNarrator, the first generalist EEG-to-text foundation model designed to translate electrophysiological segments into precise clinical narratives. A cornerstone of this framework is the curation of NeuroCorpus-160K, the first harmonized large-scale resource pairing over 160,000 EEG segments with structured, clinically grounded natural-language descriptions. Our architecture first aligns temporal EEG waveforms with spatial topographic maps via a rigorous contrastive objective, establishing spectro-spatially grounded representations. Building on this grounding, we condition a Large Language Model through a state-space-inspired formulation that integrates historical temporal and spectral context to support coherent clinical narrative generation. This approach establishes a principled bridge between continuous signal dynamics and discrete clinical language, enabling interpretable narrative generation that facilitates expert interpretation and supports clinical reporting workflows. Extensive evaluations across diverse benchmarks and zero-shot transfer tasks highlight NeuroNarrator's capacity to integrate temporal, spectral, and spatial dynamics, positioning it as a foundational framework for time-frequency-aware, open-ended clinical interpretation of electrophysiological data.
