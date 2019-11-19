import numpy as bi

X = bi.random.randint(100, size=(5, 5))
print ("\n","Array X: ", "\n", "\n", X)

mean = bi.mean(X)
scale = bi.std(X)

Z = (X - mean)/scale

print ("\n","Normalized Array Z: ", "\n", "\n", Z)


