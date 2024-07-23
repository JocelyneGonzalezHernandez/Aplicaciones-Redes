import requests

# Definir la URL
url = "https://httpbin.org"

# Realizar una solicitud GET a la URL
respuesta_get = requests.get(url)

# Verificar si la solicitud GET fue exitosa
if respuesta_get.status_code == 200:
    print("\nSolicitud exitosa!")
elif respuesta_get.status_code == 404:
    print("\nPágina no encontrada.")


print(f"Respuesta a {url} con GET:")
print(respuesta_get.text)

respuesta_post = requests.post(url, data={"key": "value"})
print(f"\nRespuesta a {url} con POST:")
print(respuesta_post.content)

respuesta_put = requests.put(url, data={"key": "value"})
print(f"\nRespuesta a {url} con PUT:")
print(respuesta_put.content)

respuesta_delete = requests.delete(url)
print(f"\nRespuesta a {url} con DELETE:")
print(respuesta_delete.content)

respuesta_head = requests.head(url)
print(f"\nRespuesta a {url} con HEAD:")
print(respuesta_head)

respuesta_patch = requests.patch(url, data={"key": "value"})
print(f"\nRespuesta a {url} con PATCH:")
print(respuesta_patch.content)

respuesta_options = requests.options(url)
print(f"\nRespuesta a {url} con OPTIONS:")
print(respuesta_options.content)



