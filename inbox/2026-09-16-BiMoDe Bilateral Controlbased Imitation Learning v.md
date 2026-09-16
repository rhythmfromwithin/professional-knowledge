---
interest: medium
link: https://arxiv.org/abs/2609.16040
next_step: skim
priority: medium
slack_ts: '1789532927.843249'
source: cs.RO - Robotics
status: unread
title: 'Bi-MoDe: Bilateral Control-based Imitation Learning via Modifier-Conditioned
  Decoding for Modulation of Execution Speed and Contact Intensity'
---
# Bi-MoDe: Bilateral Control-based Imitation Learning via Modifier-Conditioned Decoding for Modulation of Execution Speed and Contact Intensity
> 原文: [https://arxiv.org/abs/2609.16040](https://arxiv.org/abs/2609.16040)

arXiv:2609.16040v1 Announce Type: new
Abstract: Bilateral control-based imitation learning captures both position and force information, making it well suited to contact-rich manipulation. However, existing approaches provide limited means for an operator to specify how a learned task should be executed at inference time, such as slowly or quickly, gently or firmly. We propose Bi-MoDe, a modifier-conditioned decoding framework that injects a constrained latent into every layer of the Transformer action decoder via adaLN-Zero, allowing behavioral directives to directly influence action-chunk generation. We evaluate the method on a real-world whiteboard wiping task with combinations of temporal and physical modifiers. Bi-MoDe improves physical directive following over the action-chunking baseline while maintaining comparable temporal control. An ablation further shows that decoder conditioning and latent-space composition interact, and that their combination is important for accurate physical directive following. Additional material is available at the https://mertcookimg.github.io/bi-mode/
