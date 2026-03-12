---
interest: medium
link: https://medium.com/airbnb-engineering/academic-publications-airbnb-tech-2025-year-in-review-7d79f57d3b52?source=rss
next_step: skim
slack_ts: '1773283525.266519'
source: Airbnb Engineering
title: 'Academic Publications & Airbnb Tech: 2025 Year in Review'
----53c7c27702d5---4
priority: medium
status: unread
---
# Academic Publications & Airbnb Tech: 2025 Year in Review
> 原文: [https://medium.com/airbnb-engineering/academic-publications-airbnb-tech-2025-year-in-review-7d79f57d3b52?source=rss----53c7c27702d5---4](https://medium.com/airbnb-engineering/academic-publications-airbnb-tech-2025-year-in-review-7d79f57d3b52?source=rss----53c7c27702d5---4)

![](https://cdn-images-1.medium.com/max/1024/1*FfdFpfjGZODh7ltZ2W2Mrg.jpeg)

2025 was a big year for research at Airbnb, as we made significant progress toward our mission to use AI, data science, and machine learning to become the best travel and living platform.

Specifically, we doubled down on our presence at long-standing venues like KDD and CIKM — two of the most selective conferences in machine learning. At the same time, we expanded our research footprint by sharing our work in NLP, optimization, and measurement science at conferences such as COLING, LION, and VLDB.

Across these conferences, Airbnb researchers engaged directly with academic and industry peers by publishing and presenting papers, learning about the latest innovations, launching new collaborations, and mentoring emerging researchers. In this blog post, we’ll recap the conferences and key papers we presented in 2025, organized by research themes.

### Applied machine learning for search, ranking, and personalization

### KDD (Knowledge and Data Mining)

[*KDD*](https://kdd2025.kdd.org/) *is a flagship conference in data science research. Hosted annually by a special interest group of the Association for Computing Machinery (ACM), it’s where researchers learn about some of the most groundbreaking developments in data mining, knowledge discovery, and large-scale data analytics, which are critical to Airbnb’s efforts to improve core products like search and recommendations.*

**Our participation**

We’ve been presenting at KDD since 2018, and 2025 was another strong year for us. We received multiple contributions across the applied data science track and workshops, which were well-received by the broader community and even inspired us to consider open-sourcing some of our technology. We were also inspired by the related research in this area and are eager to explore these methods through new collaborations.

**Research highlights**

1. [Harnessing the Power of Interleaving and Counterfactual Evaluation for Airbnb Search Ranking](https://arxiv.org/abs/2508.00751): While A/B tests are crucial for developing ranking algorithms and recommender systems, they’re difficult to set up and can take extensive time to reach statistical significance (especially for products with long conversion cycles, like accommodation booking). In this paper, we shared techniques for rapid pre-A/B online assessments that help teams identify the most promising experiments, streamlining the overall process without sacrificing accuracy.
2. [High Precision Audience Expansion via Extreme Classification in a Two-Sided Marketplace](https://drive.google.com/file/d/1Zeqk6aKXsCEFevB_jAbw4AXzxJ30uKwR/view): Airbnb search balances diverse global inventory with varied guest preferences for location, amenities, style, and price. This process requires efficient location retrieval to find the listings guests might realistically book by determining which geographic areas to query. We introduce a new approach to location retrieval by using a set of relevant, high-precision categorical location cells.

**Link to all papers**

* [Harnessing the Power of Interleaving and Counterfactual Evaluation for Airbnb Search Ranking](https://dl.acm.org/doi/10.1145/3711896.3737232) (Qing Zhang, Alex Deng, Michelle Du, Huiji Gao, Liwei He, Sanjeev Katariya)
* [High Precision Audience Expansion via Extreme Classification in a Two-Sided Marketplace](https://drive.google.com/file/d/1Zeqk6aKXsCEFevB_jAbw4AXzxJ30uKwR/view) (Dillon Davis, Huiji Gao, Thomas Legrand, Juan Manuel Caicedo Carvajal, Malay Haldar, Kedar Bellare, Moutupsi Paul, Soumyadip Banerjee, Liwei He, Stephanie Moyerman, and Sanjeev Katariya)
* [TSMO: Two-sided Marketplace Optimization](https://sites.google.com/view/tsmo2025/home)

### CIKM (Conference on Information and Knowledge Management)

[*CIKM*](https://cikm2025.org/) *is a premier forum for discussing and presenting research at the intersection of information and knowledge management, including topics like AI, data mining, database systems, and information retrieval. Many of these topics directly intersect with our core product challenges, such as search, ranking, and recommendations.*

**Our participation**

At CIKM 2025, Airbnb’s Relevance and Personalization team had [five peer-reviewed papers accepted for publication](https://sites.google.com/view/airbnb-relevance-publications/home?authuser=0), building on our participation in 2023 and 2024. These papers focused on advanced AI/ML techniques for search and recommendations, and sharing real-world insights from using these technologies at Airbnb’s scale. Industry and academic researchers, especially those working on two-sided marketplaces, engaged with our work and provided valuable feedback.

**Research highlights**

1. [Augmenting Guest Search Results with Recommendations at Airbnb](https://dl.acm.org/doi/10.1145/3746252.3761526): When guests use overly narrow criteria to search for accommodations, they often receive insufficient results, leading to a frustrating experience. This paper introduces a recommendation system that dynamically suggests alternatives — different dates, relaxed amenities, or adjusted price ranges — to help guests find suitable accommodations and improve the platform’s booking rate. *Authors: Haowei Zhang, Philbert Lin, Dishant Ailawadi, Soumyadip Banerjee, Shashank Dabriwal, Hao Li, Kedar Bellare, Liwei He, Sanjeev Katariya*
2. [Maps Ranking Optimization in Airbnb](https://dl.acm.org/doi/10.1145/3746252.3761563): Maps play a crucial role in Airbnb search and bookings, accounting for roughly 80% of search interactions. Yet map ranking has traditionally reused feed-ranking assumptions, which break down when we examine the NDCG (Normalized Discounted Cumulative Gain) metric. This paper explains why list-based NDCG fails to model user attention on maps, introduces a map-specific NDCG, and reports experiments showing that optimizing it yields booking gains. *Authors: Hongwei Zhang, Malay Haldar, Kedar Bellare, Sherry Chen, Soumyadip Banerjee, Xiaotang Wang, Mustafa Abdool, Huiji Gao, Pavan Tapadia, Liwei He, Sanjeev Katariya, Stephanie Moyerman*
3. [BListing: Modality Alignment for Listings](https://dl.acm.org/doi/10.1145/3746252.3761577): To improve search ranking, we introduce BiListing (Bimodal Listing) embeddings to use unstructured text and photo listing data as ranking signals. BiListing leverages large-language models and pretrained language-image models to create unified representations of diverse unstructured data into a single embedding vector per list and modality. Our experiment results show a 0.425% increase in NDCB (Normalized Discounted Cumulative Booking) gain and drove tens of millions in incremental revenue. *Authors: Guillaume Guy, Mihajlo Grbovic, Chun How Tan, Han Zhao*
4. [Beyond Pairwise Learning-To-Rank At Airbnb](https://dl.acm.org/doi/10.1145/3746252.3761521): In this paper, we introduce a method to improve the accuracy of pairwise learning-to-rank algorithms, the bedrock of modern search stacks. This approach captures interactions between items during pairwise comparisons, thereby giving us a better sense of what searchers truly want. We also share ways to implement this algorithm performantly, and results from online and offline experiments. *Authors: Malay Haldar, Daochen Zha, Huiji Gao, Liwei He, Sanjeev Katariya*
5. [Learning to Comparison-Shop](https://dl.acm.org/doi/10.1145/3746252.3761567): Traditional ranking models often evaluate items in isolation, disregarding the context in which users compare multiple items on a search results page. In this paper, we propose a novel ranking architecture, the Learning-to-Comparison-Shop (LTCS) System, that explicitly models and learns users’ comparison-shopping behaviors. Our experiments show statistically significant improvements of 1.7% in Normalized Discounted Cumulative Gain (NDCG) and 0.6% in booking conversion rate. *Authors: Jie Tang, Daochen Zha, Xin Liu, Huiji Gao, Liwei He, Stephanie Moyerman, Sanjeev Katariya*

### NLP & building LLM systems in production

### EMNLP (Empirical Methods in Natural Language Processing)

[*EMNLP*](https://2025.emnlp.org/) *is a top-tier NLP conference that brings together practitioners and researchers to discuss new architectures and training strategies for language models, safety and evaluation strategies for LLMs, and real-world NLP applications. These research areas directly intersect with many of Airbnb’s product surfaces, such as customer support, search & discovery, and trust & safety. Additionally, each EMNLP cycle includes the release of new datasets, evaluation suites, and open-source libraries to help teams benchmark their progress against community standards.*

**Our participation**

In 2025, we sponsored EMNLP and presented two papers on humans-in-the-loop in AI systems and advanced summarization techniques. We also used EMNLP’s community datasets to benchmark our system, which showcased where we excel and where we can build upon our success with additional best practices. The conference deepened academic collaborations through discussions on LLM evaluation, safety, and agentic AI design, including mentoring students and early-career researchers.

**Research highlights**

1. [Agent-in-the-Loop, A Data Flywheel for Continuous Improvement in LLM-based Customer Support](https://arxiv.org/abs/2510.06674): To improve our LLM-based customer support system, this paper introduces an Agent-in-the-Loop (AITL) framework that leverages new interaction data to continuously enhance model performance. This flywheel can help the system stay up to date with new product features, shifting user preferences, and updated support policies and procedures. We launched a pilot in the US, and the results demonstrate significant improvement in accuracy and helpfulness. *Authors: Cen Mia Zhao, Tiantian Zhang, Hanchen Su, Yufeng Wayne Zhang, Shaowei Su, Mingzhi Xu, Yu Elaine Liu, Wei Han, Jeremy Werner, Claire Na Cheng, Yashar Mehdad*
2. [Incremental Summarization for Customer Support via Progressive Note-Taking and Agent Feedback](https://arxiv.org/abs/2510.06677): Customer service agents multitask during support interactions, identifying core issues, tracking prior actions, and producing accurate notes. To streamline this workflow, we introduced an incremental summarization system that intelligently determines when to generate concise bullet notes during conversations, reducing agents’ context-switching effort without sacrificing quality. To improve the system over time, we also introduced a learning framework that enables agents to make real-time edits, immediately refining online note generation. *Authors: Yisha Wu, Cen Mia Zhao, Yuanpei Cao, Xiaoqing Su, Yashar Mehdad, Mindy Ji, Claire Na Cheng*

### COLING (International Conference on Computational Linguistics)

[*COLING*](https://coling2025.org/) *is a top-tier NLP conference that covers both foundational research and industry applications of language models, including reasoning, evaluation, multilingual NLP, and real-world LLM systems. The work presented at this conference helps validate Airbnb’s technical direction and directly informs future investments.*

**Our participation**

In 2025, Airbnb presented at COLING for the first time, sharing a paper titled “[LLM-Friendly Knowledge Representation for Customer Support](https://arxiv.org/abs/2510.10331)” by Hanchen Su, Wei Luo, Wei Han, Yu Elaine Liu, Yufeng Wayne Zhang, Cen Mia Zhao, Ying Joy Zhang, and Yashar Mehdad. The paper presents a new format, Intent, Context, and Action (ICA), for structuring business knowledge in LLM-based QA and customer support workflows. Initial experiments in production show promising results. We also discovered relevant research in knowledge retrieval, LLM evaluation, and hallucination detection that will inspire future projects.

### Optimization, causal inference, and measurement science

### MIT CODE (Conference on Digital Experimentation)

[*MIT CODE*](https://ide.mit.edu/events/2025-conference-on-digital-experimentation-mit-codemit/) *is one of the premier venues for researchers and practitioners to discuss topics in online digital experimentation, causal inference, and data-driven product innovation. The conference supports our commitment to data-driven decision-making and using experimentation to understand the long-term impacts on guests, hosts, and marketplace health.*

**Our participation**

In 2025, we had another strong showing at CODE, with a cohort of 6 data scientists and 3 academic collaborators. We gave talks in two sessions and presented a poster, which led to meaningful discussions with peer companies and interest in collaborating with academic research groups.

**Research highlights**

1. [Beyond the Experiment Window: Prospective Impacts Under Long-Term Ranking Dynamics](https://airbnb.tech/wp-content/uploads/sites/19/2026/01/BSTAR_abstract_5pages.pdf): Product teams frequently leverage A/B tests to assess different rankers. While these experiments are typically conducted over shorter periods, we also recognize the value of understanding longer-term dynamics (such as seasonality and user evolution) to further support sustained business objectives, like marketplace health. To solve this problem, we developed a causal framework that allows us to estimate the long-term impacts of ranking changes with strategic goals (like marketplace health) using A/B testing data.
2. [Trustworthy Bayesian Inference in Batch-Adaptive Experimentation](https://drive.google.com/file/d/1y_3sYhpydOKd8CmOGNT-2hPyJR2mb-QW/view?usp=sharing): Adaptive experimentation, like multi-arm bandit methods, can improve experiment efficiency by reallocating traffic toward promising treatments. Continued advancements in these approaches are expanding our ability to maintain high standards of statistical validity. This paper introduces a practical Bayesian framework for inference in batch-adaptive experiments, specifically tailored to the operational realities of online platforms.

**Link to all papers**

* [Beyond the Experiment Window: Prospective Impacts Under Long-Term Ranking Dynamics](https://drive.google.com/file/d/13W6ihExC-qyFZmlciO2d7kM88LnNIoUp/view) (Lo-Hua Yuan)
* [Trustworthy Bayesian Inference in Batch-Adaptive Experimentation](https://drive.google.com/file/d/1y_3sYhpydOKd8CmOGNT-2hPyJR2mb-QW/view?usp=sharing) (Yicheng Li)
* [Experimental Design for Product Launches with Collaborative User Networks](https://drive.google.com/file/d/1TixwWkoHn_H4Lyrvml5h3XrdWxlGVC29/view?usp=sharing) (Monu Kala)

### INFORMS (Institute for Operations Research and the Management Sciences)

[*INFORMS*](https://meetings.informs.org/wordpress/annual/) *brings together academics and industry professionals to discuss and share research across data science, machine learning, economics, behavioral science, and analytics.*

**Our participation**

In 2025, our data science team was invited to INFORMS to present two talks in a session about bridging the gap between statistical methods and industry applications.

**Research highlights**

1. [Beyond Multi-Arm Bandits: Tackling Challenges in Adaptive Experiments at Airbnb](https://docs.google.com/presentation/d/1RkcTBkhqg1xNeQ-boeXVvgZK9JIUg37Zo590Eo67zgc/edit?slide=id.gc91b80c485_0_550#slide=id.gc91b80c485_0_550). In this talk, we walked through the metrics and infrastructure challenges when using classic bandit algorithms, which make it difficult to operationalize adaptive experiments. We propose a hybrid approach that incorporates bandit algorithms into A/B experiments to enable adaptive testing. We also discussed how we onboard and validate adaptive experiments across individual product domains at Airbnb.

**Link to all papers**

* [Beyond the Experiment Window: Prospective Impacts Under Long-Term Ranking Dynamics](https://drive.google.com/file/d/13W6ihExC-qyFZmlciO2d7kM88LnNIoUp/view) (Lo-Hua Yuan)
* [Beyond Multi-Arm Bandits: Tackling Challenges in Adaptive Experiments at Airbnb](https://docs.google.com/presentation/d/1RkcTBkhqg1xNeQ-boeXVvgZK9JIUg37Zo590Eo67zgc/edit?slide=id.gc91b80c485_0_550#slide=id.gc91b80c485_0_550) (Yicheng Li)

### LION (Learning and Intelligent Optimization)

*The* [*LION*](https://lion19.org/) *conference is a premier gathering of researchers exploring the intersection of machine learning, artificial intelligence, and mathematical optimization.*

**Our participation**

While Airbnb has attended LION in the past, 2025 was the first time we presented at the conference. Nathan Brixius presented “[Optimal Matched Block Design For Multi-Arm](https://airbnb.tech/wp-content/uploads/sites/19/2025/10/brixius_block.pdf)

[Experiments](https://airbnb.tech/wp-content/uploads/sites/19/2025/10/brixius_block.pdf),” which introduces a new optimization formula using mixed-integer programming (MIP) to group subjects in multi-armed experiments, leading to more balanced groups and, in turn, more accurate experimental results. We also connected with leading experts in metaheuristics and AI fairness to help shape our future roadmap and sponsored the awards for the best papers presented at the conference.

### Data systems

### VLDB (Very Large Data Bases)

*The* [*VLDB*](https://vldb.org/2025/) *Conference is one of the top 2 flagship conferences in data management and large-scale data systems, with over 1,500 researchers and practitioners attending.*

**Our participation**

“In 2025, we published our first paper at VLDB: ‘[SQL:Trek Automated Index Design at Airbnb](https://www.vldb.org/pvldb/vol18/p5210-lightstone.pdf)’ by Sam Lightstone and Ping Wang. The paper presents a novel approach for automated index design (code-named SQL:Trek). It uses query compiler cost models to identify effective indexes across many relational databases, including most MySQL and PostgreSQL derivatives. Additionally, the Airbnb team attended sessions on system efficiency, graph computing, and AI databases, and had the opportunity to meet other researchers.

### Conclusion

Conferences remain a big part of our research program at Airbnb, helping us validate and refine our ideas through community feedback and providing a forum to share real-world insights that advance the field. In 2025, we doubled down on this vision by publishing papers for the first time at conferences in domains such as NLP, optimization, causal inference, and data systems, reflecting our ongoing commitment to using these technologies to create the best possible travel experiences.

As we look to 2026, we’re eager to expand our presence at these conferences and discover new ways to use AI, machine learning, and data science to build a best-in-class travel and living platform. If you’re interested in doing this type of work with us, consider joining us. [Apply for one of our open positions](https://careers.airbnb.com/).

![](https://medium.com/_/stat?event=post.clientViewed&referrerSource=full_rss&postId=7d79f57d3b52)

---

[Academic Publications & Airbnb Tech: 2025 Year in Review](https://medium.com/airbnb-engineering/academic-publications-airbnb-tech-2025-year-in-review-7d79f57d3b52) was originally published in [The Airbnb Tech Blog](https://medium.com/airbnb-engineering) on Medium, where people are continuing the conversation by highlighting and responding to this story.
