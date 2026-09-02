// @ts-check

import mdx from '@astrojs/mdx';
import sitemap from '@astrojs/sitemap';
import { defineConfig, fontProviders } from 'astro/config';
import fs from 'fs';
import path from 'path';

const lastmodData = JSON.parse(
  fs.readFileSync(path.resolve('./src/data/sitemap-lastmod.json'), 'utf-8')
);

// https://astro.build/config
export default defineConfig({
	site: 'https://haoyongjichang.com',
	integrations: [
		mdx(),
		sitemap({
			serialize(item) {
				const url = new URL(item.url);
				let pathname = url.pathname;
				if (!pathname.endsWith('/')) pathname += '/';
				
				if (lastmodData[pathname]) {
					item.lastmod = lastmodData[pathname];
				}
				return item;
			}
		})
	],
	fonts: [
		{
			provider: fontProviders.local(),
			name: 'Atkinson',
			cssVariable: '--font-atkinson',
			fallbacks: ['sans-serif'],
			options: {
				variants: [
					{
						src: ['./src/assets/fonts/atkinson-regular.woff'],
						weight: 400,
						style: 'normal',
						display: 'swap',
					},
					{
						src: ['./src/assets/fonts/atkinson-bold.woff'],
						weight: 700,
						style: 'normal',
						display: 'swap',
					},
				],
			},
		},
	],
});
