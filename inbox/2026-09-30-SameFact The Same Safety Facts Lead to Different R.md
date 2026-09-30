---
interest: medium
link: https://arxiv.org/abs/2609.35872
next_step: skim
priority: low
slack_ts: '1790745152.176429'
source: cs.CR - Cryptography and Security
status: unread
title: 'SameFact: The Same Safety Facts Lead to Different Responses Across Interfaces'
---
# SameFact: The Same Safety Facts Lead to Different Responses Across Interfaces
> 原文: [https://arxiv.org/abs/2609.35872](https://arxiv.org/abs/2609.35872)

arXiv:2609.35872v1 Announce Type: new
Abstract: Safety evaluations often ask whether a model recognizes that an action is unsafe, whereas agent evaluations ask what the model chooses to do. Using safety judgments as evidence about action selection therefore raises a measurement question: does the influence of the same safety-relevant fact persist across response interfaces? We introduce SameFact, a matched-counterfactual benchmark that tests this question directly. SameFact contains 300 safe/unsafe pairs that hold the task, prior observations, candidate action, identifiers, and non-target facts fixed while changing a single state-grounded safety fact. Across six LLM backbones, we measure the effect of this matched intervention through three interfaces at the same candidate-action boundary: explicit safety judgment, checkpoint candidate admission, and open first-action selection. All six backbones show lower aggregate sensitivity under open first-action selection than under judgment, but the change is not a uniform attenuation: across 24 model-factor cells, Spearman agreement falls from 0.817 between judgment and checkpoint admission to 0.470 between judgment and open first-action selection, while pairwise ordering disagreement rises from 18.5% to 32.6%. A follow-up 2x2 first-response experiment shows that a checkpoint-style protocol increases measured sensitivity in all six backbones by 8.4-29.3 percentage points, whereas action-space effects and their interactions with protocol vary in magnitude and direction across models. These results show that the response interface is part of the measured quantity: judgment and action interfaces share safety signal, but do not provide interchangeable measurements of how safety-relevant facts shape model responses.
