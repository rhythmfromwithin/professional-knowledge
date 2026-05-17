---
interest: medium
link: https://arxiv.org/abs/2605.14020
next_step: skim
priority: low
slack_ts: '1778990760.009689'
source: cs.CR - Cryptography and Security
status: unread
title: Memory Forensics Techniques for Automated Detection and Analysis of Go Malware
---
# Memory Forensics Techniques for Automated Detection and Analysis of Go Malware
> 原文: [https://arxiv.org/abs/2605.14020](https://arxiv.org/abs/2605.14020)

arXiv:2605.14020v1 Announce Type: new
Abstract: The Go programming language has become increasingly popular among malware developers due to its ability to produce statically linked, cross-platform executables that challenge traditional analysis techniques. These binaries embed a substantial runtime and compiler-generated metadata and are compiled with aggressive optimizations that discard type information for function parameters and local variables. Go's design further complicates analysis by representing strings as pointer-length pairs rather than null-terminated sequences, employing a caller-allocated stack model that obscures argument boundaries, and fragmenting program state across concurrent goroutines. Although existing static analysis and reverse engineering tools provide Go-specific support, they remain limited to compile-time artifacts and cannot recover runtime execution state and artifacts that persist solely in memory. To address this gap, we present the first memory forensics framework for runtime analysis of Go binaries. By parsing Go's internal structures, our framework reconstructs type and function metadata, recovers heap-allocated and static strings, and distinguishes application-level functions. Through ABI-aware backward analysis, it derives execution paths and argument values from call sites. To capture runtime state beyond what static analysis reveals, it analyzes goroutine stacks to identify actively executing functions and recover their runtime argument values. We implemented all capabilities as Volatility 3 plugins and evaluated them against malware seen in recent incidents, such as the BRICKSTORM backdoor, Obscura ransomware, and Pantegana RAT, as well as open-source samples for reproducibility. The framework successfully recovered C2 endpoints, persistence mechanisms, encryption keys, ransom notes, and execution state, including critical runtime artifacts that were absent from published threat intelligence.
