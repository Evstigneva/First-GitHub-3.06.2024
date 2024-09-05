import tensorflow as tf
from tensorflow.keras import datasets, layers, models
import matplotlib.pyplot as plt

(train_images, train_labels), (test_images, test_labels) = datasets.fashion_mnist.load_data()

plt.figure(figsize=(10,10))
for i in range(25):
    plt.subplot(5,5,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(train_images[i], cmap='Greys')
plt.show()
flattened_train_images = train_images.reshape(60000, 784)
flattened_test_images = test_images.reshape(10000, 784)

m = models.Sequential()
m.add(layers.Dense(512, activation='relu', input_shape=(784,)))
m.add(layers.Dropout(0.1))
m.add(layers.Dense(512, activation='relu'))
m.add(layers.Dropout(0.1))
m.add(layers.Dense(10, activation='softmax'))

m.summary()

m.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

his = m.fit(flattened_train_images, train_labels, epochs=100, 
                    validation_data=(flattened_test_images, test_labels))

plt.plot(his.history['accuracy'], label='accuracy')
plt.plot(his.history['val_accuracy'], label = 'val_accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.ylim([0, 1])
plt.legend(loc='lower right')

test_loss, test_acc = m.evaluate(flattened_test_images,  test_labels, verbose=2)
print(test_acc)
