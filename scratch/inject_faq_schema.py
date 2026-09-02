import os
import re
import json

base_dir = r"c:\Users\USER\Desktop\haoyongjichang.com\src\pages\guide"

for root, dirs, files in os.walk(base_dir):
    for dir_name in dirs:
        index_path = os.path.join(root, dir_name, "index.astro")
        if not os.path.exists(index_path):
            continue
            
        with open(index_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if 'application/ld+json' in content and 'FAQPage' in content:
            continue
            
        # Extract FAQ items
        pattern = r'<h3>Q\d+:\s*(.*?)</h3>\s*<p>答：(.*?)</p>'
        matches = re.findall(pattern, content, re.DOTALL)
        
        if not matches:
            continue
            
        # Build Schema.org JSON
        main_entity = []
        for q, a in matches:
            # clean up HTML tags inside answer if any
            clean_a = re.sub(r'<[^>]+>', '', a).strip()
            clean_q = re.sub(r'<[^>]+>', '', q).strip()
            
            main_entity.append({
                "@type": "Question",
                "name": clean_q,
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": clean_a
                }
            })
            
        faq_schema = {
            "@context": "https://schema.org",
            "@type": "FAQPage",
            "mainEntity": main_entity
        }
        
        json_str = json.dumps(faq_schema, ensure_ascii=False, indent=2)
        script_block = f'\n  <script type="application/ld+json">\n    {json_str}\n  </script>\n</BaseLayout>'
        
        # Inject at the end, replace </BaseLayout>
        if '</BaseLayout>' in content:
            new_content = content.replace('</BaseLayout>', script_block)
            with open(index_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Injected FAQ Schema into {dir_name} ({len(matches)} FAQs)")
        else:
            print(f"Failed to inject into {dir_name}: No closing BaseLayout tag")
