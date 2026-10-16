---
title: "Forensic Analysis of the HackRF One with PortaPack Mayhem Firmware"
source: "cs.CR - Cryptography and Security"
link: https://arxiv.org/abs/2610.20647
priority: low
status: unread
interest: medium
next_step: skim
---
# Forensic Analysis of the HackRF One with PortaPack Mayhem Firmware
> 原文: [https://arxiv.org/abs/2610.20647](https://arxiv.org/abs/2610.20647)

arXiv:2610.20647v1 Announce Type: new
Abstract: Software-defined radios (SDRs) have become an inexpensive, portable platform for replay attacks, location spoofing and jamming. The HackRF One can operate stand-alone when fitted with a PortaPack interface board running the open-source Mayhem firmware. No peer-reviewed study has addressed the forensic analysis of this device family. This work establishes, at source-code level, where forensically relevant data reside on the microSD card of a device running Mayhem v2.0.1, in which format, when they are written and how they should be interpreted. The methodology is applied to an SD card image that the author acquired from their own device after four months of real use, and every inference is drawn from the image alone. The workflow covers timestamp rules that depend on the real-time clock (RTC) battery state, traces of on-device trimming and text editing, cluster-level recovery of deleted in-phase/quadrature (IQ) captures, and decoding of recorded signals cross-checked with an independent decoder. In the example image, the final part of a deleted IQ capture and a trimmed-away capture segment are recovered, and six captures are attributed to a single rolling-code on-off keying (OOK) transmitter sharing one 32-bit identifier. The study provides practitioners with an artifact catalogue, interpretation rules and acquisition recommendations.
