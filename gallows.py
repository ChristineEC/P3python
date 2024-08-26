"""
dictionary for hangman figures
"""

gallows = {
    6:
    """
        ____________
        |  /       |
        | /
        |/
        |                The gallows await!
       _|_
    __|_|_|__________
    """,
    5:
    """
        ____________
        |  /       |
        | /        O
        |/              Oh, no!
        |                 You've lost your head!
       _|_
    __|_|_|__________
    """,
    4:
    """
        ____________
        |  /       |
        | /        O
        |/         |
        |               Yikes!
       _|_                Your torso, too!
    __|_|_|__________
    """,
    3:
    """
        ____________
        |  /       |
        | /        O
        |/        /|
        |                One arm gone!
       _|_
    __|_|_|__________
    """,
    2:
    """
        ____________
        |  /       |
        | /        O
        |/        /|L
        |               There goes the other arm!
       _|_
    __|_|_|__________
    """,
    1:
    """
        ____________
        |  /       |
        | /        O
        |/        /|L     Egads!
        |         /         Careful, you'll
       _|_                    soon be a goner!  
    __|_|_|__________   
    """,
    0:
    """
        ____________
        |  /       |
        | /        O
        |/        /|L     Oh, no!
        |         / L       You've been HUNG!
       _|_
    __|_|_|__________
    """,
    -1:
    """ 

             O
            /|L        You walk free!
            /L
   """,
   -2:
    """ 
        ___________
        |  /      |
        | /                     Come back to 
        |/                        play again soon!
        |               O 
       _|_             /|L
    __|_|_|__________  / L
   """,
}