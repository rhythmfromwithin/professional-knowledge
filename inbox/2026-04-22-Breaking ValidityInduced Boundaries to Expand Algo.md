---
interest: medium
link: https://arxiv.org/abs/2604.16420
next_step: skim
priority: low
slack_ts: '1776828600.656989'
source: cs.NE - Neural and Evolutionary Computing
status: unread
title: 'Breaking Validity-Induced Boundaries to Expand Algorithm Search Space: A Two-Stage
  AST-Based Operator for LLM-Driven Automated Heuristic Evolution'
---
# Breaking Validity-Induced Boundaries to Expand Algorithm Search Space: A Two-Stage AST-Based Operator for LLM-Driven Automated Heuristic Evolution
> 原文: [https://arxiv.org/abs/2604.16420](https://arxiv.org/abs/2604.16420)

arXiv:2604.16420v1 Announce Type: new
Abstract: Large Language Model (LLM) based automated heuristic design (AHD) has shown great potential in discovering efficient heuristics. Most existing LLM-AHD frameworks use semantic evolutionary operators that rely entirely on the LLM's pre-trained knowledge. These one-stage methods strictly require the generated code to be valid during the operation and often rely on a ``thought-code'' representation. We argue that this end-to-end generation fundamentally limits the exploration ability within the algorithm search space.
In this paper, we propose a two-stage, structure-based evolutionary operator for LLM-AHD. In the first stage, our approach directly performs crossover and mutation on the Abstract Syntax Trees (ASTs) of the heuristic code, intentionally generating diverse but often invalid structural variants. In the second stage, the LLM is employed to repair these invalid heuristics into executable, high-quality code. Depending on the underlying framework, either the raw invalid variants or the repaired heuristics are integrated into the population to preserve potential structural patterns. We demonstrate that the proposed operator can significantly enhance the search ability of state-of-the-art LLM-AHD algorithms, such as EoH-S. Experimental results on the Traveling Salesman Problem (TSP) and the Online Bin Packing Problem (OBP) show that our method effectively improves both optimization performance and convergence speed.
