---
interest: medium
link: https://arxiv.org/abs/2605.11059
next_step: skim
priority: medium
slack_ts: '1778817947.578519'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: Uniform Scaling Limits in AdamW-Trained Transformers
---
# Uniform Scaling Limits in AdamW-Trained Transformers
> 原文: [https://arxiv.org/abs/2605.11059](https://arxiv.org/abs/2605.11059)

arXiv:2605.11059v1 Announce Type: new
Abstract: We study the large-depth limit of transformers trained with AdamW, by modelling the hidden-state dynamics as an interacting particle system (IPS) coupled through the attention mechanism. Under appropriate scaling of the attention heads, we prove that the joint dynamics of the hidden states and backpropagated variables converge in $L^2$, uniformly over the initial condition, to the solution of a forward--backward system of ODEs at rate $\mathcal O(L^{-1}+L^{-1/3}H^{-1/2})$. Here, $L$ and $H$ denote the depth and number of heads of the transformer, respectively. The limiting system of ODEs can be identified with a McKean--Vlasov ODE (MVODE) when the attention heads do not incorporate causal masking. By using the flow maps associated with this MVODE and applying concentration of measure techniques, we obtain bounds on the difference between the discrete and continuous models that are uniform over compact sets of initial conditions. As this is achieved without resorting to a covering argument, the constants in our bounds are independent of the number of tokens. Furthermore, under a suitable adaptation to AdamW, the bounds become independent of the token embedding dimension.
