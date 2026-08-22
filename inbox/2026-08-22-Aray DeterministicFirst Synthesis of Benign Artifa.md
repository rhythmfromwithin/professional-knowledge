---
title: "Aray: Deterministic-First Synthesis of Benign Artifacts for YARA Validation"
source: "cs.CR - Cryptography and Security"
link: https://arxiv.org/abs/2608.19387
priority: low
status: unread
interest: medium
next_step: skim
---
# Aray: Deterministic-First Synthesis of Benign Artifacts for YARA Validation
> 原文: [https://arxiv.org/abs/2608.19387](https://arxiv.org/abs/2608.19387)

arXiv:2608.19387v1 Announce Type: new
Abstract: A YARA rule is easy to distribute, but the malware sample used to demonstrate a positive match is not. This complicates storage, continuous integration, disaster-recovery exercises, and reproducible scanner validation. Constructing a replacement fixture requires more than embedding literals: YARA conditions can combine alternatives, counts, offsets, integer reads, and executable-container constraints, while the resulting file should not reproduce malware behavior. Positive validation is existential: it requires one file-level member of a rule's match set, not reconstruction of the originating sample. We present Aray, a deterministic-first YARA interpreter and positive-fixture synthesizer. Models may propose constructive normalizations or typed extraction fallbacks, but never backend source or binary structure. Conventional code validates normalized rules, derives string and integer witnesses, and performs extraction, routing, collision-checked layout, and ELF, PE, or generic serialization. Only residual normalization semantics reach a bounded model judge. We evaluated Aray over 416 public-rule entries. Normalization accepted 182 entries without model assistance and 234 after model normalization. Constructibility preflight admitted 406 entries, and every admitted fixture matched its upstream original rule. This yields 406/416 (97.6%) overall and 406/406 among constructible rules, with ten expected preflight dispositions and no scanner mismatches or construction failures. An unreachable endpoint confirmed zero model invocations during realization. The original-rule oracle validates generated fixtures against their source rules; proving implication for all possible files is a separate, stronger objective. Two anchored-regex failures were repaired before the final run, so these are post-fix systems results, not a held-out estimate.
