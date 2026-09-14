---
interest: medium
link: https://arxiv.org/abs/2609.11952
next_step: skim
priority: low
slack_ts: '1789360365.762679'
source: cs.CR - Cryptography and Security
status: unread
title: 'ChemMat-AgentSafetyBench: Evaluating Long-Horizon Attacks and Defenses in
  Chemistry and Materials Agents'
---
# ChemMat-AgentSafetyBench: Evaluating Long-Horizon Attacks and Defenses in Chemistry and Materials Agents
> 原文: [https://arxiv.org/abs/2609.11952](https://arxiv.org/abs/2609.11952)

arXiv:2609.11952v1 Announce Type: new
Abstract: Chemistry and materials agents integrate literature retrieval, candidate generation, property prediction, and protocol planning into continuous discovery workflows. Consequently, the relevant safety question is shifting from whether a model answers a hazardous question to whether an agent releases a hazardous protocol through a tool-mediated workflow. We introduce \bench, a benchmark that evaluates whether chemistry and materials agents can be steered toward hazardous endpoints through user input, tool observations, or persistent memory. The benchmark contains 432 fixed harmful case specifications spanning eight hazard classes, three scenario shells, four tool-and-memory environments, a single-turn direct-attack baseline, and five online long-horizon attacks: intent hijacking, tool chaining, objective drifting, task injection, and memory poisoning. The concrete language of each online attack is generated from the evolving trajectory at runtime and is therefore not counted in the static benchmark size. In the four-model main experiment with a fixed attacker, agents release complete hazardous synthesis or preparation procedures in 25.6\% of runs. Replacing the attacker model yields mean success rates from 18.4\% to 26.5\%, indicating that the risk is not an artifact of a single attacker. Input- and state-level defenses adapted from general-purpose agent safety, as well as candidate checks designed for chemistry and materials, reduce some failures but still leave complete-path release rates between 9.2\% and 22.5\%. Existing defenses therefore do not simultaneously cover multi-entry contamination, tool state, and the final artifact boundary. These results highlight a widening gap between the rapid development of scientific agents and the safety evaluation and defenses available to the chemistry and materials community.
