# HANGMAN <a name="title"></a>
Hangman is a Python terminal game played in Code Institute's mock terminal in Heroku. 

[Link to the deployed app](https://hangman-p3-91321cd944d0.herokuapp.com/)

## Table of Contents
- [How to play the game](#how-to-play-the-game)
- [Design](#design)
- [User experience](#user-experience)
    - [User stories](#user-stories)
    - [Developer objectives](#developer-objectives)
- [Features](#features)
    - [Game introduction](#game-introduction)
    - [Personal greeting and game start](#personal-greeting-and-game-start)
    - [Validation of user input](#validation-of-user-input)
    - [Game progression](#game-progression)
    - [Game result](#game-result)
    - [Play again](#play-again)
- [Libraries](#libraries)
- [Testing and validation](#testing-and-validation)
    - [Manual testing](#manual-testing)
        - [User input](#user-input)
        - [Game progress](#game-progress)
        - [Browser testing](#browser-testing)
        - [Code validation](#code-validation)
    - [PEP8 linter](#pep8-linter)
- [Bugs](#bugs)
    - [Solved bugs](###solved-bugs)
    - [Unsolved bugs - none](#unsolved-bugs-none)
- [Future features](#future-features)
- [Deployment](#deployment)
- [Credits and Acknowledgements](#credits-and-acknowledgements)

## How to play the game
The player must guess all of the letters of a word of a given length, chosen at random, before a complete stick-figure body appears below the gallows. Each wrong guess adds a new body part. Each correct guess is displayed in its proper place, with underscores to represent any letters as-yet unguessed. If the player guesses all of the letters, that is, the whole word, before they're hung, they win. Otherwise, well, they're hung and they lose. Either way, they can play again and again, to their heart's delight. In this version, win or lose, when they quit the game, they walk away in one piece with a friendly goodbye.

## Design
The design of the game was kept purposefully simple. As a lover of word games, I don't like to be distracted by a lot of busy graphics. I considered adding some ascii art or ascii word art to the project, but I personally find some of it to be so visually overwhelming as to cause atual discomfort, so I chose to cater to those with similar tastes to mine. (That said, I think that the addition of color would be beneficial to the user experience in a new iteration.) One aspect of the design I did feel was important, though, was the hangman art. While the hangman art I created is simple, I feel that the humorous messages that accompany each hangman state definitely enhance the user experience. I also chose to program out the possibility of the game using words of length less than four. I just think there is something inherently boring and pointless and frustrating about playing hangman with a three letter word. Just ask Kay, our facilitator, who got a three-letter word while demonstrating the game to us and used up nearly 10 tries just to get to the end of the round.

## User experience

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
- to be told if I've made a duplicate guess and given the chance to guess again,
- to be told when I've made a good move or a wrong move,
- to see, both in written and graphic form, the results of my move, and
- to be kept up to date on the progress of the game in terms of what I've guessed so far, both right and wrong, and how many wrong guesses I have left before I lose or how many unguessed letters there are left in word.

Finally, I want
- to be told when the game is over and if I've won or lost,
- to see the whole word displayed at the end of the game, win or lose,
- to be invited to play again or quit, and
- and to be able to play again or receive a friendly goodbye.

I also want an uncluttered terminal and fun but simple (not overwhelming) graphics to keep me interested and in good spirits.

### Developer objectives
As a developer, I want to provide a simple and easy-to-play game that nevertheless provides a new challenge each play. For this reason, I chose to use a list of nearly 3000 words.

I also want to be able to develop the game further, and to this end, for example, I used a google API to import words from a google sheet which can be further modified by sorting the currently unsorted list into new columns in any number of ways, such as by word length, word difficulty, words with x's and z's, or by various themes.

## Features
A few seconds after the app is opened in Heroku, the hangman program removes the default text at the top of the terminal, as it is not part of the game:

![The terminal as it first appears:](assets/screenshots/terminal.png)

### Game introduction <a name="feat-intro"></a>
The opening screen then appears, showing the title, a game graphic, and the rules and instructions. The player is invited to start the game by entering their name.

![Intro screen](assets/screenshots/intro.png)

### Personal greeting and game start <a name="feat-start"></a>
After the player enters their name, a new screen appears, welcoming the player by name, showing the empty gallows, telling (and showing with underscores) the player the length of the word they are to guess, and asking the player to enter a letter.

![Welcomeandstart](assets/screenshots/start.png)

### Validation of user input
At every step where the user gives input, that input is validated. The user name and user guesses must consist of letters A-Z. The user can only answer Y or N (upper or lower case) to the question of whether they want to play again. If the player types in any other character, more than one character, or no character at all, the game tells the player that they've given invalid input, what that input was, and asks for the input again until a valid input is received.

![validate name as alphabetic](assets/screenshots/validname.png)


![validate letter input](assets/screenshots/validltr.png)


![validate yes or no](assets/screenshots/validyesorno.png)


In addition, if a player enters a letter they've already guessed, they are informed and invited to choose again.

![validate new guess](assets/screenshots/validnew.png)

### Game progression
Each time the player guesses a new letter, the game tells the player whether it was a right or wrong guess and either displays it in the proper place in the word, if it's a correct guess, or displays a new body part hanging from the gallows, if it's an incorrect guess. In addition, the player is shown all of their guesses so far and, for wrong answers, the new state of the gallows. They are also informed of how many wrong guesses they have left until they are hung. They can see in the printed letters-and-underscores representing the word how many letters they still have to guess (though some underscores may represent the same letter occurring in different places, and that is why the program can't tell them the number of right guesses they need to win.)

![game progress](assets/screenshots/gamefeats.png)

Here are some screenshots of the different states of the gallows that aren't shown elsewhere in the document:

![head and torso hung](assets/screenshots/torso.png)

![one arm hung](assets/screenshots/onearm.png)

![the other arm hung](assets/screenshots/otherarm.png)

![a leg hung](assets/screenshots/soongoner.png)

### Game result
When the player has either guessed all of the letters in the word or run out of body parts to be hung, the game displays the game results and asks the player if they want to play again. The game results look like this:

![Win](assets/screenshots/win.png)


![Lose](assets/screenshots/lost.png)

### Play again
Once the player finishes a round of hangman, eithr winning or losing, they are asked if they want to play again. If they choose to play again, the main play loop is started again and a start screen appears as follows:

![Play again](assets/screenshots/playagain.png)

If the player chooses not to play again, a friendly graphic is displayed, showing a person walking away from the gallows in one piece (just in case they lost their last round!), and the player is given a friendly goodbye and thanks for playing:

![Bye, thanks, and come play again soon](assets/screenshots/byethanks.png)


## Libraries



## Testing and validation

### Manual testing

#### User input
User input was validated through the use of try statements and the raising of exceptions. Several examples of these (or the results of these) can be seen in the features section. See [Validation of user input](#validation-of-user-input).

I manually tested user input validation for guesses by typing in
    - a non-alphabetical character
    - more than one character
    - nothing
For user name, I checked whether all characters input were A-Z.
For player's choice of whether to continue with a new game, I checked for
    - no input
    - any input other than 'y' or 'Y' or 'n' or 'N'

#### Game progress
I played the game many, many times in both the terminal and in the deployed version in Heroku to ensure everything worked as expected:
    - Intro and start screens appeared as expected
    - Player greeted by name
    - Letters guessed were correctly compared to the word, with expected outcome displayed for the player at each stage of the game
    - Wins and losses occurred as expected
    - Play again function worked as expected

#### Browser testing
The live app was tested in the following browsers and worked as expected.
- Chrome
- Firefox
- Microsoft Edge
- Opera
There is a known issue with Safari, and it was not possible to bring up the app in that browser.


#### Code validation
Testing of the code throughout the development process was enabled by the use of print statements in each function, and often between functions, to indicate when the code was running the function and what was being returned. Messages such as "Y is being returned from the while loop" or lines of code such as "print(already_guessed)" or "print(set(word))" were used to determine what was happening with the code at any given point. The print statements were removed only after thorough manual testing of each function.

To make manaual testing more efficient, I often commented out the function for generating a random word and simply set the word variable to a fixed word. I also printed the unguessed word at the beginning of the game during testing to enable me to see that the program was comparing guesses to the word correctly and yielding correct results.

### PEP8 Python linter

Run.py and gallows.py were run through Code Institute's Python linter, both with results "all clear, no errors found."

![PEP8 Python linter for run.py](assets/screenshots/pep8.png)
![PEP8 Python linter for gallows.py](assets/screenshots/pep8hangart.png)

## Bugs
### Solved bugs
**Bug:** The empty underscores and the message telling the player how many letters were in the word (i.e., length) kept appearing when it was no longer needed. 
**Fix:** I recoded so that the terminal would clear that text and not bring it up again after the number of guesses was greater than zero.

**Bug:** When the cursor position for player input of a guess was at the bottom of the heroku terminal, it obscured the first underscore of the unguessed word (i.e., in the case where the first letter had not yet been guessed). 
**Fix:** This was fixed by adding a line space above code/request for player input.

**Bug:** The script "Running startup command: python3 run.py" remained at the top of the Heroku terminal during game play. 
**Fix:** To fix this, I call the clear() function at the top of the main function to clear it from the player terminal.

**Bug:** When the player chose to play another round of the game, the empty gallows were not printed and the game simply displayed the word length and asked for a guess, yielding poor user experience. 
**Fix:** The print statement for printing the empty gallows was moved to the beginning of the main game loop (from the earlier function asking for the player's name). This had no effect on the first round (for the player) but made it so that they would still see the empty gallows at the beginning of a new game.

**Bug:** While testing the code after coding to allow the player to start a new game or exit, it was discovered that the guesses from the round before were still contained in the various game variables such that display_underscores function was showing not only blank underscores for the number of letters in the new word but also the "correct" placement of letters in the new word taken from the "already guessed" group from the previous game.  Here is a screenshot of the issue as it appeared for the player:

![Screenshot of the bug](assets/screenshots/bugshot.png)

**Fix:** This was fixed by placing the global variable 'already_guessed' at the top of the start_game() function, just before the play loop, and by assigning the variable to an emtpy set at the point in the function after a game is won or lost (that is, after the play loop but still within the start_game() function) and before the player can chose to either play again or quit.

### Unsolved bugs - none
The developer is not aware of any unsolved bugs after thorough testing described herein.

## Future features
Some of the features I would like to develop further for this game are as follows:
- Design: add color to the text to enhance user experience
- Word bank: 
    - It would be interesting to sort the words in the currently "unsorted" column into separate columns so the player could choose word length or a specific theme or word difficulty.
    - It would also be interesting to add functionality so that the user could add words, as they are played (at the end of a round of play), to pre-defined columns in the google worksheet, columns which could then be accessed at the beginning of the game as a specific category of play, such as "tricky" or "funny" or variously themed.
- Other game functionality might include the ability to keep score of wins and losses within the game, or to compare scores between players (with data written to and retrieved from the google sheet).

## Deployment


## Credits and Acknowledgements
- Code Institute for teaching me how to code, and specifically for this project, for the Python Essentials module and Love Sandwiches Walkthrough in the LMS.

- Many thanks to Code Institute's Marko Tot and Kay Welfare for sharing their hangman projects with me and for their encouragement during weekly standups. 

- I also want to thank my mentor, Akshat Garg, for providing invaluable direction for and feedback on the project.

- I watched most of the 15-hour long [Harvard CS50’s Introduction to Programming with Python – Full University Course](https://www.youtube.com/watch?v=nLRL_NcnK-4) as a supplement to the Python Essentials module and referred back to it frequently for reminders or refreshers about syntax, while loops, and try-except statements.

- When it came time to make the game more user friendly in terms of clearing unnecessary text from the terminal, I remembered that Marko mentioned a method to do this in his README file. I could see that he used an os method involving 'cls', but I wanted to understand it better before using it. 
    - I found some information on [StackOverflow](https://stackoverflow.com/questions/63855637/clearing-the-terminal-for-my-python-text-adventure) and then felt I was ready to use the method. However, when I checked back on Marko's GitHub to compare the syntax used, I noticed that his was different. To understand why, I looked further. 
    - On [Code360 by Coding Ninjas](https://www.naukri.com/code360/library/how-to-clear-a-screen-in-python) I found the explanation I was looking for and decided to use the code as Marko had written it. Many thanks, Marko, for making this piece of code available to me. I later got the idea to us an os method to get the width of the player's terminal from Marko's hangman game in GitHub, which he so kindly shared with me while I was developing this game. 
    - I combined this with the code I found at [W3Schools](https://www.w3schools.com/python/trypython.asp?filename=demo_ref_string_center2) for centering the game title in the player's terminal. 
    - It was entirely my idea to use the clear command to get rid of that nasty python code at the top of the player terminal.

- I obtained a list of words to use in the game from [Gökhan YAVAŞ](https://github.com/gokhanyavas/Oxford-3000-Word-List), who in turn credits [Oxford Learner's Dictionaries](http://www.oxfordlearnersdictionaries.com/us/wordlist/english/oxford3000/) for a list of 3000 most important words for learners of English, although I weeded out some of the words in the google sheet I copied it to.

- The code `words_list = sum(data, [])` for flattening the list of lists obtained from my google sheet (i.e., a list consisting of each word in a separate list) was obtained from reading numerous entries by different contributors at StackOverflow.

- I made frequent use of [W3Schools](https://www.w3schools.com/) and [Python.org](https://www.python.org/) during development.

- Several YouTube tutorials were of use to me, especially the following:
    - Kylie Ying's [How to Code a Game of Hangman... The EASY Way!!](https://www.youtube.com/watch?v=cJJTnI22IF8)
    - Kite's [How to build HANGMAN with Python in 10 MINUTES](https://www.youtube.com/watch?v=m4nEnsavl6w)

- For deployment instructions I relied on the Love Sandwiches Walkthrough lesson in Code Institute's LMS.

