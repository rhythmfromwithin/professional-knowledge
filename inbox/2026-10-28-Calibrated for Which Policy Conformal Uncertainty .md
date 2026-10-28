---
title: "Calibrated for Which Policy? Conformal Uncertainty for Fixed World Models Under Intervention"
source: "cs.LG - Machine Learning"
link: https://arxiv.org/abs/2610.35877
priority: high
status: unread
interest: medium
next_step: skim
---
# Calibrated for Which Policy? Conformal Uncertainty for Fixed World Models Under Intervention
> 原文: [https://arxiv.org/abs/2610.35877](https://arxiv.org/abs/2610.35877)

arXiv:2610.35877v1 Announce Type: new
Abstract: Changing a deployment policy can invalidate a world model's uncertainty while leaving the physical transition mechanism and predictor unchanged. For one-step prediction, if source and target laws share the conditional mechanism $P(Y|X)=Q(Y|X)$, then the intervention is identified by the pre-outcome change of measure $w(X)=dQ\_X/dP\_X$. For policy-controlled dynamics this ratio factors into state-occupancy and action-propensity terms. Weighted conformal calibration transports marginal coverage to the target law; with an estimated ratio $\hat w$, $P\_Q\{Y \in C\_{\hat w}(X)\} \ge 1-\alpha-TV(Q,\hat Q) \ge 1-\alpha-E\_P|w-\hat w|$. Population log-loss regret for a source-versus-target domain classifier bounds the same ratio error. If $h$ is its clipped target posterior, $\rho$ is the target-domain prior, and $\Delta(h)$ is population log-loss regret, then $E\_P|w-\hat w\_h| \le (1/(\rho\gamma))\sqrt{\Delta(h)/2}$. An exact cancellation improves the dependence from a generic odds-map bound of order $\gamma^{-2}$ to $(\rho\gamma)^{-1}$. Our experiments use a released DINO-feature world model and physical Franka trajectories. Under the strongest controlled state-action shift, ordinary 90% conformal sets cover 55.0%, whereas oracle and learned-ratio calibration cover 91.0% and 90.9%. The learned surrogate remains within 0.9% total variation of the target law. Calibration is relative to the deployment law: the model can remain fixed while calibration follows the intervention. We machine-check in Lean 4 the finite-support algebraic and causal identities used in the classifier-regret argument, including its coverage-composition step.
