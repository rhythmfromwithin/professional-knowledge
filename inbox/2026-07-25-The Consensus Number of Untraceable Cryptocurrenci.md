---
interest: medium
link: https://arxiv.org/abs/2607.20929
next_step: skim
priority: medium
slack_ts: '1785124091.514159'
source: cs.DC - Distributed Computing
status: unread
title: The Consensus Number of Untraceable Cryptocurrencies
---
# The Consensus Number of Untraceable Cryptocurrencies
> 原文: [https://arxiv.org/abs/2607.20929](https://arxiv.org/abs/2607.20929)

arXiv:2607.20929v1 Announce Type: new
Abstract: Sender untraceability hides the account spent by a cryptocurrency transfer among a set of candidates, its masking set. What a transfer does to that set separates two designs: classical schemes retain the whole set and append a nullifier marking the spent account, so the ledger grows with every transfer; constant-state schemes instead consume and replace the entire set. We ask how this choice affects synchronization.
We formalize the two designs as the linear and constant untraceable asset transfer objects (LUAT and CUAT) and locate them in the consensus hierarchy. In LUAT, transfers from distinct accounts commute. Its consensus number is 2, compared with 1 for standard asset transfer, independently of the masking-set size and of the untraceability notion, and LUAT is starvation-free. Partitioning the accounts into fixed masking sets lets exhausted sets be garbage-collected without increasing that number.
In CUAT, a transfer consumes and replaces every account of its masking set, so two transfers whose sets intersect cannot both take effect. We formalize this with the conflict graph on masking sets, whose edges join sets sharing an account. Under weak untraceability, which protects a transaction in isolation, the consensus number is unbounded already for one-round protocols. Under strong untraceability, which protects against an observer of the complete history, untraceability holds on a history exactly when any two accounts sharing a masking set occur in the same number of the masking sets in it. This uniform incidence bounds the conflict graph, and matching constructions attain it, so the consensus number is determined exactly and grows quadratically in the masking-set size. Finally, CUAT is not starvation-free. The two objects therefore pay for the same privacy differently: LUAT in storage, CUAT in synchronization and fairness.
