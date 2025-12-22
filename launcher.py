import http.server, socketserver, webbrowser, threading, os
PORT = 8000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))
class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)
def run():
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        httpd.serve_forever()
if __name__ == "__main__":
    t = threading.Thread(target=run, daemon=True)
    t.start()
    webbrowser.open(f"http://localhost:{PORT}/index.html")
    print("PDF Overlay Studio Pro is running. Close this window to exit.")
    t.join()