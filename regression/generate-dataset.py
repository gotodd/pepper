#!/usr/bin/env python3
#2x+5y^2+3z^3=a
#5y+9x^2+4z^4=b

import sklearn
from sklearn.datasets import make_regression
#X, y = make_regression(n_samples=1000, n_features=10, n_informative=5, n_targets=3, random_state=2)
#print(X.shape,y.shape)

f = open("x.txt", "a")
f2 = open("a.txt", "a")

for x in range(1,30):
	for y in range (1,30):
		for z in range (1,30):
			a=2*x+5*pow(y,2)+3*pow(z,3)
			b=5*y+9*pow(x,2)+4*pow(z,4)
			print(x,y,z,file=f)
			print(a,b,file=f2)

f.close()
f2.close()
