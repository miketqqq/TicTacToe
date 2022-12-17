<<<<<<< HEAD
import TicTacToe as tic
import random

def game():
    human = tic.Human("o")
    computer = tic.Computer("x")

    ttt = tic.TicTacToe(state=[" "]*9, occupied=set())
        
    checking_dict = {"human_move": random.randint(0,1), "win": False}

    while checking_dict["win"] == False:
        if len(ttt.occupied) == 9:
            return "Draw"

        if checking_dict["human_move"]:
            ttt.placement(human)            
        else:
            ttt.placement(computer)
        ttt.statePrint()
        
        checking_dict["win"] , winplayer = ttt.checkWin()
        if checking_dict["win"]:
            return winplayer + " wins!"

        checking_dict["human_move"] = not checking_dict["human_move"]

if __name__ == "__main__":
    print(game())