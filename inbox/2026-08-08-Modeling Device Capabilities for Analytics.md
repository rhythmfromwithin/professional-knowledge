---
link: https://netflixtechblog.com/modeling-device-capabilities-for-analytics-e7607acebde8?source=rss
slack_ts: '1786328463.813619'
source: Netflix Tech Blog
title: Modeling Device Capabilities for Analytics
----2615bd06b42e---4
priority: high
status: unread
interest: medium
next_step: skim
---
# Modeling Device Capabilities for Analytics
> 原文: [https://netflixtechblog.com/modeling-device-capabilities-for-analytics-e7607acebde8?source=rss----2615bd06b42e---4](https://netflixtechblog.com/modeling-device-capabilities-for-analytics-e7607acebde8?source=rss----2615bd06b42e---4)

by [Aarti Laddha](https://www.linkedin.com/in/aarti-laddha-70666557/), [Richard Diaz-Cool](https://www.linkedin.com/in/richardjcool/), [Rishika Idnani](https://www.linkedin.com/in/rishikaidnani/), [Venkatesh Selveraj](https://www.linkedin.com/in/venkatesh-selvaraj-88824137/)

Netflix supports a vast and evolving set of features and content types, ranging from 4K streaming and immersive audio to live streaming and cloud gaming, across a diverse ecosystem of devices. However, not all devices are created equal. Hardware limitations such as available RAM, CPU cores, display capabilities, or platform support mean that some features cannot be supported on certain device models. To ensure the best possible user experience, we rely on a deep understanding of device capabilities. We have invested in building a comprehensive device capability data model and integrating feature flags from internal systems, paving the way for smarter, more granular feature management across our global device landscape. This approach helps us identify bottlenecks in feature penetration and accelerates the pace of innovation.

We have designed our data storage and modeling strategies to efficiently support analytics at scale. We use a cumulative table to process information about the device’s capabilities. This table is structured to efficiently capture the latest state of each device and its associated capabilities (like Screen resolutions, Video Profiles Supported, Surround Sound, RAM size etc) making it ideal for analytics and reporting use cases.

```
{  
"Screen Height": ["720"],  
"Screen Width": ["1280"],  
"Video Profiles":   
[  
"playready",  
"hevc",  
],  
}
```

For aggregate analytics, we leverage a histogram table that captures active device counts over the past 28 days, broken down by device model and software version. This table also records the number of devices supporting specific capabilities, enabling detailed distribution analysis. One use case for this histogram data is to analyze the distribution of external display capabilities attached to streaming sticks. For example, the histogram below shows that out of total X number of devices, all supported the HD profile (playready), while only 20% devices supported the UHD profile (hevc).

```
{  
"Video Profiles": {  
      "playready": 100%, # HD profile  
      "hevc": 20% # UHD profile  
}  
}
```

We have built analytical products that leverage these datasets to provide a comprehensive view of feature reach such as 4K Ultra HD, Netflix Spatial Audio, Cloud Gaming and the latest UI. By relying on data-driven insights, we can make informed decisions about which features to enable on specific devices, ensuring both performance and reliability.

![](https://medium.com/_/stat?event=post.clientViewed&referrerSource=full_rss&postId=e7607acebde8)

---

[Modeling Device Capabilities for Analytics](https://netflixtechblog.com/modeling-device-capabilities-for-analytics-e7607acebde8) was originally published in [Netflix TechBlog](https://netflixtechblog.com) on Medium, where people are continuing the conversation by highlighting and responding to this story.
