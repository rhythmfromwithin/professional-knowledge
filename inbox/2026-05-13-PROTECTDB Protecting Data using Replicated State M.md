---
title: "PROTECT-DB: Protecting Data using Replicated State Machines: Efficient Corruption Detection & Recovery"
source: "cs.DB - Databases"
link: https://arxiv.org/abs/2605.11953
priority: low
status: unread
interest: medium
next_step: skim
---
# PROTECT-DB: Protecting Data using Replicated State Machines: Efficient Corruption Detection & Recovery
> 原文: [https://arxiv.org/abs/2605.11953](https://arxiv.org/abs/2605.11953)

arXiv:2605.11953v1 Announce Type: new
Abstract: Data is critical for the operation of any organization and needs to be protected, especially against attacks that compromise the state of the database. In this paper, we explore an approach based on Byzantine-fault tolerant replicated state machines, built on top of a deterministic extension of PostgreSQL. Each replica deterministically executes transactions recorded in a shared log/blockchain. Our focus is on creating a practical system that is designed for efficient and quick detection of corruption, as well as quick repair concurrent with execution of transactions. We also present a performance study showing the efficiency and practicality of our approach. We believe our work lays the foundations for the practical use of the BFT replicated state machine approach in the context of databases.
