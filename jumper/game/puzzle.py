import random

class Puzzle:
    """The word determiner and keeper of letters. 
    
    The responsibility of puzzle is to choose and keep track of the secret word for the puzzle and provide feedback on guessed letters
    
    Attributes:
        _words_list (list): a list of words to choose from
        _word (string): The word chosen for this round of the game
        _letter_count (int): The length of the secret word
    """

    def __init__(self):
        """Constructs a new puzzle.
        Args:
            self (Puzzle): An instance of Puzzle.
        """
        self._words_list = ["able", "jester", "ridge", "misery", "safety", "stand", "microphone", "suit", "situation", "absolute", "brink", "bathtub", "reception", "organ", "veil", "leftovers", "royalty"]
        self._word = ""
        self._puzzle = ""
        self._select_word()
        self._build_puzzle()

    def _select_word(self):
        self._word = self._words_list[random.randint(0,6)]

    def _build_puzzle(self):
        """Build the intial puzzle with all blanks
        Args:
            self (Puzzle): an instance of the Puzzle
        
        """
        self._puzzle = ["_ "] * len(self._secret_word)

    def update_puzzle(self, jumper_guess):
        """Update the puzzle with users latest guess
        Args:
            self (Puzzle): An instance of Puzzle.
            jumper_guess: a character guessed by the jumper
        
        """
        i=0
        found = True
        valid_guess = False
        while found:
            location = self._word.find(jumper_guess,i)
            if location != -1:
                self._puzzle[location] = jumper_guess + " "
                i = location + 1
                valid_guess = True
            else:
                found = False
        return valid_guess

    def reveal_puzzle(self):
        """Whether or not the hider has been found.
        Args:
            self (puzzle): An instance of Puzzle.
            
        Returns:
            puzzle string: the puzzle list without brackets and commas.
        """
        # for i in range(len(self._puzzle)):
        #     puzzle.append self._puzzle[i]
        return "".join(self._puzzle)
        
    def puzzle_solved(self):
        """Checks to see if the puzzle is solved.
        Args:
            self (puzzle): An instance of Puzzle.
        Returns:
            boolean: True if the puzzle is solved
        """
        test = "_ " not in self._puzzle
        return test