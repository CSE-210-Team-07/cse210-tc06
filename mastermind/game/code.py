# stores the guess and the number generated for one player
# get the guess , establish x's and o's 
import random 
class code:



    def __init__(self, guess):
        """The class constructor.
        
        
        """
        
        self._guess = guess

    def get_code(self):
        """
        Returns a random int from 1000-9999 
        """
        code = random.randint(1000,9999)

        return code      

    def get_guess(self, guess):
        """Returns the guess given by player.

        
        """
        return self._guess