"""Build the portable, offline HTML demo with embedded local photographs."""
from pathlib import Path
import base64
import re

root = Path(__file__).resolve().parent
html = (root / 'index.html').read_text()
def embed(match):
    file = root / match.group(1)
    mime = 'image/png' if file.suffix == '.png' else 'image/jpeg'
    return 'src="data:' + mime + ';base64,' + base64.b64encode(file.read_bytes()).decode() + '"'
html = re.sub(r'src="(assets/[^\"]+)"', embed, html)
html = re.sub(r'<a href="dauxillium-voorbeeld.html"[^>]*>Download voorbeeld</a>', '', html)
(root / 'dauxillium-voorbeeld.html').write_text(html)
print('Standalone demo:', (root / 'dauxillium-voorbeeld.html').stat().st_size, 'bytes')
