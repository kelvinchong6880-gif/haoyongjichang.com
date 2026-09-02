import os
import re

brand_info = {
    "weifeng": {"name": "微风", "url": "https://edp01.breezenetaff.com/#/?code=hM8APccJ", "code": "hM8APccJ"},
    "feimao": {"name": "飞猫云", "url": "https://flycat1.flycatvipaff.cc/#/?code=w5lO9fqB", "code": "w5lO9fqB"},
    "firefly": {"name": "Firefly", "url": "https://vip02.fireflyaff.com/#/?code=8nDg6OEY", "code": "8nDg6OEY"},
    "wuyou": {"name": "无忧链接", "url": "https://wep01.worryfreeaff.com/#/?code=s1kH64A8", "code": "s1kH64A8"},
    "kuajie": {"name": "跨界云", "url": "https://vip02.kuajieaff.com/#/?code=hh3QezsW", "code": "hh3QezsW"},
    "lingmao": {"name": "灵猫", "url": "https://edp01.civetaff.com/#/?code=CYg7QSJo", "code": "CYg7QSJo"},
    "shanyue": {"name": "闪跃", "url": "https://wep01.flashleapaff.com/#/?code=cs0ekCMG", "code": "cs0ekCMG"},
    "flybit": {"name": "Flybit", "url": "https://1.flybit.network/#/register?code=Aga7bd1s", "code": "Aga7bd1s"},
    "xsus": {"name": "xsus", "url": "https://xsus.cloud/register?code=QQh1M1i9", "code": "QQh1M1i9"},
    "xxyun": {"name": "小新云", "url": "https://www.xx-yun.com/?code=pi9fB906", "code": "pi9fB906"}
}

action_template = """      <div class="rp-action" style="margin-top: 50px; text-align: center;">
        <div class="rp-promo" style="display: inline-block; background: #fffbeb; border: 1px solid #fde68a; padding: 12px 24px; border-radius: 8px; margin-bottom: 24px; color: #b45309; font-size: 1.1rem; font-weight: 600;">
          🎁 本站专属优惠码：<code style="background: #fef3c7; padding: 4px 8px; border-radius: 4px; color: #ea580c; font-size: 1.2rem; margin-left: 4px; user-select: all;">{code}</code>
        </div>
        <br>
        <a href="{url}" target="_blank" rel="nofollow sponsored noopener noreferrer" class="rp-btn-official" style="display: inline-flex; align-items: center; justify-content: center; gap: 10px; background: linear-gradient(135deg, #3b82f6, #2563eb); color: #fff; font-size: 1.25rem; font-weight: 700; padding: 18px 48px; border-radius: 50px; text-decoration: none; box-shadow: 0 10px 20px rgba(59,130,246,0.3); transition: transform 0.2s, box-shadow 0.2s; max-width: 90%; margin: 0 auto;">
          前往 {name} 官网注册安全通道 
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path><polyline points="15 3 21 3 21 9"></polyline><line x1="10" y1="14" x2="21" y2="3"></line></svg>
        </a>
        <div style="margin-top: 40px;">
          <a href="/" class="rp-btn-back" style="color: #64748b; font-size: 1.05rem; text-decoration: none; border-bottom: 1px solid #cbd5e1; padding-bottom: 2px; transition: color 0.2s;">
            ← 返回机场推荐列表
          </a>
        </div>
      </div>
"""

base_dir = r"c:\Users\USER\Desktop\haoyongjichang.com\src\pages\review"

for slug, info in brand_info.items():
    filepath = os.path.join(base_dir, slug, "index.astro")
    if not os.path.exists(filepath):
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # We want to replace everything from <div class="rp-action"> to </div> </div> </div>
    # Actually, we can just find <div class="rp-action"> and replace it until </div> </div> </div>
    # Or simply use regex
    pattern = r'<div class="rp-action">.*?</div>\s*</div>\s*</div>'
    replacement = action_template.format(
        name=info['name'],
        url=info['url'],
        code=info['code']
    ) + "\n    </div>\n  </div>"
    
    new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    
    # Let's inject hover state for the new button if needed
    if ".rp-btn-official:hover" not in new_content:
        new_content = new_content.replace("</style>", """    .rp-btn-official:hover {
      transform: translateY(-2px);
      box-shadow: 0 15px 25px rgba(59,130,246,0.4) !important;
    }
    .rp-btn-back:hover {
      color: #3b82f6 !important;
      border-color: #3b82f6 !important;
    }
  </style>""")
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"Updated {filepath} with CTA")
