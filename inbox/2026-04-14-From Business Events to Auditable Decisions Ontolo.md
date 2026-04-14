---
interest: medium
link: https://arxiv.org/abs/2604.08603
next_step: skim
priority: high
slack_ts: '1776137321.563559'
source: cs.AI - Artificial Intelligence
status: unread
title: 'From Business Events to Auditable Decisions: Ontology-Governed Graph Simulation
  for Enterprise AI'
---
# From Business Events to Auditable Decisions: Ontology-Governed Graph Simulation for Enterprise AI
> 原文: [https://arxiv.org/abs/2604.08603](https://arxiv.org/abs/2604.08603)

arXiv:2604.08603v1 Announce Type: new
Abstract: Existing LLM-based agent systems share a common architectural failure: they answer from the unrestricted knowledge space without first simulating how active business scenarios reshape that space for the event at hand -- producing decisions that are fluent but ungrounded and carrying no audit trail. We present LOM-action, which equips enterprise AI with \emph{event-driven ontology simulation}: business events trigger scenario conditions encoded in the enterprise ontology~(EO), which drive deterministic graph mutations in an isolated sandbox, evolving a working copy of the subgraph into the scenario-valid simulation graph $G\_{\text{sim}}$; all decisions are derived exclusively from this evolved graph. The core pipeline is \emph{event $\to$ simulation $\to$ decision}, realized through a dual-mode architecture -- \emph{skill mode} and \emph{reasoning mode}. Every decision produces a fully traceable audit log. LOM-action achieves 93.82% accuracy and 98.74% tool-chain F1 against frontier baselines Doubao-1.8 and DeepSeek-V3.2, which reach only 24--36% F1 despite 80% accuracy -- exposing the \emph{illusive accuracy} phenomenon. The four-fold F1 advantage confirms that ontology-governed, event-driven simulation, not model scale, is the architectural prerequisite for trustworthy enterprise decision intelligence.
