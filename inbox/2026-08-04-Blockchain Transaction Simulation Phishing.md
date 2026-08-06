---
interest: medium
link: https://arxiv.org/abs/2607.28747
next_step: skim
priority: low
slack_ts: '1785986395.564969'
source: cs.CR - Cryptography and Security
status: unread
title: Blockchain Transaction Simulation Phishing
---
# Blockchain Transaction Simulation Phishing
> 原文: [https://arxiv.org/abs/2607.28747](https://arxiv.org/abs/2607.28747)

arXiv:2607.28747v1 Announce Type: new
Abstract: Cryptocurrency users have increasingly become targets of phishing and scam attacks. To mitigate these threats, leading crypto wallets (e.g., MetaMask) have introduced transaction simulation, which previews a transaction's balance changes before on-chain execution. While effective against traditional fund-draining attacks, we show that this defense can itself be exploited by a new phishing technique, which we term transaction simulation phishing. This attack uses carefully crafted smart contracts whose execution depends on dynamic blockchain state, causing simulations to display benign or profitable outcomes while the actual on-chain execution redirects users' funds to attacker-controlled addresses.
We present the first comprehensive study of transaction simulation phishing. We first develop a taxonomy of phishing contracts that can be utilized to facilitate this attack. Then, we propose SIMGUARD, a bytecode-level detection system that combines static and dynamic program analysis to identify phishing contracts. Applying SIMGUARD to Ethereum, Binance Smart Chain, Avalanche, and Polygon, we detect over 4,000 phishing contracts deployed between August 2024 and June 2025. Our analysis identifies more than 5,700 victims and approximately $3.48 million USD in losses, 91.5% of which occurred on Ethereum. Moreover, our clustering result reveals that the largest phishing contract cluster alone accounts for about 83% of the total losses. These results expose a critical weakness in current wallet defenses and highlight the urgent need for more robust transaction simulation mechanisms.
