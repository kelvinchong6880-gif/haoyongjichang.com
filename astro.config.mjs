// @ts-check
import mdx from '@astrojs/mdx';
import sitemap from '@astrojs/sitemap';
import { defineConfig } from 'astro/config';
import fs from 'fs';
import path from 'path';

const lastmodData = JSON.parse(fs.readFileSync(path.resolve('./src/data/sitemap-lastmod.json'), 'utf-8'));
const PRIORITY = [
  [/^https:\/\/haoyongjichang\.com\/$/, 1.0],
  [/\/(recommend|cheap-airport|best-value-airport|top-10-airports|quick-guide|ai-streaming|buying-guide)\/$/, 0.9],
  [/\/review\/[^/]+\/$/, 0.8],
  [/\/guide\/[^/]*\/?$/, 0.7],
];

// https://astro.build/config
export default defineConfig({
  site: 'https://haoyongjichang.com',
  trailingSlash: 'always',
  integrations: [
    mdx(),
    sitemap({
      filter: (page) => !page.includes('/404'),
      serialize(item) {
        let pathname = new URL(item.url).pathname;
        if (!pathname.endsWith('/')) pathname += '/';
        if (lastmodData[pathname]) item.lastmod = lastmodData[pathname];
        item.priority = PRIORITY.find(([re]) => re.test(item.url))?.[1] ?? 0.5;
        return item;
      },
    }),
  ],
});
