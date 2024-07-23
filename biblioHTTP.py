import http.client

# Definir la URL
url = "httpbin.org"

# Realizar una solicitud GET a la URL
conn = http.client.HTTPConnection(url)
conn.request("GET", "/")
respuesta_get = conn.getresponse()

print(f"Respuesta a {url} con GET:")
print(respuesta_get.read().decode())

conn.request("POST", "/", body="key=value", headers={"Content-type": "application/x-www-form-urlencoded"})
respuesta_post = conn.getresponse()

print(f"\nRespuesta a {url} con POST:")
print(respuesta_post.read().decode())


conn.request("PUT", "/", body="key=value", headers={"Content-type": "application/x-www-form-urlencoded"})
respuesta_put = conn.getresponse()

print(f"\nRespuesta a {url} con PUT:")
print(respuesta_put.read().decode())


conn.request("DELETE", "/")
respuesta_delete = conn.getresponse()

print(f"\nRespuesta a {url} con DELETE:")
print(respuesta_delete.read().decode())

# Realizar una solicitud HEAD a la URL base
conn.request("HEAD", "/")
respuesta_head = conn.getresponse()

print(f"\nRespuesta a {url} con HEAD:")
print(respuesta_head.headers)

# Cerrar la conexión
conn.close()
