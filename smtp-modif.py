import smtplib
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import json
import getpass

def cargar_credenciales():
    try:
        with open('credenciales.json', 'r') as file:
            credenciales = json.load(file)
            return credenciales['email'], credenciales['password']
    except FileNotFoundError:
        print("El archivo de credenciales no se encontró.")
        exit()

def cargar_contenido():
    try:
        with open('contenido_correo.html', 'r') as file:
            contenido = file.read()
            return contenido
    except FileNotFoundError:
        print("El archivo de contenido del correo no se encontró.")
        exit()

def enviar_correo():
    remitente, password = cargar_credenciales()
    destinatarios = ['destinatario1@example.com', 'destinatario2@example.com']
    contenido = cargar_contenido()

    mensaje = MIMEMultipart()
    mensaje['From'] = remitente
    mensaje['To'] = ', '.join(destinatarios)
    mensaje['Subject'] = 'Mensaje de Prueba desde Python'

    texto = MIMEText(contenido, 'html')
    mensaje.attach(texto)

    # Adjuntar archivo
    with open('archivo_adjunto.pdf', 'rb') as archivo:
        adjunto = MIMEApplication(archivo.read(), _subtype='pdf')
        adjunto.add_header('Content-Disposition', 'attachment', filename='archivo_adjunto.pdf')
    mensaje.attach(adjunto)

    servidor_smtp = smtplib.SMTP('smtp-mail.outlook.com', 587)
    servidor_smtp.starttls()
    servidor_smtp.login(remitente, password)
    servidor_smtp.sendmail(remitente, destinatarios, mensaje.as_string())
    servidor_smtp.quit()

if __name__ == "__main__":
    enviar_correo()
