import keras
import numpy
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

#신경망은 지도학습
X = numpy.array([0, 1, 2, 3, 4, 5])
Y = X * 2 + 1

model = keras.models.Sequential()
model.add(keras.layers.Dense(1, input_shape=(1,)))
#Dense : 깊이
model.compile(optimizer='SGD', loss='mse', metrics=['accuracy'])

hist = model.fit(X[:2], Y[:2], epochs=1000, verbose=0)

print('Target : ', Y[2:])
print('Prediction : ', model.predict(X[2:]).flatten())
print(model.summary())