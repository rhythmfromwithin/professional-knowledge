---
interest: medium
link: https://arxiv.org/abs/2606.24934
next_step: skim
priority: low
slack_ts: '1782360772.797409'
source: cs.CR - Cryptography and Security
status: unread
title: Unprivileged Topology Certificates for Cloud GPU Attestation
---
# Unprivileged Topology Certificates for Cloud GPU Attestation
> 原文: [https://arxiv.org/abs/2606.24934](https://arxiv.org/abs/2606.24934)

arXiv:2606.24934v1 Announce Type: new
Abstract: Cloud GPU tenants receive a model name and a region, but cannot directly inspect the physical accelerator that runs their job. We present a software-only attestation primitive for this setting. A CUDA probe measures an SM-by-memory-region latency matrix using physical SM labels and dependent global loads. A streaming reducer commits sufficient statistics, configuration, code hashes, network evidence, and a compressed raw data archive into a certificate that a verifier can check without a GPU. The certificate supports three claims. First, the per-SM latency map is a stable physical fingerprint. Over a six-hour full-load RTX 5090 run, its median temporal jitter is 0.09 cycles, while shape-only leave-one-out classification separates distinct Blackwell dies with 100.0% accuracy. Second, cache-bypassing HBM sweeps recover hardware-class topology across generations, including a unified Volta V100 memory domain, a two-way Hopper H200 L2 split, and a Blackwell B200 two-die NV-HBI package whose 74/74 SM partition carries a 30-cycle, 15.5 ns cross-die penalty. Third, public network landmarks bind the same certificate to a coarse location. In the B200 run, 169 RIPE Atlas probes place the server within 44 km of its claimed datacentre and reject all 11 decoy sites. Together, these measurements check cloud-GPU identity, class, and coarse location without privileged access or a vendor key.
