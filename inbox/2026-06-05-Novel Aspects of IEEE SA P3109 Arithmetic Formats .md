---
title: "Novel Aspects of IEEE SA P3109 Arithmetic Formats for Machine Learning"
source: "cs.LG - Machine Learning"
link: https://arxiv.org/abs/2606.04028
priority: high
status: unread
interest: medium
next_step: skim
---
# Novel Aspects of IEEE SA P3109 Arithmetic Formats for Machine Learning
> 原文: [https://arxiv.org/abs/2606.04028](https://arxiv.org/abs/2606.04028)

arXiv:2606.04028v1 Announce Type: new
Abstract: The IEEE P3109 draft standard defines a parameterized family of binary floating-point formats and associated operations, with a focus on facilitating machine learning. These formats allow efficient and consistent representation of values in a small number of bits. The defined formats are parameterized over width and precision in bits, signedness, and the presence of infinities. Operations are defined by decoding floating-point values to the set of closed extended reals: the reals augmented with positive and negative infinity and NaN (Not a Number). Explicit treatment of NaN and infinite operands ensures that only real arithmetic is invoked in operation definitions. Extensive rounding and saturation modes are defined; stochastic rounding is included. Operations are exception-free, accelerating throughput, with exceptional situations communicated through return values, e.g., NaN. Operations on blocks of values sharing a common scale factor are defined in terms of the underlying operations in a uniform manner. System vendors may describe approximate implementations via a novel scale-invariant measure, akin to units in the last place, called kappa-approximation. Standard function definitions and various other properties are mechanically verified and generated using formal specifications.
