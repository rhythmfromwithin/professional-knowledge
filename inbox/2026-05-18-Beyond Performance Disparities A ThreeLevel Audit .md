---
interest: medium
link: https://arxiv.org/abs/2605.15312
next_step: skim
priority: medium
slack_ts: '1779164067.814479'
source: cs.CY - Computers and Society
status: unread
title: 'Beyond Performance Disparities: A Three-Level Audit of Representational Harm
  in CelebA'
---
# Beyond Performance Disparities: A Three-Level Audit of Representational Harm in CelebA
> 原文: [https://arxiv.org/abs/2605.15312](https://arxiv.org/abs/2605.15312)

arXiv:2605.15312v1 Announce Type: new
Abstract: Large-scale facial datasets like CelebA are widely used in computer vision, yet the cultural biases embedded in their labels remain underexplored. Fairness research has distinguished representational from allocational harms, but audits of computer vision datasets have mostly examined categorical labels, leaving open how such harms appear in learned features and model attention. This paper examines CelebA at three levels: dataset structure, learned feature weights, and spatial attention, focusing on how gendered double standards of ageing and beauty are encoded in the data and reproduced in model behaviour. First, hierarchical clustering of 202,599 images shows that the 39 attributes organise into latent trait bundles aligned with cultural archetypes: performative femininity (youth, makeup, adornment) and professional masculinity (ageing, facial hair, formal attire). Female faces, though more often rated attractive overall, incur steep penalties when assigned to ageing or masculine-coded clusters. Second, XGBoost with SHAP analysis reveal gender-specific effects, such as adiposity reducing attractiveness only for females. Third, Grad-CAM finds that predictions for female and younger male subgroups concentrate on mid-face cues, whereas predictions for older males drift toward peripheral cues such as hair and clothing. Older males attain the highest accuracy but the lowest average precision, indicating categorical exclusion of groups outside the dataset's evaluative templates. Cultural double standards thus pass from media representation into dataset labels, feature weights, and model attention, producing two representational harms: hyper-scrutiny of women under a narrow evaluative template, and exclusion of older men from the scheme entirely. Fairness metrics focused on performance disparities mask both, underscoring the need to address representational harm in fairness research.
