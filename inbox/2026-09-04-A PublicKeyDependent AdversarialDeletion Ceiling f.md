---
interest: medium
link: https://arxiv.org/abs/2609.02943
next_step: skim
priority: low
slack_ts: '1788581039.719759'
source: cs.CR - Cryptography and Security
status: unread
title: A Public-Key-Dependent Adversarial-Deletion Ceiling for Fixed-Alphabet Multi-Bit
  Pseudorandom Codes
---
# A Public-Key-Dependent Adversarial-Deletion Ceiling for Fixed-Alphabet Multi-Bit Pseudorandom Codes
> 原文: [https://arxiv.org/abs/2609.02943](https://arxiv.org/abs/2609.02943)

arXiv:2609.02943v1 Announce Type: new
Abstract: A pseudorandom code (PRC) is a keyed error-correcting code whose codewords are computationally indistinguishable from uniform strings. We study public-key PRCs over fixed alphabets against adversarial deletions, where the deletion channel may both depend on the public encoding key and the transmitted codeword.
Let $\gamma\_q^{\mathrm{LCS}}$ denote the asymptotic normalised longest-common-subsequence length of two independent uniform $q$-ary strings. We prove that for every fixed $q\ge2$ no multi-message public-key PRC with a single-output decoder is robust against all such $\delta$-deletion channels for any $\delta>1-\gamma\_q^{\mathrm{LCS}}$. For $q=2$, the current rigorous bound $\gamma\_2\ge0.792665992$ rules out every constant $\delta>0.207334008$. The proof uses pseudorandomness only to transfer an LCS event from uniform strings to independently sampled codewords and therefore also the resulting collision argument is information-theoretic and requires no secret key. We also extend the argument to list decoding: for every fixed constant $L$, provided the message space contains at least $L+1$ messages, no such PRC with output lists of size at most $L$ is robust for $\delta>1-\gamma\_2^{(L+1)}$. Since $\gamma\_2^{(m)}=1/2+\Theta(1/\sqrt m)$, these thresholds approach $1/2$. Our bounds are specific to public-key-dependent adversarial channels and do not apply to oblivious edit channels.
