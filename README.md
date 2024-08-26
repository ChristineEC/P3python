# Project 3 : A game of hangman

## Reminders

- Your code must be placed in the `run.py` file
- Your dependencies must be placed in the `requirements.txt` file
- Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

---

Happy coding!

### Development



#### Bugs

The empty underscores and the text telling the player how many letters were in the word (i.e., length) kept appearing when it was no longer needed. I recoded so that the terminal would clear that text and not bring it up again after the number of guesses was greater than zero.

When the cursor position for player input of a guess was at the bottom of the heroku terminal, it obscured the first underscore of the unguessed word (i.e., in the case where the first letter had not yet been guessed). This was fixed by adding a line space above the user input field.

While testing the code intended to allow the player to start a new game or exit, it was discovered that the guesses from the round before were still contained in the various game variables such that display_underscores function was showing not only blank underscores for the number of letters in the word but also the "correct" placement of letters in the new word taken from the "already guessed" group from the previous game. Here is a screenshot of the issue as it appeared for the player:

![Screenshot of the bug](<Bug shot.png>)


### Credits

I learned the code for centering text in the terminal from [W3Schools](https://www.w3schools.com/python/trypython.asp?filename=demo_ref_string_center2).

I got the idea to us an os method to get the width of the player's terminal from Marko's hangman game in GitHub, which he so kindly shared with me while I was developing this game.

When it came time to make the game more user friendly in terms of clearing unnecessary text from the terminal, I remembered that Marko mentioned a method to do this in his README file. I could see that he used an os method involving 'cls', but I wanted to understand it better before using it. I found some information on [stack overflow](https://stackoverflow.com/questions/63855637/clearing-the-terminal-for-my-python-text-adventure) and then felt I was ready to use the method. However, when I checked back on Marko's GitHub to compare the syntax used, I noticed that his was different. On [Code360 by Coding Ninjas](https://www.naukri.com/code360/library/how-to-clear-a-screen-in-python) I found the explanation I was looking for and decided to use the code as Marko had written it. Many thanks, Marko, for making this piece of code available to me.