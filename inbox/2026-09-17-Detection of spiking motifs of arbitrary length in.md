---
interest: medium
link: https://arxiv.org/abs/2511.15296
next_step: skim
priority: low
slack_ts: '1789705159.582199'
source: q-bio.NC - Neurons and Cognition
status: unread
title: Detection of spiking motifs of arbitrary length in neural activity using bounded
  synaptic delays
---
# Detection of spiking motifs of arbitrary length in neural activity using bounded synaptic delays
> 原文: [https://arxiv.org/abs/2511.15296](https://arxiv.org/abs/2511.15296)

arXiv:2511.15296v2 Announce Type: replace
Abstract: In the context of spiking neural networks, the temporal coding hypothesis is increasingly preferred over the rate coding hypothesis due to its advantages in processing speed and energy efficiency. In temporal coding, synaptic delays are crucial for processing signals with precise spike timings, known as spiking motifs. Synaptic delays are however bounded in the brain and can thus be shorter than the duration of a motif. This prevents the use of motif recognition methods that consist of setting heterogeneous delays to synchronize the input spikes on a single output neuron acting as a coincidence detector. To address this issue, we developed a method to detect motifs of arbitrary length using a sequence of output neurons connected to input neurons by bounded synaptic delays. Each output neuron is associated with a sub-motif of bounded duration. A motif is recognized if all sub-motifs are sequentially detected by the output neurons. We simulated this network using leaky integrate-and-fire neurons and tested it on the Spiking Heidelberg Digits (SHD) database, that is, on audio data converted to spikes via a cochlear model, as well as on random simultaneous motifs. The results demonstrate that the network can effectively recognize motifs of arbitrary length extracted from the SHD database. Our method features a correct detection rate of about 60\% in presence of ten simultaneous motifs from the SHD dataset and up to 80\% for five motifs, showing the robustness of the network to noise. Results on random overlapping patterns show that the recognition of a single motif overlapping with other motifs is most effective for a large number of input neurons and sparser motifs. Our method provides a foundation for more general models for the storage and retrieval of neural information of arbitrary temporal lengths.
