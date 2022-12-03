from constants import gameconstants
from controllers.TerminalController import TerminalController
from controllers.RoundController import RoundController
from models.PlayerModel import PlayerModel


class GameController:
    terminalC: TerminalController()
    roundC: RoundController()
    running = True
    player1: PlayerModel
    player2: PlayerModel
    rounds = []

    def __init__(self):
        print('Initialising GameController class.')
        self.terminalC = TerminalController()
        self.roundC = RoundController()
        self.player1 = PlayerModel()
        self.player2 = PlayerModel()

    def decide_winner(self, p1, p2):
        if gameconstants.dictionary[p2] == gameconstants.loses_to[gameconstants.dictionary[p1]]:
            self.terminalC.print_line('P2 LOSES WITH ' + str(gameconstants.dictionary[p2]) + ' against ' +
                                      str(gameconstants.dictionary[p1]))
            return self.player1
        elif gameconstants.dictionary[p1] == gameconstants.loses_to[gameconstants.dictionary[p2]]:
            self.terminalC.print_line('P1 LOSES WITH ' + str(gameconstants.dictionary[p1]) + ' against ' +
                                      str(gameconstants.dictionary[p2]))
            return self.player2
        self.terminalC.print_line('draw WITH ' + str(gameconstants.dictionary[p1]) + ' against ' +
                                  str(gameconstants.dictionary[p2]))
        return None

    def mimic(self, p1, p2):
        if gameconstants.dictionary[p2] == 'LOSS':
            return gameconstants.loses_to[gameconstants.dictionary[p1]] # Return weakness of p1 choice
        elif gameconstants.dictionary[p2] == 'DRAW':
            return gameconstants.dictionary[p1]  # Return identical input as that of p1
        else:
            return gameconstants.find_weakness[gameconstants.dictionary[p1]]  # Return strength against p1 choice

    def play_strategy(self):
        self.terminalC.print_line('Game is starting!')
        self.rounds = self.roundC.load_rounds()

        for r in self.rounds:
            # Set choices
            self.player1.choice = r.p1choice

            # Set choice based on input
            self.player2.choice = gameconstants.reverse_dictionary[self.mimic(self.player1.choice, r.p2choice)]

            # Set shape scores
            self.player1.increase_score(gameconstants.dictionary[self.player1.choice])
            self.player2.increase_score(gameconstants.dictionary[self.player2.choice])

            winner = self.decide_winner(r.p1choice, self.player2.choice)

            if winner is None:  # Draw
                self.player1.increase_score(gameconstants.DRAW)
                self.player2.increase_score(gameconstants.DRAW)
            else:
                winner.increase_score(gameconstants.WIN)

        if self.player1.get_score() > self.player2.get_score():
            self.terminalC.print_line('WINNER IS THE ELF WITH A SCORE OF: ' + str(self.player1.get_score())
                                      + ' HUMAN LOST WITH SCORE: ' + str(self.player2.get_score()))
        elif self.player1.get_score() == self.player2.get_score():
            self.terminalC.print_line('DRAW BETWEEN ELF : ' + str(self.player1.get_score()) +
                                      'AND HUMAN: ' + str(self.player2.get_score()))
        else:
            self.terminalC.print_line('WINNER IS THE HUMAN WITH A SCORE OF: ' + str(self.player2.get_score()) +
                                      ' AND ELF: ' + str(self.player1.get_score()))
