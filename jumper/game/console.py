
class Console:
    """A code template for a computer console. The responsibility of this 
    class of objects is to manager the user input.
    
    Stereotype:
        Service Provider, Interfacer

    Attributes:
        prompt (string): The prompt to display the chosen letter.
    """
     
    def read(self, prompt):
        """Gets text input from the user through the screen.

        Args: 
            self (Screen): An instance of Screen.
            prompt (string): The prompt to display to the user.

        Returns:
            string: The user's input as text.
        """
        return input(prompt)

    def read_letter(self, prompt):
        """Gets alphabetic input from the user through the screen.

        Args: 
            self (Screen): An instance of Screen.
            prompt (string): The prompt to display to the user.

        Returns:
            string: The user's input as a string.
        """
        return str(input(prompt))
        
    def write(self, text):
        """Displays the given text on the screen. 

        Args: 
            self (Screen): An instance of Screen.
            text (string): The text to display.
        """
        print(text)