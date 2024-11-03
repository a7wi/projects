import sys
print(sys.version)

if 5 > 2:
  print("Five is greater than two!")

x = "awesome"

def myfunc():
  global x
  x = "fantastic"
  print('Python is ', x)

myfunc()

#print("Python is " + x) 

x = 5j

print(type(x))

#x = int(x)
print(type(x)) 
print(x)

myfunc()



import random

print(random.randrange(1, 10)) 