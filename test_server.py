import BaseHTTPServer
import ssl


HOST_IP = 'localhost'
PORT = 8080


class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
	def set_headers(self):
		self.send_response(200)
		self.send_header('Content-type', 'text/html')
		self.end_headers()

	def do_GET(self):
		if self.path == '/testserver':
				self.set_headers()
				self.wfile.write('UA Sports. It\'s in the game!')

def run():
	server = BaseHTTPServer.HTTPServer((HOST_IP, PORT), MyHandler)
#	server.socket = ssl.wrap_socket(server.socket, certfile='server.pem', server_side=True)
	server.serve_forever()

if __name__ == '__main__':
	run()




