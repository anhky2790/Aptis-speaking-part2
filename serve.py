# serve.py — chạy web tĩnh trong thư mục hiện tại
import http.server, socketserver, os

PORT = 8000
os.chdir(os.path.dirname(__file__))  # phục vụ đúng thư mục chứa file

Handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at http://localhost:{PORT}")
    print("Nhấn Ctrl+C hoặc nút Stop trong Thonny để dừng.")
    httpd.serve_forever()
