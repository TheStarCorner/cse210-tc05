import random

class Word:

    def __init__(self):
        list_of_words = open('words.txt', 'r').readlines()
        self.actual = list_of_words[random.randint(0,9999)]
        self.guess = [None] * (len(self.actual)-1)
    
    def check_guess(self, letter):
        correct_guess = False
        for i in range(len(self.actual)):
            if letter == self.actual[i]:
                self.guess[i] = letter
                correct_guess = True
        return correct_guess
    
    def print(self):
        for i in self.guess:
            if(i == None):
                i = '_'
            print(i, end = "")
        print('\n')

    def has_won(self):
        for i in self.guess:
            if i == None:
                return False
        return True
    
    def print_actual(self):
        print("\x1b[0;37;41m" + self.actual + "\x1b[0m")