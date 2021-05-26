import random

# TODO: Define the Board class here

class Mastermind:
    
    def __init__(self):
        self._players = []
        self._prepare()

    def to_string(self):
        """
        Prints the players name, guess, and hint

        Returns:
            The printed 'board'
        """
        print("\n---------------------------")
        for i in range(len(self._players)):
            print("Player " + player.get_name + code.guess + ",", end = "")
            print(self.encode(code.get_code,code.get_guess))
        print("\n---------------------------")
    
    def encode(self, code, guess):
        """Generates a hint based on the given code and guess.

        Returns:
            string: A hint in the form [xxxx]
        """ 
        hint = ""
        for index, letter in enumerate(guess):
            if code[index] == letter:
                hint += "x"
            elif letter in code:
                hint += "o"
            else:
                hint += "*"
        return hint

    def _prepare(self):
        numOfPlayers = len(roster.players)
        for i in range(numOfPlayers):
            playerCode = code.get_code
            self._players.append(playerCode)
    