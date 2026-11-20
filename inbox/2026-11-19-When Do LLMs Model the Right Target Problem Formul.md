---
interest: medium
link: https://arxiv.org/abs/2611.23638
next_step: skim
priority: medium
slack_ts: '1795157504.924739'
source: cs.CY - Computers and Society
status: unread
title: When Do LLMs Model the Right Target? Problem Formulation in High-Stakes Risk
  Prediction
---
# When Do LLMs Model the Right Target? Problem Formulation in High-Stakes Risk Prediction
> 原文: [https://arxiv.org/abs/2611.23638](https://arxiv.org/abs/2611.23638)

arXiv:2611.23638v1 Announce Type: new
Abstract: Generative AI is increasingly used to assist with data science tasks, yet fundamental questions remain about its ability to correctly formulate analytical problems. We investigate how well large language models (LLMs) can formulate prediction problems when developing models for high-stakes decision making. We focus on one particular challenge to validity: decision dependency, which arises when historical decisions affect observed outcomes. We evaluate this aspect of problem formulation in LLM-generated code and explanations across child-welfare, healthcare, and employment settings, using 11 models from OpenAI and Anthropic and seven prompt conditions. We assess whether the LLM-generated code implements a procedure appropriate for estimating the intended outcome under the study's assumptions and whether the explanation acknowledges decision dependency. We find that LLMs do not reliably address decision dependency without guidance in the prompt. When prompts specify the target, the assumption needed to estimate it, and the estimation procedure, target-aligned implementation reaches 99-100%. Among frontier models, a simple prompt description of how decisions affect outcomes appears sufficient to elicit target-aligned implementation. Some responses also acknowledge decision dependency without addressing it in their code. Our findings suggest that analysts should not rely on LLMs to correctly formulate prediction problems without explicit methodological guidance and careful review. We propose validity-centered guidelines for LLM-assisted predictive modeling, covering prompt formulation, validation of the target and estimation procedure, and identification of key assumptions. Establishing validity is a necessary early step in evaluating whether to deploy a predictive model in a high-stakes setting, but deployment requires weighing broader ethical, institutional, and practical considerations.
