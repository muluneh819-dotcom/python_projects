
import random
x=9;
user=None;
while user!=x:
 user=int(input("enter the number:"))
 if user>x:
    print("too high.try again")
 elif user<x:
    print("too low.try again")
else:
    print("you got it!")
      