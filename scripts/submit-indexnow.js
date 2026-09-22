import fs from 'fs';
import path from 'path';
import https from 'https';

const HOST = 'haoyongjichang.com';
const KEY = 'e33c47144a279867bb4e7b4e891d05ff';
const KEY_LOCATION = `https://${HOST}/${KEY}.txt`;
const API_URL = 'api.indexnow.org';

const sitemapPath = path.resolve('dist/sitemap-0.xml');

if (!fs.existsSync(sitemapPath)) {
  console.error(`Sitemap not found at ${sitemapPath}. Build might have failed or sitemap generation is off.`);
  process.exit(1);
}

const sitemapContent = fs.readFileSync(sitemapPath, 'utf-8');
// Extract URLs using regex
const urls = [];
const regex = /<loc>(.*?)<\/loc>/g;
let match;
while ((match = regex.exec(sitemapContent)) !== null) {
  urls.push(match[1]);
}

if (urls.length === 0) {
  console.warn('No URLs found in the sitemap.');
  process.exit(0);
}

const payload = JSON.stringify({
  host: HOST,
  key: KEY,
  keyLocation: KEY_LOCATION,
  urlList: urls
});

const options = {
  hostname: API_URL,
  port: 443,
  path: '/indexnow',
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'Content-Length': Buffer.byteLength(payload)
  }
};

console.log(`Submitting ${urls.length} URLs to IndexNow...`);

const req = https.request(options, (res) => {
  let data = '';
  res.on('data', (chunk) => {
    data += chunk;
  });
  res.on('end', () => {
    if (res.statusCode === 200 || res.statusCode === 202) {
      console.log('✅ IndexNow submission successful!');
    } else {
      console.error(`❌ IndexNow submission failed. Status: ${res.statusCode}`);
      console.error(data);
    }
  });
});

req.on('error', (e) => {
  console.error(`❌ Request error: ${e.message}`);
});

req.write(payload);
req.end();
