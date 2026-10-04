// 好用机场：10 家机场的统一数据源。首页、推荐、便宜、性价比、十大排行榜、AI 流媒体、选购指南和测评页全部从这里读取。
// 改价格 / 流量 / 优惠码只改这里。billing: Monthly 月付 | Quarterly 季付 | Yearly 年付 | One-Time 不限时（一次性）
// traffic：周期套餐为“每月 GB”，不限时套餐为“总 GB”。custom: 定制套餐，不参与价格排序。

export type Billing = 'Monthly' | 'Quarterly' | 'Yearly' | 'One-Time';
export interface Plan { name: string; price: number; billing: Billing; traffic: number; custom?: boolean; note?: string }
export interface Airport {
  slug: string; // 测评页网址 /review/{slug}/
  name: string;
  logo: string;
  aff: string; // 推广链接
  promo: string | null; // 结算优惠码（不是邀请码）
  lines: string[]; // 线路
  streaming: boolean | null; // 官网写明支持流媒体
  ai: boolean | null; // 官网写明支持 ChatGPT 等 AI
  devices: string;
  nodeRegions: string;
  verdict: string; // 一句话推荐理由
  bestFor: string; // 适合人群
  plans: Plan[];
}

export const UPDATED = '2026-10-04';
export const UPDATED_LABEL = '2026 年 10 月 4 日';
export const UPDATED_MONTH = '2026年10月';
export const SITE = 'https://haoyongjichang.com';
export const SITE_NAME = '好用机场';

export const AIRPORTS: Airport[] = [
  {
    slug: 'sogo', name: 'Sogo云', logo: '/images/brands/sogo.webp', aff: 'https://wzjc.sogoyunaff.cc/#/?code=BC2BL855', promo: 'sogo10000',
    lines: ['IPLC', 'IEPL'], streaming: true, ai: true, devices: '不限设备数',
    nodeRegions: '香港×20、台湾×5、日本×10、新加坡×10、美国×10、马来西亚×2，以及英国、法国、德国、土耳其、泰国、巴西等',
    verdict: 'IPLC + IEPL 双专线，¥25/月 150GB 起，9 款套餐里有 4 款不限时包，各种用途都能覆盖',
    bestFor: '想要一家用到底、晚高峰稳定、看剧和 AI 都要的人',
    plans: [
      { name: '小包-年付版', price: 98, billing: 'Yearly', traffic: 60 },
      { name: '基础版', price: 25, billing: 'Monthly', traffic: 150 },
      { name: '优选版', price: 45, billing: 'Monthly', traffic: 350 },
      { name: '强化版', price: 80, billing: 'Monthly', traffic: 550 },
      { name: '顶配版', price: 150, billing: 'Monthly', traffic: 1050 },
      { name: '基础餐不限时版', price: 120, billing: 'One-Time', traffic: 120 },
      { name: '优选餐不限时版', price: 220, billing: 'One-Time', traffic: 250 },
      { name: '强化餐不限时版', price: 450, billing: 'One-Time', traffic: 500 },
      { name: '至尊餐不限时版', price: 850, billing: 'One-Time', traffic: 1000 },
    ],
  },
  {
    slug: 'weifeng', name: '微风', logo: '/images/brands/weifeng.webp', aff: 'https://edp01.breezenetaff.com/#/?code=hM8APccJ', promo: 'weifeng90',
    lines: ['IPLC'], streaming: null, ai: null, devices: '不限设备数',
    nodeRegions: '香港、台湾、日本、新加坡、美国、马来西亚等',
    verdict: '同价位流量最多：¥27/月 200GB、¥57/月 500GB，追剧和多设备更划算',
    bestFor: '经常看 4K、YouTube，每月要 200GB 以上的人',
    plans: [
      { name: '清风', price: 137, billing: 'Yearly', traffic: 100 },
      { name: '乘风', price: 27, billing: 'Monthly', traffic: 200 },
      { name: '破风', price: 57, billing: 'Monthly', traffic: 500 },
      { name: '御风', price: 127, billing: 'Monthly', traffic: 1200 },
      { name: '信风·不限时', price: 200, billing: 'One-Time', traffic: 270 },
      { name: '长风·不限时', price: 370, billing: 'One-Time', traffic: 570 },
    ],
  },
  {
    slug: 'feimao', name: '飞猫云', logo: '/images/brands/feimao.webp', aff: 'https://flycat1.flycatvipaff.cc/#/?code=w5lO9fqB', promo: 'flycat888',
    lines: ['IPLC'], streaming: true, ai: true, devices: '不限设备数',
    nodeRegions: '香港×20、台湾×10、日本×10、新加坡×10、美国×10、韩国×3，以及马来西亚、越南、菲律宾、泰国、印度、英国、德国、阿根廷等',
    verdict: '节点地区最多，学生版 ¥84/年；另有 ¥550/月 的独享原生 IP 定制套餐',
    bestFor: '学生党、需要冷门地区节点、做 TikTok / 外贸要固定 IP 的人',
    plans: [
      { name: '学生版', price: 84, billing: 'Yearly', traffic: 50 },
      { name: '星耀版', price: 25, billing: 'Monthly', traffic: 150 },
      { name: '星环版', price: 45, billing: 'Monthly', traffic: 300 },
      { name: '银河版', price: 85, billing: 'Monthly', traffic: 600 },
      { name: '宇宙版', price: 150, billing: 'Monthly', traffic: 1000 },
      { name: '不限时套餐', price: 680, billing: 'One-Time', traffic: 1000 },
      { name: '定制套餐（独享原生 IP）', price: 550, billing: 'Monthly', traffic: 500, custom: true },
    ],
  },
  {
    slug: 'firefly', name: 'Firefly', logo: '/images/brands/firefly.webp', aff: 'https://vip02.fireflyaff.com/#/?code=8nDg6OEY', promo: 'firefly',
    lines: ['IPLC'], streaming: null, ai: null, devices: '不限设备数',
    nodeRegions: '香港、台湾、日本、新加坡、美国、马来西亚等',
    verdict: '套餐简单清楚，¥100 就能买 100GB 永久不过期流量',
    bestFor: '偶尔才用、想买一次用很久，或者给家人备一个的人',
    plans: [
      { name: '年付版', price: 96, billing: 'Yearly', traffic: 60 },
      { name: 'Lite', price: 25, billing: 'Monthly', traffic: 150 },
      { name: 'Plus', price: 45, billing: 'Monthly', traffic: 300 },
      { name: 'Blaze', price: 85, billing: 'Monthly', traffic: 600 },
      { name: 'Nova', price: 150, billing: 'Monthly', traffic: 1000 },
      { name: '不限时', price: 100, billing: 'One-Time', traffic: 100 },
    ],
  },
  {
    slug: 'wuyou', name: '无忧链接', logo: '/images/brands/wuyou.webp', aff: 'https://wep01.worryfreeaff.com/#/?code=s1kH64A8', promo: 'wuyou',
    lines: ['IPLC'], streaming: true, ai: true, devices: '不限设备数',
    nodeRegions: '香港、台湾、日本、新加坡、美国等',
    verdict: '专线里月付最便宜：¥19/月 100GB，年付 ¥79 起，官网写明支持 ChatGPT 和 4K Netflix',
    bestFor: '预算有限、主要查资料和用 ChatGPT 的人',
    plans: [
      { name: 'MINI链接', price: 79, billing: 'Yearly', traffic: 40 },
      { name: '舒心链接', price: 19, billing: 'Monthly', traffic: 100 },
      { name: '省心链接', price: 33, billing: 'Monthly', traffic: 200 },
      { name: '随心链接', price: 77, billing: 'Monthly', traffic: 500 },
      { name: '忘忧链接', price: 117, billing: 'Monthly', traffic: 1000 },
      { name: '100G 永久不限时', price: 108, billing: 'One-Time', traffic: 100 },
      { name: '300G 永久不限时', price: 298, billing: 'One-Time', traffic: 300 },
    ],
  },
  {
    slug: 'kuajie', name: '跨界云', logo: '/images/brands/kuajie.webp', aff: 'https://vip02.kuajieaff.com/#/?code=hh3QezsW', promo: 'kuajie',
    lines: ['IPLC'], streaming: true, ai: true, devices: '不限设备数',
    nodeRegions: '香港、台湾、日本、新加坡、美国、马来西亚等',
    verdict: '大流量单价最低的专线：1.8TB 只要 ¥130/月，¥20/月 120GB 入门',
    bestFor: '全家共用、经常下载、每月要 1TB 以上的人',
    plans: [
      { name: '年付版', price: 96, billing: 'Yearly', traffic: 60 },
      { name: '轻云 Lite', price: 20, billing: 'Monthly', traffic: 120 },
      { name: '跃云 Leap', price: 40, billing: 'Monthly', traffic: 330 },
      { name: '凌云 Soar', price: 90, billing: 'Monthly', traffic: 830 },
      { name: '无界 Infinity', price: 130, billing: 'Monthly', traffic: 1800 },
    ],
  },
  {
    slug: 'lingmao', name: '灵猫', logo: '/images/brands/lingmao.webp', aff: 'https://edp01.civetaff.com/#/?code=CYg7QSJo', promo: 'lingmao',
    lines: ['IPLC'], streaming: true, ai: true, devices: '不限客户端',
    nodeRegions: '香港、台湾、日本、新加坡、美国等',
    verdict: '少见的季付档，年付 Big ¥295 每月 300GB，折合不到 ¥25/月',
    bestFor: '想季付，或者确定长期每月用 300GB 的人',
    plans: [
      { name: '年付小包', price: 85, billing: 'Yearly', traffic: 45 },
      { name: '年付 Small', price: 195, billing: 'Yearly', traffic: 150 },
      { name: '年付 Big', price: 295, billing: 'Yearly', traffic: 300 },
      { name: '季付 Big', price: 125, billing: 'Quarterly', traffic: 300 },
      { name: '月付 Small', price: 25, billing: 'Monthly', traffic: 150 },
      { name: '月付 Big', price: 45, billing: 'Monthly', traffic: 300 },
    ],
  },
  {
    slug: 'shanyue', name: '闪跃', logo: '/images/brands/shanyue.webp', aff: 'https://wep01.flashleapaff.com/#/?code=cs0ekCMG', promo: 'shanyue',
    lines: ['IPLC'], streaming: true, ai: true, devices: '官网未写明',
    nodeRegions: '香港、台湾、日本、新加坡、美国等',
    verdict: '同档位便宜 ¥1：¥24/月 150GB、¥44/月 300GB，全节点 1 倍率',
    bestFor: '和主流机场比价、每档都想省一点的人',
    plans: [
      { name: '年付版', price: 96, billing: 'Yearly', traffic: 60 },
      { name: '闪动 Flicker', price: 24, billing: 'Monthly', traffic: 150 },
      { name: '飞跃 Leap', price: 44, billing: 'Monthly', traffic: 300 },
      { name: '瞬移 Teleport', price: 84, billing: 'Monthly', traffic: 600 },
      { name: '跃迁 Warp', price: 134, billing: 'Monthly', traffic: 1000 },
    ],
  },
  {
    slug: 'flybit', name: 'Flybit', logo: '/images/brands/flybit.webp', aff: 'https://1.flybit.network/#/register?code=Aga7bd1s', promo: null,
    lines: [], streaming: null, ai: null, devices: '可共享',
    nodeRegions: '官网列出 30 多个国家和地区',
    verdict: '不限时包门槛最低：¥36 买 128GB，¥238 买 1TB，流量不过期',
    bestFor: '一个月只用几次、想要便宜备用机场的人',
    plans: [
      { name: '每月 128G', price: 15, billing: 'Monthly', traffic: 128 },
      { name: '每月 192G', price: 22, billing: 'Monthly', traffic: 192 },
      { name: '每月 256G', price: 28, billing: 'Monthly', traffic: 256 },
      { name: '每月 512G', price: 52, billing: 'Monthly', traffic: 512 },
      { name: '不限时 128G', price: 36, billing: 'One-Time', traffic: 128 },
      { name: '不限时 256G', price: 68, billing: 'One-Time', traffic: 256 },
      { name: '不限时 512G', price: 128, billing: 'One-Time', traffic: 512 },
      { name: '不限时 1024G', price: 238, billing: 'One-Time', traffic: 1024 },
    ],
  },
  {
    slug: 'xxyun', name: '小新云', logo: '/images/brands/xxyun.webp', aff: 'https://www.xx-yun.com/?code=pi9fB906', promo: null,
    lines: ['BGP 中转'], streaming: null, ai: null, devices: '不限设备数',
    nodeRegions: '香港、台湾、日本、新加坡、美国等',
    verdict: '价格最低：¥9.99/月 100GB、¥39.9/月 1TB，但走 BGP 中转不是专线',
    bestFor: '预算极低、能接受晚高峰偶尔变慢的人',
    plans: [
      { name: '初级 月付 100G', price: 9.99, billing: 'Monthly', traffic: 100 },
      { name: '中级 月付 300G', price: 19.9, billing: 'Monthly', traffic: 300 },
      { name: '高级 月付 1000G', price: 39.9, billing: 'Monthly', traffic: 1000 },
    ],
  },
];

/* ---------------- 计算 ---------------- */
export const priced = (a: Airport) => a.plans.filter((p) => !p.custom);
export function monthlyEq(p: Plan): number | null {
  if (p.billing === 'Monthly') return p.price;
  if (p.billing === 'Quarterly') return p.price / 3;
  if (p.billing === 'Yearly') return p.price / 12;
  return null;
}
export const perGB = (p: Plan) => (monthlyEq(p) ?? p.price) / p.traffic;
export const fmtGB = (n: number) => (n >= 1000 ? `${+(n / 1000).toFixed(2)}TB` : `${n}GB`);
export const fmtPrice = (n: number) => `¥${Number.isInteger(n) ? n : +n.toFixed(2)}`;
export const unit = (b: Billing) => ({ Monthly: '月', Quarterly: '季', Yearly: '年', 'One-Time': '次' })[b];
export const billingLabel = (b: Billing) => ({ Monthly: '月付', Quarterly: '季付', Yearly: '年付', 'One-Time': '不限时' })[b];
export const planPrice = (p: Plan) => `${fmtPrice(p.price)}/${unit(p.billing)}`;
export const planTraffic = (p: Plan) => (p.billing === 'One-Time' ? `${fmtGB(p.traffic)}（不过期）` : `${fmtGB(p.traffic)}/月`);
export const lineLabel = (a: Airport) => (a.lines.length ? a.lines.join(' + ') : '官网未写明');
export const isPremium = (a: Airport) => a.lines.some((l) => l === 'IPLC' || l === 'IEPL');
export const monthly = (a: Airport) => priced(a).filter((p) => p.billing === 'Monthly').sort((x, y) => x.price - y.price);
export const yearly = (a: Airport) => priced(a).filter((p) => p.billing === 'Yearly').sort((x, y) => x.price - y.price);
export const oneTime = (a: Airport) => priced(a).filter((p) => p.billing === 'One-Time').sort((x, y) => x.price - y.price);
export const entry = (a: Airport) => monthly(a)[0] ?? null;
export const bestValue = (a: Airport) =>
  priced(a).filter((p) => p.billing !== 'One-Time').sort((x, y) => perGB(x) - perGB(y))[0] ?? null;
export const trafficRange = (a: Airport) => {
  const t = priced(a).filter((p) => p.billing !== 'One-Time').map((p) => p.traffic);
  return `${fmtGB(Math.min(...t))}–${fmtGB(Math.max(...t))}`;
};
export const unlockText = (a: Airport) =>
  a.streaming && a.ai ? 'Netflix + ChatGPT' : a.streaming ? '流媒体' : a.ai ? 'ChatGPT' : '官网未写明';
export const reviewUrl = (a: Airport) => `/review/${a.slug}/`;
export const bySlug = (s: string) => AIRPORTS.find((a) => a.slug === s)!;

export const USAGE = [
  { key: 'light', label: '轻度', need: 50, desc: '查资料、用 ChatGPT、刷社交软件' },
  { key: 'daily', label: '日常', need: 150, desc: '每天看 1–2 小时视频' },
  { key: 'video', label: '追剧', need: 300, desc: '经常看 4K、YouTube、Netflix' },
  { key: 'heavy', label: '重度', need: 600, desc: '多设备、全家共用、常下载' },
];
export function cheapestFor(a: Airport, need: number): Plan | null {
  return (
    priced(a)
      .filter((p) => p.billing !== 'One-Time' && p.traffic >= need)
      .sort((x, y) => monthlyEq(x)! - monthlyEq(y)! || y.traffic - x.traffic)[0] ?? null
  );
}
export const usagePrice = (p: Plan) =>
  p.billing === 'Monthly' ? `${fmtPrice(p.price)}/月` : `${planPrice(p)}（折合 ${fmtPrice(+monthlyEq(p)!.toFixed(1))}/月）`;

/* ---------------- 结构化数据 ---------------- */
export const faqSchema = (faq: { q: string; a: string }[]) => ({
  '@context': 'https://schema.org',
  '@type': 'FAQPage',
  mainEntity: faq.map((f) => ({ '@type': 'Question', name: f.q, acceptedAnswer: { '@type': 'Answer', text: f.a } })),
});
export const itemListSchema = (name: string, list: Airport[]) => ({
  '@context': 'https://schema.org',
  '@type': 'ItemList',
  name,
  numberOfItems: list.length,
  itemListElement: list.map((a, i) => ({ '@type': 'ListItem', position: i + 1, name: a.name, url: `${SITE}${reviewUrl(a)}` })),
});
