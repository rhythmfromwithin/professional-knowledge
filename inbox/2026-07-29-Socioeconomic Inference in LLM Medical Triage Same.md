---
interest: medium
link: https://arxiv.org/abs/2607.22605
next_step: skim
priority: medium
slack_ts: '1785468998.186929'
source: cs.CY - Computers and Society
status: unread
title: 'Socioeconomic Inference in LLM Medical Triage: Same Symptoms, Different ZIP
  Code'
---
# Socioeconomic Inference in LLM Medical Triage: Same Symptoms, Different ZIP Code
> 原文: [https://arxiv.org/abs/2607.22605](https://arxiv.org/abs/2607.22605)

arXiv:2607.22605v1 Announce Type: new
Abstract: We investigate whether large language models alter medical triage recommendations for identical symptoms when only the patient's socioeconomic status (SES) varies. Using three deployment-tier models (Gemini 3.5 Flash, Claude Sonnet 4.6, GPT-5.4-mini), we hold a single neurological symptom profile fixed and vary the SES signal along two channels: explicit (insurance status, occupation, housing) and implicit (a US ZIP code, with no other socioeconomic information). All three models raise their emergency-room (ER) referral rate for lower-SES patients given the explicit signal (spreads of 13-50 percentage points). The effect is in the protective direction: lower-SES patients are sent to the ER more often, not less. The model's stated reasoning stays clinically near-identical across conditions, so the shift is invisible to a reasoning-trace audit. Critically, sensitivity to the implicit ZIP-code signal is model-dependent: Gemini infers SES from geography alone, shifting its ER rate by a pooled 11.4 points across six US ZIP-code pairs (p = 1.4e-7, same direction in 6/6 pairs), while Claude Sonnet 4.6 stays flat (-0.1 points) and GPT-5.4-mini shows only a small difference that is not sign-consistent (2.0 points, predicted direction in just 2 of 6 pairs), neither a reliable ZIP-code effect, despite both responding to the explicit signal. This reveals an explicitness gradient in the signal: every model acts on socioeconomic status when it is stated outright, but only Gemini Flash acts on it when it must be inferred from a proxy as thin as five digits. We read this as a model-specific difference rather than a size or cost effect. A single-sentence system-prompt instruction reduces but does not eliminate the effect (Gemini's gap between low- and high-income ZIPs falls from 11.4 to 5.8 points). We release all code, prompts, and raw results.
