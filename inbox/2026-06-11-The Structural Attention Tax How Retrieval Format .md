---
interest: medium
link: https://arxiv.org/abs/2606.11198
next_step: skim
priority: high
slack_ts: '1781153123.844299'
source: cs.CL - Computation and Language (NLP)
status: unread
title: 'The Structural Attention Tax: How Retrieval Format Hijacks In-Context Learning
  Independent of Content'
---
# The Structural Attention Tax: How Retrieval Format Hijacks In-Context Learning Independent of Content
> 原文: [https://arxiv.org/abs/2606.11198](https://arxiv.org/abs/2606.11198)

arXiv:2606.11198v1 Announce Type: new
Abstract: Retrieval-augmented generation (RAG) systems inject external knowledge to improve LLM outputs, yet the format of injected content -- distinct from its semantic relevance -- can independently distort the model's attention distribution. We identify and formalise a phenomenon we term the structural attention tax: knowledge graph (KG) triples, due to their relational delimiters and repeated slot patterns, capture 2-3x more attention per token than semantically equivalent natural-language text ($\hat{o}$(KG) $\approx$ 0.70 vs. $\hat{o}$(neutral) $\approx$ 0.25), compressing demonstration attention by up to 42% -- regardless of whether the triples are relevant or noise. We develop a formal framework decomposing attention scores into semantic and structural components (Eq. 2), derive a compression bound (Proposition 1) connecting token-level format bias to demonstration attention loss, and show that the structural term governs how much attention is diverted while the semantic term governs whether this helps or hurts. This decoupling reveals two orthogonal axes for improving retrieval-augmented ICL: optimising retrieval quality (semantic axis) and reducing format-driven attention capture (structural axis). Empirically, across two model families (Mistral-7B, LLaMA-3-8B) and three QA benchmarks, we observe that source-task alignment dominates: task-matched BM25 retrieval achieves 58-62% on HotpotQA vs. ConceptNet's 25-27%, a >30 pp gap that dwarfs all gating strategies ($\leq$2 pp). We derive five structure-aware mitigation strategies from the framework, ranging from zero-cost prompt modifications to training-time regularisation; format flattening (S3) is validated by both accuracy and attention-level evidence from a verbalized-triple control, while structural dispersal (S1) yields mixed results that illuminate the challenges of format-level intervention.
