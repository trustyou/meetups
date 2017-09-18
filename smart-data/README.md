# spaCy + Keras example

Train a model that predicts hotel review scores just from its titles.

You can find a reduced training set in [titles10k.tsv](titles10k.tsv).

## Installation

```commandline
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
python -m spacy download en
```

## Training

```commandline
python train.py < titles.tsv
```

## Predicting

```commandline
python predict.py
```

… will open an interactive shell where you can type in review titles!