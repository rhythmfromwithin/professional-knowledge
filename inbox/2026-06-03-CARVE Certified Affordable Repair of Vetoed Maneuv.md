---
title: "CARVE: Certified Affordable Repair of Vetoed Maneuvers via Envelopes for Interactive Driving"
source: "cs.RO - Robotics"
link: https://arxiv.org/abs/2606.02641
priority: medium
status: unread
interest: medium
next_step: skim
---
# CARVE: Certified Affordable Repair of Vetoed Maneuvers via Envelopes for Interactive Driving
> 原文: [https://arxiv.org/abs/2606.02641](https://arxiv.org/abs/2606.02641)

arXiv:2606.02641v1 Announce Type: new
Abstract: Interactive driving exposes a failure mode that is easy to miss in rule-aware autonomous-driving stacks: a hard-rule margin can be negative for an ego candidate even though a small lawful accommodation by a non-priority agent would restore feasibility. Existing rulebooks, shields, and reachability filters are strong at vetoing unsafe actions, while prediction-based planners model likely responses. Neither returns a runtime proof object that states which bounded multi-agent edit repairs the maneuver, who owns the edit, whether the request is right-of-way affordable, and what ego fallback remains if the request is not observed. We formulate this missing object as \*interactive repair certification\* and introduce \*CARVE\*, a prediction-free certificate layer over a finite lattice of ego-owned and agent-owned tactical operators. Agent-owned requests are admissible only inside \(B\_j(s) = \beta(\pi\_j)\alpha\_j^{\max}(s)\), a cooperation envelope that separates kinematic reachability from normative priority. The resulting certificate records the binding rule, repair category, repair set, responsibility-weighted cost split, and fallback. On 589 Lanelet2-geometry-grounded INTERACTION replay episodes, CARVE-Greedy accepts 98.64% of initially vetoed maneuvers and recovers 370/378 human-resolved false vetoes, while preserving 589/589 right-of-way respect, zero priority-agent false positives, and 400/400 negative-stress vetoes. We prove certificate soundness, structural right-of-way respect, exact finite-lattice minimality, fallback contingency, and blame-consistency conditions. CARVE does not predict or require another driver's compliance; it certifies whether a proposed interaction is bounded, attributable, and normatively admissible under declared assumptions.
