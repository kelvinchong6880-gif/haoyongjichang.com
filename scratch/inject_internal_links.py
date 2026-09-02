import os
import re

base_dir = r"c:\Users\USER\Desktop\haoyongjichang.com\src\pages\guide"

client_dirs = ['clash-for-android', 'clash-verge-rev', 'mac', 'shadowrocket', 'sing-box']
trouble_dirs = ['troubleshooting-no-internet', 'troubleshooting-routing-mode', 'troubleshooting-lan-proxy']
scenario_dirs = ['scenario-ai-unblock', 'scenario-streaming-unblock', 'scenario-telegram']
knowledge_dirs = ['knowledge-network-lines', 'knowledge-protocols', 'knowledge-subconverter', 'knowledge-airport-buying-guide']

def get_related_html(folder_name):
    html = """
        <hr style="margin-top: 60px; margin-bottom: 40px; border-top: 2px dashed #e2e8f0;" />
        <h2 id="related-reading">🔗 相关阅读与延伸推荐</h2>
        <div class="related-links-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; margin-top: 24px;">
"""
    if folder_name in client_dirs:
        html += """
          <a href="/guide/troubleshooting-no-internet/" class="rl-card" style="padding: 20px; border: 1px solid #e2e8f0; border-radius: 12px; text-decoration: none; display: block; transition: all 0.2s; background: #f8fafc;">
            <div style="font-size: 1.1rem; color: #0f172a; font-weight: 600; margin-bottom: 8px;">🔧 连上了但没网？</div>
            <div style="font-size: 0.95rem; color: #64748b;">排查 DNS 污染与系统代理冲突，5 分钟恢复网络。</div>
          </a>
          <a href="/guide/scenario-streaming-unblock/" class="rl-card" style="padding: 20px; border: 1px solid #e2e8f0; border-radius: 12px; text-decoration: none; display: block; transition: all 0.2s; background: #f8fafc;">
            <div style="font-size: 1.1rem; color: #0f172a; font-weight: 600; margin-bottom: 8px;">🎬 流媒体解锁指南</div>
            <div style="font-size: 0.95rem; color: #64748b;">配置好客户端后，如何丝滑观看 Netflix 与 Disney+。</div>
          </a>
          <a href="/guide/troubleshooting-routing-mode/" class="rl-card" style="padding: 20px; border: 1px solid #e2e8f0; border-radius: 12px; text-decoration: none; display: block; transition: all 0.2s; background: #f8fafc;">
            <div style="font-size: 1.1rem; color: #0f172a; font-weight: 600; margin-bottom: 8px;">🚦 路由模式怎么选？</div>
            <div style="font-size: 0.95rem; color: #64748b;">详解全局、规则与直连模式的区别，告别流量浪费。</div>
          </a>
"""
    elif folder_name in trouble_dirs:
        html += """
          <a href="/guide/scenario-ai-unblock/" class="rl-card" style="padding: 20px; border: 1px solid #e2e8f0; border-radius: 12px; text-decoration: none; display: block; transition: all 0.2s; background: #f8fafc;">
            <div style="font-size: 1.1rem; color: #0f172a; font-weight: 600; margin-bottom: 8px;">🤖 满血解锁 ChatGPT</div>
            <div style="font-size: 0.95rem; color: #64748b;">网络恢复正常后，体验原生 IP 带来的丝滑 AI 体验。</div>
          </a>
          <a href="/guide/knowledge-network-lines/" class="rl-card" style="padding: 20px; border: 1px solid #e2e8f0; border-radius: 12px; text-decoration: none; display: block; transition: all 0.2s; background: #f8fafc;">
            <div style="font-size: 1.1rem; color: #0f172a; font-weight: 600; margin-bottom: 8px;">⚡ 直连、中转与专线</div>
            <div style="font-size: 0.95rem; color: #64748b;">如果您的节点经常抽风，可能是架构问题，快来补课。</div>
          </a>
          <a href="/recommend/" class="rl-card" style="padding: 20px; border: 1px solid #e2e8f0; border-radius: 12px; text-decoration: none; display: block; transition: all 0.2s; background: #fdf4ff; border-color: #fbcfe8;">
            <div style="font-size: 1.1rem; color: #be185d; font-weight: 600; margin-bottom: 8px;">🏆 2026 高性价比机场</div>
            <div style="font-size: 0.95rem; color: #9d174d;">排错太累？不如换一家自带专线防封锁的顶级机场。</div>
          </a>
"""
    elif folder_name in scenario_dirs:
        html += """
          <a href="/guide/knowledge-airport-buying-guide/" class="rl-card" style="padding: 20px; border: 1px solid #e2e8f0; border-radius: 12px; text-decoration: none; display: block; transition: all 0.2s; background: #f8fafc;">
            <div style="font-size: 1.1rem; color: #0f172a; font-weight: 600; margin-bottom: 8px;">避坑：新手选购指南</div>
            <div style="font-size: 0.95rem; color: #64748b;">解锁流媒体与 AI 需要高质量节点，看看如何避免跑路坑。</div>
          </a>
          <a href="/guide/knowledge-subconverter/" class="rl-card" style="padding: 20px; border: 1px solid #e2e8f0; border-radius: 12px; text-decoration: none; display: block; transition: all 0.2s; background: #f8fafc;">
            <div style="font-size: 1.1rem; color: #0f172a; font-weight: 600; margin-bottom: 8px;">🔒 订阅转换安全防泄露</div>
            <div style="font-size: 0.95rem; color: #64748b;">在使用第三方工具导入节点时，如何保护流量不被盗用。</div>
          </a>
          <a href="/top-10-airports/" class="rl-card" style="padding: 20px; border: 1px solid #e2e8f0; border-radius: 12px; text-decoration: none; display: block; transition: all 0.2s; background: #fffbeb; border-color: #fde68a;">
            <div style="font-size: 1.1rem; color: #b45309; font-weight: 600; margin-bottom: 8px;">👑 顶级专线机场排行</div>
            <div style="font-size: 0.95rem; color: #92400e;">无需自己折腾 IP，官方自带全链路流媒体与 OpenAI 解锁。</div>
          </a>
"""
    elif folder_name in knowledge_dirs:
        html += """
          <a href="/recommend/" class="rl-card" style="padding: 20px; border: 1px solid #e2e8f0; border-radius: 12px; text-decoration: none; display: block; transition: all 0.2s; background: #f0fdf4; border-color: #bbf7d0;">
            <div style="font-size: 1.1rem; color: #15803d; font-weight: 600; margin-bottom: 8px;">🔥 2026 高性价比推荐</div>
            <div style="font-size: 0.95rem; color: #166534;">懂了底层逻辑后，快来看看我们精挑细选的优质梯子吧。</div>
          </a>
          <a href="/cheap-airport/" class="rl-card" style="padding: 20px; border: 1px solid #e2e8f0; border-radius: 12px; text-decoration: none; display: block; transition: all 0.2s; background: #f0f9ff; border-color: #bae6fd;">
            <div style="font-size: 1.1rem; color: #0369a1; font-weight: 600; margin-bottom: 8px;">💰 便宜机场选购大全</div>
            <div style="font-size: 0.95rem; color: #075985;">学生党专属！月付十元以内的高性价比中转/直连机场。</div>
          </a>
          <a href="/guide/" class="rl-card" style="padding: 20px; border: 1px solid #e2e8f0; border-radius: 12px; text-decoration: none; display: block; transition: all 0.2s; background: #f8fafc;">
            <div style="font-size: 1.1rem; color: #0f172a; font-weight: 600; margin-bottom: 8px;">📚 教程中心总览</div>
            <div style="font-size: 0.95rem; color: #64748b;">返回教程大全，学习更多科学上网的进阶技巧与客户端配置。</div>
          </a>
"""
    else:
        return ""
        
    html += """        </div>"""
    return html

for root, dirs, files in os.walk(base_dir):
    for dir_name in dirs:
        index_path = os.path.join(root, dir_name, "index.astro")
        if not os.path.exists(index_path):
            continue
            
        with open(index_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if 'id="related-reading"' in content:
            # Already injected
            continue
            
        related_html = get_related_html(dir_name)
        if not related_html:
            continue
            
        # Inject right before the closing tag of .article-content
        # Find </div>\n    </article>
        
        # A more robust way: find </article> and inject before its preceding </div>
        # Actually, let's just replace `      </div>\n    </article>` with `      [related]</div>\n    </article>`
        
        replace_target = '      </div>\n    </article>'
        if replace_target in content:
            new_content = content.replace(replace_target, related_html + '\n' + replace_target)
            
            # Let's add hover css inside <style is:inline>
            css_inject = """
    .rl-card:hover {
      transform: translateY(-3px);
      box-shadow: 0 10px 20px rgba(0,0,0,0.05);
      border-color: #3b82f6 !important;
    }
"""
            new_content = new_content.replace("<style is:inline>", "<style is:inline>\n" + css_inject)
            
            with open(index_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
                
            print(f"Injected internal links into {dir_name}")
        else:
            print(f"Could not find injection point in {dir_name}")
