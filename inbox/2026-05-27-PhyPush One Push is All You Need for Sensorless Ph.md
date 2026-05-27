---
title: "PhyPush: One Push is All You Need for Sensorless Physical Property Estimation with Physics-Guided Transformers"
source: "cs.RO - Robotics"
link: https://arxiv.org/abs/2605.26284
priority: medium
status: unread
interest: medium
next_step: skim
---
# PhyPush: One Push is All You Need for Sensorless Physical Property Estimation with Physics-Guided Transformers
> 原文: [https://arxiv.org/abs/2605.26284](https://arxiv.org/abs/2605.26284)

arXiv:2605.26284v1 Announce Type: new
Abstract: Accurately estimating object mass and friction is fundamental to achieving reliable and adaptive robotic manipulation. Although interactive perception provides a powerful mechanism for inferring such properties, most existing approaches depend on specialized hardware such as force/torque sensors, tactile arrays, or multi-camera motion-capture systems, limiting scalability and deployment. This paper presents PhyPush, a physics-guided Transformer framework that estimates an object's mass and friction coefficient using only kinematically derived end-effector velocity from a single push. This typically requires data available on standard robotic arms. The model incorporates constraints from Newton's second law and the Coulomb friction model through a physics-guided loss, improving physical consistency and generalization to unseen objects and surfaces. Across diverse simulation and real-world setups, PhyPush consistently achieves more accurate mass and friction estimation in challenging out-of-domain conditions. In simulation, it reduces error by over 10% compared with a baseline that has privileged access to full force information, while in real-world experiments, it outperforms a data-driven loss approach. Overall, the results demonstrate that physics-guided learning can enable low-cost, sensor-efficient estimation of physical properties, relying solely on a single push and readily available kinematic data.
