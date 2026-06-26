---
interest: medium
link: https://arxiv.org/abs/2606.26216
next_step: skim
priority: low
slack_ts: '1782447546.293179'
source: cs.CR - Cryptography and Security
status: unread
title: 'CyberChainBench: Can AI Agents Secure Smart Contracts Against Real-World On-Chain
  Vulnerabilities?'
---
# CyberChainBench: Can AI Agents Secure Smart Contracts Against Real-World On-Chain Vulnerabilities?
> 原文: [https://arxiv.org/abs/2606.26216](https://arxiv.org/abs/2606.26216)

arXiv:2606.26216v1 Announce Type: new
Abstract: We present CyberChainBench, a benchmark for evaluating LLM-based agents on smart contract security across three complementary tasks: vulnerability detection, exploit generation, and patch synthesis. Built from 541 real-world exploit incidents from DeFiHackLabs spanning 9 EVM chains, the benchmark provides end-to-end on-chain evaluation where agents interact with historical blockchain state through isolated evaluation environments orchestrated by Harbor, using tools to read code, trace transactions, and validate exploits on mainnet forks. Each case is anchored to a specific block and includes structured ground truth covering vulnerability type, localization, and attacker profit. Exploits are graded by economic impact on historical forks; patches are validated by replaying historical attacks and legitimate transactions as fail-to-pass test oracles on a proxy-upgradeable subset. We define a five-type vulnerability taxonomy and evaluate multiple agent--model configurations. Results reveal a clear difficulty gradient: the best configuration scores 37.5% on detection, 43.7% on exploitation, but only 23.4% on patching, with the top agent (Codex with GPT-5.5) realizing \$57.4M in total exploit profit across the 200-case exploit set at a cost of $2.39 per case.
