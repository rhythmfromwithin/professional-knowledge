---
title: "EndoLIFT: Language-Disambiguated Latent-Conditioned Rectified Flow for Bidirectional Endoscopic Control"
source: "cs.RO - Robotics"
link: https://arxiv.org/abs/2608.20478
priority: medium
status: unread
interest: medium
next_step: skim
---
# EndoLIFT: Language-Disambiguated Latent-Conditioned Rectified Flow for Bidirectional Endoscopic Control
> 原文: [https://arxiv.org/abs/2608.20478](https://arxiv.org/abs/2608.20478)

arXiv:2608.20478v1 Announce Type: new
Abstract: Routine gastrointestinal endoscopy is intrinsically bidirectional: the instrument is advanced to reach target anatomy and later withdrawn or retroflexed for inspection, while an external cue may require earlier reversal. When the requested phase changes before the visual scene does, nearly identical observations can require opposite axial actions. We identify and formalize this ambiguity in bidirectional endoscopic control as intent aliasing. We propose EndoLIFT (Endoscopic Language-Instruction Flow with Trajectory Latents), a vision-language-action policy that combines explicit language-based intent conditioning with a latent-conditioned rectified-flow action expert. The policy receives RGB, a language instruction, and the previous-action state; a 32-D variational trajectory latent stochastically conditions continuous action-chunk generation. Controlled same-observation instruction swaps establish that language selects the axial mode, independently of whether the trajectory latent is present. Relative to the matched model without latent conditioning, EndoLIFT improves navigation-direction accuracy by 11.1 percentage points and reduces wrong-direction advance by 83\%. An architecture-controlled 1-bit mode-flag reference exhibits weaker canonical-anchor switching, while EndoLIFT retains 82.8\% intent-following accuracy across 44 held-out linguistic variants. In closed-loop evaluation, EndoLIFT improves overall success by 30 percentage points over EndoLIFT w/o VTL on both the seen colon phantom and the unseen lung and stomach phantoms, and completes 10/10 ex-vivo porcine-trachea trials. These results separate language-based intent selection from the trajectory latent's contribution to directional correctness and robust retraction.
