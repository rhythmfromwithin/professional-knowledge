---
title: "C8s: A Confidential Kubernetes Architecture"
source: "cs.CR - Cryptography and Security"
link: https://arxiv.org/abs/2604.26974
priority: low
status: unread
interest: medium
next_step: skim
---
# C8s: A Confidential Kubernetes Architecture
> 原文: [https://arxiv.org/abs/2604.26974](https://arxiv.org/abs/2604.26974)

arXiv:2604.26974v1 Announce Type: new
Abstract: This paper presents C8s, a confidential computing architecture for Kubernetes that provides cryptographically rooted confidentiality, integrity, and verifiability guarantees for Kubernetes clusters from infrastructure operators. These guarantees are cryptographically provable to any independent third party verifier. The architecture is built on hardware Trusted Execution Environments (TEEs), specifically AMD SEV-SNP, Intel TDX, and NVIDIA Confidential Computing support, to establish an attestation-rooted trust boundary around confidential VMs. This design is compatible with managed Kubernetes services such as Amazon EKS, Google GKE, and Microsoft AKS, where the control plane cannot be attested. Under this boundary, three groups gain guarantees that are absent from conventional deployments. Data and artifact owners can deploy sensitive workloads and proprietary artifacts on third-party infrastructure without risking exfiltration. Compute providers can offer execution services without revealing workloads to cloud operators. End users can submit requests that remain opaque to all parties except the attested TEE processing them. Representative workloads include AI inference, securing AI model weights, and training or fine-tuning on sensitive data.
