---
title: "URCHIN: A Horizontal Spiking Language Model for Data-Constrained Pretraining"
source: "q-bio.NC - Neurons and Cognition"
link: https://arxiv.org/abs/2609.13899
priority: low
status: unread
interest: medium
next_step: skim
---
# URCHIN: A Horizontal Spiking Language Model for Data-Constrained Pretraining
> 原文: [https://arxiv.org/abs/2609.13899](https://arxiv.org/abs/2609.13899)

arXiv:2609.13899v1 Announce Type: new
Abstract: The BabyLM challenge measures how much language a model can learn from developmentally-plausible, child-scale data rather than internet-scale corpora, yet prior language models forgo the biological constraints of the neural circuitry that acquires human language: spiking neurons separated into excitatory and inhibitory populations wired by a recurrent lateral connectome. This paper presents URCHIN (Unified Recurrent Connectome with Horizontal Integrate-and-fire Neurons), which applies the Parallelized Hierarchical Connectome Spiking State-space Model (PHCSSM) to language modeling: leaky integrate-and-fire neurons coupled by a Dale's-law lateral connectome resolve each token through a multi-transmission loop that recirculates activity to a fixed point. The instantiation is deliberately minimal: a single horizontal layer of 128 neurons, no attention, and 4.23M parameters. Two implementations share one set of weights and produce identical benchmark scores, so URCHIN is trained once and deployed either way with no conversion step: a parallel state-space model (SSM) scan that is GPU-efficient for training, or an event-driven recurrent spiking neural network (RSNN) with constant-cost inference for CPU or neuromorphic edge deployment. Across all three BabyLM tracks (Strict-100M, Strict-Small, and Multilingual), URCHIN offers a biologically plausible, efficient, and directly deployable reference point.
