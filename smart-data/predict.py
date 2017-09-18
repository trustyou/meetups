from cmd import Cmd

import keras
import spacy

from features import get_features
from train import max_length


class PredictShell(Cmd):
    """
    Interactive shell to try out a model manually.
    """

    intro = "Predict overall score from review title. Enter empty line to exit."
    prompt = "Enter review title: "

    def __init__(self, nlp, model):
        super().__init__()
        self.nlp = nlp
        self.model = model

    def predict(self, text: str) -> int:
        """
        Predict review score based on review title.
        :param text: Review title
        :return: Predicted score, in [0, 100] range
        """
        doc = self.nlp(text)
        X = get_features([doc], max_length)
        y = self.model.predict(X)
        return int(round(y[0][0] * 100))

    def default(self, text: str):
        """
        Read a line of input from the shell.
        """
        score = self.predict(text)
        print("Review score: ", score)

    def emptyline(self):
        """
        User entered an empty line - let's exit.
        """
        return True


if __name__ == "__main__":

    nlp = spacy.load("en", parser=False, tagger=False, entity=False)
    model = keras.models.load_model("model.h5")

    shell = PredictShell(nlp, model)
    shell.cmdloop()
