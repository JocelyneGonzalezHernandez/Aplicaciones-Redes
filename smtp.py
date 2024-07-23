import smtplib
from email.message import EmailMessage
#Servidor SMTP de Hotmail: smtp-mail.outlook.com
#Servidor SMTP de Gmail: smtp.gmail.com
try:
    servidorSmtp = smtplib.SMTP('smtp-mail.outlook.com', 587)
    servidorSmtp.ehlo()
    servidorSmtp.starttls()
    servidorSmtp.login('optimus.prime84@hotmail.com', 'PutinZelenski22#')
    
    mensaje = EmailMessage()
    mensaje['From'] = 'optimus.prime84@hotmail.com'
    mensaje['To'] = 'p37676@correo.uia.mx'
    mensaje['Subject'] = 'Mensaje de Prueba desde Python de JOCELYNE'
    
    texto = 'Este es el contenido del cuerpo del mensaje'
    mensaje.set_content(texto)
    
    servidorSmtp.sendmail('optimus.prime84@hotmail.com', 'p37676@correo.uia.mx', mensaje.as_string())
    print('Mensaje enviado!')
except smtplib.SMTPException as e:
    print('Error SMTP:', e)
except Exception as e:
    print('Error:', e)
