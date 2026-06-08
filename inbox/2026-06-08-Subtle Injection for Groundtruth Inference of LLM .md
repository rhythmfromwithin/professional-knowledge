---
title: "Subtle Injection for Ground-truth Inference of LLM Training Data"
source: "cs.CR - Cryptography and Security"
link: https://arxiv.org/abs/2606.06502
priority: low
status: unread
interest: medium
next_step: skim
---
# Subtle Injection for Ground-truth Inference of LLM Training Data
> 原文: [https://arxiv.org/abs/2606.06502](https://arxiv.org/abs/2606.06502)

arXiv:2606.06502v1 Announce Type: new
Abstract: As large language models (LLMs) are increasingly trained on scraped web corpora without authorisation, content owners require forensic methods to prove that their documents were included in a model's training set. We propose \textbf{SIGIL} (\textbf{S}ubtle \textbf{I}njection for \textbf{G}round-truth \textbf{I}nference of \textbf{L}LM training data), a framework that embeds imperceptible \emph{canary sequences} into protected text and code such that any LLM trained on those documents exhibits statistically detectable behavioural signatures when probed with targeted queries.
SIGIL defines five canary strategies -- lexical-rare, lexical-phrase, syntactic, semantic, and code-pattern -- and a \emph{Membership Inference Score} (MIS) grounded in the Neyman-Pearson hypothesis testing framework with formal false-positive rate (FPR) control. Simulator parameters are calibrated against the empirical membership inference literature, yielding realistic heterogeneous results across $36{,}000$ trials: overall AUC $= 0.892$, rising from $0.831$ at $0.1\%$ injection to $0.947$ at $10\%$. Detection rates range from $33\%$ to $78\%$ across model-size and injection-rate conditions. Code Pattern canaries achieve the highest AUC ($0.903$, Cohen's $d = 1.84$); Syntactic Structure the lowest ($0.875$, $d = 1.63$). All four experimental factors -- injection rate, model size, canary strategy, and mixture ratio -- have significant independent effects on MIS ($p < 0.001$). SIGIL maintains AUC $> 0.86$ even under $100\%$ paraphrasing ($\text{AUC} = 0.864$), confirming robustness through semantic leakage that survives surface-level rewriting.
