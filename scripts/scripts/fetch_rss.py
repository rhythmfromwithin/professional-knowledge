import feedparser
import yaml
import os
import requests
from datetime import datetime
from markdownify import markdownify as md

def load_config():
    with open('sources/feeds.yaml', 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def fetch():
    config = load_config()
    if not os.path.exists('inbox'): os.makedirs('inbox')
    
    # 整合所有 sources
    sources = []
    if 'engineering_blogs' in config: sources.extend(config['engineering_blogs'])
    if 'vc_blogs' in config: sources.extend(config['vc_blogs'])
    if 'arxiv_feeds' in config: sources.extend(config['arxiv_feeds'])

    for src in sources:
        name = src.get('name', 'Unknown')
        # 处理不同格式的 feeds 结构
        feed_urls = [f['url'] for f in src.get('feeds', [])] if 'feeds' in src else [src.get('url')]
        
        for url in feed_urls:
            if not url: continue
            print(f"Fetching: {name}")
            feed = feedparser.parse(url)
            
            for entry in feed.entries[:3]: # 每次取最新3篇
                date_str = datetime.now().strftime("%Y-%m-%d")
                safe_title = "".join([c for c in entry.title if c.isalnum() or c==' ']).strip()[:50]
                filename = f"inbox/{date_str}-{safe_title}.md"
                
                if os.path.exists(filename): continue

                with open(filename, 'w', encoding='utf-8') as f:
                    content = f"""---
title: "{entry.title}"
source: "{name}"
link: {entry.link}
priority: {src.get('priority', 'medium')}
status: unread
---
# {entry.title}
> 原文: [{entry.link}]({entry.link})

{md(entry.summary) if 'summary' in entry else "请点击原文查看详情"}
"""
                    f.write(content)

if __name__ == "__main__":
    fetch()