---
interest: medium
link: https://arxiv.org/abs/2608.14736
next_step: skim
priority: low
slack_ts: '1787190033.340769'
source: cs.CR - Cryptography and Security
status: unread
title: 'Not Discrete Enough: On the Inherent Insecurity of dTPMs for Measured Boot'
---
# Not Discrete Enough: On the Inherent Insecurity of dTPMs for Measured Boot
> 原文: [https://arxiv.org/abs/2608.14736](https://arxiv.org/abs/2608.14736)

arXiv:2608.14736v1 Announce Type: new
Abstract: Measured Boot, a mechanism enabled through Trusted Platform Modules (TPMs), is commonly used for passwordless protection of data-at-rest, aiming to protect data when the device is lost or stolen. Microsoft's standpoint is neutral on which way a TPM should be implemented: Firmware-based TPMs (fTPMs) are viewed as more economical but less secure. Despite the inherent susceptibility to bus sniffing attacks, discrete TPMs (dTPMs) are still seen as the gold standard, as many deliver better on-paper tamper resistance. It is often argued that attacks against the bus can be mitigated by bus encryption and, ideally, mutual authentication between the CPU and TPM. This position paper aims to emphasize another inherent, difficult-to-mitigate attack against dTPMs that was originally shown against a TPM 1.1 over 20 years ago: We demonstrate that even brief physical access to a TPM 2.0 and the ability to boot from an attacker-controlled system enable an attacker to reset and replay arbitrary measurements, thereby allowing an attacker to unseal, for example, a disk encryption key solely protected by the TPM. While there have been attacks against fTPMs, too, we argue that their practical attack surface is fundamentally smaller. Bus protection techniques can be used to protect dTPMs, but only guard against passive attacks. After all, we argue that, from a security standpoint, firmware TPMs, or any TPM internal to the SoC, are superior to discrete (external) ones. Lastly, in order for dTPM-based setups to provide meaningful protection of sealed secrets, configurations must require a user-provided PIN or password along with the Measured Boot configuration.
