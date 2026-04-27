---
interest: medium
link: https://arxiv.org/abs/2604.19749
next_step: skim
priority: high
slack_ts: '1777261681.635559'
source: cs.AI - Artificial Intelligence
status: unread
title: 'The Tool-Overuse Illusion: Why Does LLM Prefer External Tools over Internal
  Knowledge?'
---
# The Tool-Overuse Illusion: Why Does LLM Prefer External Tools over Internal Knowledge?
> 原文: [https://arxiv.org/abs/2604.19749](https://arxiv.org/abs/2604.19749)

arXiv:2604.19749v1 Announce Type: new
Abstract: Equipping LLMs with external tools effectively addresses internal reasoning limitations. However, it introduces a critical yet under-explored phenomenon: tool overuse, the unnecessary tool-use during reasoning. In this paper, we first reveal this phenomenon is pervasive across diverse LLMs. We then experimentally elucidate its underlying mechanisms through two key lenses: (1) First, by analyzing tool-use behavior across different internal knowledge availability regions, we identify a \textit{knowledge epistemic illusion}: models misjudge internal knowledge boundaries and fail to accurately perceive their actual knowledge availability. To mitigate this, we propose a knowledge-aware epistemic boundary alignment strategy based on direct preference optimization, which reduces tool usage in by 82.8\% while yielding an accuracy improvement. (2) Second, we establish a causal link between reward structures and tool-use behavior by visualizing the tool-augmented training process. It reveals that \textit{outcome-only rewards} inadvertently encourage tool overuse by rewarding only final correctness, regardless of tool efficiency. To verify this, we balance reward signals during training rather than relying on outcome-only rewards, cutting unnecessary tool calls by 66.7\% (7B) and 60.7\% (32B) without sacrificing accuracy. Finally, we provide theoretical justification in this two lenses to understand tool overuse.
