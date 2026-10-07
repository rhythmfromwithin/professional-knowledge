---
interest: medium
link: https://arxiv.org/abs/2610.03888
next_step: skim
priority: high
slack_ts: '1791351203.066889'
source: cs.AI - Artificial Intelligence
status: unread
title: 'REACT: Physically and Chemically Consistent Reconstruction of Marine Active
  Tracers'
---
# REACT: Physically and Chemically Consistent Reconstruction of Marine Active Tracers
> 原文: [https://arxiv.org/abs/2610.03888](https://arxiv.org/abs/2610.03888)

arXiv:2610.03888v1 Announce Type: new
Abstract: Reconstructing global sea surface pH from sparse observations is critical for monitoring ocean acidification and understanding marine carbon cycling. Traditional assimilation and inverse models are physically grounded but costly for large-scale reconstruction. Recent black-box and physics-guided AI models improve efficiency, but are mainly designed for passive tracers, where the reconstructed variable is also the transported inventory. In contrast, pH is an active carbonate tracer: it is the prediction target, while dissolved inorganic carbon (DIC) is the conserved carbon inventory. This mismatch can produce low pH error while violating carbonate closure and source-free carbon conservation. To address this, we introduce \textbf{REACT}, a carbon-first reconstruction framework that decouples transport, active correction, and chemical decoding. REACT transports a latent carbonate state with a conservative advection--diffusion solver, captures non-conservative carbon-cycle variations with a source module, decodes the corrected state into pH, and constrains the output through carbonate equilibrium. This design keeps pH as the target while enforcing consistency on the underlying carbon state. On simulation data, REACT reduces pH NRMSE by (14.7%) and chemical consistency error by (24.0%) over the best baseline. Cross-temporal-scale evaluations show robustness against error accumulation from coarse to fine temporal scales, and ablation studies validate the effectiveness of each component.
