---
title: "A Camera-Native Stereo VR180 Dataset"
source: "cs.CV - Computer Vision"
link: https://arxiv.org/abs/2610.10607
priority: medium
status: unread
interest: medium
next_step: skim
---
# A Camera-Native Stereo VR180 Dataset
> 原文: [https://arxiv.org/abs/2610.10607](https://arxiv.org/abs/2610.10607)

arXiv:2610.10607v1 Announce Type: new
Abstract: Immersive VR180 video is increasingly produced with professional stereo fisheye cameras, yet public VR180 research resources are mostly collected from online platforms such as YouTube: already stitched, projected and compressed by unknown pipelines, and without lens calibration. We present a firsthand-captured stereo VR180 dataset recorded with two Blackmagic URSA Cine Immersive cameras. It contains 1,211 samples -- 636 stereo video clips (2,220.8 s, mostly 90 fps) and 575 stereo stills -- each released as camera-native Blackmagic RAW, separate-eye native fisheye HEVC (8160x7200 per eye) and half-equirectangular HEVC (7200x7200 per eye), together with the factory lens calibration, portable fisheye/half-equirectangular conversion tools and AI-generated scene and visual-challenge annotations. Re-encoding the released fisheye and half-equirectangular renders with x265 over 24 clips, both eyes, four rate points and nine viewing directions, native-fisheye coding needed more bitrate than half-equirectangular coding at equal viewport quality for all 24 clips (median +38%), in every part of the field of view. Data: https://huggingface.co/datasets/lulinxuan/VR180 ; code: https://github.com/lulinxuan/vr180-dataset-tools
