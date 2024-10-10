#!/usr/bin/python3

from http.server import HTTPServer
from http.server import BaseHTTPRequestHandler
import json


class CustomHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):

        if self.path == "/":

            self.send_response(200)
            self.send_header("Content-type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write("Hello, this is a simple API!".encode())

        elif self.path == "/data":
            response = {"name": "John", "age": 30, "city": "New York"}

            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()

            responseBody = json.dumps(response)
            self.wfile.write(responseBody.encode('utf-8'))

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write("OK".encode())

        elif self.path == "/info":
            response = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }

            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()

            responseBody = json.dumps(response)
            self.wfile.write(responseBody.encode('utf-8'))

        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write("Endpoint not found".encode())


server_address = ("", 8000)
httpd = HTTPServer(server_address, CustomHTTPRequestHandler)
httpd.serve_forever()
