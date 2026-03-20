---
interest: medium
link: https://arxiv.org/abs/2603.13239
next_step: skim
priority: high
slack_ts: '1773974671.737759'
source: cs.AI - Artificial Intelligence
status: unread
title: Benchmarking Zero-Shot Reasoning Approaches for Error Detection in Solidity
  Smart Contracts
---
# Benchmarking Zero-Shot Reasoning Approaches for Error Detection in Solidity Smart Contracts
> 原文: [https://arxiv.org/abs/2603.13239](https://arxiv.org/abs/2603.13239)

arXiv:2603.13239v1 Announce Type: new
Abstract: Smart contracts play a central role in blockchain systems by encoding financial and operational logic. Still, their susceptibility to subtle security flaws poses significant risks of financial loss and erosion of trust. LLMs create new opportunities for automating vulnerability detection, yet the effectiveness of different prompting strategies and model choices in real-world contexts remains uncertain. This paper evaluates state-of-the-art LLMs on Solidity smart contract analysis using a balanced dataset of 400 contracts under two tasks: (i) Error Detection, where the model performs binary classification to decide whether a contract is vulnerable, and (ii) Error Classification, where the model must assign the predicted issue to a specific vulnerability category. Models are evaluated using zero-shot prompting strategies, including zero-shot, zero-shot Chain-of-Thought (CoT), and zero-shot Tree-of-Thought (ToT). In the Error Detection task, CoT and ToT substantially increase recall (often approaching $\approx 95$--$99\%$), but typically reduce precision, indicating a more sensitive decision regime with more false positives. In the Error Classification task, Claude 3 Opus attains the best Weighted F1-score (90.8) under the ToT prompt, followed closely by its CoT.
