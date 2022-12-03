from models.RoundModel import RoundModel
from controllers.InputController import InputController
import numpy as np

class RoundController:
    rounds = []
    inputC: InputController

    def __init__(self):
        print('Initialising RoundController class.')
        self.inputC = InputController()
        self.inputC.__init__()

    def load_rounds(self):
        for line in self.inputC.get_marray():
            self.rounds.append(RoundModel(line[0], line[2]))  # Where line[2] is the space
        return self.rounds
