import os

pages_data = {
    "about": {
        "title": "关于好用机场 - 我们的初衷与愿景",
        "description": "了解好用机场的创立初衷。我们致力于为您提供全网最中立、客观的高端专线与高性价比机场评测，帮您避开跑路陷阱。",
        "heading": "关于好用机场",
        "content": """
        <p class="lead-text">欢迎来到 <strong>好用机场</strong>，这是一个致力于为广大网民提供中立、专业、客观的科学上网（翻墙）服务评测平台。</p>
        
        <h3>我们的初衷</h3>
        <p>在当前的网络环境下，寻找一款速度快、不卡顿且不会跑路的代理服务变得越来越困难。市场上充斥着大量虚假宣传的“低价年付机场”，许多新手朋友在购买后经常遭遇“刚买就跑路”或“晚高峰卡成幻灯片”的惨痛经历。</p>
        <p>为了打破这种信息差，我们成立了“好用机场”。我们不仅自费购买市面上的主流机场进行长期监控，还深入研究了它们背后的线路架构（如 IPLC/IEPL 专线、BGP 中转等），旨在为您筛选出真正靠谱的优质服务。</p>
        
        <h3>我们的核心价值观</h3>
        <ul>
          <li><strong>客观中立：</strong> 我们所有的测速图与流媒体解锁截图均为真实环境下的实际测试结果，绝不为劣质机场粉饰太平。</li>
          <li><strong>拒绝跑路：</strong> 我们将“稳定性”与“跑路风险”作为第一考核指标，坚决抵制任何具有明显“庞氏圈钱”特征的机场。</li>
          <li><strong>全场景覆盖：</strong> 无论您是重度 Netflix/Disney+ 追剧党，还是对延迟极度敏感的外服游戏玩家，亦或是需要稳定原生 IP 解锁 ChatGPT/Claude 的 AI 开发者，我们都能为您提供最精准的推荐。</li>
        </ul>
        
        <p>我们希望通过我们的努力，能让您花最稳的钱，上最快的网，把精力放在更有价值的事情上，而不是每天在寻找节点和排错中内耗。</p>
        """
    },
    "contact": {
        "title": "联系我们 - 合作与反馈",
        "description": "如果您有任何关于机场评测的建议、商务合作、广告投放或文章纠错，欢迎随时通过 Telegram 或邮件联系我们。",
        "heading": "联系我们",
        "content": """
        <p class="lead-text">无论是商务合作、机场推荐、网站纠错还是仅仅想和我们交流心得，我们都非常欢迎您的声音！</p>
        
        <div class="contact-card-grid">
          <div class="contact-card">
            <div class="cc-icon" style="background: #eef2ff; color: #4f46e5;">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="width:28px;height:28px;"><line x1="22" y1="2" x2="11" y2="13"></line><polygon points="22 2 15 22 11 13 2 9 22 2"></polygon></svg>
            </div>
            <h3>Telegram (首选)</h3>
            <p>对于时效性要求较高的咨询或商务合作，我们建议您通过 Telegram 与我们取得联系，我们通常会在几个小时内回复。</p>
            <a href="https://t.me/kelvin8chong" target="_blank" class="cc-btn">@kelvin8chong</a>
          </div>
          
          <div class="contact-card">
            <div class="cc-icon" style="background: #f0fdf4; color: #16a34a;">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="width:28px;height:28px;"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg>
            </div>
            <h3>电子邮件</h3>
            <p>如果您需要发送详细的测试报告、附件，或者不方便使用即时通讯软件，可以通过发送电子邮件联系我们。</p>
            <a href="mailto:kelvinchong6880@gmail.com" class="cc-btn">kelvinchong6880@gmail.com</a>
          </div>
        </div>
        
        <h3>常见合作形式</h3>
        <ul>
          <li><strong>机场上榜与评测：</strong> 如果您是机场主，且对自己的专线质量有绝对的信心，欢迎提供测试账号，我们将进行为期一周的综合考核。</li>
          <li><strong>广告位投放：</strong> 我们在首页、评测页及右侧侧边栏提供高曝光的广告位展示。</li>
          <li><strong>文章纠错：</strong> 如果您发现我们的评测数据过期，或者某个机场已经出现跑路前兆，请务必联系我们进行下架处理。</li>
        </ul>
        """
    },
    "privacy": {
        "title": "隐私政策 - 好用机场",
        "description": "好用机场的隐私政策说明。了解我们如何处理流量统计数据以及第三方链接的隐私说明。",
        "heading": "隐私政策",
        "content": """
        <p class="update-time">最后更新日期：2026年9月2日</p>
        
        <p>好用机场（以下简称“本站”）非常重视用户的隐私保护。本《隐私政策》旨在向您说明本站在您访问时如何收集、使用和保护您的信息。</p>
        
        <h3>1. 信息的收集</h3>
        <p><strong>无需注册访问：</strong> 浏览本站的评测文章和教程不需要您注册任何账号或提供真实姓名、身份证、手机号等敏感个人隐私信息。</p>
        <p><strong>流量统计分析：</strong> 为了优化网站的用户体验和页面加载速度，我们可能会使用第三方统计工具（如 Google Analytics 等）。这些工具可能会收集您的 IP 地址、浏览器类型、访问时间、引用页面等非身份识别数据。</p>
        
        <h3>2. Cookie 的使用</h3>
        <p>本站可能会使用 Cookie 来提升您的浏览体验，例如记住您的弹窗关闭状态或暗黑模式偏好。您可以通过浏览器的设置随时禁用 Cookie，这不会影响您阅读本站的核心评测内容。</p>
        
        <h3>3. 第三方链接说明</h3>
        <p>本站的评测文章中包含了大量指向第三方代理服务商（机场）的链接。当您点击这些链接离开本站后，您的隐私将受该第三方网站的隐私政策约束。<strong>本站无法控制第三方网站的隐私保护措施，也无法为其安全漏洞或信息泄露负责。</strong></p>
        
        <h3>4. 联系我们</h3>
        <p>如果您对本隐私政策有任何疑问，请通过以下方式联系我们：</p>
        <ul>
          <li>Telegram: <a href="https://t.me/kelvin8chong" target="_blank">@kelvin8chong</a></li>
          <li>Email: <a href="mailto:kelvinchong6880@gmail.com">kelvinchong6880@gmail.com</a></li>
        </ul>
        """
    },
    "terms": {
        "title": "使用条款 - 好用机场",
        "description": "请在使用好用机场提供的评测资源前仔细阅读本使用条款。本站提供的内容仅用于技术交流与网络优化参考。",
        "heading": "使用条款",
        "content": """
        <p class="update-time">最后更新日期：2026年9月2日</p>
        
        <p>欢迎访问好用机场。在您使用本站提供的评测、教程与推荐服务之前，请务必仔细阅读以下条款。访问和使用本站即表示您同意接受本条款的约束。</p>
        
        <h3>1. 网站定位与用途</h3>
        <p>好用机场是一个中立的第三方技术评测博客。本站提供的内容（包括代理协议介绍、专线测速、流媒体解锁测试等）仅供技术交流、学术研究以及改善国际网络访问体验之用。</p>
        
        <h3>2. 法律合规</h3>
        <p>用户在参考本站教程或购买本站推荐的第三方服务时，<strong>必须严格遵守所在国家或地区的法律法规</strong>。禁止使用相关服务从事任何违法犯罪、危害国家安全或侵犯他人合法权益的活动。对于用户的不当行为，本站概不负责。</p>
        
        <h3>3. 版权声明</h3>
        <p>本站所发布的原创评测文章、图表和设计元素，其版权均归好用机场所有。未经书面授权，严禁任何形式的商业转载、洗稿或爬虫抓取。对于恶意抄袭者，我们将保留追究其法律责任的权利。</p>
        
        <h3>4. 条款修改</h3>
        <p>本站保留随时修改本使用条款的权利，修改后的条款一旦公布即刻生效。建议您定期查看本页面以了解最新规定。</p>
        """
    },
    "disclaimer": {
        "title": "免责声明 - 好用机场",
        "description": "好用机场免责声明。本站不对第三方机场的稳定性、跑路风险及服务中断承担连带责任，请理性消费。",
        "heading": "免责声明",
        "content": """
        <p class="update-time">最后更新日期：2026年9月2日</p>
        
        <p>在您根据好用机场的推荐进行消费决策前，请务必阅读并理解以下免责声明，以保障您的个人权益。</p>
        
        <h3>1. 信息时效性与准确性</h3>
        <p>本站的测速数据、流媒体解锁情况以及套餐价格均基于我们撰写评测时的真实状态。由于代理行业的特殊性，机场的线路架构、服务器 IP 库和价格可能会随时发生变动。本站不对因信息滞后或机场单方面更改规则而造成的用户体验落差承担任何责任。</p>
        
        <h3>2. 第三方服务中断与跑路风险</h3>
        <p><strong>代理（机场）行业属于高风险行业，没有任何一家服务商可以保证 100% 绝对安全且永不跑路。</strong></p>
        <p>本站仅作为信息展示平台，不对任何第三方机场的运营状况提供担保。若您购买的服务商遭遇 DDOS 攻击、不可抗力断网或老板卷款跑路（拔线），本站不提供退款、赔偿或任何形式的连带法律责任。</p>
        
        <h3>3. 消费建议 (防坑指南)</h3>
        <p>为了最大化降低您的风险，我们强烈建议所有用户：</p>
        <ul>
          <li><strong>拒绝年付：</strong> 除非是已经稳定运营多年的顶级老牌专线，否则对于新机场或便宜机场，请务必优先选择<strong>按月付费</strong>或最多<strong>按季付费</strong>。</li>
          <li><strong>备用原则：</strong> 强烈建议准备两个以上的机场（例如一家包月主用，一家按量付费备用），以防单一机场出现故障导致您与外部网络彻底失联。</li>
        </ul>
        
        <p>最终的购买决定由您自行做出，并由您自行承担相应的交易风险。</p>
        """
    }
}

template = """---
import BaseLayout from '../../layouts/BaseLayout.astro';
---

<BaseLayout 
  title="{title}" 
  description="{description}"
>
  <div class="legal-page-shell">
    <div class="lp-header">
      <h1>{heading}</h1>
    </div>
    
    <article class="lp-content">
{content}
    </article>
  </div>

  <style is:inline>
    .legal-page-shell {{
      max-width: 800px;
      margin: 0 auto;
      padding: 60px 20px 100px;
    }}
    .lp-header {{
      text-align: center;
      margin-bottom: 50px;
      padding-bottom: 30px;
      border-bottom: 2px solid #f1f5f9;
    }}
    .lp-header h1 {{
      font-size: 2.5rem;
      color: #0f172a;
      font-weight: 800;
      margin: 0;
    }}
    
    .lp-content {{
      font-size: 1.1rem;
      color: #334155;
      line-height: 1.8;
    }}
    .lp-content h3 {{
      font-size: 1.4rem;
      color: #0f172a;
      margin-top: 40px;
      margin-bottom: 16px;
      font-weight: 700;
      display: flex;
      align-items: center;
      gap: 10px;
    }}
    .lp-content h3::before {{
      content: "";
      display: inline-block;
      width: 4px;
      height: 20px;
      background: #3b82f6;
      border-radius: 2px;
    }}
    .lp-content p {{
      margin-bottom: 20px;
    }}
    .lp-content ul {{
      margin-bottom: 24px;
      padding-left: 24px;
    }}
    .lp-content li {{
      margin-bottom: 12px;
      color: #475569;
    }}
    .lp-content strong {{
      color: #0f172a;
    }}
    .lp-content a {{
      color: #3b82f6;
      text-decoration: underline;
      text-underline-offset: 4px;
    }}
    .lp-content a:hover {{
      color: #2563eb;
    }}
    
    .lead-text {{
      font-size: 1.25rem !important;
      color: #475569 !important;
      line-height: 1.8 !important;
      margin-bottom: 40px !important;
    }}
    
    .update-time {{
      font-size: 0.95rem !important;
      color: #94a3b8 !important;
      font-style: italic;
      text-align: center;
      margin-top: -10px;
      margin-bottom: 40px !important;
    }}
    
    /* 联系我们卡片样式 */
    .contact-card-grid {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 24px;
      margin: 40px 0;
    }}
    .contact-card {{
      background: #ffffff;
      border: 1px solid #e2e8f0;
      border-radius: 16px;
      padding: 30px;
      text-align: center;
      box-shadow: 0 4px 6px rgba(0,0,0,0.02);
      transition: transform 0.2s, box-shadow 0.2s;
    }}
    .contact-card:hover {{
      transform: translateY(-4px);
      box-shadow: 0 10px 25px rgba(0,0,0,0.05);
    }}
    .cc-icon {{
      width: 60px;
      height: 60px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      margin: 0 auto 20px;
    }}
    .contact-card h3 {{
      font-size: 1.25rem;
      margin: 0 0 12px 0;
      color: #0f172a;
      justify-content: center;
    }}
    .contact-card h3::before {{
      display: none;
    }}
    .contact-card p {{
      font-size: 1rem;
      color: #64748b;
      margin-bottom: 24px;
      min-height: 70px;
    }}
    .cc-btn {{
      display: inline-block;
      background: #f8fafc;
      color: #0f172a;
      font-weight: 600;
      padding: 12px 24px;
      border-radius: 30px;
      border: 1px solid #cbd5e1;
      text-decoration: none !important;
      transition: all 0.2s;
    }}
    .cc-btn:hover {{
      background: #3b82f6;
      color: #ffffff;
      border-color: #3b82f6;
    }}
    
    @media (max-width: 600px) {{
      .lp-header h1 {{
        font-size: 2rem;
      }}
      .contact-card-grid {{
        grid-template-columns: 1fr;
      }}
    }}
  </style>
</BaseLayout>
"""

base_dir = r"c:\Users\USER\Desktop\haoyongjichang.com\src\pages"

for slug, data in pages_data.items():
    page_dir = os.path.join(base_dir, slug)
    if not os.path.exists(page_dir):
        os.makedirs(page_dir)
        
    filepath = os.path.join(page_dir, "index.astro")
    
    content = template.format(
        title=data['title'],
        description=data['description'],
        heading=data['heading'],
        content=data['content']
    )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Created {filepath}")
