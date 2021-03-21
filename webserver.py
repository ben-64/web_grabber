#!/usr/bin/env python3

import sys
import http.server
import socketserver
import ssl
import os

PORT = 8000

class MyRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        path = os.path.join(os.getcwd(),self.path[1:]) if self.path[0] == "/" else os.path.join(os.getcwd(),self.path)
        if "?" in path:
            path = path[:path.find("?")]
        if not os.path.exists(path):
            with open(self.output,"a") as f:
                f.write(self.path + "\n")
        return http.server.SimpleHTTPRequestHandler.do_GET(self)


class MyServer(socketserver.TCPServer):
    allow_reuse_address = True


def parse_args():
    """ Parse command line arguments """
    import argparse
    parser = argparse.ArgumentParser(description="Tiny webserver")
    parser.add_argument("--cert","-c",metavar="CERTFILE",help="Certfile for HTTPS")
    parser.add_argument("--key","-k",metavar="KEYFILE",help="Keyfile for HTTPS")
    parser.add_argument("--output","-o",metavar="PATH",default="404.txt",help="Output listing for 404 requests")
    return parser.parse_args()

def main():
    args = parse_args()

    if args.cert and not args.key:
        print("keyfile is missing")
        return -1

    MyRequestHandler.output = args.output

    with MyServer(("", PORT), MyRequestHandler) as httpd:
        if args.cert:
            httpd.socket = ssl.wrap_socket(httpd.socket, keyfile=args.key, certfile=args.cert, server_side=True)
        print("serving at port", PORT)
        httpd.serve_forever()


if __name__ == "__main__":
    sys.exit(main())
