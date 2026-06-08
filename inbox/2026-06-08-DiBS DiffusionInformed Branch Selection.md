---
interest: medium
link: https://arxiv.org/abs/2606.06518
next_step: skim
priority: high
slack_ts: '1780894165.138429'
source: cs.AI - Artificial Intelligence
status: unread
title: 'DiBS: Diffusion-Informed Branch Selection'
---
# DiBS: Diffusion-Informed Branch Selection
> 原文: [https://arxiv.org/abs/2606.06518](https://arxiv.org/abs/2606.06518)

arXiv:2606.06518v1 Announce Type: new
Abstract: Sudoku is a representative constraint satisfaction problem that requires global structural reasoning under strict discrete constraints. The existing works of solving Sudoku mainly focus on two dominant approaches, i.e., traditional heuristic and deep learning solver. However, they suffer from two complementary limitations: learning-based solvers lack hard correctness guarantees, while complete symbolic solvers are still prone to long-tail search. To address these shortcomings, we propose a novel diffusion model-guided approach, termed as DiBS, for the branch selection search process. Specifically, DiBS keeps the symbolic solver complete and uses the diffusion model as a branch-ordering guide. The core method is ranking candidate values under the current partial assignment and lightweight consistency signal. Furthermore, we provide an in-depth theoretical proof to reveal how it works and why it works. Experiments on the challenging Royle 17-clue Sudoku benchmark show that our DiBS substantially reduces search cost relative to strong heuristic baselines, especially in nodes, backtracks, and long-tail percentiles. Besides, these results confirm that learned global guidance is effective on hard instances where branch-order mistakes are most expensive. All codes are available at https://github.com/shanxierdan/DiBS.
