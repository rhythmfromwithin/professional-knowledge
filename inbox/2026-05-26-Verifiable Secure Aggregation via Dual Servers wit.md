---
title: "Verifiable Secure Aggregation via Dual Servers with Linear Tags in Federated Learning"
source: "cs.CR - Cryptography and Security"
link: https://arxiv.org/abs/2605.24054
priority: low
status: unread
interest: medium
next_step: skim
---
# Verifiable Secure Aggregation via Dual Servers with Linear Tags in Federated Learning
> 原文: [https://arxiv.org/abs/2605.24054](https://arxiv.org/abs/2605.24054)

arXiv:2605.24054v1 Announce Type: new
Abstract: Federated learning (FL) enables collaborative model training by aggregating local updates without requiring raw data sharing. However, prior studies have shown that servers can exploit gradient inversion to compromise user privacy or manipulate aggregation results, undermining the utility of the global model. To address these concerns, we propose a secure and verifiable aggregation scheme with lightweight cryptographic primitives for FL. Our method leverages pseudo-random functions (PRFs) and a non-colluding dual-server architecture to achieve secure aggregation with mutual server verification, while maintaining communication overhead comparable to plaintext aggregation and a constant verification tag size. Crucially, it preserves user privacy and achieves end-to-end secure aggregation with verification. Moreover, our scheme significantly reduces both user computation and verification overhead, making it suitable for FL with a large number of participants. For instance, with an input dimension of 20K, user computation time is reduced to 18 ms, approximately 7$\times$ faster than OPSA, while verification time decreases to 9.5 ms, approximately 2.4$\times$ faster than OPSA.
