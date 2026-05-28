---
title: "Genetic algorithm vs. gradient descent for training a neural network architecture dedicated to low data regimes in small medical datasets"
source: "cs.NE - Neural and Evolutionary Computing"
link: https://arxiv.org/abs/2605.27411
priority: low
status: unread
interest: medium
next_step: skim
---
# Genetic algorithm vs. gradient descent for training a neural network architecture dedicated to low data regimes in small medical datasets
> 原文: [https://arxiv.org/abs/2605.27411](https://arxiv.org/abs/2605.27411)

arXiv:2605.27411v1 Announce Type: new
Abstract: Aim/Introduction: Distance-encoding biomorphic-informational neural network (DEBI-NN) is a recently proposed architecture in which connection weights are defined by the distances between neurons positioned in a Euclidian space. This approach drastically reduces the number of trainable parameters compared to classical neural networks in which weights are directly trained. The training process for DEBI-NN is based on a genetic algorithm (GA), rather than gradient descent (GD) which remains the prevailing optimization algorithm in deep learning. We aim to design and implement a GD learner for DEBI-NN and assess its performance compared to GA.
Materials and Methods: We designed a spatial backpropagation scheme tailored to DEBI-NN and carried out a comparison between GD and GA for classification tasks, using a synthetic non-linear "two-moons" dataset, two clinical medical imaging radiomic datasets and a fetal cardiotocography dataset with a sample sizes ranging from n=85 to n=2126. Each optimizer was tuned through targeted hyperparameter searches adapted to each dataset.
Results: Across all experiments, GA consistently produced superior decision boundaries and classification performance (Synthetic: 100% vs 83%; DLBCL: 83% vs 78%; HECKTOR: 80% vs 67%; Fetal: 81% vs 66%), whereas GD exhibited instability and failed to fully capture the non-linear patterns inherent to DEBI-NN's spatial encoding. The entangled gradients resulting from neuron interdependencies limit the effectiveness of classical backpropagation.
Conclusion: These findings highlight fundamental limitations of gradient-based methods in architectures with highly interdependent spatial parameters and confirm the suitability of evolutionary strategies for training DEBI-NN.
