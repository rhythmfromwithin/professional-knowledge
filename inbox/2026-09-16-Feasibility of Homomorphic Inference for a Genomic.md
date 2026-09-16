---
title: "Feasibility of Homomorphic Inference for a Genomic Foundation Model"
source: "cs.CR - Cryptography and Security"
link: https://arxiv.org/abs/2609.16211
priority: low
status: unread
interest: medium
next_step: skim
---
# Feasibility of Homomorphic Inference for a Genomic Foundation Model
> 原文: [https://arxiv.org/abs/2609.16211](https://arxiv.org/abs/2609.16211)

arXiv:2609.16211v1 Announce Type: new
Abstract: Human genomic sequences can identify individuals, cannot be replaced after disclosure, and are the inputs that genomic foundation models are designed to interpret. We assess whether a compute provider can execute a released genomic foundation model without receiving query-derived genomic values in plaintext and whether correctness, memory, or cost prevents complete encrypted inference. We first reproduce the released model on three genomic task families and freeze an independently validated numerical reference. We then implement a client-assisted approximate homomorphic encryption protocol: the provider evaluates linear algebra on ciphertexts, while the key-holding data owner evaluates exact normalization, causal softmax, and activation functions at fixed boundaries. A noninteractive configuration completes one released-weight block but exceeds the tested accelerator-memory envelope when configured for composition. The client-assisted configuration executes all released transformer blocks and the task head for one heldout genomic-signal input at its full prompt length. It matches the frozen final label, peaks at 9,839 mebibytes of accelerator memory, and completes in 6,683 seconds on one accelerator. These results establish arithmetic feasibility for a complete classifier, while repeatability, network transport, and private token-index lookup remain unresolved. The biomedical significance is that, under the stated threat model, a served genomic model can process an encoded sequence without exposing plaintext queryderived activations to the compute provider.
