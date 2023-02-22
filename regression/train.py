#!/usr/bin/env python3

# use mlp for prediction on multi-output regression
from numpy import asarray
from sklearn.datasets import make_regression
from keras.models import Sequential,load_model
from keras.layers import Dense
from sklearn.model_selection import RepeatedKFold
import numpy as np

# get the dataset
def get_dataset():
	#X, y = make_regression(n_samples=1000, n_features=10, n_informative=5, n_targets=3, random_state=2)
	X=np.loadtxt("x.txt")
	y=np.loadtxt("a.txt")
	return X, y

# get the model
def get_model(n_inputs, n_outputs):
	model = Sequential()
	#relu
	N=60
	model.add(Dense(N, input_dim=n_inputs, kernel_initializer='he_uniform', activation='relu'))
	model.add(Dense(N,  kernel_initializer='he_uniform', activation='relu'))
	model.add(Dense(N,  kernel_initializer='he_uniform', activation='relu'))
	model.add(Dense(N,  kernel_initializer='he_uniform', activation='relu'))
	model.add(Dense(N,  kernel_initializer='he_uniform', activation='relu'))
	model.add(Dense(N,  kernel_initializer='he_uniform', activation='relu'))
	model.add(Dense(n_outputs, kernel_initializer='he_uniform'))
	model.compile(loss='mae', optimizer='adam')
	return model


def calculate(row):
	x,y,z= row
	a=2*x+5*pow(y,2)+3*pow(z,3)
	b=5*y+9*pow(x,2)+4*pow(z,4)
	print("calculated:",a,b)



# load dataset
X, y = get_dataset()
# get model
n_inputs, n_outputs = X.shape[1], y.shape[1]

# fit the model on all data
model = get_model(n_inputs, n_outputs)
model.fit(X, y, verbose=0, epochs=300)
model.save('./model.bin')

## load model
#model = load_model('./model.bin')

# make a prediction for new data
rows = [[22.5,13.5,5.5],[5,6,7],[4,9,20],[20,4,4,]]
for row in rows:
	print(model.predict(asarray([row])))
	calculate(row)

