---
interest: medium
link: https://arxiv.org/abs/2608.21470
next_step: skim
priority: low
slack_ts: '1787820611.780839'
source: cs.CR - Cryptography and Security
status: unread
title: 'Structural Inference in Undocumented Mobile Databases: A Reproducible Benchmark
  for Evaluating Agentic Reasoning in Digital Forensics'
---
# Structural Inference in Undocumented Mobile Databases: A Reproducible Benchmark for Evaluating Agentic Reasoning in Digital Forensics
> 原文: [https://arxiv.org/abs/2608.21470](https://arxiv.org/abs/2608.21470)

arXiv:2608.21470v1 Announce Type: new
Abstract: Agentic large language models are increasingly used in digital forensic analysis, yet their ability to infer relational structure inside undocumented mobile application databases remains poorly understood. In forensic contexts, structurally incorrect inferences can yield results that appear plausible while remaining evidentially unsound. This work evaluates agentic structural inference as an isolated capability, treating execution success and structural correctness as distinct evaluation axes. It examines how an agent reconstructs table relationships, linking attributes, and executable join paths when given only a raw database and a natural-language investigative prompt. We apply a fixed, deterministic evaluation pipeline to two contrasting SQLite repositories: Android's SMS database with stable identifier propagation, and Snapchat's database with irregular schemas, ephemeral identifiers, and polymorphic relationships. Using expert-verified SQL ground truth, we evaluate (i) structural correctness of inferred relational links, (ii) execution coherence under multi-table reasoning, and (iii) robustness and failure modes of inferred structure when execution succeeds but relational interpretation diverges from expert ground truth. Evaluation is performed independently of semantic interpretation, with full queries and execution traces provided in the Appendix. Results show that structural inference remains reliable in regular schemas but degrades sharply as schema ambiguity increases, frequently producing structurally plausible yet incorrect joins that execute successfully. These findings clarify where schema-agnostic agentic reasoning can support forensic analysis, how its robustness degrades under realistic schema irregularities, and why additional verification remains essential before inferred relationships can be treated as reliable evidence.
