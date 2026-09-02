import os
import re

src_dir = r"c:\Users\USER\Desktop\haoyongjichang.com\src"
public_dir = r"c:\Users\USER\Desktop\haoyongjichang.com\public"
pages_dir = os.path.join(src_dir, "pages")

def check_internal_link(href):
    # Remove hash
    if '#' in href:
        href = href.split('#')[0]
        
    if not href or href == '/':
        return True
        
    if href.startswith('mailto:') or href.startswith('tel:'):
        return True
        
    # Is it a file in public?
    public_path = os.path.join(public_dir, href.lstrip('/'))
    if os.path.exists(public_path) and os.path.isfile(public_path):
        return True
        
    # Is it a route in pages?
    # e.g. /guide/ -> pages/guide/index.astro
    # e.g. /about -> pages/about.astro or pages/about/index.astro
    route_path = href.strip('/')
    
    # Check 1: direct .astro file
    direct_astro = os.path.join(pages_dir, route_path + ".astro")
    if os.path.exists(direct_astro):
        return True
        
    # Check 2: index.astro in directory
    index_astro = os.path.join(pages_dir, route_path, "index.astro")
    if os.path.exists(index_astro):
        return True
        
    # It might be dynamic route like /review/[slug]/index.astro
    # For now, let's just do a basic dynamic route check for review/[slug]
    if route_path.startswith("review/"):
        return True # we know review pages are generated
        
    return False

all_links = set()
dead_links = []

for root, dirs, files in os.walk(src_dir):
    for file in files:
        if file.endswith((".astro", ".md", ".mdx")):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                
            links = re.findall(r'href="([^"]+)"', content)
            for link in links:
                if link.startswith('http://') or link.startswith('https://'):
                    continue # skip external for now to avoid false positives with anti-bots
                    
                if link.startswith('/'):
                    if not check_internal_link(link):
                        dead_links.append((filepath, link))

if dead_links:
    print(f"Found {len(dead_links)} dead internal links:")
    for filepath, link in dead_links:
        # Simplify filepath for display
        rel_path = os.path.relpath(filepath, src_dir)
        print(f"  [{link}] in {rel_path}")
else:
    print("No dead internal links found!")
