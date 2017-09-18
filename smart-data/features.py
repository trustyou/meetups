from typing import Iterable

import numpy
from spacy.tokens.doc import Doc


def get_features(docs: Iterable[Doc], max_length: int) -> numpy.array:
    """
    Convert documents into feature vectors.
    :param docs: Iterable of spaCy docs, e.g. as returned by nlp.pipe()
    :param max_length: Only consider the first `max_length` tokens of each document
    :return: Features, i.e. word rank vectors
    """
    docs = list(docs)
    Xs = numpy.zeros((len(docs), max_length), dtype="int32")
    for i, doc in enumerate(docs):
        for j, token in enumerate(doc[:max_length]):
            Xs[i, j] = token.rank if token.has_vector else 0
    return Xs
