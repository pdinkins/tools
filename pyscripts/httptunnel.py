import http.client

conn = http.client.HTTPSConnection("localhost", 8080)
conn.set_tunnel("www.python.org")
conn.request("HEAD","/index.html")