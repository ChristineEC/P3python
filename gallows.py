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
        |                The gallows await
       _|_
    __|_|_|__________

    """,
    5:
    """
        ____________
        |  /       |
        | /        O
        |/
        |               Oh, no! Your head
       _|_              is hanging :(
    __|_|_|__________

    """,
    4:
    """
        ____________
        |  /       |
        | /        O
        |/         |
        |
       _|_              Yikes! The body, too!
    __|_|_|__________

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

    """,
    0:
    """
        ____________
        |  /       |
        | /        O
        |/        /|L
        |         / L     Game over! You've been hung :(
       _|_
    __|_|_|__________     Better luck next time!

    """,
   
}