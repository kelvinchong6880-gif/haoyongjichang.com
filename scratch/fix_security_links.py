import os
import re

base_dir = r"c:\Users\USER\Desktop\haoyongjichang.com\src\pages"

files_to_fix_normal = [
    os.path.join(base_dir, r"contact\index.astro"),
    os.path.join(base_dir, r"privacy\index.astro"),
    os.path.join(base_dir, r"guide\scenario-telegram\index.astro")
]

file_to_fix_sponsored = os.path.join(base_dir, r"top-10-airports\index.astro")

def add_rel_to_tag(match, new_rel):
    tag = match.group(0)
    if 'rel=' in tag:
        # Avoid replacing if it already has rel (unless we want to overwrite)
        return tag
    # Insert rel after target="_blank"
    return tag.replace('target="_blank"', f'target="_blank" rel="{new_rel}"')

# Fix normal files
for filepath in files_to_fix_normal:
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Regex to find <a ... target="_blank" ...> without rel=
        new_content = re.sub(r'<a\s+[^>]*target="_blank"[^>]*>', lambda m: add_rel_to_tag(m, "noopener noreferrer"), content)
        
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Fixed security links in {os.path.basename(os.path.dirname(filepath))}")

# Fix top 10 airports (sponsored)
if os.path.exists(file_to_fix_sponsored):
    with open(file_to_fix_sponsored, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = re.sub(r'<a\s+[^>]*target="_blank"[^>]*>', lambda m: add_rel_to_tag(m, "nofollow sponsored noopener noreferrer"), content)
    
    if new_content != content:
        with open(file_to_fix_sponsored, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("Fixed sponsored security links in top-10-airports")

