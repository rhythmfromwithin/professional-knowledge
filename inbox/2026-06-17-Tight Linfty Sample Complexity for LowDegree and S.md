---
slack_ts: '1781759638.231599'
---
# Tight $L_\infty$ Sample Complexity for Low-Degree and Sparse Boolean Polynomials
> 原文: [https://arxiv.org/abs/2606.17319](https://arxiv.org/abs/2606.17319)

arXiv:2606.17319v1 Announce Type: new
Abstract: Motivated by the optimization of bounded binary black-box functions, we study the problem of learning polynomial surrogates over the Boolean hypercube. To ensure that optimizing the surrogate yields good solutions for the underlying objective, we require uniform $L\_\infty$-error guarantees rather than the usual $L\_2$-type guarantees. We characterize the minimax sample complexity of uniform estimation under subgaussian noise for two classes of bounded polynomials. First, for polynomials of degree at most $d$ on $n$ variables, the sample complexity scales as $n^{d+1}$. Second, for $s$-sparse Fourier-Walsh polynomials with $s \leq n$, it scales as $ns^2$. These rates differ structurally from the noiseless setting, where uniform exact recovery scales as $n^d$ and $ns$, respectively. Our lower bounds hold even for arbitrary adaptive learners, showing that the additional factors are intrinsic to the noisy cases. Standard Fourier-analysis tools for the $L\_2$-norm do not naturally extend to the $L\_\infty$-setting in a way that yields uniform guarantees. Our proofs overcome this difficulty by relying on suitably chosen auxiliary norms that serve as proxies for controlling the $L\_\infty$-error. Together, our results provide a tight characterization of the sample complexity of learning optimization-safe polynomial surrogates.
