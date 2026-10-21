---
title: "One-shot learning of paired association navigation with biologically plausible schemas"
source: "cs.NE - Neural and Evolutionary Computing"
link: https://arxiv.org/abs/2106.03580
priority: low
status: unread
interest: medium
next_step: skim
---
# One-shot learning of paired association navigation with biologically plausible schemas
> 原文: [https://arxiv.org/abs/2106.03580](https://arxiv.org/abs/2106.03580)

arXiv:2106.03580v5 Announce Type: replace
Abstract: After learning a multiple paired-association (MPA) navigation task, rodents can rapidly learn new cue-location associations after a single exposure, a phenomenon proposed to be facilitated by cognitive schemas. However, it remains unclear what schemas support this behavior and how they could be implemented in biological neural circuits. Here, we identify a set of schemas sufficient for gradual then one-shot paired-association navigation, and implement them in a fully neural agent using biologically plausible plasticity rules. The agent gradually acquires a low-dimensional spatial metric representation using a path-integration based temporal-difference error, enabling self-localization across different environments. It also contains a memory network that forms one-shot associations between sensory cues and goal locations, implemented using reward-modulated exploratory Hebbian (EH) plasticity. A third network performs vector subtraction between the agent's current and goal location to compute goal-directed actions. Supplementing these schemas with an actor-critic enables one-shot navigation past obstacles. Lastly, learning a working-memory gating mechanism using the temporal-difference error enables one-shot learning even with brief cue and distractor presentation. The model reproduces key behavioral features of rodent learning in the MPA task and generates testable predictions about the neural mechanisms underlying schema-based one-shot learning.
