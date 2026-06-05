---
title: "NIV: Neural Axis Variations for Variable Font Generation"
source: "cs.CV - Computer Vision"
link: https://arxiv.org/abs/2606.05261
priority: medium
status: unread
interest: medium
next_step: skim
---
# NIV: Neural Axis Variations for Variable Font Generation
> 原文: [https://arxiv.org/abs/2606.05261](https://arxiv.org/abs/2606.05261)

arXiv:2606.05261v1 Announce Type: new
Abstract: Variable fonts enable continuous variation of glyph geometry along semantic design axes such as weight, width, slant, and optical size. However, constructing a variable font from a static font remains a labor-intensive process requiring expert typographic design and manual specification of glyph variation data. We introduce NIV (Neural Axis Variations), a method that automatically converts a static font into a fully functional variable font. Given glyph outlines and a set of desired design axes, NIV predicts per-point displacements. The model operates directly on vector glyph geometry and employs a novel Property Embedding mechanism that captures interactions between multiple axes, enabling consistent multi-axis variation within a unified framework. We train NIV on a newly constructed dataset derived from variable Google Fonts, comprising over one million variation tuples. The resulting model generalizes across unseen code points, unseen font styles, high-complexity CJK glyphs, and even out-of-distribution handwriting inputs. The generated outputs are standard variable font files supporting continuous interpolation via existing rendering engines. To facilitate research, we release the dataset, the complete training and inference implementation, and trained models at https://github.com/ndvbd/NIV. Beyond typography, our approach demonstrates how structured geometric objects with continuous parametric variation can be synthesized using neural deformations.
