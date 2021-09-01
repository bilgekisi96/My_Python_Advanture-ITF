import smtplib
server=smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
server.login("ozkokener","yavuz1234.")
message="bu bizim mesajımız pythondan gönderdiğim"
server.sendmail("yavuzselimozkok@gmail.com",)
server.quit()
