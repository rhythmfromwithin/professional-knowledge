---
title: "Rank-Aware Resource Scheduling for Tightly-Coupled MPI Workloads on Kubernetes"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2603.22691
priority: medium
status: unread
interest: medium
next_step: skim
---
# Rank-Aware Resource Scheduling for Tightly-Coupled MPI Workloads on Kubernetes
> 原文: [https://arxiv.org/abs/2603.22691](https://arxiv.org/abs/2603.22691)

arXiv:2603.22691v1 Announce Type: new
Abstract: Fully provisioned Message Passing Interface (MPI) parallelism achieves near-optimal wall-clock time for Computational Fluid Dynamics (CFD) solvers. This work addresses a complementary question for shared, cloud-managed clusters: can fine-grained CPU provisioning reduce resource reservation of low-load subdomains, improving cluster packing efficiency without unacceptably degrading performance?
We propose rank-aware resource scheduling on Kubernetes, mapping each MPI rank to a pod whose CPU request is proportional to its subdomain cell count. We also demonstrate In-Place Pod Vertical Scaling (Kubernetes v1.35 GA) for mid-simulation CPU adjustment without pod restart.
Three findings emerge. First, hard CPU limits via the Linux CFS bandwidth controller cause 78x slowdown through cascading stalls at MPI\_Allreduce barriers; requests-only allocation eliminates throttling entirely. Second, on non-burstable c5.xlarge instances, concentric decomposition with equal CPU is 19% faster than the Scotch baseline, while adding proportional CPU yields a further 3% improvement. Third, at 16 MPI ranks on 101K-cell meshes, proportional allocation is 20% faster than equal allocation while reducing sparse-subdomain provisioned CPU by 82%, freeing 6.5 vCPU of scheduling headroom.
Experiments are conducted on AWS EC2 c5.xlarge clusters (4-16 ranks) running k3s v1.35. All scripts and data are released as open source.
