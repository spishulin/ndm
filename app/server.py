#!/usr/bin/env python3

import http.server
import socketserver

class handler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
      xff = self.headers.get('X-Forwarded-For', '-')
      super().log_message(format + f' [{xff}]', *args)
    
with socketserver.TCPServer(("", 8080), handler) as httpd:

   httpd.serve_forever()
