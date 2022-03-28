import json
import os, sys
import random

all_swedish_words = None

class Game(object):
    def __init__(self, word_length = 5):
        self.Start_new_game(word_length)

    def Start_new_game(self, word_length = 5):
        with open(os.path.join(sys.path[0], 'svenska-ord.json')) as json_file:
            self.swedish_words = json.load(json_file)
        self.words_in_game = list(filter(lambda x: len(x)==word_length and "-" not in x and " " not in x, self.swedish_words))
        self._word = random.choice(self.words_in_game)
        self.num_guesses = 0

    def Guess(self, word_guess):
        """ Ger gissningen mot det dolda ordet som array lika lång som gissat or. En int för varje gissad bokstav. 
                2 - rätt bokstav på rätt plats
                1 - bokstaven finns i ordet
                0 - bokstaven finns ej i ordet
        """
        self.num_guesses += 1

        if len(word_guess) != len(self._word):
             raise ValueError(f"Felaktig längd på ord. Du gissade \"{word_guess}\". Detta spel är om ord som är {len(self._word)} i längd")

        if word_guess not in self.words_in_game:
             raise ValueError(f"Felaktigt ord. Du gissade \"{word_guess}\" vilket inte är ett ord i ordlistan.")

        result = []
        for i,c in enumerate(word_guess):
            if c == self._word[i]:
                result.append(2)
            elif c in self._word:
                result.append(1)
            else:
                result.append(0)
             
        return result
