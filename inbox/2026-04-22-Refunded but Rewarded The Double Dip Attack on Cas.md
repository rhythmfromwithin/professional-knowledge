---
interest: medium
link: https://arxiv.org/abs/2604.16427
next_step: skim
priority: low
slack_ts: '1776915190.975689'
source: cs.CR - Cryptography and Security
status: unread
title: 'Refunded but Rewarded: The Double Dip Attack on Cashback Reward Engines'
---
# Refunded but Rewarded: The Double Dip Attack on Cashback Reward Engines
> 原文: [https://arxiv.org/abs/2604.16427](https://arxiv.org/abs/2604.16427)

arXiv:2604.16427v1 Announce Type: new
Abstract: Cashback reward programs now serve as central instruments in the competitive landscape of cards, digital wallets, and payment platforms. Despite their financial significance, the business logic governing these programs is seldom treated as a security critical surface. In this paper, we study a class of reward abuse attacks that arise from flaws in how reward systems accrue, redeem, and adjust incentives when underlying transactions are reversed through refunds. Using controlled, small scale experiments on six issuer accounts we legitimately hold, we document a spectrum of real world behaviors in production systems. At one extreme, a debit based cashback program (Issuer A) never adjusts rewards when refunded transactions post, enabling a deterministic double dip cashback reward abuse attack. A credit card program (Issuer B) exhibits an analogous reward integrity violation through a statement cycle timing gap that allows reward redemption before the merchant return window closes. At an intermediate tier, a credit card issuer (Issuer F) creates negative reward entries on refunds at statement close but makes rewards redeemable immediately upon settlement, creating a timing asymmetry that allows users to extract reward value before clawback occurs. At the robust end, three credit card issuers (C, D, and E) implement indefinite negative balance enforcement with proportional clawback. We formalize reward engines as state machines, introduce two integrity invariants (Reward Integrity and Refund Reward Consistency), develop a taxonomy of vulnerability classes mapped to CWE and OWASP, and present defensive pseudo algorithms with a semi formal correctness argument that close the identified loopholes. The primary vulnerability (Issuer A) was reported through a private bug bounty program and has been acknowledged by the vendor; good faith disclosure efforts for Issuer B are detailed in Section 8.
