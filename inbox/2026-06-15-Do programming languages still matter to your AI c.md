---
interest: medium
link: https://arxiv.org/abs/2606.13763
next_step: skim
priority: low
slack_ts: '1781500242.277929'
source: cs.SE - Software Engineering
status: unread
title: Do programming languages still matter to your AI coding agent teammate? Evidence
  at scale from chess engines
---
# Do programming languages still matter to your AI coding agent teammate? Evidence at scale from chess engines
> 原文: [https://arxiv.org/abs/2606.13763](https://arxiv.org/abs/2606.13763)

arXiv:2606.13763v1 Announce Type: new
Abstract: Frontier coding agents now promise end-to-end authorship of complete software systems. Two empirical questions follow: can AI coding-agent teammates program in any target language, including ones with no comparable prior open-source artefact? If so, does language choice still shape the artefact, and along which dimensions? We study both through a polyglot case study built around chess engines: non-trivial multi-component systems that admit a hierarchy of language-agnostic oracles, from exact move-generation correctness to a strength scale (Elo), observable from Rust to Brainfuck. We prompted two frontier agents (Claude Code and Codex) at the capability level, without chess knowledge or implementation guidance, under a documented intervention and stopping policy. The agents produced 34 chess engines spanning 17 primary programming languages, from mainstream to specialised, domain-specific, legacy, and esoteric targets. We combine per-engine feature analysis, independent Elo assessment, and session trajectories with qualitative analysis of code and transcripts.
Frontier coding agents are genuinely polyglot: every language we tried produced at least one feature-rich working engine, several with no prior open-source counterpart of comparable scope (e.g., LaTeX), and the code is synthesised from scratch rather than copied. Yet language choice still matters: strong playing strength is only reachable in mainstream compiled languages, cost and engineering effort grow sharply as the language becomes more exotic, and feature choices shift across language families. Agents validate their own work unprompted, but their strength self-estimates are biased and a few engines cheated by calling a chess library. Programming language is no longer about whether AI teammates can build a working system, but about performance, cost, what gets built, and how much human supervision validation still needs.
