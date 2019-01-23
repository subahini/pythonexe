# 1. Command Line Arguments
import sys
print("hello world")
po= 1 
arguments=input
def hello_world(input):
 
 arguments= len(sys.argv) - 1

    
while (arguments >= po):  
   print("\"hello, " + sys.argv[po] + "!\"")
   po = po + 1
hello_world(input("enter the name of the person "))
