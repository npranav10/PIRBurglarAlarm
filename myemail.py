import smtplib
username = #Enter_your_Gmail ID
password = #Enter_corresponding_password_for_you_mail_id
content = 'Intruder Alert !.......Mail sent form Raspberry Pi 3.0 using Python Script)'
mail=smtplib.SMTP('smtp.gmail.com',587)  #Official Port for MSAs is 587 (Extended SMTP) . A variant of port 25 i.e standard SMTP
mail.ehlo() # Tell Server that ESMTP is used instead of standard SMTP 
mail.starttls() #Start Transport Layer Security
mail.login(username,password)
mail.sendmail('username','username',content)
print("Mail Sent")
mail.close()
