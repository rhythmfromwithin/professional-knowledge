---
title: "Costs of Arbitrary Real Matrix Factorizations for Pure-DP Continual Counting"
source: "cs.CR - Cryptography and Security"
link: https://arxiv.org/abs/2607.28703
priority: low
status: unread
interest: medium
next_step: skim
---
# Costs of Arbitrary Real Matrix Factorizations for Pure-DP Continual Counting
> 原文: [https://arxiv.org/abs/2607.28703](https://arxiv.org/abs/2607.28703)

arXiv:2607.28703v1 Announce Type: new
Abstract: Let \(T\_n\) be the lower-triangular prefix-sum matrix and let \(\cfrob(T\_n)\) and \(\ctwo(T\_n)\) be the factorization costs that govern mean and maximum per-coordinate squared error of the Laplace matrix mechanism under pure \(\eps\)-differential privacy, for \(\eps>0\). We prove \(\cfrob(T\_n),\ctwo(T\_n)=\Theta\bigl((\log(n+1))^{3/2}\bigr)\) with no sign, sparsity, or squareness restriction and with arbitrary finite inner dimension. Consequently, within the pure-\(\eps\)-DP matrix-mechanism class the optimized maximum and mean squared errors are both \(\Theta(\eps^{-2}\log^{3}(n+1))\). Under the factorization contract of Arkhipov and Kalinin (arXiv:2607.08963v1), who prove the matching lower order for factors with entries in \(\{0,1\}\) and state the arbitrary-factor extension as open, the theorem below establishes the order for arbitrary real factors. The lower bound runs through a \(p\)-nuclear obstruction: an aggregate column-width estimate \(D\_k(T\_n)\asymp n^{3/2}k^{-1/2}\), valid in the low-rank range \(1\leq k\leq n/16\), for the prefix chain, fed into the classical approximation-space conversion of Pietsch and Hinrichs--Pietsch, becomes harmonic at the critical exponent \(p=2/3\), and H\"older's inequality transfers it to both factorization costs. The same computation determines \(\nucpow\_p(T\_n)\) for each fixed \(0

<1\): order \(n\) below \(2/3\), \(n\log n\) at \(2/3\), and \(n^{3p/2}\) above. A Fenwick interval factorization supplies matching upper bounds. The claims are confined to pure-\(\eps\)-DP Laplace matrix mechanisms and the two stated squared-error criteria; they do not cover non-matrix continual mechanisms, approximate-DP sensitivity, or expected maxima across coordinates.
