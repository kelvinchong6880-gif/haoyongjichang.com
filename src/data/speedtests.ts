// 机场实测数据：按测速截图逐个节点整理。speed 为测速成功节点的平均下载速度（MB/s），rtt 为该地区节点 TLS RTT 中位数（ms）。
// 不同测试的线路带宽、线程数不同，速度只能和同一次测试里的其他地区比较，不能跨机场直接比。

export interface RegionResult {
  region: string;
  nodes: number; // 该地区节点数
  ok: number; // 测速成功的节点数
  rtt: number;
  speed: number;
  unlock: string;
}
export interface SpeedTest {
  slug: string;
  date: string; // 测试时间（北京时间）
  source: string; // 测试来源（截图水印）
  line: string; // 测试端网络
  threads: number;
  peak: boolean; // 是否在晚高峰 20:00–23:00 测试
  regions: RegionResult[];
  notes: string[];
  images: { src: string; width: number; height: number; alt: string; caption: string }[];
}

export const SPEEDTESTS: SpeedTest[] = [
  {
    slug: 'sogo',
    date: '2026-04-13 17:32',
    source: 'FFQ.LA 公共测速',
    line: '辽宁移动 1Gbps',
    threads: 8,
    peak: false,
    regions: [
      { region: '香港', nodes: 20, ok: 17, rtt: 144, speed: 52.5, unlock: 'Netflix、Disney+、YouTube、哔哩哔哩港澳台' },
      { region: '台湾', nodes: 10, ok: 8, rtt: 144, speed: 49.4, unlock: 'Netflix、Disney+、YouTube、ChatGPT、哔哩哔哩台湾' },
      { region: '日本', nodes: 10, ok: 9, rtt: 95, speed: 49.0, unlock: 'Netflix、Disney+、YouTube、ChatGPT' },
      { region: '新加坡', nodes: 10, ok: 10, rtt: 156, speed: 39.0, unlock: 'Netflix、YouTube、ChatGPT（Disney+ 查询失败）' },
      { region: '美国', nodes: 10, ok: 10, rtt: 230, speed: 47.5, unlock: 'Netflix、Disney+、YouTube、ChatGPT' },
    ],
    notes: [
      '测试线路是 1Gbps、8 线程，多数节点平均速度在 40–55MB/s（约 320–440Mbps），各地区差距不大，美国节点也有约 47MB/s。',
      '1 分钟后的第二次测试（截图 2）里，60 个节点有 59 个测速成功，第一次失败的香港 02、09、15 等节点都恢复正常，说明是偶发失败。',
      '香港节点没有测 ChatGPT（ChatGPT 本身不支持香港）；台湾节点的 Netflix、Disney+ 解锁地区显示为西班牙（ES）。',
    ],
    images: [
      { src: '/images/tests/sogo/speedtest-1.webp', width: 808, height: 1280, alt: 'Sogo云 60 个节点测速与流媒体解锁结果（第一次）', caption: '第一次测试：2026-04-13 17:32，辽宁移动 1Gbps，测速 + Disney+ / Netflix / YouTube / 哔哩哔哩 / ChatGPT 解锁' },
      { src: '/images/tests/sogo/speedtest-2.webp', width: 808, height: 1280, alt: 'Sogo云 60 个节点测速与流媒体解锁结果（第二次）', caption: '第二次测试：2026-04-13 17:33，同一线路复测' },
    ],
  },
  {
    slug: 'firefly',
    date: '2026-07-18 20:35',
    source: 'lilyMiaoKobot 测速',
    line: '珠海联通 9Gbps',
    threads: 32,
    peak: true,
    regions: [
      { region: '香港', nodes: 15, ok: 14, rtt: 109, speed: 529.7, unlock: 'YouTube、Netflix、Disney+' },
      { region: '台湾', nodes: 5, ok: 5, rtt: 160, speed: 53.5, unlock: 'YouTube、Netflix、Disney+' },
      { region: '日本', nodes: 10, ok: 10, rtt: 140, speed: 99.9, unlock: 'YouTube、Netflix、Disney+' },
      { region: '新加坡', nodes: 10, ok: 9, rtt: 95, speed: 384.1, unlock: 'YouTube、Netflix、Disney+' },
      { region: '美国', nodes: 10, ok: 10, rtt: 243, speed: 10.7, unlock: 'YouTube、Netflix、Disney+' },
    ],
    notes: [
      '测试时间是晚上 20:35，正好在晚高峰，香港节点平均仍有 500MB/s 以上，新加坡约 380MB/s。',
      '测试线路是 9Gbps、32 线程，所以香港、新加坡的速度数字很高；美国节点约 10MB/s（约 86Mbps），看 4K 够用，但明显比亚洲节点慢。',
      '50 个节点全部解锁 YouTube、Netflix、Disney+，且解锁地区和节点地区一致；这次测试没有测 ChatGPT。',
    ],
    images: [
      { src: '/images/tests/firefly/speedtest.webp', width: 837, height: 1280, alt: 'Firefly 50 个节点晚高峰测速结果', caption: '速度测试：2026-07-18 20:35，珠海联通 9Gbps，32 线程' },
      { src: '/images/tests/firefly/streaming.webp', width: 763, height: 1280, alt: 'Firefly 50 个节点 YouTube、Netflix、Disney+ 解锁结果', caption: '流媒体测试：2026-07-18 20:36，YouTube / Netflix / Disney+' },
    ],
  },
];

export const speedTestFor = (slug: string) => SPEEDTESTS.find((t) => t.slug === slug) ?? null;
export const totalNodes = (t: SpeedTest) => t.regions.reduce((n, r) => n + r.nodes, 0);
export const totalOk = (t: SpeedTest) => t.regions.reduce((n, r) => n + r.ok, 0);
export const fastest = (t: SpeedTest) => [...t.regions].sort((x, y) => y.speed - x.speed)[0];
export const lowestRtt = (t: SpeedTest) => [...t.regions].sort((x, y) => x.rtt - y.rtt)[0];
export const mbps = (mbs: number) => Math.round(mbs * 8);
