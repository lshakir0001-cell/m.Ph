// Mini Pharmacy service worker: network first so the team's updates show up at once,
// with a cached copy so the app still opens without internet.
const CACHE = 'mph-v5';
const SHELL = ['./', './index.html', './manifest.webmanifest', './icons/icon.svg', './icons/icon-192.png', './icons/icon-512.png', './catalog/catalog.js'];

self.addEventListener('install', (e) => {
  // also keep the medicine pictures listed in catalog.js, so they show without internet
  e.waitUntil(
    caches.open(CACHE).then(async (c) => {
      await c.addAll(SHELL);
      try {
        const txt = await (await fetch('./catalog/catalog.js')).text();
        const imgs = [...new Set(txt.match(/catalog\/img\/[\w.-]+/g) || [])].map((p) => './' + p);
        await c.addAll(imgs);
      } catch (err) {}
    })
  );
  self.skipWaiting();
});

self.addEventListener('activate', (e) => {
  e.waitUntil(
    caches.keys().then((keys) => Promise.all(keys.filter((k) => k !== CACHE).map((k) => caches.delete(k))))
  );
  self.clients.claim();
});

self.addEventListener('fetch', (e) => {
  // only cache normal web requests (skip browser-extension and other schemes)
  if (e.request.method !== 'GET' || !e.request.url.startsWith('http')) return;
  e.respondWith(
    fetch(e.request)
      .then((res) => {
        const copy = res.clone();
        caches.open(CACHE).then((c) => c.put(e.request, copy));
        return res;
      })
      .catch(() => caches.match(e.request).then((r) => r || caches.match('./index.html')))
  );
});
