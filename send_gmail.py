import smtplib as s

server = s.SMTP('smtp.gmail.com', 587) # 1st arguement is server name and 2nd is port number
server.ehlo() # ehlo method identify the domain name of the sending host to SMTP
server.starttls() # starttls method tells the email server to swith connection from insecure to secure
sender_mail = "Sender Gmail Address"
app_password = "App Password"
sub = input("Subject: ")
body = input("body: ")
receiver_add = input('Receiver Gmail Address: ')
server.login(sender_mail, app_password)
massage = "Subject: {}\n\n{}".format(sub, body)
server.sendmail(sender_mail ,receiver_add, massage)
print('Mail Sent!')
server.quit()



