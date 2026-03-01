from http.server import HTTPServer, SimpleHTTPRequestHandler
import os

os.chdir('/Users/zhiqiangjia/Claude-Global/公众号国际化/assets')

class CORSHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', '*')
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

HTTPServer(('', 8765), CORSHandler).serve_forever()
