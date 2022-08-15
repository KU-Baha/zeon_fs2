from http.server import HTTPServer, BaseHTTPRequestHandler


class Server(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.flush_headers()
        content_type = self.headers["Accept"].split(',')[0]

        if self.path == '/info':
            if content_type == 'text/html':
                html = open(".zeon_docker/meta.html")
                self.send_header("content-type", "text/html")
                self.end_headers()
                self.wfile.write(bytes(html.read(), "utf-8"))
                html.close()
            elif content_type == 'x-json':
                data = open(".zeon_docker/meta.txt")
                self.send_header("content-type", "x-json")
                self.end_headers()
                self.wfile.write(bytes(data.read(), "utf-8"))
                data.close()
            else:
                data = open(".zeon_docker/meta.txt")
                self.send_header("content-type", "*/*")
                self.end_headers()
                self.wfile.write(bytes(data.read(), "utf-8"))
                data.close()


def start_server(ip: str, port: int):
    print("Server now running")
    server = HTTPServer((ip, port), Server)
    server.serve_forever()
    server.server_close()
    print("Server stopped!")
