---
title: "Offering Microsecond-Scale Cross-VM Core Elasticity on Colocated Lightweight Virtual Machines"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2608.12633
priority: medium
status: unread
interest: medium
next_step: skim
---
# Offering Microsecond-Scale Cross-VM Core Elasticity on Colocated Lightweight Virtual Machines
> 原文: [https://arxiv.org/abs/2608.12633](https://arxiv.org/abs/2608.12633)

arXiv:2608.12633v1 Announce Type: new
Abstract: Serverless platforms commonly colocate many diverse workloads, each in a fast-booting, memory-lean virtual machine (VM), to improve deployment density. Overprovisioning each VM for its peak protects tail latency during traffic bursts but hurts density; maintaining high density while effectively protecting tail latency requires the infrastructure to be able to shift physical cores, at a microsecond timescale, to whichever latency-sensitive VM is bursting and reclaim them as the burst subsides. No VM substrate delivers this: conventional VMs resize a guest's cores only through a millisecond-scale vCPU hot-plug path, Firecracker fixes a VM's core count at boot, and the ultralight VMs that boot fastest drop multicore execution entirely.
We present HyperFlux, a commodity-KVM ultralight VM substrate that makes a VM's parallelism width (the number of physical cores backing it) elastic at runtime. We show that HyperFlux can move a core across VMs in merely 13$\mu$s, even when forcibly reclaiming it from a busy donor, orders of magnitude faster than vCPU hot-plug. A HyperFlux VM incurs only a 3.2MB memory footprint and can cold-boot in 1.37ms, on par with the fastest-booting ultralight VMs, while uniquely supporting multicore parallelism. Under colocation, it can reduce high-priority VMs' tail latency by up to 10x under high load compared to static core-sharing with Firecracker and Cloud Hypervisor, and deliver a lower and more stable tail latency compared to using cgroup and vCPU hot-plug under changing load bursts.
