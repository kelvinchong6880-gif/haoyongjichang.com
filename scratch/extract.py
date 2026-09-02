import re

filepath = r"c:\Users\USER\Desktop\haoyongjichang.com\src\pages\index.astro"
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# We need to find each brand's URL. The structure is roughly:
# <div class="brand-card-premium">
#   <div class="bcp-header">
#     <a href="/review/weifeng/" ...>
#   ...
#   <a href="https://..." class="button bcp-btn">前往官网注册

# Let's split by brand-card-premium
cards = content.split('class="brand-card-premium"')
for card in cards[1:]:
    # Find the review link to identify the brand slug
    match_slug = re.search(r'href="/review/([^/]+)/"', card)
    if not match_slug:
        continue
    slug = match_slug.group(1)
    
    # Find the official URL
    match_url = re.search(r'href="(https?://[^"]+)"[^>]*>[\s\n]*前往官网注册', card)
    url = match_url.group(1) if match_url else ""
    
    # Find the promo code if exists
    match_code = re.search(r'<code>([^<]+)</code>', card)
    code = match_code.group(1) if match_code else ""
    
    print(f"{slug}|{url}|{code}")
