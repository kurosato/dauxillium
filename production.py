"""Build the official static site without changing the GitHub Pages preview."""
from pathlib import Path
import re
import shutil

root = Path(__file__).resolve().parent
out = root / 'dist'
out.mkdir(exist_ok=True)
html = (root / 'index.html').read_text()
html = html.replace('<meta name="robots" content="noindex, nofollow">', '<meta name="robots" content="index, follow">\n<link rel="canonical" href="https://dauxilium.be/">')
html = re.sub(r'<span class="prototype-label">.*?</span>', '', html)
html = re.sub(r'<a href="dauxillium-voorbeeld.html"[^>]*>Download voorbeeld</a>', '', html)
(out / 'index.html').write_text(html)
shutil.copytree(root / 'assets', out / 'assets', dirs_exist_ok=True)
(out / 'robots.txt').write_text('User-agent: *\nAllow: /\nSitemap: https://dauxilium.be/sitemap.xml\n')
(out / 'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>https://dauxilium.be/</loc></url></urlset>\n')
(out / 'healthz').write_text('ok\n')
print('Production site built in dist/')
