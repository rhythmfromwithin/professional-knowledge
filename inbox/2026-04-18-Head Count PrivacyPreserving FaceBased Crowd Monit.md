---
title: "Head Count: Privacy-Preserving Face-Based Crowd Monitoring"
source: "cs.CR - Cryptography and Security"
link: https://arxiv.org/abs/2604.14250
priority: low
status: unread
interest: medium
next_step: skim
---
# Head Count: Privacy-Preserving Face-Based Crowd Monitoring
> 原文: [https://arxiv.org/abs/2604.14250](https://arxiv.org/abs/2604.14250)

arXiv:2604.14250v1 Announce Type: new
Abstract: An important aspect of crowd monitoring is knowing how many people we are dealing with. Sometimes, knowing the size of a crowd in a single location and at a specific moment is enough. Matters become problematic when counting the same people across dif ferent locations or counting them over longer periods of time. In those cases, we need to identify and later reidentify a person, which immediately leads to privacy concerns. Until recently, solutions have been based on unique identification of carry-on devices, yet privacy improvements have caused transmitted information to be randomized, rendering this technique mostly useless. We propose to use biometric data instead. We introduce a pipeline that counts people based on face recognition, yet without ever being able to reveal the identity of individuals. To count, a camera initially detects a face, extracts its features, and derives an identifier using a fuzzy extractor. The original facial image is then deleted. Identifiers are inserted into homomorphically encrypted Bloom filters. This allows oblivious set membership testing directly on encrypted data, enabling the system to count across locations or across different moments, without revealing any identities. We provide an initial evaluation of our method that shows promising results.
