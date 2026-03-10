---
title: "HLER: Human-in-the-Loop Economic Research via Multi-Agent Pipelines for Empirical Discovery"
source: "econ.GN - General Economics (AI Economics)"
link: https://arxiv.org/abs/2603.07444
priority: low
status: unread
interest: medium
next_step: skim
---
# HLER: Human-in-the-Loop Economic Research via Multi-Agent Pipelines for Empirical Discovery
> 原文: [https://arxiv.org/abs/2603.07444](https://arxiv.org/abs/2603.07444)

arXiv:2603.07444v1 Announce Type: cross
Abstract: Large language models (LLMs) have enabled agent-based systems that aim to automate scientific research workflows. Most existing approaches focus on fully autonomous discovery, where AI systems generate research ideas, conduct analyses, and produce manuscripts with minimal human involvement. However, empirical research in economics and the social sciences poses additional constraints: research questions must be grounded in available datasets, identification strategies require careful design, and human judgment remains essential for evaluating economic significance. We introduce HLER (Human-in-the-Loop Economic Research), a multi-agent architecture that supports empirical research automation while preserving critical human oversight. The system orchestrates specialized agents for data auditing, data profiling, hypothesis generation, econometric analysis, manuscript drafting, and automated review. A key design principle is dataset-aware hypothesis generation, where candidate research questions are constrained by dataset structure, variable availability, and distributional diagnostics, reducing infeasible or hallucinated hypotheses. HLER further implements a two-loop architecture: a question quality loop that screens and selects feasible hypotheses, and a research revision loop where automated review triggers re-analysis and manuscript revision. Human decision gates are embedded at key stages, allowing researchers to guide the automated pipeline. Experiments on three empirical datasets show that dataset-aware hypothesis generation produces feasible research questions in 87% of cases (versus 41% under unconstrained generation), while complete empirical manuscripts can be produced at an average API cost of $0.8-$1.5 per run. These results suggest that Human-AI collaborative pipelines may provide a practical path toward scalable empirical research.
