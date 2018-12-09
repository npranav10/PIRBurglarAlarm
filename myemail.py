import smtplib
content = 'Intruder Alert !.......Mail sent form Raspberry Pi 3.0 using Python Script)'
mail=smtplib.SMTP('smtp.gmail.com',587)
mail.ehlo()
mail.starttls()
mail.login('username','password')
mail.sendmail('username','username',content)
print("Mail Sent")
mail.close()
