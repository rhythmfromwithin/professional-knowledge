---
title: "Privacy Failure in Split-LLM Training, The Returned Gradient Nullifies the Decoys"
source: "cs.CR - Cryptography and Security"
link: https://arxiv.org/abs/2609.04382
priority: low
status: unread
interest: medium
next_step: skim
---
# Privacy Failure in Split-LLM Training, The Returned Gradient Nullifies the Decoys
> 原文: [https://arxiv.org/abs/2609.04382](https://arxiv.org/abs/2609.04382)

arXiv:2609.04382v1 Announce Type: new
Abstract: We present a systems-security case study of a two-node split-LLM training system whose privacy evaluation passed while leaving an observable channel untested. The Trusted Local Node (TLN) sends protected activations to the Untrusted Cloud Node (UCN), the UCN returns its output, and TLN, holding the private loss, returns the output gradient. The frame the UCN receives mixes real rows with decoys, and the loss ignores the decoys. Their gradients are exactly zero, so the pattern of zeros reveals which rows were real. We measure it with a protocol fixed in advance: a leak injected at known strength to prove the instrument can see one, a shuffled-label control to prove it does not report absent leaks, and a threshold set before the runs. Across nine seeds, the zeros identified the real rows on every frame, 4,096 of 4,096 per run. An attack on the frame contents recovered about one extra token per hundred over a constant-guess baseline (+0.65 to +1.50 percentage points); the shuffled controls recovered nothing. A second set of runs repeated this on a configuration that keeps model quality within budget, so the finding is not confined to a setting nobody would deploy. On both datasets, every such run passed the forward-channel privacy check and the quality check, yet failed that same check once the returned gradient was included. Clipping and noising each row of the gradient closed the leak for about 0.01 nats of held-out cross-entropy. The system is not thereby safe: five classes of attack, including those accumulating observations across training steps, were never measured.
