"""
POLICY COMPLIANCE REVIEW (Vortex Internal Tooling)
File: launcher.py
Reviewed: 2026-02-01
Reviewer: Codex

Compliant:
- [ ] Serves local files only from the application directory.
- [ ] No hard-coded secrets or outbound network calls.

Non-compliant:
- [ ] None noted.

Needs review:
- [ ] Local HTTP server has no auth/TLS; confirm localhost-only usage is acceptable.

Notes / Actions:
- Bind explicitly to localhost to avoid LAN exposure.
"""

import http.server, socketserver, webbrowser, threading, os
PORT = 8000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))
class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)
def run():
    with socketserver.TCPServer(("localhost", PORT), Handler) as httpd:
        httpd.serve_forever()
if __name__ == "__main__":
    t = threading.Thread(target=run, daemon=True)
    t.start()
    webbrowser.open(f"http://localhost:{PORT}/index.html")
    print("PDF Overlay Studio Pro is running. Close this window to exit.")
    t.join()
