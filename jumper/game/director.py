from game.terminal_service import TerminalService
from game.puzzle import Puzzle
from game.jumper import Jumper


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.
    Attributes:
        is_playing (boolean): Whether or not to keep playing.
        puzzle (Puzzle): The game's puzzle which consists of a secret word and the displayed puzzle that shows letter positions and
            correct letters guessed.
        jumper (Jumper): The game's player who is floating to the ground but losing portions of his parachute for each letter that
            is guessed that is wrong
        terminal_service: For getting and displaying information on the terminal.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self._puzzle = Puzzle()
        self._jumper = Jumper()
        self._terminal_service = TerminalService()
        self._is_playing = True
        self._jumper_guess = ""
        self._jumper_level = 0
        
    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self._is_playing:
            self._display_puzzle()
            self._display_jumper()
            self._get_guess()
            self._update()
            self._check_guess()

    def _display_puzzle(self):
        """Shows the puzzle to the user.
        Args:
            self (Director): An instance of Director.       
        """
        self._terminal_service.write_text("")
        self._terminal_service.write_text(self._puzzle.reveal_puzzle())

    def _display_jumper(self):
        """Shows the puzzle to the user.
        Args:
            self (Director): An instance of Director.       
        """
        self._terminal_service.write_text("")
        for i in range(len(self._jumper.parachute)):
            self._terminal_service.write_text(self._jumper.parachute[i])

    def _get_guess(self):
        """Gets the jumpers latest guess.
        Args:
            self (Director): An instance of Director.
        """
        self._jumper_guess = self._terminal_service.read_letter("\nGuess a letter [a-z]: ")
        self._terminal_service.write_text("")
        
    def _update(self):
        """Update the puzzle to see how the jumper is doing with guessing the word.
        Args:
            self (Director): An instance of Director.
        """
        good_guess = self._puzzle.update_puzzle(self._jumper_guess)
        if not good_guess:
            self._jumper.remove_section()
            self._jumper_level += 1
        
    def _check_guess(self):
        """Lets director know if the puzzle has been solved.
        Args:
            self (Director): An instance of Director.
        """
        if self._puzzle.puzzle_solved():
            self._display_jumper()
            self._display_puzzle()
            self._terminal_service.write_text('')
            self._terminal_service.write_text('You win!')
            self._terminal_service.write_text('')
            self._is_playing = False
        else:
            if self._jumper_level == 5:
                self._display_jumper()
                self._display_puzzle()
                self._terminal_service.write_text('')
                self._terminal_service.write_text('No more guesses. Game over!')
                self._terminal_service.write_text('')
                self._is_playing = False