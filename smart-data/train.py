import math
import sys
from typing import List

import keras
import numpy
import spacy
from sklearn.metrics import mean_squared_error

from features import get_features


# Model and training parameters
max_length = 16
lstm_units = 16
dropout_rate = 0.1
train_epochs = 3
train_validation_split = 0.1


def train(nlp, texts: List[str], labels: List[float]) -> keras.models.Model:
    """
    :param nlp: spaCy pipeline
    :param texts: List of texts to be used for training
    :param labels: List of review scores, same length as `texts`
    :return: Trained model
    """
    embeddings = get_embeddings(nlp.vocab)
    model = compile_lstm(embeddings)
    train_X = get_features(nlp.pipe(texts), max_length)
    model.fit(train_X, labels, epochs=train_epochs, validation_split=train_validation_split)
    return model


def compile_lstm(embeddings: numpy.ndarray) -> keras.models.Model:
    """
    Build our neural network topology.
    :param embeddings: Word embeddings for first NN layer.
    :return: Untrained Keras model.
    """
    model = keras.models.Sequential()
    model.add(
        keras.layers.Embedding(
            embeddings.shape[0],
            embeddings.shape[1],
            input_length=max_length,
            trainable=False,
            weights=[embeddings],
        )
    )
    model.add(keras.layers.Bidirectional(keras.layers.LSTM(lstm_units)))
    model.add(keras.layers.Dropout(dropout_rate))
    model.add(keras.layers.Dense(1, activation="sigmoid"))
    model.compile(optimizer="adam", loss="mean_squared_error", metrics=["accuracy"])
    return model


def get_embeddings(vocab) -> numpy.ndarray:
    """
    Get embeddings weights for the first NN layer from all English vocabulary.
    :param vocab: English vocabulary, i.e. `nlp.vocab`
    """
    max_rank = max(lex.rank for lex in vocab if lex.has_vector)
    vectors = numpy.ndarray((max_rank+1, vocab.vectors_length), dtype="float32")
    for lex in vocab:
        if lex.has_vector:
            vectors[lex.rank] = lex.vector
    return vectors


if __name__ == "__main__":

    print("Loading spacy …")
    nlp = spacy.load("en")

    print("Loading texts …")
    texts = []
    labels = []
    for line in sys.stdin:
        text, label_str = line.strip().split("\t", 1)
        # Normalize score data to be in [0, 1]
        label = float(label_str) / 100.0
        texts.append(text)
        labels.append(label)

    print("Training model …")
    model = train(nlp, texts, labels)

    holdout = 1000
    score_labels = labels[:holdout]
    score_predict = model.predict(get_features(nlp.pipe(texts[:holdout]), max_length))
    score = math.sqrt(mean_squared_error(score_labels, score_predict))
    print("MSE score on first {} elements: {}".format(holdout, score))

    print("Saving to file!")
    model.save("model.h5")
