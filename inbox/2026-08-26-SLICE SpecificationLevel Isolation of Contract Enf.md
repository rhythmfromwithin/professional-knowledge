---
interest: medium
link: https://arxiv.org/abs/2608.21483
next_step: skim
priority: low
slack_ts: '1787820610.243399'
source: cs.SE - Software Engineering
status: unread
title: 'SLICE: Specification-Level Isolation of Contract Enforcement'
---
# SLICE: Specification-Level Isolation of Contract Enforcement
> 原文: [https://arxiv.org/abs/2608.21483](https://arxiv.org/abs/2608.21483)

arXiv:2608.21483v1 Announce Type: new
Abstract: Programming problems commonly specify both the computation a function should perform and the conditions that its inputs must satisfy. Large language models are widely used to generate code from these problem specifications, and the generated function must implement the required computation while enforcing the stated input conditions. The stated input conditions collectively form an input contract. Enforcing this contract is difficult: incomplete enforcement accepts inputs that should be rejected, whereas overly restrictive enforcement rejects inputs that should be accepted. Existing code generation methods do not provide a generation process that identifies both the input contract and the functional requirements and generates code that satisfies them jointly. We therefore introduce SLICE, a generation framework that identifies both requirements and addresses them through separate generation stages. SLICE consists of three stages: (i) Graph-based specification structuring, which grounds contract conditions to description segments in a specification graph and removes contract-only segments to form a functional view; (ii) Functional body generation, which produces multiple candidate function bodies through greedy and sampled decoding, ranks them using execution scores, and resolves ties using difference-region log probabilities; and (iii) Contract assertion generation, which generates input-validation assertions from the identified contract conditions and attaches them to the selected function body. We evaluate SLICE on ContractEval across four LLMs and compare it with six competing methods. Relative to the strongest evaluated baseline for each model, SLICE improves performance in generating code that satisfies both the functional requirements and the input contract by an average of 6.58%. Our code is available at https://github.com/suhanmen/SLICE.
