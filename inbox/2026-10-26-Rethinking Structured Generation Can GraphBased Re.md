---
title: "Rethinking Structured Generation: Can Graph-Based Reasoning Resolve Ambiguity?"
source: "cs.CL - Computation and Language (NLP)"
link: https://arxiv.org/abs/2610.31681
priority: high
status: unread
interest: medium
next_step: skim
---
# Rethinking Structured Generation: Can Graph-Based Reasoning Resolve Ambiguity?
> 原文: [https://arxiv.org/abs/2610.31681](https://arxiv.org/abs/2610.31681)

arXiv:2610.31681v1 Announce Type: new
Abstract: Structured generation is typically formulated as a deterministic mapping from input to a single structured output. This assumption is fundamentally misaligned with natural language, which often admits multiple structurally distinct yet semantically valid interpretations. As a result, existing methods rely on single-reference supervision that collapses ambiguity into one prediction, leading to unstable and inconsistent outputs under underspecified inputs. We reformulate structured generation as an \textit{ambiguity-aware inference problem}, where the objective is to reason over a set of plausible structured outputs rather than predict a single solution. We show that standard training inherently suppresses valid alternatives, and instead adopt a multi-valid learning framework that preserves ambiguity during optimization. To operationalize this formulation, we construct a candidate space of structured outputs, represent each candidate as a graph capturing entities and their relationships, and perform selection via graph-based reasoning over semantic alignment and relational consistency. This enables principled comparison across competing interpretations beyond token-level likelihoods. Experiments on structured generation benchmarks demonstrate consistent improvements in accuracy, stability, and robustness under varying levels of ambiguity. These results highlight the importance of modeling ambiguity explicitly and suggest a shift from single-output prediction to set-level reasoning in structured generation.
