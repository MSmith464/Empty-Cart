
import smtplib
import EmptySecrets


with smtplib.SMTP('smtp.gmail.com', 587) as smtp:   #default smtp port is 587
    smtp.ehlo()         #ehlo identifies itself with the mail server. likely is called automatically but using just in case
    smtp.starttls()     #encrypting traffic
    smtp.ehlo()         #reintriduction after encryption

    smtp.login(EmptySecrets.Email_Address, EmptySecrets.Email_Pass)

    subject = 'ABB Cart'
    body = 'ABB cart is ready to order!'

    msg = f'Subject: {subject}\n\n{body}'

    smtp.sendmail(EmptySecrets.Email_Address, EmptySecrets.Receiver, msg)