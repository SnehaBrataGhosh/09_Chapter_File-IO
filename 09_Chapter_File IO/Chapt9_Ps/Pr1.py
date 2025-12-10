import random
def game():
    print("You are playing the game: ")
    soc = random.randint(1, 69)
    with open("HighScore.txt", "r") as j:
        hs = j.read()
        if(hs!=""):
            hs = int(hs)
        else:
            hs = 0
    print(f"Your Score is {soc}")
    if(soc>hs):
        with open("HighScore.txt", "w") as j:
            j.write(str(soc))
    return soc




game()
