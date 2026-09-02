import os
import re

brands_data = {
    "微风": {
        "name": "微风",
        "intro": "微风机场成立于2023年，是一家专注于提供高端网络体验的老牌服务商。全线采用顶级的 IPLC 国际专线，彻底免疫防火墙干扰，运营团队技术实力雄厚，旨在为极客和商务人士提供最极致的科学上网体验。",
        "coverage": "微风节点精准覆盖香港、台湾、日本、新加坡、美国、英国等优质核心区，所有节点均采用专线内网传输，高峰期速率依然能够达到 100% 满血状态，完全不限速、不限制在线设备数。",
        "unlock": "全链路原生 IP 落地，完美解锁 Netflix、Disney+、Hulu 等全球流媒体，对 ChatGPT、Claude、Gemini 等 AI 平台提供丝滑的原生解锁支持，让您不再遇到 Access Denied 报错。",
        "price": "虽然定位高端专线，但微风提供了极具诚意的入门价格。基础套餐每月仅需几十元，支持支付宝、微信等主流支付方式，支持全平台主流客户端一键导入，新手也能一秒上手。"
    },
    "飞猫云": {
        "name": "飞猫云",
        "intro": "飞猫云是一家极具性价比的创新型机场，主打“花中转的钱，体验专线的速度”。后端采用 BGP 多线中继结合部分 IEPL 专线，完美兼顾了日常浏览与重度下载的双重需求。",
        "coverage": "飞猫云在全球部署了超过 80 个精选节点，除了常见的港日新美，还囊括了土耳其、阿根廷等汇率优势区，所有节点支持 UDP 转发，适合游戏与语音需求。",
        "unlock": "流媒体与 AI 解锁能力拉满。不仅秒开 Netflix 4K，还能完美支持 TikTok 运营与 ChatGPT 注册。智能分流系统确保国内流量直连，海外流量走代理，互不干扰。",
        "price": "飞猫云以亲民著称，低至每月 15 元即可享受百 G 大流量，更有极具诱惑力的年付优惠。提供详尽的各平台使用教程，支持微信扫码秒级开通，售后响应极快。"
    },
    "Firefly": {
        "name": "Firefly",
        "intro": "Firefly 萤火虫是一家追求极致稳定性的老牌专线机场。团队拥有丰富的跨国网络运维经验，全节点采用昂贵的企业级 IPLC/IEPL 专线，承诺提供金融级别的低延迟与抗丢包能力。",
        "coverage": "精心优化的亚太与欧美路由，香港、日本、新加坡节点延迟低至个位数。Firefly 坚持“少而精”的节点策略，拒绝滥竽充数的无效节点，确保每一个节点都能满载运行。",
        "unlock": "提供专门的流媒体与 AI 解锁线路，无论是追剧狂人还是 AI 深度开发者，都能享受丝滑不掉线的极致体验。支持主机游戏加速，是 PS5/Switch 玩家的福音。",
        "price": "套餐设计灵活，从轻度冲浪到重度 4K 影视都有对应的高性价比选项。支持支付宝安全支付，不记录任何用户隐私日志，安全与速度并重。"
    },
    "无忧": {
        "name": "无忧链接",
        "intro": "无忧链接成立于 2024 年底，采用全新 VLESS 协议与 IPLC 专线，运营团队为海外团队，主打稳定、低延迟的线路体验，全天客服轮班响应用户需求。",
        "coverage": "无忧链接节点覆盖香港、台湾、新加坡、日本、美国等主流地区，全部套餐不限速、不限制同时在线设备数量。",
        "unlock": "支持解锁 ChatGPT、Gemini 等 AI 工具，以及 Netflix、Disney+、YouTube、TikTok 等国外流媒体与短视频平台。同时官方声明不记录日志、不屏蔽 BT 下载。",
        "price": "轻量级套餐低至 6 元每月，大促期间全新 6.8 折。支持订阅链接无需转换，支持 iOS/安卓/Windows/MAC 等客户端。支持支付宝、微信、USDT 支付，首次订阅享 85 折优惠。"
    },
    "跨界云": {
        "name": "跨界云",
        "intro": "跨界云致力于打破网络边界，采用最新的 Trojan 协议结合专线直达架构。团队由资深网络工程师组成，为跨境电商与外贸工作者提供极高纯净度的独立 IP 服务。",
        "coverage": "除了常规的高速亚洲节点，跨界云特别强化了欧美、东南亚等冷门电商地区的节点覆盖，满足 TikTok 矩阵运营与海外社交媒体营销的特殊需求。",
        "unlock": "拥有极强的数据中心与原生 ISP 解锁能力，轻松绕过 Netflix 与各大 AI 平台的严苛风控。全程加密传输，高度保护用户的商业隐私与数据安全。",
        "price": "跨界云提供了独具特色的定制化套餐，按需付费，丰俭由人。无论是企业级团队共享还是个人轻量使用，都能找到最合适的价位。支持支付宝与加密货币结算。"
    },
    "灵猫": {
        "name": "灵猫",
        "intro": "灵猫机场以其“灵动、轻快”的特点在圈内广受好评。全站采用 Shadowsocks 与 Vless 混合协议，配合优质的 BGP 隧道中转，为用户带来极低延迟的秒开体验。",
        "coverage": "节点布局科学合理，主打亚太地区超低延迟，日韩新港节点晚高峰表现极其优异，无论看视频还是刷网页都能体验到“无感翻墙”的顺畅。",
        "unlock": "灵猫对流媒体的支持可谓不遗余力，内置强大的 DNS 解锁服务端，Netflix、Disney+ 解锁率高达 99%。ChatGPT 日常使用从不弹验证码。",
        "price": "极其良心的定价策略是灵猫的一大杀手锏。即便是学生党也能轻松负担，且常年有拼团与节假日大额优惠券。提供长达 3 天的无理由退款保证，买得放心。"
    },
    "闪跃": {
        "name": "闪跃",
        "intro": "闪跃 (Flash) 就像它的名字一样，以雷霆万钧的速度征服用户。底层依托强大的企业级带宽资源，全节点部署最新拥塞控制算法，即使在最拥堵的晚高峰也能逆风翻盘。",
        "coverage": "全球核心骨干网直连，香港、台湾、日本、美国四大核心区带宽冗余极高。闪跃不做花里胡哨的百国节点，只把最常用的线路打磨到极致的快与稳。",
        "unlock": "完美应对 Netflix 封杀与 OpenAI IP 限制，落地端每日自动检测并更新原生 IP 库，确保用户在任何时候打开海外应用都能无缝畅享。",
        "price": "价格透明，拒绝套路。提供按量付费与周期包月双模式，流量单价极具竞争力。全自动化运维，购买后一秒下发订阅，支持支付宝等国内便捷支付。"
    },
    "Flybit": {
        "name": "Flybit",
        "intro": "Flybit 是一家拥有极客基因的高端技术流机场，首批全线拥抱 Hysteria 2 与 TUIC 协议的先驱者。通过暴力的 UDP 协议加速，彻底消灭了跨国网络的卡顿与丢包。",
        "coverage": "节点网络遍布全球 30 多个国家，所有节点均经过严格的 SLA 在线率监控。Flybit 特别为极客玩家提供了众多稀有国家节点，满足全方位的网络漫游需求。",
        "unlock": "不仅能解锁主流的流媒体与 ChatGPT，Flybit 甚至对 Hulu、HBO Max 等冷门流媒体都有极佳的兼容性。专为追求极致自由的网络探索者打造。",
        "price": "虽然技术含量极高，但 Flybit 的定价却非常亲民，提供多种灵活档位的套餐选择。官网设计极简大气，不强制年付，支持 USDT 等加密资产匿名支付。"
    },
    "xsus": {
        "name": "xsus",
        "intro": "xsus (叉速) 专注于为高净值用户提供“如丝般顺滑”的 IEPL 专线网络。彻底抛弃公网传输，100% 物理内网过境，将网络波动与墙的干扰降至绝对的零。",
        "coverage": "xsus 的节点犹如精密切割的钻石，数量不在多而在精。香港与日本节点常年保持在个位数延迟，是炒美股、玩外服竞技游戏的绝佳物理外挂。",
        "unlock": "原生纯净住宅 IP 库是 xsus 的护城河。Netflix 4K 秒缓冲只是基础，完美避开 OpenAI 风控、轻松注册各大海外严苛平台才是其真正的实力体现。",
        "price": "xsus 定位中高端，但带来的体验绝对物超所值。提供大流量团队套餐与精简个人套餐，完善的工单售后系统，让您花的每一分钱都能感受到 VIP 般的尊贵服务。"
    },
    "小新云": {
        "name": "小新云",
        "intro": "小新云 (Xiaoxinyun) 是一款深受年轻人喜爱的二次元友好型机场。以清新活泼的品牌形象和极其硬核的 BGP 中转实力，在竞争激烈的机场圈杀出了一条血路。",
        "coverage": "除了标配的高速亚太节点，小新云还对日本、台湾等二次元重镇进行了深度带宽扩容，下载大体量游戏、观看海外直播无任何缓冲烦恼。",
        "unlock": "追番看剧的终极神器。全网流媒体绿灯解锁，ChatGPT 随叫随到，让您在探索海外内容时毫无阻碍。不限制终端数，手机电脑平板可以同时丝滑在线。",
        "price": "小新云主打极致性价比，每月仅需一杯奶茶钱。界面亲切易用，提供傻瓜式的一键导入教程，对小白用户极其友好，是新手第一次翻墙的完美首选。"
    }
}

html_template = """      <div class="bcp-text-intro">
        <h3>{name}机场简介</h3>
        <p>{intro}</p>
        
        <h3>节点覆盖</h3>
        <p>{coverage}</p>
        
        <h3>流媒体与AI解锁</h3>
        <p>{unlock}</p>
        
        <h3>价格套餐</h3>
        <p>{price}</p>
      </div>"""

pages_dir = r"c:\Users\USER\Desktop\haoyongjichang.com\src\pages"

for root, dirs, files in os.walk(pages_dir):
    for file in files:
        if file.endswith(".astro"):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            if 'class="brand-card-premium"' not in content:
                continue
                
            new_content = content
            
            if ".bcp-text-intro" not in new_content:
                css_to_add = """
    .bcp-text-intro {
      margin: 24px 0 30px;
      padding: 30px;
      background-color: #f8fafc;
      border-radius: 16px;
      border: 1px solid #e2e8f0;
    }
    .bcp-text-intro h3 {
      font-size: 1.25rem;
      color: #0f172a;
      margin-top: 0;
      margin-bottom: 12px;
      font-weight: 700;
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .bcp-text-intro h3::before {
      content: "";
      display: inline-block;
      width: 4px;
      height: 18px;
      background: #3b82f6;
      border-radius: 2px;
    }
    .bcp-text-intro p {
      font-size: 1.05rem;
      color: #475569;
      line-height: 1.8;
      margin-bottom: 24px;
    }
    .bcp-text-intro h3:not(:first-child) {
      margin-top: 28px;
    }
    .bcp-text-intro p:last-child {
      margin-bottom: 0;
    }
"""
                if "<style is:inline>" in new_content:
                    new_content = new_content.replace("<style is:inline>", "<style is:inline>\n" + css_to_add)

            for key, data in brands_data.items():
                pattern = r'(alt="' + key + r'".*?</a>\s*</div>)(\s*)<div class="bcp-grid">'
                
                html_snippet = html_template.format(
                    name=data['name'], 
                    intro=data['intro'],
                    coverage=data['coverage'],
                    unlock=data['unlock'],
                    price=data['price']
                )
                
                if html_snippet in new_content or "<h3>" + data['name'] + "机场简介</h3>" in new_content:
                    continue
                    
                new_content = re.sub(pattern, r'\1\n' + html_snippet + r'\2<div class="bcp-grid">', new_content, flags=re.DOTALL)
                
            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated {filepath}")
