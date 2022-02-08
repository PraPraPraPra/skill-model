from keras.models import Sequential
from keras.layers import Conv1D, GlobalMaxPooling1D, Embedding, LSTM
from keras.layers.core import Dense, Dropout, Activation
from keras.preprocessing.text import Tokenizer
from keras import metrics, regularizers
from keras.preprocessing import sequence
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelBinarizer


#Load cleaned dataset
data = pd.read_csv('data/ggeop/Cleaned_JobDescs.csv', header = 0, names = ['Query', 'Description'])
#data = pd.read_csv('../../Results/Cleaned_JobsNonIT.csv', header = 0, names = ['Query', 'Description'])

#Split the dataset to Training and Test subsets (90/10)
train, test = train_test_split(data, test_size = 0.1, random_state = 17) #random_state = None

train_descs = train['Description']
train_labels = train['Query']
 
test_descs = test['Description']
test_labels = test['Query']

# Model Parameters
vocab_size = 1000

sequences_length = 1200

embedding_dimensionality = 64 #possibly low??
max_features = 2000 #equal to vocab_size

num_labels = len(train_labels.unique())
batch_size = 32
nb_epoch = 10

nof_filters = 200
kernel_size = 16

hidden_dims = 512

# Convert Texts to Numeric Vectors for Input
tokenizer = Tokenizer(num_words = vocab_size)
tokenizer.fit_on_texts(train_descs)

x_train = tokenizer.texts_to_sequences(train_descs)
x_test = tokenizer.texts_to_sequences(test_descs)

x_train = sequence.pad_sequences(x_train, maxlen = sequences_length, padding = 'post')
x_test = sequence.pad_sequences(x_test, maxlen = sequences_length, padding = 'post')

encoder = LabelBinarizer()
encoder.fit(train_labels)
y_train = encoder.transform(train_labels)
y_test = encoder.transform(test_labels)

model = Sequential()
model.add(Embedding(max_features, embedding_dimensionality, input_length = 1200))
#model.add(LSTM(100, dropout=0.2, recurrent_dropout=0.2))

model.add(Conv1D(nof_filters, kernel_size, padding='valid', activation='relu', strides = 1))
model.add(GlobalMaxPooling1D())

model.add(Dense(hidden_dims))
model.add(Dropout(0.3))
model.add(Activation('relu'))

model.add(Dense(num_labels))
model.add(Activation('softmax'))

model.summary()
model.compile(loss='categorical_crossentropy', optimizer='adam', #'sgd', 'adam', 'RMSprop', 'Adagrad'
                   metrics = [metrics.categorical_accuracy])

history = model.fit(x_train, y_train,
                    batch_size = batch_size,
                    epochs = nb_epoch,
                    verbose = True,
                    validation_split = 0.2)

score = model.evaluate(x_test, y_test, batch_size = batch_size, verbose = True)

model.save('models/ggeop')

 
print('\nTest categorical_crossentropy:', score[0])
print('Categorical accuracy:', score[1])

# summarize history for accuracy
import matplotlib.pyplot as plt

plt.plot(history.history['categorical_accuracy'])
plt.plot(history.history['val_categorical_accuracy'])
plt.title('model accuracy')
plt.ylabel('classification accuracy')
plt.xlabel('epochs')
plt.legend(['train', 'test'], loc='upper left')
plt.show()