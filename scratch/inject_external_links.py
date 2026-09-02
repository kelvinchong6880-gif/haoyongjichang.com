import os
import re

base_dir = r"c:\Users\USER\Desktop\haoyongjichang.com\src\pages\guide"

# Define the external links to inject for specific articles
# Format: { "folder_name": [ ("keyword", '<a href="URL" target="_blank" rel="noopener noreferrer">keyword</a>', count) ] }
# We will only replace the first occurrence to avoid over-linking.

outbound_links_map = {
    "clash-verge-rev": [
        ("Clash Verge Rev", '<a href="https://github.com/clash-verge-rev/clash-verge-rev" target="_blank" rel="noopener noreferrer">Clash Verge Rev</a>', 1)
    ],
    "clash-for-android": [
        ("Clash for Android", '<a href="https://github.com/Kr328/ClashForAndroid" target="_blank" rel="noopener noreferrer">Clash for Android</a>', 1)
    ],
    "mac": [
        ("ClashX Pro", '<a href="https://github.com/yichengchen/clashX" target="_blank" rel="noopener noreferrer">ClashX Pro</a>', 1)
    ],
    "sing-box": [
        ("Sing-box", '<a href="https://sing-box.sagernet.org/" target="_blank" rel="noopener noreferrer">Sing-box</a>', 1)
    ],
    "scenario-ai-unblock": [
        ("ChatGPT", '<a href="https://chatgpt.com/" target="_blank" rel="nofollow noopener noreferrer">ChatGPT</a>', 1),
        ("Anthropic", '<a href="https://www.anthropic.com/" target="_blank" rel="nofollow noopener noreferrer">Anthropic</a>', 1)
    ],
    "scenario-streaming-unblock": [
        ("Netflix", '<a href="https://www.netflix.com/" target="_blank" rel="nofollow noopener noreferrer">Netflix</a>', 1),
        ("Disney+", '<a href="https://www.disneyplus.com/" target="_blank" rel="nofollow noopener noreferrer">Disney+</a>', 1)
    ],
    "scenario-telegram": [
        ("Telegram", '<a href="https://telegram.org/" target="_blank" rel="nofollow noopener noreferrer">Telegram</a>', 1)
    ],
    "knowledge-protocols": [
        ("V2Ray", '<a href="https://www.v2fly.org/" target="_blank" rel="nofollow noopener noreferrer">V2Ray</a>', 1),
        ("Hysteria 2", '<a href="https://v2.hysteria.network/" target="_blank" rel="nofollow noopener noreferrer">Hysteria 2</a>', 1)
    ],
    "knowledge-subconverter": [
        ("Subconverter", '<a href="https://github.com/tindy2013/subconverter" target="_blank" rel="noopener noreferrer">Subconverter</a>', 1)
    ],
    "knowledge-network-lines": [
        ("Cloudflare", '<a href="https://www.cloudflare.com/" target="_blank" rel="nofollow noopener noreferrer">Cloudflare</a>', 1)
    ]
}

for root, dirs, files in os.walk(base_dir):
    for dir_name in dirs:
        if dir_name not in outbound_links_map:
            continue
            
        index_path = os.path.join(root, dir_name, "index.astro")
        if not os.path.exists(index_path):
            continue
            
        with open(index_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # We only want to replace within the article content to avoid messing up metadata or TOC
        start_marker = '<div class="article-content">'
        end_marker = '<h2 id="related-reading">'
        
        start_idx = content.find(start_marker)
        end_idx = content.find(end_marker) if end_marker in content else content.find('</article>')
        
        if start_idx == -1 or end_idx == -1:
            print(f"Skipping {dir_name}: Could not find content boundaries")
            continue
            
        before = content[:start_idx]
        article_body = content[start_idx:end_idx]
        after = content[end_idx:]
        
        replacements_made = 0
        for keyword, link_html, count in outbound_links_map[dir_name]:
            # Regex to replace word not already inside an anchor tag
            # This complex regex ensures we don't replace "keyword" if it's already part of <a href="...">keyword</a>
            pattern = rf'(?<!<a href="[^"]*">)(?<!<a href="[^"]*" target="_blank" rel="nofollow noopener noreferrer">)(?<!<a href="[^"]*" target="_blank" rel="noopener noreferrer">)\b({re.escape(keyword)})\b(?![^<]*</a>)'
            
            # Since some keywords might not have \b boundaries nicely (like Disney+), we use a simpler approach
            # Just find the first occurrence that is NOT inside an existing <a> tag.
            # A simple trick is to split by <a> tags, replace in the text parts, and rejoin.
            
            parts = re.split(r'(<a[^>]*>.*?</a>)', article_body)
            for i in range(0, len(parts), 2): # Even indices are outside <a> tags
                if keyword in parts[i]:
                    parts[i] = parts[i].replace(keyword, link_html, count)
                    replacements_made += 1
                    break # Only replace the very first occurrence
                    
            article_body = "".join(parts)
            
        if replacements_made > 0:
            new_content = before + article_body + after
            with open(index_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Injected {replacements_made} outbound link(s) into {dir_name}")
