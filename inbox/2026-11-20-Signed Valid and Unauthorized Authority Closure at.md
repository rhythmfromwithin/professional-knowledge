---
title: "Signed, Valid, and Unauthorized: Authority Closure at the Trust Boundary Between Agent Commerce Protocols and Crypto Wallets"
source: "cs.CR - Cryptography and Security"
link: https://arxiv.org/abs/2611.24989
priority: low
status: unread
interest: medium
next_step: skim
---
# Signed, Valid, and Unauthorized: Authority Closure at the Trust Boundary Between Agent Commerce Protocols and Crypto Wallets
> 原文: [https://arxiv.org/abs/2611.24989](https://arxiv.org/abs/2611.24989)

arXiv:2611.24989v1 Announce Type: new
Abstract: Agent commerce protocols let software agents pay with stablecoins. A buyer approves a payee, asset, spending cap and time window, but the wallet signs an object whose effects depend on the contracts that consume it. Matching the displayed fields or simulating one payment can miss transfers that the signed object still permits. We define authority closure as the set of transfer sequences that holding the signed object can enable. A wallet object respects the mandate when every such sequence meets the buyer's constraints. We characterize when wallet objects can satisfy this property and implement Closure, a wallet-side checker covering 13 families of signed objects. In an evaluation of 2,130 generated objects and 62,979 execution programs, 265 objects with an observed violation passed both a field-and-expiry check and an address allow-list. Under the test model, Closure rejected all 1,680 objects with an observed violation and accepted the remaining 450. In two local checkouts using the x402 reference client, approved payments settled and Closure refused requests outside the mandate before signing. The median decision time was at most 12 microseconds per family.
