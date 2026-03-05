---
title: "Quantifying Frontier LLM Capabilities for Container Sandbox Escape"
source: "cs.CR - Cryptography and Security"
link: https://arxiv.org/abs/2603.02277
priority: low
status: unread
---
# Quantifying Frontier LLM Capabilities for Container Sandbox Escape
> 原文: [https://arxiv.org/abs/2603.02277](https://arxiv.org/abs/2603.02277)

arXiv:2603.02277v1 Announce Type: new
Abstract: Large language models (LLMs) increasingly act as autonomous agents, using tools to execute code, read and write files, and access networks, creating novel security risks. To mitigate these risks, agents are commonly deployed and evaluated in isolated "sandbox" environments, often implemented using Docker/OCI containers. We introduce SANDBOXESCAPEBENCH, an open benchmark that safely measures an LLM's capacity to break out of these sandboxes. The benchmark is implemented as an Inspect AI Capture the Flag (CTF) evaluation utilising a nested sandbox architecture with the outer layer containing the flag and no known vulnerabilities. Following a threat model of a motivated adversarial agent with shell access inside a container, SANDBOXESCAPEBENCH covers a spectrum of sandboxescape mechanisms spanning misconfiguration, privilege allocation mistakes, kernel flaws, and runtime/orchestration weaknesses. We find that, when vulnerabilities are added, LLMs are able to identify and exploit them, showing that use of evaluation like SANDBOXESCAPEBENCH is needed to ensure sandboxing continues to provide the encapsulation needed for highly-capable models.
