---
interest: medium
link: https://arxiv.org/abs/2607.27261
next_step: skim
priority: medium
slack_ts: '1785555394.572679'
source: cs.RO - Robotics
status: unread
title: 'It''s Not Just More Demos: Counterfactual Action Sensitivity Coverage for
  Data-Efficient Robust Robot Imitation'
---
# It's Not Just More Demos: Counterfactual Action Sensitivity Coverage for Data-Efficient Robust Robot Imitation
> 原文: [https://arxiv.org/abs/2607.27261](https://arxiv.org/abs/2607.27261)

arXiv:2607.27261v1 Announce Type: new
Abstract: Visuomotor imitation learning has demonstrated success for manipulation tasks. However, the trained policies remain brittle to visual `nuisances', with even minor task-preserving variations such as lighting, distractions or changes in colour result in heavy degradation of the trained policy's performance. While increasing data diversity can improve robustness, it is unclear which additional demonstrations are informative for a particular trained policy. We propose Counterfactual Nuisance Behaviour Cloning (CFNBC), an offline data-selection framework for targeted robustness repair. Starting from a nominal policy trained on `clean' demonstrations, CFNBC generates paired clean and nuisance observations that preserve the expert action, then measures \emph{action drift}: the change in the policy's predicted action under a nuisance that should not alter the desired behaviour. This provides a policy-specific sensitivity signal for selecting a compact, response-diverse repair set from a larger candidate pool, without requiring rollout success labels or online policy execution. We show in MuJoCo bimanual cube transfer and SimplerEnv cube stacking that action drift correlates with nuisance-induced failure, and that response-guided repair with only $20$--$30$ selected candidates substantially outperforms matched-budget random selection while approaching the performance of much larger random repair budgets. These results support a data-centric view of robustness repair: the most useful data are not necessarily the most numerous, visually diverse, or obviously difficult, but the examples that cover fragile response modes of the current policy.
