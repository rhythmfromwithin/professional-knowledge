---
title: "V-Nutri: Dish-Level Nutrition Estimation from Egocentric Cooking Videos"
source: "cs.CV - Computer Vision"
link: https://arxiv.org/abs/2604.11913
priority: medium
status: unread
interest: medium
next_step: skim
---
# V-Nutri: Dish-Level Nutrition Estimation from Egocentric Cooking Videos
> 原文: [https://arxiv.org/abs/2604.11913](https://arxiv.org/abs/2604.11913)

arXiv:2604.11913v1 Announce Type: new
Abstract: Nutrition estimation of meals from visual data is an important problem for dietary monitoring and computational health, but existing approaches largely rely on single images of the finally completed dish. This setting is fundamentally limited because many nutritionally relevant ingredients and transformations, such as oils, sauces, and mixed components, become visually ambiguous after cooking, making accurate calorie and macronutrient estimation difficult. In this paper, we investigate whether the cooking process information from egocentric cooking videos can contribute to dish-level nutrition estimation. First, we further manually annotated the HD-EPIC dataset and established the first benchmark for video-based nutrition estimation. Most importantly, we propose V-Nutri, a staged framework that combines Nutrition5K-pretrained visual backbones with a lightweight fusion module that aggregates features from the final dish frame and cooking process keyframes extracted from the egocentric videos. V-Nutri also includes a cooking keyframes selection module, a VideoMamba-based event-detection model that targets ingredient-addition moments. Experiments on the HD-EPIC dataset show that process cues can provide complementary nutritional evidence, improving nutrition estimation under controlled conditions. Our results further indicate that the benefit of process keyframes depends strongly on backbone representation capacity and event detection quality. Our code and annotated dataset is available at https://github.com/K624-YCK/V-Nutri.
