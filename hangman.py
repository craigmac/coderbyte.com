#! /usr/bin/python

from sys import exit


''' Hangman.py

    Simple one-player hangman game.

'''



# Ask for user input.
# 1. Guess is in the secretword

class gameEngine(object):

    # Set all variables
    SECRETWORD = 'elephant'
    used_letters = ''
    found_list = []
    game_running = True
    pname = ''
    hangman_index = 0
    guess_num = 0
    correct_letters = 0

    HANGMAN = ['''
        --------
        |      |
               |
               |
              *|*
             * | *
            *  |  *
     ====================''', '''
        --------
        |      |
        O      |
               |
              *|*
             * | *
            *  |  *
     ====================''', '''
        --------
        |      |
        O      |
        |      |
              *|*
             * | *
            *  |  *
     ====================''', '''
        --------
        |      |
        O      |
      --|      |
              *|*
             * | *
            *  |  *
     ====================''','''
        --------
        |      |
        O      |
      --|--    |
              *|*
             * | *
            *  |  *
     ====================''', '''
        --------
        |      |
        O      |
      --|--    |
        |     *|*
             * | *
            *  |  *
     ====================''','''
        --------
        |      |
        O      |
      --|--    |
        |     *|*
       /     * | *
            *  |  *
     ====================''','''
        --------
        |      |
        O      |
      --|--    |
        |     *|*
       / \   * | *
            *  |  *
     ===================='''] 

      
    def playAgain(self):
        print 'Thank you for playing Hangman Beta.'
        print 'Would you like to play again?'

        ok_answers = ['yes', 'no']
        ans = raw_input('> ')

        while ans not in ok_answers:
            ans = raw_input('> ')

        if ans == 'yes':
            self.setup()

        elif ans == 'no':
            self.exitGame()

        else:
            print 'Something went wrong in gameEngine.playAgain() method.'
            exit(0)# Close here later.
        

    def lose(self):
        print '\n\nSorry, you have lost.'
        self.playAgain()
        

    def win(self): 
        print '\n\nYou\'ve correctly guessed the secret word!'
        self.playAgain()
        

    def setup(self):
        #Reset variables.
        self.SECRETWORD = 'elephant'
        self.used_letters = ''
        self.found_list = []
        self.game_running = True
        self.pname = ''
        self.hangman_index = 0
        self.guess_num = 0
        self.correct_letters = 0

        # Start game
        self.start()

    def exitGame(self):
        print 'Exiting...'
        exit(1)

    def start(self): # Set up the game
        print '='*50
        print '\t Welcome to Hangman Beta'
        print '\t written by Craig MacEachern'
        print '='*50
        print 'Please enter your name to continue, or (CTRL+C) to exit at any time:'
        pname = raw_input('> ')
        print 'Welcome, %s!' % pname
        print 'Choosing random word...'

        # Write random word function below later!!!
 
        # Create empty spaces for drawing to screen. 
        for i in range(len(self.SECRETWORD)):
            self.found_list.append('__ ')
        
        print 'Done setup.'
        print '+' * 50
        self.main()
        

    def main(self): # Main game loop.

        
        img_counter = 0 # Hangman drawing counter.
        while self.game_running:
            print 'Incorrect letters: [' + self.used_letters + ']'
            print self.HANGMAN[img_counter]
            for e in self.found_list: # Draw to screen found letters.
                print e,
            
            #print 'Guess number: %d' % (guess_num) # Increment this later.

            
            if self.correct_letters == len(self.SECRETWORD): # All letters guessed.
                self.win()
            elif img_counter == (len(self.HANGMAN) - 1): # Last hangman img.
                self.lose()
            else:          
                # Add non-letter check here later!!!
                print '\n'
                ans = raw_input('\nGuess a letter: ')

                # PROBLEM -> We enter 'e' and it draws it to screen
                # then we keep entering 'e' again and again and we somehow win.
                # ANSWER -> Check if ans in found_letters or used_letters already.
                
                if ans in self.SECRETWORD: # Correct guess.
                    count = self.SECRETWORD.count(ans) # No. of times ans found.
                    index = 0
                    self.correct_letters = self.correct_letters + count
                    while count >= 1:
                        index = self.SECRETWORD.find(ans, index)
                        self.found_list[index] = ans + '  '
                        index += 1
                        count -= 1
                else: # Incorrect guess.
                    self.used_letters = self.used_letters + ans + ', '
                    img_counter += 1                       


# Run the game.
hangman = gameEngine()
hangman.setup()

