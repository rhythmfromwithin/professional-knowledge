---
slack_ts: '1782708430.663799'
---
# Position: The Term "Machine Unlearning" Is Overused in LLMs
> 原文: [https://arxiv.org/abs/2606.27379](https://arxiv.org/abs/2606.27379)

arXiv:2606.27379v1 Announce Type: new
Abstract: Large language models increasingly face demands to "forget" training data, knowledge, or behaviors due to regulatory deletion obligations, copyright/licensing disputes, and safety or product-policy requirements. This position paper argues that machine unlearning is overused as a term in LLM research and should be reserved for dataset-defined deletion: removing the training influence of a precisely specified forget set such that the resulting model is approximately indistinguishable from retraining without that data. We contend that many tasks currently labeled "unlearning" (e.g., refusal for harmful requests, entity/knowledge removal, or targeted suppression) pursue different, often policy-dependent objectives and therefore require different terminology and baselines (e.g., alignment, suppression, editing, obfuscation). We further argue that this confusion is not cosmetic: because papers make different implicit guarantees under the same label, metrics and benchmarks are frequently reused outside their intended scope, rewarding surface-level non-disclosure (e.g., low ROUGE/forget accuracy) even when retraining-equivalence is not tested and derived capabilities remain. We conclude by calling for stricter terminology tied to explicit guarantees and reference models, and for evaluations that match the claimed objective.
