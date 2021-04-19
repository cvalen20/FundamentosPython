# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 10:42:10 2021

@author: Camilo
"""

import smtplib

from credenciales import usuario, clave


#datos del correo
desde = 'cvalen20@gmail.com'
para = [ 'cvalen20@gmail.com', 'linagonza89@gmail.com', 'backupnotreply01@gmail.com' ]
asunto = 'Asunto cualquiera'
cuerpo = 'Hola, esto es una prueba'

#se ensambla el correo
email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (desde, ", ".join(para), asunto, cuerpo)


#conexión al servidor de gmail

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.ehlo()
server.login( usuario, clave )
server.sendmail(desde, para, email_text)
server.close()