---
title: "AutoTrace: From Patches to Triggers via Agentic Interprocedural Exploration"
source: "cs.SE - Software Engineering"
link: https://arxiv.org/abs/2607.12058
priority: low
status: unread
interest: medium
next_step: skim
---
# AutoTrace: From Patches to Triggers via Agentic Interprocedural Exploration
> 原文: [https://arxiv.org/abs/2607.12058](https://arxiv.org/abs/2607.12058)

arXiv:2607.12058v1 Announce Type: new
Abstract: Given a vulnerability-fixing commit, trigger localization asks which specific statement turns the vulnerable program state into a concrete unsafe operation. This question is harder than binary vulnerability detection because the answer demands interprocedural, causal reasoning: in a substantial fraction of real-world CVEs the triggering statement lies several call layers outside the patched function, beyond the reach of static rule sets and pattern-matching language models alike. We present AutoTrace, an agentic pipeline that localizes vulnerability triggers by exploring a code property graph layer by layer, with LLM agents deciding where to look next and deterministic admissibility gates deciding what evidence is required before a trigger can be reported. Agents never accept a trigger on their own authority; every reported trigger is backed by explicit evidence drawn from the graph, so the pipeline covers both intra- and interprocedural vulnerabilities without relying on ungrounded model judgment. On the full InterPVD benchmark, AutoTrace reaches 75.0% VulnHit and 80.8% FuncHit, surpassing the prior state of the art on the same corpus. Building on the same machinery, we construct SinkTrace-Bench, a dataset that exposes each vulnerability as a source-to-sink (S2S) causal chain from attacker-controlled input through propagation to the dangerous operation, drawn from matched vulnerable and patched program states. It comprises 1,542 verifier-confirmed, perfectly balanced vulnerable/safe samples whose label fidelity we audit against expert annotations. Benchmarking frontier LLMs on it, we find that even the strongest struggle to separate the matched pairs, exposing the causal-reasoning gap that trigger localization targets. Artifact available at https://github.com/Erroristotle/AutoTrace.
