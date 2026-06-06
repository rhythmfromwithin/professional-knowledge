---
interest: medium
link: https://arxiv.org/abs/2606.05228
next_step: skim
priority: low
slack_ts: '1780718924.143659'
source: cs.SE - Software Engineering
status: unread
title: Where Do Large Language Models Fail on Competitive Programming? A Taxonomy
  of Failures by Algorithm Type and Difficulty Rating
---
# Where Do Large Language Models Fail on Competitive Programming? A Taxonomy of Failures by Algorithm Type and Difficulty Rating
> 原文: [https://arxiv.org/abs/2606.05228](https://arxiv.org/abs/2606.05228)

arXiv:2606.05228v1 Announce Type: new
Abstract: Large language models (LLMs) demonstrate increasing proficiency on competitive programming benchmarks, yet technical reports predominantly publish aggregate pass rates, obscuring domain-specific vulnerabilities. We present a systematic empirical study of LLM failure patterns using a balanced taxonomy of 315 Codeforces problems across seven algorithm categories and three difficulty tiers. We evaluate GPT-4o and Claude Sonnet 4.6 under strict execution-based conditions, controlling for temperature (T = 0.2). To isolate the impact of reasoning frameworks on algorithmic correctness, we conduct an ablation study comparing direct zero-shot generation against zero-shot Chain-of-Thought (CoT). Our findings reveal a severe divergence from standard NLP benchmarks: forcing CoT aggressively penalizes GPT-4o, dropping its pass rate from 46.0% to 36.8% and exacerbating a critical weakness in Greedy logic. Conversely, while Claude maintains a higher logical baseline (63.5% under CoT), the expanded text generation severely degrades its markdown instruction adherence, causing its Compile Errors to more than triple (from 9 to 31, a 244% increase). Furthermore, failure-mode analysis indicates that Wrong Answer (WA) is the dominant verdict for both models--accounting for over 90% of GPT-4o's and roughly 70% of Claude's unaccepted solutions. These findings empirically demonstrate that standard prompt engineering techniques fail to bridge the algorithmic reasoning gap in competitive programming environments.
