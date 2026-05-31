---
interest: medium
link: https://arxiv.org/abs/2605.28845
next_step: skim
priority: medium
slack_ts: '1780202385.152289'
source: cs.DC - Distributed Computing
status: unread
title: 'HPC-vQPU: A Service-Export Architecture for Virtual QPUs on Batch-Scheduled
  HPC Systems'
---
# HPC-vQPU: A Service-Export Architecture for Virtual QPUs on Batch-Scheduled HPC Systems
> 原文: [https://arxiv.org/abs/2605.28845](https://arxiv.org/abs/2605.28845)

arXiv:2605.28845v1 Announce Type: new
Abstract: Device-aware quantum simulation increasingly requires HPC-scale accelerators, yet secure supercomputers expose batch-scheduled execution environments rather than the interactive, backend-oriented interfaces expected by quantum software. The key obstacle is not only remote job submission: an HPC-hosted virtual QPU must preserve topology, native-gate, and calibration semantics across queue delay, scheduler allocation, compute-node isolation, and partial execution-side failures, without opening inbound paths into the cluster.
We present HPC-vQPU, a service-export architecture for virtual QPUs on batch-scheduled HPC systems. HPC-vQPU separates a cloud-facing control plane, which owns device identity, task lifecycle, snapshot binding, and event projection, from an HPC-resident execution plane, which claims work and realises it through scheduler-backed GPU jobs. Coordination is exclusively outbound and agent initiated. The central abstraction is a topology- and calibration-aware device snapshot bound atomically at claim time and carried into execution as an immutable contract, making each scheduled job hermetic while preserving fresh device semantics.
We implement HPC-vQPU at the Pawsey Supercomputing Research Centre using Setonix GPUs, Qiskit-Aer/cuQuantum, and IBM Fez calibration data. Production experiments show that service overhead is bounded and additive, while workload scaling remains confined to the simulator; calibration-bearing snapshots produce measurable output shifts; claim-time binding prevents stale execution after pre-claim device mutation; concurrent agents complete 50/50 tasks exactly once; and explicit recovery restores stale running tasks after agent failure. These results show that secure, scheduler-mediated HPC infrastructure can export device-faithful quantum simulation as an interactive virtual-QPU service.
