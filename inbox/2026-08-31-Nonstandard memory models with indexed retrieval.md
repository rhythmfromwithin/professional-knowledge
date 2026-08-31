---
title: "Non-standard memory models with indexed retrieval"
source: "q-bio.NC - Neurons and Cognition"
link: https://arxiv.org/abs/2608.27479
priority: low
status: unread
interest: medium
next_step: skim
---
# Non-standard memory models with indexed retrieval
> 原文: [https://arxiv.org/abs/2608.27479](https://arxiv.org/abs/2608.27479)

arXiv:2608.27479v1 Announce Type: new
Abstract: The standard memory models for neural networks are variants of the Hopfield network, where feature representations are stored as vectors in a matrix. Retrieval happens based on similarity between an input vector and the set of stored vectors in a content-addressable manner such that the network evolves towards the closest stored attractor. In other words, the useful property of addressing items in memory directly by index is lost in Hopfield-style neural network models ("associative memory"). In this extended abstract, we present a new model which is extremely simple, derived from biological observation, yet introduces a significant conceptual advance and technical benefits. The goal is to establish adaptivity based on the neuron-centric hypothesis: Plasticity is organized by the neuron which regulates its own synapses. Accordingly we implemented a localist, neuron-centric one-shot learning method and applied it to a simple pattern classification problem (MNIST). We were looking for the existence of high information neurons, to act as indices into the representations. The idea was that we would be able to restore full patterns by indexed retrieval, instead of associative vector retrieval from attractors.
