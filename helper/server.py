from http.server import HTTPServer, BaseHTTPRequestHandler


class Server(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.flush_headers()
        content_type = self.headers["Accept"].split(',')[0]
        if self.path == '/info':
            if content_type == 'text/html':
                self.send_header("content-type", "text/html")
                self.end_headers()
                self.wfile.write(bytes("<h1>Working</h1>", "utf-8"))
            elif content_type == 'x-json':
                self.send_header("content-type", "x-json")
                self.end_headers()
                self.wfile.write(bytes("<h1>Json</h1>", "utf-8"))
            else:
                self.send_header("content-type", "*/*")
                self.end_headers()
                self.wfile.write(bytes("<h1>Another</h1>", "utf-8"))


def start_server(ip: str, port: int):
    print("Server now running")
    server = HTTPServer((ip, port), Server)
    server.serve_forever()
    server.server_close()
    print("Server stopped!")
