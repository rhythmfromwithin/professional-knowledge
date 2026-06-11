---
interest: medium
link: https://arxiv.org/abs/2606.11416
next_step: skim
priority: low
slack_ts: '1781153118.859829'
source: cs.CR - Cryptography and Security
status: unread
title: 'MPC-Patch-Bench: Security-Aware LLM Code Patch for Multi-Party Computation'
---
# MPC-Patch-Bench: Security-Aware LLM Code Patch for Multi-Party Computation
> 原文: [https://arxiv.org/abs/2606.11416](https://arxiv.org/abs/2606.11416)

arXiv:2606.11416v1 Announce Type: new
Abstract: Repository-level benchmarks for evaluating Large Language Model (LLM) code repair on Secure Multi-Party Computation (MPC) software do not yet exist, and directly transplanting general-purpose benchmarks such as SWE-bench fails on three structural fronts: (i) MPC repositories are dominated by generic Python infrastructure rather than cryptographic logic; (ii) high-value MPC fixes lack the standardized tests rigid extraction pipelines require; and (iii) standard fail-to-pass evaluation is insufficient for code that must also be cryptographically safe. MPC is increasingly deployed for privacy-preserving machine learning, biomedical collaboration, and secure analytics. Existing MPC-specific code-synthesis efforts cover only operator-level or single-framework tasks; evaluating LLM agents on real repository-level MPC repair instead demands MPC-aware data curation and a verifier matched to the security and numerical-fidelity guarantees MPC programs must obey neither of which existing benchmarks provide. We introduce MPC-Patch-Bench, a repository-level benchmark organised around two frameworks. (1)The Data Curation Framework combines a domain-specific curation agent that filters raw pull requests through three cryptographic layers with a human-AI completion engine that synthesizes missing problem statements and Fail-to-Pass/Pass-to-Pass tests, yielding 205 fully verified instances. (2)The MPC Verifier provides dedicated security and numerical-fidelity checks via dynamic differential testing against plaintext oracles and MPC-specific static analysis rules that flag unsafe reveals, insecure arithmetic, and illegal public/private casts. The strongest evaluated LLM functionally resolves only 22.9% of MPC-Patch-Bench tasks; the MPC Verifier further reduces verified resolution to 17.1%, with up to 40% of functionally-passing patches rejected for cryptographic or numerical-fidelity violations.
