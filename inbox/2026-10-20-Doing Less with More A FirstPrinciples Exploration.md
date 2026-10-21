---
interest: medium
link: https://arxiv.org/abs/2610.23921
next_step: skim
priority: high
slack_ts: '1792556397.916749'
source: cs.AI - Artificial Intelligence
status: unread
title: 'Doing Less with More: A First-Principles Exploration of the Suitability of
  Agentic Computing over Alternative Architectural Choices'
---
# Doing Less with More: A First-Principles Exploration of the Suitability of Agentic Computing over Alternative Architectural Choices
> 原文: [https://arxiv.org/abs/2610.23921](https://arxiv.org/abs/2610.23921)

arXiv:2610.23921v1 Announce Type: new
Abstract: There is growing interest in automating business activities with Agentic Artificial Intelligence (AI) due to latter's seeming ease of use. Never has it been easier, or costlier, to do less with more. However, little is known about when agents are preferable to established alternatives such as local computation, Representational State Transfer (REST), the Simple Object Access Protocol (SOAP), and the Model Context Protocol (MCP), particularly when development speed, performance, and operational cost are considered. We investigate this question using a controlled mathematical task that compares seven methods on a benchmark of 1,000 arithmetic expressions where semantics of operator precedence has to be preserved. We ran this setup across a native Function Calling baseline (Python library), REST, SOAP and MCP microservice architectures, direct responses from large language models (LLMs) using a Groq cloud API and five locally deployed Ollama models, and agentic systems in which five local LLMs invoke MCP tools. The deterministic methods achieve 100% accuracy with negligible latency. Direct LLM evaluation achieves at most 92.9% accuracy at over 22,000x the latency of a native function call. With MCP tools, the best agent reaches 99.9% accuracy, but incurs nearly 1,000,000x the baseline latency. These results demonstrate that LLMs approaches are poorly suited for exact arithmetic evaluation and motivate an informed architectural decision framework (ADF) for choosing an architecture based on accuracy and throughput requirements. We recognize that an actual interaction with an agent may span both reasoning and linguistic tasks. Hence our recommendation is to explore multiple architectural choices (based on task type) rather than one-size-fits-all solution (LLMs).
Code is available at - https://github.com/Ritvik-G/adf/
