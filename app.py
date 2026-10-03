import json
import os
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, urlsplit


def add(a, b):
    return a + b


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        url = urlsplit(self.path)
        args = parse_qs(url.query)
        if url.path == "/health":
            body = {"status": "ok"}
        elif url.path == "/add":
            body = {"result": add(int(args.get("a", ["0"])[0]), int(args.get("b", ["0"])[0]))}
        else:
            body = {"service": "IRIS public automatic repair demo"}
        data = json.dumps(body).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)


HTTPServer(("0.0.0.0", int(os.environ.get("PORT", "8080"))), Handler).serve_forever()
