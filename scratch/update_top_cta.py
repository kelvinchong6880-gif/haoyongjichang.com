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

base_dir = r"c:\Users\USER\Desktop\haoyongjichang.com\src\pages\review"

for slug, info in brand_info.items():
    filepath = os.path.join(base_dir, slug, "index.astro")
    if not os.path.exists(filepath):
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # The current rp-header looks like this:
    # <div class="rp-header">
    #   <img src="..." alt="..." class="rp-logo" onerror="..." />
    #   <div class="rp-title-wrap">
    #     <h1>...</h1>
    #     <p class="rp-subtitle">2026年最新测速与解锁报告</p>
    #   </div>
    # </div>
    
    # We want to transform it to:
    # <div class="rp-header">
    #   <div class="rp-header-left">
    #     <img src="..." ... />
    #     <div class="rp-title-wrap">...</div>
    #   </div>
    #   <div class="rp-header-right">
    #     <div class="rp-top-promo">专属优惠码：<code>{code}</code></div>
    #     <a href="{url}" ... class="rp-btn-official-top">前往官网注册</a>
    #   </div>
    # </div>
    
    # First, let's extract the inner content of rp-header
    header_pattern = r'<div class="rp-header">\s*(<img.*?>)\s*<div class="rp-title-wrap">(.*?)</div>\s*</div>'
    match = re.search(header_pattern, content, flags=re.DOTALL)
    
    if match:
        img_tag = match.group(1)
        title_wrap_inner = match.group(2)
        
        # Build the new header
        new_header = f"""<div class="rp-header">
      <div class="rp-header-left">
        {img_tag}
        <div class="rp-title-wrap">{title_wrap_inner}</div>
      </div>
      <div class="rp-header-right">"""
      
        if info['code']:
            new_header += f"""
        <div class="rp-top-promo">
          <span>专属优惠码</span>
          <code>{info['code']}</code>
        </div>"""
        
        new_header += f"""
        <a href="{info['url']}" target="_blank" rel="nofollow sponsored noopener noreferrer" class="rp-btn-official-top">
          前往官网注册 <span>↗</span>
        </a>
      </div>
    </div>"""
        
        content = content.replace(match.group(0), new_header)

    # Now add CSS for the new classes
    # We need to update .rp-header to display: flex; justify-content: space-between; align-items: center;
    if ".rp-header-left" not in content:
        css_addition = """
    .rp-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 40px;
      padding-bottom: 30px;
      border-bottom: 1px solid #e2e8f0;
      flex-wrap: wrap;
      gap: 20px;
    }
    .rp-header-left {
      display: flex;
      align-items: center;
      gap: 24px;
    }
    .rp-header-right {
      display: flex;
      flex-direction: column;
      align-items: flex-end;
      gap: 10px;
    }
    .rp-top-promo {
      background: #fffbeb;
      border: 1px solid #fde68a;
      padding: 6px 12px;
      border-radius: 8px;
      font-size: 0.95rem;
      color: #b45309;
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .rp-top-promo code {
      background: #fef3c7;
      padding: 2px 6px;
      border-radius: 4px;
      color: #ea580c;
      font-weight: 700;
      user-select: all;
    }
    .rp-btn-official-top {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: linear-gradient(135deg, #3b82f6, #2563eb);
      color: #fff;
      font-size: 1.1rem;
      font-weight: 700;
      padding: 12px 28px;
      border-radius: 50px;
      text-decoration: none;
      box-shadow: 0 4px 12px rgba(59,130,246,0.25);
      transition: all 0.2s;
    }
    .rp-btn-official-top:hover {
      transform: translateY(-2px);
      box-shadow: 0 8px 20px rgba(59,130,246,0.35);
      color: #fff;
    }
    @media (max-width: 768px) {
      .rp-header {
        flex-direction: column;
        text-align: center;
        justify-content: center;
      }
      .rp-header-left {
        flex-direction: column;
      }
      .rp-header-right {
        align-items: center;
        margin-top: 10px;
      }
    }
"""
        # We need to replace the old .rp-header { ... } block
        # Using regex to replace the old .rp-header block
        old_header_css_pattern = r'\.rp-header\s*\{[^}]*\}'
        content = re.sub(old_header_css_pattern, '', content)
        
        # Insert new css at the beginning of <style is:inline>
        content = content.replace("<style is:inline>", "<style is:inline>\n" + css_addition)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Updated {filepath} with Top CTA")
