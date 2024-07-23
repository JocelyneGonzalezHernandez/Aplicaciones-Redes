import smtplib
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

def enviar_correo():
    remitente = 'te__amo__choi@hotmail.com'
    destinatarios = ['josg289@gmail.com', 'jocelyneg89@gmail.com']  # Lista de destinatarios
    asunto = 'Transferencia pendiente'

    # Cargar contenido del correo desde un archivo
    try:
        with open('p.html', 'r') as file:
            contenido = file.read()
    except FileNotFoundError:
        print("El archivo de contenido del correo no se encontró.")
        return

    mensaje = MIMEMultipart()
    mensaje['From'] = remitente
    mensaje['To'] = ', '.join(destinatarios)
    mensaje['Subject'] = asunto

    # Dar formato al contenido utilizando HTML
    texto = MIMEText(contenido, 'html', _charset='utf-8')
    mensaje.attach(texto)

    # Adjuntar archivo
    try:
        with open('notificacion.pdf', 'rb') as archivo:
            adjunto = MIMEApplication(archivo.read(), _subtype='pdf')
            adjunto.add_header('Content-Disposition', 'attachment', filename='Notificacion-Urgente.pdf')
            mensaje.attach(adjunto)
    except FileNotFoundError:
        print("El archivo adjunto no se encontró.")

    servidor_smtp = smtplib.SMTP('smtp-mail.outlook.com', 587)
    servidor_smtp.starttls()

    try:
        servidor_smtp.login(remitente, 'XXXibgdrgn')  # Inserta tu contraseña aquí
        servidor_smtp.send_message(mensaje)
        print('Mensaje enviado!')
    except smtplib.SMTPAuthenticationError:
        print('Error de autenticación: Contraseña incorrecta.')
    except smtplib.SMTPException as e:
        print('Error SMTP:', e)
    finally:
        servidor_smtp.quit()

if __name__ == "__main__":
    enviar_correo()
