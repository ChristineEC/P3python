# HANGMAN
Hangman is a python terminal game played in Code Institute's mock terminal in Heroku. 

## How to play the game
The player must guess all of the letters of a word of a given length, chosen at random, before a complete stick-figure body appears below the gallows. Each wrong guess adds a new body part. Each correct guess is displayed in its proper place, with underscores to represent any letters as-yet unguessed. If the player guesses all of the letters, that is, the whole word, before they're hung, they win. Otherwise, well,they're hung and they lose. Either way, they can play again and again, to their heart's delight. In this version, win or lose, when they quit the game, they walk away in one piece with a friendly goodbye.

### UX
### Program goals


### User stories
As a user, I want at the start
- to see the title of the game,
- to be given clear, concise rules and playing instructions, and
- to see a simple graphic representation of the game.

I then want
- to be able to enter my name to receive a friendly, personalized greeting,
- and to be told exactly what I need to do to start the game.

Throughout play, I want
- to be told exactly what kind of input I need to give,
- to be informed when I've given invalid input and what that input was,
- to be given the chance to give new, valid input,
- to have my input repeated back to me, so I know the game is working,
- to be told when I've made a good move or a wrong move,
- to see, both in written and graphic form, the results of my move, and
- to be kept up to date on the progress of the game in terms of what I've guessed so far, both right and wrong, and how many wrong guesses I have left before I lose or how many letters I have left to guess before I win.

Finally, I want
- to be told when the game is over and if I've won or lost,
- to see the whole word displayed at the end of the game, win or lose,
- to be invited to play again or quit, and
- and to be able to play again or receive a friendly goodbye.

I also want an uncluttered terminal and fun but simple (not overwhelming) graphics to keep me interested.

### Developer
As a developer, I want to provide a simple and easy-to-play game that nevertheless provides a new challenge each play. For this reason, I chose to use a list of nearly 3000 words.

I also want to be able to develop the game further, and to this end, for example, I used a google API to import words from a google sheet which can be further modified with columns sorting the currently unsorted list into new columns in any number of ways, such as by word length, word difficulty, words with x's and z's, various themes, etc.

## Features
Immediately upon running, the program removes the default text at the top of the terminal, as it is not part of the game:



## Testing
### Manual testing
### PEP8 linter

## Development

## Bugs


The empty underscores and the message telling the player how many letters were in the word (i.e., length) kept appearing when it was no longer needed. I recoded so that the terminal would clear that text and not bring it up again after the number of guesses was greater than zero.

When the cursor position for player input of a guess was at the bottom of the heroku terminal, it obscured the first underscore of the unguessed word (i.e., in the case where the first letter had not yet been guessed). This was fixed by adding a line space above the user input field.

The script "Running startup command: python3 run.py" remained at the top of the Heroku terminal during game play. To fix this, I call the clear() function to clear it from the terminal once the main function is called.

When the player chose to play another round of the game, the empty gallows were not printed and the game simply displayed the word length and asked for a guess, yielding poor user experience. To improve user experience in this respect, the print statement for printing the empty gallows was moved to the beginning of the main game loop and deleted from the earlier function asking for the player's name. This made it so that the player would still see the gallows immediately after entering their name but would now also see the empty gallows at the beginning of a new game.

While testing the code intended to allow the player to start a new game or exit, it was discovered that the guesses from the round before were still contained in the various game variables such that display_underscores function was showing not only blank underscores for the number of letters in the new word but also the "correct" placement of letters in the new word taken from the "already guessed" group from the previous game. Here is a screenshot of the issue as it appeared for the player:

![Screenshot of the bug](<Bug shot.png>)


### Credits

Many thanks to Code Institute's Marko Tot and Kay Welfare for sharing their hangman projects with me and for their encouragement during weekly standups.

When it came time to make the game more user friendly in terms of clearing unnecessary text from the terminal, I remembered that Marko mentioned a method to do this in his README file. I could see that he used an os method involving 'cls', but I wanted to understand it better before using it. I found some information on [stack overflow](https://stackoverflow.com/questions/63855637/clearing-the-terminal-for-my-python-text-adventure) and then felt I was ready to use the method. However, when I checked back on Marko's GitHub to compare the syntax used, I noticed that his was different. On [Code360 by Coding Ninjas](https://www.naukri.com/code360/library/how-to-clear-a-screen-in-python) I found the explanation I was looking for and decided to use the code as Marko had written it. Many thanks, Marko, for making this piece of code available to me. I later got the idea to us an os method to get the width of the player's terminal from Marko's hangman game in GitHub, which he so kindly shared with me while I was developing this game. I combined this with the code I found at [W3Schools](https://www.w3schools.com/python/trypython.asp?filename=demo_ref_string_center2) for centering the game title in the player's terminal.

I obtained a list of words to use in the game from [Gökhan YAVAŞ](https://github.com/gokhanyavas/Oxford-3000-Word-List), who in turn credits [Oxford Learner's Dictionaries](http://www.oxfordlearnersdictionaries.com/us/wordlist/english/oxford3000/) for a list of 3000 most important words for learners of English, although I weeded out some of the words from the google sheet I copied it to to connect to my program.

