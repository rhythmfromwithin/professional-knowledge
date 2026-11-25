---
title: "Look Where Camouflage Breaks: Concealment-Guided Observation for Camouflaged Object Detection"
source: "cs.CV - Computer Vision"
link: https://arxiv.org/abs/2611.31392
priority: medium
status: unread
interest: medium
next_step: skim
---
# Look Where Camouflage Breaks: Concealment-Guided Observation for Camouflaged Object Detection
> 原文: [https://arxiv.org/abs/2611.31392](https://arxiv.org/abs/2611.31392)

arXiv:2611.31392v1 Announce Type: new
Abstract: A camouflaged object can blend into its surroundings at one scale and become distinguishable at another. Yet a region's apparent ambiguity gives limited guidance on which observation would resolve it. The challenge is to connect the form and scale of concealment to the evidence that a new view can reveal. We introduce CamoBreak, an active framework for camouflaged object detection guided by a Concealment Spectrum. From the image and current predictions, the spectrum measures regional resemblance and boundary ambiguity across comparison scales, distinguishing persistent concealment from separation emerging at finer or broader scales. These measurements guide crop selection from the already-captured image and recognition against global foreground and background references. An object-conditioned spatial preference then selects where local evidence should update the prediction and feature memory, retaining target corrections while suppressing background distractions. Accepted corrections reshape the next measurement, while predicted segmentation benefit determines whether to observe again. Experiments across encoder families and related segmentation tasks show consistent improvements. Targeted analyses support improved small-target recovery, multiple-object coverage, and selective evidence integration. Code will be released.
