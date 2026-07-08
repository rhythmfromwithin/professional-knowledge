---
interest: medium
link: https://arxiv.org/abs/2607.03556
next_step: skim
priority: low
slack_ts: '1783481422.930629'
source: q-bio.NC - Neurons and Cognition
status: unread
title: Shunting Inhibition and Dendritic Branching Shape Local Credit Assignment
---
# Shunting Inhibition and Dendritic Branching Shape Local Credit Assignment
> 原文: [https://arxiv.org/abs/2607.03556](https://arxiv.org/abs/2607.03556)

arXiv:2607.03556v1 Announce Type: new
Abstract: Biological neurons assign credit across branching dendrites, where synaptic drive, dendritic conductance, local voltage, and somatic teaching signals interact to shape synaptic plasticity. We study conductance-based dendritic networks with E/I synapse banks, shunting inhibition, and tree-structured branch-to-soma coupling, and examine when restricted somatic feedback can approximate compartment-specific backpropagated errors. Exact gradients factor into local eligibility x compartment error terms: the eligibility uses presynaptic activity, driving force, and input resistance, whereas the fast non-local term is a path-specific error obtained by transporting a soma error through dendritic gains. This factorization turns local learning into a credit-signal compression problem. We test the hypothesis that shunting inhibition benefits learning under these constraints when it reshapes the compartment-error field to better match global scalar, per-soma, low-rank, or path-structured feedback. Exact-gradient reconstruction verifies the factorization; path-gain, rank, broadcast-fidelity, inhibition-intervention, and transported-error-oracle diagnostics support the proposed mechanism. Under nonnegative conductances and per-soma 5-factor (5F) feedback, shunting LocalCA remains 5--6 percentage points below matched backpropagation on MNIST, Fashion-MNIST, and figure-ground MNIST, indicating that feedback-field fidelity remains a major bottleneck. These results show how E/I conductance, shunting inhibition, and dendritic branching can reshape credit-signal geometry in restricted local learning.
