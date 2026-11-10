---
interest: medium
link: https://arxiv.org/abs/2611.08654
next_step: skim
priority: medium
slack_ts: '1794293792.971279'
source: cs.RO - Robotics
status: unread
title: 'CS-Pi: Constraint-Satisfying Flow Policy Sampling'
---
# CS-Pi: Constraint-Satisfying Flow Policy Sampling
> 原文: [https://arxiv.org/abs/2611.08654](https://arxiv.org/abs/2611.08654)

arXiv:2611.08654v1 Announce Type: new
Abstract: A flow-matching policy deployed in the field must often satisfy a constraint that was absent from its demonstrations, such as avoiding an obstacle it has never seen. Retraining for every new constraint is impractical, so the constraint must be enforced at inference time. Enforcing it must not discard what the policy learned: an action the policy would rarely sample may avoid the obstacle yet fail the task. We therefore want actions that are both safe, satisfying the constraint, and plausible, remaining likely under the policy. Gradient guidance, the most common approach, steers noisy states, so it must evaluate its cost on the policy's running estimate of the clean action; when the policy is uncertain between passing left or right of an obstacle, this estimate is their average and can pass straight through it. We instead build on rejection and projection. Rejection redraws actions until one is safe: every output is plausible, but the wait is intractable when safe actions are rare. Projection moves an action to the nearest safe one: it is efficient, but the result need not be plausible. Our key insight is that flow-matching sampling lets us combine the two, keeping projection's efficiency and rejection's plausibility. CS-Pi, our draw-project-renoise sampler, projects each draw to the nearest safe action, adds noise back scaled to how far the projection moved it, and re-runs the unmodified policy until a draw is safe. Replacing only the projection step extends CS-Pi to continuous costs. Across a 2D diagnostic, a 7-DoF shelf pick-and-place, an orientation preference, and a zero-shot Franka deployment, CS-Pi reaches 81% safe success on the shelf and 55% on hardware, against 55% and 40% for projection, while staying plausible.
