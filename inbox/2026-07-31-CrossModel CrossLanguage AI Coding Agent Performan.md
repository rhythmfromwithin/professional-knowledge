---
interest: medium
link: https://arxiv.org/abs/2607.26083
next_step: skim
priority: low
slack_ts: '1785469013.499709'
source: cs.SE - Software Engineering
status: unread
title: 'Cross-Model Cross-Language AI Coding Agent Performance: Accuracy and Speed
  of Parallel CLRS Algorithms'
---
# Cross-Model Cross-Language AI Coding Agent Performance: Accuracy and Speed of Parallel CLRS Algorithms
> 原文: [https://arxiv.org/abs/2607.26083](https://arxiv.org/abs/2607.26083)

arXiv:2607.26083v1 Announce Type: new
Abstract: AI coding agents have quickly become omnipresent in software engineering. Their serial performance, both in terms of accuracy and speed, has been extensively covered. However, recent initial results suggest their parallel programming capabilities lag behind serial programming capabilities. This paper presents a cross-language evaluation of three coding agents -- Cursor's Composer 2.0, GPT 5.4, and Claude Sonnet 4.6 -- on parallel code generation across three algorithm categories -- sorting, graph traversal, and search -- in C++, Python, and Julia. For each algorithm and language pair, we prompt a coding agent to produce a parallel implementation from a serial baseline, track the prompting effort required to achieve both functional correctness and performance improvements, and measure speedup against both custom serial baselines and third-party library implementations. We find that coding agents can produce correct parallel implementations with modest prompting effort, but that achieving meaningful speedup is heavily algorithm- and language-dependent. Sonnet 4.6 delivers the strongest overall performance gains, whereas GPT 5.4 produces no measurable speedups despite consistent correctness. C++ is most consistently parallelizable for graph algorithms, while Python and Julia achieve the largest speedups on search algorithms: no single language dominates across all categories. Python and Julia each achieve speedup on some graph algorithms but regress on others. These findings underscore the impact of including runtime performance efficiency as a main LLM performance metric, in addition to accuracy, particularly for parallel implementations.
