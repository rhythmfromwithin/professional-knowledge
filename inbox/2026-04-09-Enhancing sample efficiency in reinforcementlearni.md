---
title: "Enhancing sample efficiency in reinforcement-learning-based flow control: replacing the critic with an adaptive reduced-order model"
source: "cs.LG - Machine Learning"
link: https://arxiv.org/abs/2604.04986
priority: high
status: unread
interest: medium
next_step: skim
---
# Enhancing sample efficiency in reinforcement-learning-based flow control: replacing the critic with an adaptive reduced-order model
> 原文: [https://arxiv.org/abs/2604.04986](https://arxiv.org/abs/2604.04986)

arXiv:2604.04986v1 Announce Type: new
Abstract: Model-free deep reinforcement learning (DRL) methods suffer from poor sample efficiency. To overcome this limitation, this work introduces an adaptive reduced-order-model (ROM)-based reinforcement learning framework for active flow control. In contrast to conventional actor--critic architectures, the proposed approach leverages a ROM to estimate the gradient information required for controller optimization. The design of the ROM structure incorporates physical insights. The ROM integrates a linear dynamical system and a neural ordinary differential equation (NODE) for estimating the nonlinearity in the flow. The parameters of the linear component are identified via operator inference, while the NODE is trained in a data-driven manner using gradient-based optimization. During controller--environment interactions, the ROM is continuously updated with newly collected data, enabling adaptive refinement of the model. The controller is then optimized through differentiable simulation of the ROM. The proposed ROM-based DRL framework is validated on two canonical flow control problems: Blasius boundary layer flow and flow past a square cylinder. For the Blasius boundary layer, the proposed method effectively reduces to a single-episode system identification and controller optimization process, yet it yields controllers that outperform traditional linear designs and achieve performance comparable to DRL approaches with minimal data. For the flow past a square cylinder, the proposed method achieves superior drag reduction with significantly fewer exploration data compared with DRL approaches. The work addresses a key component of model-free DRL control algorithms and lays the foundation for designing more sample-efficient DRL-based active flow controllers.
