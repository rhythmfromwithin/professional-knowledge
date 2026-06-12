---
slack_ts: '1781239687.639679'
---
# Runtime Analysis of the $(\mu + 1)$-ES in a Homogenous Progress Model
> 原文: [https://arxiv.org/abs/2606.13323](https://arxiv.org/abs/2606.13323)

arXiv:2606.13323v1 Announce Type: new
Abstract: We introduce a new simple model to study the fitness progress of Evolution Strategies (ES) in generic problems. In this model, we bypass the underlying fitness landscape and assume that the mutation of any individual produces an offspring whose fitness relative to the parent is given by an invariant distribution $Z$, such as a mean-shifted Gaussian. This serves as a prototypical model for the optimisation landscape when an evolution algorithm operates far from the global optimum. This simple model can be used to approximate the optimisation process for problems where it is intractable to model the exact fitness function, including tasks such as hyperparameter tuning in machine learning models.
We rigorously analyse the expected growth rate $\mathcal{R}\_{\mu}$ of the continuous steady-state $(\mu+1)$-ES in this model. Unlike comma-selection strategies, the steady-state $(\mu+1)$-ES maintains overlapping generations, introducing complex mathematical dependencies among surviving parents that make it harder to analyse. We give a general technique to analyse the the $(\mu + 1)$-ES by constructing modified processes whose growth rates provably sandwich that of the original process. These modified processes are then easier to analyse but still close enough to the true process to give a tight bound on the expected growth rate. When $Z = \mathcal{N}(-\delta, 1)$ and $\mu \le e^{\delta}$, we show that $\mathcal{R}\_{\mu} = \frac{\log^{1 + o(1)} \mu}{\mu} \mathcal{R}\_1$.
