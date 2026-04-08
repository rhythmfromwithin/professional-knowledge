---
interest: medium
link: https://arxiv.org/abs/2604.03232
next_step: skim
priority: high
slack_ts: '1775618438.987779'
source: cs.AI - Artificial Intelligence
status: unread
title: 'IC3-Evolve: Proof-/Witness-Gated Offline LLM-Driven Heuristic Evolution for
  IC3 Hardware Model Checking'
---
# IC3-Evolve: Proof-/Witness-Gated Offline LLM-Driven Heuristic Evolution for IC3 Hardware Model Checking
> 原文: [https://arxiv.org/abs/2604.03232](https://arxiv.org/abs/2604.03232)

arXiv:2604.03232v1 Announce Type: new
Abstract: IC3, also known as property-directed reachability (PDR), is a commonly-used algorithm for hardware safety model checking. It checks if a state transition system complies with a given safety property. IC3 either returns UNSAFE (indicating property violation) with a counterexample trace, or SAFE with a checkable inductive invariant as the proof to safety. In practice, the performance of IC3 is dominated by a large web of interacting heuristics and implementation choices, making manual tuning costly, brittle, and hard to reproduce. This paper presents IC3-Evolve, an automated offline code-evolution framework that utilizes an LLM to propose small, slot-restricted and auditable patches to an IC3 implementation. Crucially, every candidate patch is admitted only through proof- /witness-gated validation: SAFE runs must emit a certificate that is independently checked, and UNSAFE runs must emit a replayable counterexample trace, preventing unsound edits from being deployed. Since the LLM is used only offline, the deployed artifact is a standalone evolved checker with zero ML/LLM inference overhead and no runtime model dependency. We evolve on the public hardware model checking competition (HWMCC) benchmark and evaluate the generalizability on unseen public and industrial model checking benchmarks, showing that IC3-Evolve can reliably discover practical heuristic improvements under strict correctness gates.
