---
interest: medium
link: https://arxiv.org/abs/2609.23317
next_step: skim
priority: low
slack_ts: '1790051350.925559'
source: q-bio.NC - Neurons and Cognition
status: unread
title: Chaotic Dynamics-Regulated Topological Learning for Patient-Specific Preictal
  State Identification
---
# Chaotic Dynamics-Regulated Topological Learning for Patient-Specific Preictal State Identification
> 原文: [https://arxiv.org/abs/2609.23317](https://arxiv.org/abs/2609.23317)

arXiv:2609.23317v1 Announce Type: new
Abstract: Epileptic seizures arise from complex, nonlinear interactions within brain networks, yet reliable electroencephalographic (EEG) prediction remains challenging due to the nonstationary and heterogeneous nature of neural dynamics. Existing methods typically analyze EEG data as static or weakly time-dependent snapshots, overlooking the intrinsic dynamics and lacking the geometric sensitivity to capture the hierarchical, localized evolution of the epileptogenic zone. To address these limitations, we propose an offline, patient-specific evaluation of chaotic dynamics-regulated topological learning (CDRTL) for distinguishing preictal from interictal EEG states. This framework unifies chaotic dynamics, multiscale algebraic topology, and local network differentiation. Specifically, we partition EEG signals into discrete functional subnets based on correlation strengths, capturing the multi-scale connectivity of the brain. By modeling each node as a Lorenz oscillator, we embed the underlying chaotic dynamics into the network architecture. We then apply the persistent Laplacian to simultaneously extract topological invariants and geometric shape evolution through harmonic and non-harmonic spectral analysis. Additionally, a node-removal topological differentiation strategy isolates localized neural contributions. Our framework was evaluated on the CHB-MIT database using balanced preictal and interictal labels and stratified channel-level cross-validation within each patient. The results support offline discrimination of preictal and interictal channel-level nodes within fixed patient-specific networks. Because representations are constructed from the complete network, including held-out unlabeled nodes, before cross-validation, the reported performance is specific to this transductive setting and does not establish generalization to unseen EEG windows, seizures, or patients.
