import http.server
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
handler = http.server.SimpleHTTPRequestHandler
httpd = http.server.HTTPServer(("", 8080), handler)
print("Serving on port 8080")
httpd.serve_forever()
