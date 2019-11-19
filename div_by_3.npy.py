import numpy as bi

x = bi.arange(1,101,1).reshape(10,10)
y = bi.multiply(x,x)

print("\n","Squares of the First (+) 100 Integers:","\n","\n", y)

z = y[y%3 == 0]

print ("\n","Numbers divisible by 3: ","\n","\n", z)