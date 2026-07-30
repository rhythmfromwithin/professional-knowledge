---
title: "Reading Without a Reader: Large Language Models Collapse Reading and Writing into a Single Entangled Code"
source: "q-bio.NC - Neurons and Cognition"
link: https://arxiv.org/abs/2607.24797
priority: low
status: unread
interest: medium
next_step: skim
---
# Reading Without a Reader: Large Language Models Collapse Reading and Writing into a Single Entangled Code
> 原文: [https://arxiv.org/abs/2607.24797](https://arxiv.org/abs/2607.24797)

arXiv:2607.24797v1 Announce Type: new
Abstract: In the literate human brain, reading and writing are two doubly-dissociable systems: a ventral decoding route (impaired in pure alexia) and a fronto-parietal encoding route (impaired in pure agraphia), sharing a partial orthographic core. A decoder-only large language model (LLM) instead drives both from a single autoregressive path optimized on text, a recent cultural invention rather than an evolved instinct. We ask how entangled that one mechanism is, comparing an input-side "reading code" $W\_E$ with an output-side "writing code" $W\_U$ via an entanglement index $E \in [0,1]$ (CKA, Procrustes residual, mutual $k$-NN) calibrated against an independent-init floor and a tied ceiling. Across nine probes on GPT-2, OPT, Pythia (14M--1.4B), T5, and BERT/RoBERTa (six consolidating established results, three introducing the read/write analysis), two complementary levels agree in direction. In the weights, untied models hold one coupled but sub-ceiling code ($E=0.23$--$0.35$, far above floor) on a non-monotonic couple-then-differentiate trajectory, with $W\_U$ drifting $\sim 3.2\times$ farther than $W\_E$ in every frequency decile. In behaviour, comprehension and production are positively coupled in all 12 non-degenerate models (sign test $p<0.001$), the opposite of the brain's double dissociation. This coupling is general, not decoder-only: encoder--decoders separate the two pathways representationally (up to 0.96) yet stay behaviourally coupled. We report our nulls plainly (the geometry $\rightarrow$ behaviour bridge is null, $\rho=0.00$). Because a single forward path makes some coupling expected a priori, our contribution is its quantification and cross-level concordance; by analogy, not homology, this situates LLMs as a distinct point in the space of possible minds.
