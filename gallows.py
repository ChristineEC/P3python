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
    \n

    """,
    5:
    """
        ____________
        |  /       |
        | /        O
        |/
        |               Oh, no! You've lost your head!
       _|_
    __|_|_|__________
    \n

    """,
    4:
    """
        ____________
        |  /       |
        | /        O
        |/         |
        |
       _|_              Yikes! Your torso, too!
    __|_|_|__________
    \n

    """,
    3:
    """
        ____________
        |  /       |
        | /        O
        |/        /|
        |
       _|_               One arm gone!
    __|_|_|__________
    \n

    """,
    2:
    """
        ____________
        |  /       |
        | /        O
        |/        /|L
        |                There goes the other arm!
       _|_
    __|_|_|__________
    \n

    """,
    1:
    """
        ____________
        |  /       |
        | /        O
        |/        /|L
        |         /     Egads!
       _|_
    __|_|_|__________   Guess correctly, or you'll be a goner!
    \n

    """,
    0:
    """
        ____________
        |  /       |
        | /        O
        |/        /|L
        |         / L     Oh, no! You've been hung!
       _|_
    __|_|_|__________

    """,
   
}