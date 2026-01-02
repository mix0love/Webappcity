import http.server
import socketserver
import os
import subprocess
import threading

def run_web_server():
    port = int(os.environ.get("PORT", 10000))
    handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", port), handler) as httpd:
        httpd.serve_forever()

threading.Thread(target=run_web_server, daemon=True).start()


print("Запуск бота...")
subprocess.call(["python", "bot.py"])
