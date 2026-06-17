---
interest: medium
link: https://arxiv.org/abs/2606.17220
next_step: skim
priority: high
slack_ts: '1781672202.732449'
source: cs.AI - Artificial Intelligence
status: unread
title: 'When Rules Learn: A Self-Evolving Agent for Legal Case Retrieval'
---
# When Rules Learn: A Self-Evolving Agent for Legal Case Retrieval
> 原文: [https://arxiv.org/abs/2606.17220](https://arxiv.org/abs/2606.17220)

arXiv:2606.17220v1 Announce Type: new
Abstract: Legal case retrieval remains challenging due to the complexity of legal language and the need for precise lexical alignment between queries and relevant cases. Although dense retrieval models have achieved notable progress, empirical studies show that BM25 continues to serve as a strong baseline in this domain. It motivates us to propose a self-evolving framework for rule-driven query rewriting that enhances BM25 without any parameter training. The framework equips an LLM-based agent with an automatic evaluation environment, enabling it to iteratively create rewriting rules, plan validation experiments over rule combinations, and eliminate ineffective rules based on historical feedbacks. We evaluate our method on the Chinese legal case retrieval benchmark LeCaRD-v2. Experimental results demonstrate that the proposed framework outperforms non-evolutionary baselines, including human-designed rules and greedy rule selection, particularly when powered by a highcapacity core LLM. We also conduct detailed analyses to investigate the mechanisms underlying self-evolution. Our findings reveal that LLM's capabilities to leverage previous experimental results and its intrinsic knowledge of rule elimination play critical roles in refining the rule set via self-evolution.
