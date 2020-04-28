import os
import re

def readFile(filename):
    filehandle = open(filename)
    #print(filehandle.read())
    for line in filehandle:
        if re.match("(.*)id(.*)", line):
            print("MATCH")
            print(line)
    filehandle.close()
#Main
fileDir = "testtext.txt"

readFile(fileDir)

