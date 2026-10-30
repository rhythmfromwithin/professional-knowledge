---
interest: medium
link: https://arxiv.org/abs/2610.35904
next_step: skim
priority: medium
slack_ts: '1793337890.752329'
source: cs.CV - Computer Vision
status: unread
title: 'ObjectTwin: Measuring the Asset Correspondence Gap for Capture-Anchored Digital
  Twins'
---
# ObjectTwin: Measuring the Asset Correspondence Gap for Capture-Anchored Digital Twins
> 原文: [https://arxiv.org/abs/2610.35904](https://arxiv.org/abs/2610.35904)

arXiv:2610.35904v1 Announce Type: new
Abstract: Object-wise reconstruction increasingly inserts generated meshes into captured scenes as editable proxies for observed objects. This use creates a requirement absent from isolated-asset scores and pose estimates: at the captured metric state, the proxy should reproduce calibrated observations of the same instance. We present ObjectTwin, a scan-grounded measurement protocol that freezes the instance, cameras, scan-projected support and recorded depth, metric anchor, and evaluation denominator, then replaces only the object representation. The resulting asset correspondence gap measures lost observation agreement relative to scan-derived visible geometry without treating the scan as complete physical ground truth. Across two indoor RGB-D capture domains and two generation backends, visible, anchored generated assets lose 0.302-0.497 MaskIoU under this replacement. Every tested scene-level estimate is positive, while same-input generator preference reverses across capture domains. Coverage and overlap-depth analyses locate disagreement in both visible support and surface placement; the evaluated conservative pose refinement does not systematically recover it. These results establish capture correspondence as a separately measurable interface between generated-asset quality and stronger physical or task-level evaluation.
