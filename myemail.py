import smtplib
username = #Enter your Gmail_ID in quotes as following
# username =  "abc@gmail.com"
password = #Enter corresponding_password for your mail_id in quotes as following
# password = "Password"
content = 'Intruder Alert !.......Mail sent form Raspberry Pi 3.0 using Python Script)'
mail=smtplib.SMTP('smtp.gmail.com',587)  #Official Port for MSAs is 587 (Extended SMTP) . A variant of port 25 i.e standard SMTP
mail.ehlo() # Tell Server that ESMTP is used instead of standard SMTP 
mail.starttls() #Start Transport Layer Security
mail.login(username,password)
mail.sendmail(username,username,content)
print("Mail Sent")
mail.close()
