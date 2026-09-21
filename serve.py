"""Local preview. Only expose demo files, never repository internals."""
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import unquote, urlsplit
import os

ROOT = Path(__file__).resolve().parent
class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)
    def send_head(self):
        path = unquote(urlsplit(self.path).path)
        allowed = {'/', '/index.html', '/dauxillium-voorbeeld.html'}
        if path not in allowed and not (path.startswith('/assets/') and '..' not in path.split('/') and Path(path).suffix in {'.jpg', '.png'}):
            self.send_error(404)
            return None
        return super().send_head()
    def end_headers(self):
        self.send_header('X-Robots-Tag', 'noindex, nofollow')
        self.send_header('X-Content-Type-Options', 'nosniff')
        self.send_header('Referrer-Policy', 'no-referrer')
        super().end_headers()

if __name__ == '__main__':
    port = int(os.environ.get('PORT', '8794'))
    print(f'Dauxillium preview on 127.0.0.1:{port}', flush=True)
    ThreadingHTTPServer(('127.0.0.1', port), Handler).serve_forever()
