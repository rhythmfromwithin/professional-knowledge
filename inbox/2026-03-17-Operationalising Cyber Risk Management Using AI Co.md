---
title: "Operationalising Cyber Risk Management Using AI: Connecting Cyber Incidents to MITRE ATT&CK Techniques, Security Controls, and Metrics"
source: "cs.CR - Cryptography and Security"
link: https://arxiv.org/abs/2603.12455
priority: low
status: unread
interest: medium
next_step: skim
---
# Operationalising Cyber Risk Management Using AI: Connecting Cyber Incidents to MITRE ATT&CK Techniques, Security Controls, and Metrics
> 原文: [https://arxiv.org/abs/2603.12455](https://arxiv.org/abs/2603.12455)

arXiv:2603.12455v1 Announce Type: new
Abstract: The escalating frequency of cyber-attacks poses significant challenges for organisations, particularly small enterprises constrained by limited in-house expertise, insufficient knowledge, and financial resources. This research presents a novel framework that leverages Natural Language Processing to address these challenges through automated mapping of cyber incidents to adversary techniques. We introduce the Cyber Catalog, a knowledge base that systematically integrates CIS Critical Security Controls, MITRE ATT&CK techniques, and SMART metrics. This integrated resource enables organisations to connect threat intelligence directly to actionable controls and measurable outcomes. To operationalise the framework, we fine-tuned all-mpnet-base-v2, a highly regarded sentence-transformers model used to convert text into numerical vectors on an augmented dataset comprising 74,986 incident-technique pairs to enhance semantic similarity between cyber incidents and MITRE ATT&CK techniques. Our fine-tuned model achieved a Spearman correlation of 0.7894 and Pearson correlation of 0.8756, demonstrating substantial improvements over top baseline models including all-mpnet-base-v2, all-distilroberta-v1, and all-MiniLM-L12-v2. Furthermore, our model exhibited significantly lower prediction errors (MAE = 0.135, MSE = 0.027) compared to all baseline models, confirming superior accuracy and consistency. The Cyber Catalog, training dataset, trained model, and implementation code made publicly available to facilitate further research and enable practical deployment in resource-constrained environments. This work bridges the gap between threat intelligence and operational security management, providing an actionable tool for systematic cyber incident response and evidence-based cyber risk management.
