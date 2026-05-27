---
interest: medium
link: https://arxiv.org/abs/2605.22874
next_step: skim
priority: high
slack_ts: '1779856024.311439'
source: cs.AI - Artificial Intelligence
status: unread
title: 'NeuroNL2LTL: A Neurosymbolic Framework for Natural Language Translation of
  Linear Temporal Logic'
---
# NeuroNL2LTL: A Neurosymbolic Framework for Natural Language Translation of Linear Temporal Logic
> 原文: [https://arxiv.org/abs/2605.22874](https://arxiv.org/abs/2605.22874)

arXiv:2605.22874v1 Announce Type: new
Abstract: Effectively translating between natural language (NL) and formal logics like Linear Temporal Logic (LTL) requires expertise that limits formal verification's reach in safety-critical development. Template-based approaches sacrifice expressiveness for reliability; neural methods achieve fluency but provide no correctness guarantees. We present NeuroNL2LTL, a neurosymbolic architecture unifying learned translation with formal verification. NeuroNL2LTL routes translation through an intermediate representation whose mapping to LTL is structure-preserving by construction. Generated specifications undergo satisfiability and non-triviality checking; a minimal-edit repair mechanism corrects near-miss outputs before they reach downstream tools. The central innovation is verifier-in-the-loop training: verification outcomes serve as reward signals for reinforcement learning, producing neural components that optimize directly for formal correctness. On 200,000+ requirements spanning aerospace, robotics, autonomous vehicles, and ten additional domains, NeuroNL2LTL achieves 28\% semantic equivalence with reference specifications while ensuring 86\% of outputs are verified satisfiable. The system also generates contextually grounded explanations from LTL, enabling domain experts to validate specifications without specialized training. This work demonstrates that formal verification can function as both training objective and runtime filter for neural specification systems, allowing us to build neural-based tools whose reliability derives from logical guarantees rather than statistical confidence.
