---
interest: medium
link: https://arxiv.org/abs/2605.22830
next_step: skim
priority: medium
slack_ts: '1779856022.651179'
source: cs.DC - Distributed Computing
status: unread
title: 'Intercloud: Eventual Consistency for Decentralised Economies via Chilling-Effect
  Consensus'
---
# Intercloud: Eventual Consistency for Decentralised Economies via Chilling-Effect Consensus
> 原文: [https://arxiv.org/abs/2605.22830](https://arxiv.org/abs/2605.22830)

arXiv:2605.22830v1 Announce Type: new
Abstract: We present Intercloud, a decentralised economic network in which streams of private data are secured by Watcher swarms that observe only cryptographic hashes, never plaintext. Intercloud requires no global consensus beyond a single shared random seed per epoch. Two mechanisms provide security: (i) ripple deduplication via epoch-stamped identifiers, preventing any ripple from propagating through the same node twice per epoch, guaranteeing termination without global coordination; and (ii) chilling-effect consensus, in which a swarm reaches finality by attesting to the absence of conflicting evidence rather than voting between alternatives. Any conflicting attestation automatically yields a self-certifying Proof of Corruption.
We prove four main results. First, execution ripples terminate in bounded time via the ripple-ID mechanism. Second, a swarm of about 35 Watchers -- assigned by a verifiable random function, independent of total network size -- suffices for double-spending prevention, matching Hoepman's lower bound. Third, two correct clients can hold conflicting finality attestations only if the adversary compromises a supermajority of the assigned swarm or eclipses both clients from all honest nodes; we prove necessity and sufficiency. Fourth, Buridan's Principle does not apply: the consensus question is absence of evidence, not a binary choice on a continuous input.
We also develop a complete economic model. Local coins are issued and retired by currency streams; security weight tracks value automatically as Intercoin weight adjusts at each epoch shuffle. Junior nodes detect corruption and earn lottery rewards for propagating Proofs of Corruption; vesting makes corruption economically irrational. The coin and content layers are strictly separated: regulators observe weight flows without learning amounts, coin types, identities, or rules.
