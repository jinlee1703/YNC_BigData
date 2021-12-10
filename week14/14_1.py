import matplotlib.pyplot as plt
from keras.datasets import mnist
from keras import models
from keras import layers
from keras.utils.np_utils import to_categorical


(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# for x in train_images[0]:
#     for i in x:
#         print('{:3}'.format(i), end='')
#     print()
# plt.imshow(train_images[0], cmap='binary')

# 전처리
train_images = train_images.reshape((60000, 28 * 28))
train_images = train_images.astype('float32')/255
test_images = test_images.reshape((10000, 28 * 28))
test_images = test_images.astype('float32')/255

train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

model = models.Sequential()
model.add(layers.Dense(512, activation='relu', input_shape=(28*28,)))
model.add(layers.Dense(10, activation='softmax'))

model.compile(optimizer='rmsprop', loss='categorical_crossentropy',
              metrics=['accuracy'])
hist = model.fit(train_images, train_labels, epochs=20, batch_size=64)
test_loss, test_acc = model.evaluate(test_images, test_labels)
print('test_acc : ', test_acc)
model.summary()