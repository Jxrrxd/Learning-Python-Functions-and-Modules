import math                     #provide mathematical functions
import random                   #generate random numbers
import datetime                 #allows us to return/manipulate dates & times
import os                       #provides a way of using the operating systems' dependent functions
import sys

print(math.pi)                  #print out the value of pi
print(random.randint(0,100))    #use randint to generate a random number between two values
print(datetime.datetime.now())  #print out the current date & time (the use of .now)
print(os.getcwd)                #print the current working directory - where the file is located on my computer
print(sys.version)              #print out the current version of Python