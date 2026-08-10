---
interest: medium
link: https://arxiv.org/abs/2608.04413
next_step: skim
priority: medium
slack_ts: '1786328460.875219'
source: cs.DC - Distributed Computing
status: unread
title: Zero-Instrumentation Dependency Discovery for Guided Microservice Migration
  Using eBPF
---
# Zero-Instrumentation Dependency Discovery for Guided Microservice Migration Using eBPF
> 原文: [https://arxiv.org/abs/2608.04413](https://arxiv.org/abs/2608.04413)

arXiv:2608.04413v1 Announce Type: new
Abstract: Migrating microservices across virtual machines (VMs) without knowledge of their runtime communication patterns risks creating cross-VM hotspots and latency spikes that are difficult to predict from static analysis alone. We use extended Berkeley Packet Filter (eBPF) kernel-level network tracing to automatically discover inter-service dependencies at runtime, with no application instrumentation, and use the resulting dependency graph to produce a traffic-aware migration plan ranked by return on investment (ROI). A two-pass process-identifier (PID) to port correlation algorithm recovers the identity of all 20 services in a shared-runtime testbed where processes are otherwise indistinguishable, matching the known ground-truth topology. The system discovers 32 dependency edges from 13,615 network events captured in three minutes, and applies spectral graph clustering with Kernighan-Lin refinement to partition services into VM-coherent groups. In simulation over the discovered graph, our ROI-ranked migration order reduces cumulative cross-VM traffic exposure during the migration window by 27% relative to alphabetical ordering, a deterministic proxy for arbitrary dependency-blind ordering. Collection overhead is mixed: in a controlled A/B test at near-saturation load on a host with two virtual CPUs (vCPUs), throughput fell by only 4.4%, but median (p50) latency rose by 383% and 99th-percentile (p99) latency by 1,050%. We therefore recommend running captures off-peak or on dedicated sampling nodes rather than under production saturation. All results are from a single 20-service testbed that we authored; we make no claim about behavior on production dependency graphs.
