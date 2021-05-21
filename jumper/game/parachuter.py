class Parachuter:
    """ 
    The class Parachuter keeps track of how many WRONG GUESSES have happened in the game
    Parachuter keeps track of NUM STRINGS and checks if the player HAS_LOST 

    #Sterotype:
    #Information Holder
    
    #Attributes:
    int wrong_guesses
    int num_strings
    #Methods:
    Cut_string()
        Void
    Display()#
        print parachuter
    has_Lost() #
        return true if the have run out of guesses

    """
    def __init__(self):
        """Class constructor. Declares and initializes instance attributes.
        Args: self (Parachuter): An instance of Parachuter.
        """
        self.wrong_Guess = 0

    def cut_string(self):
        self.wrong_Guess += 1

    def display(self):
        #Prints the first image.
        if self.wrong_Guess == 0:
            print(  "  ___  \n"
                    " /___\ \n"
                    " \   / \n"
                    "  \ /  \n"
                    "   0   \n"
                    "  /|\  \n"
                    "  / \  \n"
                    "       \n" 
                    "\n"          
                    "^^^^^^^\n")
        elif self.wrong_Guess == 1:
            print( " /___\ \n"
                   " \   / \n"
                   "  \ /  \n"
                   "   0   \n"
                   "  /|\  \n"
                   "  / \  \n"
                   "       \n" 
                   "\n"          
                   "^^^^^^^\n")
        elif self.wrong_Guess == 2:
            print( " \   / \n"
                   "  \ /  \n"
                   "   0   \n"
                   "  /|\  \n"
                   "  / \  \n"
                   "       \n" 
                   "\n"          
                   "^^^^^^^\n")
        elif self.wrong_Guess == 3:
            print( "  \ /  \n"
                   "   0   \n"
                   "  /|\  \n"
                   "  / \  \n"
                   "       \n" 
                   "\n"          
                   "^^^^^^^\n")
        elif self.wrong_Guess == 4:
            print( "   0   \n"
                   "  /|\  \n"
                   "  / \  \n"
                   "       \n" 
                   "\n"          
                   "^^^^^^^\n")
            print('\x1b[5;31;43m' + "He's in free-fall! One more wrong guess and he's a goner." + '\x1b[0m')
        elif self.wrong_Guess == 5:
            print( "   X   \n"
                   "  /?\  \n"
                   "  / /  \n"
                   "       \n" 
                   "\n"          
                   "^^^^^^^\n")

    def has_lost(self):
        #checks to see if wrongGuess is equal to 5.
        #if = to 5 then game ends.
        #if not then game continues.
        if self.wrong_Guess == 5:
            return True
        else:
            return False