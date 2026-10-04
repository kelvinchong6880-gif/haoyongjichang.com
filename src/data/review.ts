// 测评页文案：根据套餐数据自动生成优缺点和常见问题
import { AIRPORTS, entry, yearly, oneTime, priced, fmtGB, fmtPrice, planPrice, cheapestFor, usagePrice, unlockText, isPremium, lineLabel, type Airport } from './airports';

const avgEntry = () => {
  const e = AIRPORTS.map(entry).filter(Boolean).map((p) => p!.price);
  return e.reduce((x, y) => x + y, 0) / e.length;
};

export function prosCons(a: Airport) {
  const pros: string[] = [];
  const cons: string[] = [];
  const e = entry(a); const y = yearly(a)[0]; const o = oneTime(a);
  const max = Math.max(...priced(a).filter((p) => p.billing !== 'One-Time').map((p) => p.traffic));
  if (isPremium(a)) pros.push(`${lineLabel(a)} 专线，晚高峰比普通中转线路更稳`);
  else cons.push(a.lines.length ? `走 ${lineLabel(a)}，不是 IPLC / IEPL 专线，晚高峰可能变慢` : '官网没有写明线路类型，建议先月付测试晚高峰表现');
  if (e && e.price <= avgEntry() - 1) pros.push(`月付门槛低：${planPrice(e)} 就有 ${fmtGB(e.traffic)}`);
  if (e && e.price >= avgEntry() + 3) cons.push(`月付入门价 ${planPrice(e)}，比收录机场平均价高`);
  if (y) pros.push(`有年付小包：${planPrice(y)}，每月 ${fmtGB(y.traffic)}，折合约 ${fmtPrice(+(y.price / 12).toFixed(1))}/月`);
  if (o.length) pros.push(`有 ${o.length} 款不限时流量包（${fmtPrice(o[0].price)} 起），流量不过期`);
  else cons.push('没有不限时流量包，偶尔用的人只能买周期套餐');
  if (max >= 1000) pros.push(`最高 ${fmtGB(max)}/月，大流量、多设备也够用`);
  else cons.push(`最大只有 ${fmtGB(max)}/月，重度用户不够用`);
  if (a.streaming && a.ai) pros.push('官网写明可解锁 Netflix 等流媒体和 ChatGPT');
  if (a.streaming == null && a.ai == null) cons.push('官网没写流媒体和 ChatGPT 解锁情况，需要的话先月付测试');
  if (a.slug === 'feimao') { pros.push('有独享原生 IP 定制套餐（¥550/月 500GB），适合 TikTok、外贸账号'); cons.push('不限时包门槛高：¥680 起（1TB）'); }
  if (a.slug === 'lingmao') pros.push('少见的季付档：¥125/季，每月 300GB');
  if (a.slug === 'weifeng') cons.push('没有低于 ¥27 的月付档，轻度用户要选年付清风');
  return { pros, cons };
}

export function brandFaq(a: Airport) {
  const e = entry(a); const y = yearly(a)[0]; const o = oneTime(a)[0];
  const daily = cheapestFor(a, 150);
  const faq = [
    { q: `${a.name}怎么样？`, a: `${a.name}：${a.verdict}。在本站十大机场排行榜排第 ${AIRPORTS.indexOf(a) + 1} 名，适合${a.bestFor}。` },
    { q: `${a.name}多少钱一个月？`, a: `${e ? `月付最低 ${planPrice(e)}（${fmtGB(e.traffic)}）` : '没有月付'}${y ? `，年付最低 ${planPrice(y)}（每月 ${fmtGB(y.traffic)}）` : ''}${o ? `，不限时包 ${fmtPrice(o.price)} 起` : ''}。${a.promo ? `结算时填优惠码 ${a.promo}。` : ''}` },
    { q: `每天看视频，${a.name}选哪个套餐？`, a: daily ? `每天 1–2 小时视频每月约 150GB，选 ${daily.name}：${usagePrice(daily)}，每月 ${fmtGB(daily.traffic)}。` : `${a.name}没有 150GB 以上的周期套餐。` },
    { q: `${a.name}能看 Netflix、用 ChatGPT 吗？`, a: a.streaming || a.ai ? `官网写明支持：${unlockText(a)}。如果某个节点打不开，换成香港、日本、新加坡或美国的其他节点。` : '官网没有写明。如果你主要为了看 Netflix 或用 ChatGPT，建议先买月付测试，或者看本站的 AI 与流媒体解锁推荐。' },
    { q: `${a.name}有优惠码吗？`, a: a.promo ? `有，结算页填写 ${a.promo}，以结算页显示的金额为准。` : `目前没有公开的优惠码，留意官网公告里的限时活动。` },
  ];
  return faq;
}
