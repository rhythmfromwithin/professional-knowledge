---
interest: medium
link: https://arxiv.org/abs/2603.00061
next_step: skim
priority: low
slack_ts: '1773369789.980329'
source: cs.CR - Cryptography and Security
status: unread
title: 'The Hidden Costs of Domain Fine-Tuning: Pii-Bearing Data Degrades Safety and
  Increases Leakage'
---
# The Hidden Costs of Domain Fine-Tuning: Pii-Bearing Data Degrades Safety and Increases Leakage
> 原文: [https://arxiv.org/abs/2603.00061](https://arxiv.org/abs/2603.00061)

arXiv:2603.00061v1 Announce Type: new
Abstract: Domain fine-tuning is a common path to deploy small instruction-tuned language models as customer-support assistants, yet its effects on safety-aligned behavior and privacy are not well understood. In real deployments, such assistants receive a mixture of benign in-domain requests and out-of-domain user queries that are emotional, philosophical, or adversarial. Even when the target domain is benign, specialization may shift model behavior in ways that weaken refusal, increase harmful compliance, and induce privacy leakage.
We present a controlled empirical study of how training data composition (presence vs.\ removal of PII) and fine-tuning configuration (role-swapping (RS)) shape safety and out-of-domain behavior in open-source chat models up to 8B parameters. We fine-tune each model on 5{,}000 real booking-support message pairs under three settings: \textsc{NoPII-NoRS}, \textsc{PII-NoRS}, and \textsc{PII-RS} (role-swapped). We evaluate safety using \textsc{SORRY-Bench}~\cite{xie2024sorry} adversarial prompts and assess out-of-domain behavior using a suite of philosophical questions~\cite{betley2025emergent}.
Across models, domain fine-tuning causes a large distributional shift from high-quality refusals toward harmful compliance on \textsc{SORRY-Bench}, with the most severe degradation when PII is present in the fine-tuning data. For example, macro-averaged strong refusal drops from $42.6\%$ in base models to single digits after fine-tuning, while PII-bearing runs additionally exhibit double-digit rates of harmful responses with PII leakage. On philosophical queries, fine-tuned models frequently exhibit domain anchoring and, when trained with PII, leak sensitive identifiers in irrelevant contexts. Role-swapping partially mitigates PII leakage but does not reliably restore refusal behavior.
