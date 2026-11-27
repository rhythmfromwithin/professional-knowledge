---
interest: medium
link: https://arxiv.org/abs/2611.31468
next_step: skim
priority: medium
slack_ts: '1795766097.166919'
source: cs.DC - Distributed Computing
status: unread
title: 'Pearl: TEE-Enabled Fair Ordering with Minimal Replication'
---
# Pearl: TEE-Enabled Fair Ordering with Minimal Replication
> 原文: [https://arxiv.org/abs/2611.31468](https://arxiv.org/abs/2611.31468)

arXiv:2611.31468v1 Announce Type: new
Abstract: Recent research has investigated fair transaction ordering in blockchain consensus. An orthogonal line of work has demonstrated that equipping replicas with trusted execution environments (TEEs) enables more efficient consensus protocols with only $2f{+}1$ replicas. In this work, we bridge these two areas and demonstrate that two key fair-ordering properties, ordering linearizability and $\gamma$-batch-order fairness with minimal batching, cannot be implemented in partially synchronous networks with $2f{+}1$ replicas, even when the replicas are equipped with TEEs. We show that Byzantine replicas can circumvent TEE protections by manipulating the timing of transaction submissions to the enclave, thereby biasing the resulting ordering indicators. However, we prove that assuming a synchronous network allows both properties to be implemented with a reduced replica count. We propose two mechanisms: one uses absolute TEE-attested timestamps to guarantee ordering linearizability in a system of $n \ge 2f{+}1$ replicas, and the other uses TEE-maintained relative sequence numbers to guarantee $\gamma$-batch-order fairness when $n > \frac{2\gamma f}{2\gamma-1}$. Ultimately, we integrate these mechanisms into a synchronous lane-based consensus algorithm, achieving strong fair-ordering properties and superior performance while requiring fewer replicas than representative state-of-the-art baselines.
