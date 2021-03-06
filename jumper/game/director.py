from game.console import Console
from game.parachuter import Parachuter
from game.word import Word



class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        console (Console): An instance of the class of objects known as Console.
        keep_playing (boolean): Whether or not the game can continue.
        parachuter (Parachuter): An instance of the class of objects known as Parachuter.
        word (Word): An instance of the class of objects known as Word.
    """
    def __init__(self):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self.console = Console()
        self.parachuter = Parachuter()
        self.keep_playing = True
        self.word = Word()


    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        self.word.print()
        a = 0
        while self.keep_playing:
            self.do_updates(self.get_inputs())
            self.do_outputs()
            if(self.parachuter.has_lost()):
                self.keep_playing = False
                a = 1
            if(self.word.has_won()):
                self.keep_playing = False
                a = 2
        if a == 1:
            print("\x1b[0;37;41m" + "Better luck next time, buddy! The word was: " + "\x1b[0m", end='')
            self.word.print_actual()
        if a == 2:
            print('\x1b[6;30;42m' + "Nice job dude!" + '\x1b[0m')



    def get_inputs(self):
        """Gets the inputs at the beginning of each round of play. 

        Args:
            self (Director): An instance of Director.
        """
        letter = self.console.read_letter("Guess a letter [a-z]: ")
        return letter


    def do_updates(self, letter):
        """Updates the important game information for each round of play. 

        Args:
            self (Director): An instance of Director.
        """
        if not self.word.check_guess(letter):
            self.parachuter.cut_string()



         



    def do_outputs(self):
        """Outputs the important game information for each round of play. 

        Args:
            self (Director): An instance of Director.
        """
        self.word.print()
        self.parachuter.display()

        
    

