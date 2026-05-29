---
interest: medium
link: https://arxiv.org/abs/2605.26874
next_step: skim
priority: low
slack_ts: '1780028379.193719'
source: cs.DB - Databases
status: unread
title: Knowledge Graphs as the Missing Data Layer for LLM-Based Industrial Asset Operations
---
# Knowledge Graphs as the Missing Data Layer for LLM-Based Industrial Asset Operations
> 原文: [https://arxiv.org/abs/2605.26874](https://arxiv.org/abs/2605.26874)

arXiv:2605.26874v1 Announce Type: new
Abstract: LLM-based agents for industrial asset operations show limited accuracy when reasoning over flat document stores. AssetOpsBench (KDD 2026) establishes that GPT-4 agents achieve 65% on 139 industrial maintenance scenarios backed by CouchDB, YAML, and CSV. It compares LLM orchestration paradigms (Agent-As-Tool vs Plan-Execute) on a fixed data layer; we ask a complementary, orthogonal question: how much does the data model behind the tools affect agent performance?
Building on the same scenarios, we introduce a knowledge graph layer (781 nodes, 955 edges, 16 relationship types) and evaluate three architectures: (1) deterministic graph handlers (no LLM) at 99% (137/139); (2) LLM-generated Cypher over the graph at 82-83% with the same GPT-4 model the baseline uses; and (3) the original tool-augmented LLM baseline at 65% (91/139, matching the published KDD 2026 leaderboard ceiling).
Our key finding is inverted LLM usage: rather than asking the LLM to reason over raw data, we ask it to generate structured queries from a typed schema. The graph executes deterministically. We additionally contribute 40 graph-native scenarios (multi-hop dependency, vector similarity, PageRank criticality), and evaluate against the expanded HuggingFace AssetOpsBench release (467 scenarios, 6 domains), where deterministic handlers achieve 100% (467/467) with average score 0.848.
These results suggest that for structured operational domains, the data layer -- not the LLM orchestration -- is the primary bottleneck, and that knowledge graphs serve as an integration layer between raw industrial data and LLM-based reasoning.
