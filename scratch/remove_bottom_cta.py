import os
import re

base_dir = r"c:\Users\USER\Desktop\haoyongjichang.com\src\pages\review"

for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith(".astro"):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            # We need to find the exact block and replace it.
            # <div class="rp-action" ... > to the end of it
            # The structure is:
            #       </div>
            # 
            #       <div class="rp-action" style="margin-top: 50px; text-align: center;">
            #         ...
            #       </div>
            # 
            #     </div>
            #   </div>
            # 
            #   <style is:inline>
            
            pattern = r'<div class="rp-action".*?</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*<style is:inline>'
            # Wait, that's too fragile.
            # Let's just find the index of `<div class="rp-action"` and the index of `\n    </div>\n  </div>\n\n  <style is:inline>`
            
            start_idx = content.find('<div class="rp-action"')
            end_pattern = '    </div>\n  </div>\n\n  <style is:inline>'
            end_idx = content.find(end_pattern)
            
            if start_idx != -1 and end_idx != -1:
                new_content = content[:start_idx] + end_pattern + content[end_idx + len(end_pattern):]
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Removed bottom CTA from {filepath}")
