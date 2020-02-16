import smtplib
conn = smtplib.SMTP('smtp.gmail.com',587)
conn.ehlo()
conn.starttls()
conn.login('Enter  sender email here','Enter password here')
conn.sendmail('Sender email','Receiver email','Subject: I sent you this mail via cmd yaay!\n\nHello,\n This is an automated mail.oink oink xD\n\n')
conn.quit()