---
title: "GISclaw: An Open-Source LLM-Powered Agent System for Full-Stack Geospatial Analysis"
source: "cs.SE - Software Engineering"
link: https://arxiv.org/abs/2603.26845
priority: low
status: unread
interest: medium
next_step: skim
---
# GISclaw: An Open-Source LLM-Powered Agent System for Full-Stack Geospatial Analysis
> 原文: [https://arxiv.org/abs/2603.26845](https://arxiv.org/abs/2603.26845)

arXiv:2603.26845v1 Announce Type: new
Abstract: The convergence of Large Language Models (LLMs) and Geographic Information Science has opened new avenues for automating complex geospatial analysis. However, existing LLM-powered GIS agents are constrained by limited data-type coverage (vector-only), reliance on proprietary GIS platforms, and single-model architectures that preclude systematic comparisons. We present GISclaw, an open-source agent system that integrates an LLM reasoning core with a persistent Python sandbox, a comprehensive suite of open-source GIS libraries (GeoPandas, rasterio, scipy, scikit-learn), and a web-based interactive interface for full-stack geospatial analysis spanning vector, raster, and tabular data. GISclaw implements two pluggable agent architectures -- a Single Agent ReAct loop and a Dual Agent Plan-Execute-Replan pipeline -- and supports six heterogeneous LLM backends ranging from cloud-hosted flagship models (GPT-5.4) to locally deployed 14B models on consumer GPUs. Through three key engineering innovations -- Schema Analysis bridging the task-data information gap, Domain Knowledge injection for domain-specific workflows, and an Error Memory mechanism for intelligent self-correction -- GISclaw achieves up to 96% task success on the 50-task GeoAnalystBench benchmark. Systematic evaluation across 600 model--architecture--task combinations reveals that the Dual Agent architecture consistently degrades strong models while providing marginal gains for weaker ones. We further propose a three-layer evaluation protocol incorporating code structure analysis, reasoning process assessment, and type-specific output verification for comprehensive GIS agent assessment. The system and all evaluation code are publicly available.
