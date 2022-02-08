from pyexpat import model
from keras import models
from keras.models import Sequential
from keras.layers import Conv1D, GlobalMaxPooling1D, Embedding, LSTM
from keras.layers.core import Dense, Dropout, Activation
from keras.preprocessing.text import Tokenizer
from keras import metrics, regularizers
from keras.preprocessing import sequence
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelBinarizer


model = models.load_model("models/ggeop")

# Model Parameters
vocab_size = 1000

sequences_length = 1200

embedding_dimensionality = 64 #possibly low??
max_features = 2000 #equal to vocab_size

batch_size = 32
nb_epoch = 10

nof_filters = 200
kernel_size = 16

hidden_dims = 512



# Convert Texts to Numeric Vectors for Input

tokenizer = Tokenizer(num_words = vocab_size)
tokenizer.fit_on_texts(["python"])

x_test = tokenizer.texts_to_sequences(["python"])

x_test = sequence.pad_sequences(x_test, maxlen = sequences_length, padding = 'post')



to_predict = np.array(["python", "java"])
print(model.predict(x_test))
