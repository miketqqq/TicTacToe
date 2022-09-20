import random

class TicTacToe:
    def __init__(self, state, occupied):
        self.state = state
        self.occupied = occupied

    def statePrint(self):
        '''Format the print out style of the board.'''
        output_string = "|"
        for index,symbol in enumerate(self.state):
            output_string += str(symbol) + "|" 
            if index in [2,5]:
                output_string += "\n" + "|"
        print(output_string + "\n")

    def placement(self, player):
        '''Called for each step.'''
        place_number = player.action(self)  # Act according to the nature of the player.
        self.state[place_number] = player.symbol 
        self.occupied.add(place_number)
        return None

    def checkWin(self):
        '''Define the winning status.'''
        winning = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
        for set in winning:
            if self.state[set[0]] == self.state[set[1]] == self.state[set[2]] =="o":
                return True, "Human"
            elif self.state[set[0]] == self.state[set[1]] == self.state[set[2]] =="x":
                return True, "Computer"
        return False, ""

class Player:
    '''Parent class'''
    def __init__(self,symbol):
        self.symbol = symbol
    
class Computer(Player):
    def __init__(self, symbol):
        super().__init__(symbol)

    def action(self, TTTobject):
        '''TTTobject here refers to TicTacToe object'''
        place_number = 4
        while place_number in TTTobject.occupied:
            place_number = random.randint(0,8) 
        return int(place_number)
        
class Human(Player):
    def __init__(self, symbol):
        super().__init__(symbol)
    
    def action(self,TTTobject):        
        validity = True
        while validity:
            input_value = input("Choose a spot (1-9):")
            try:
                place_number = int(input_value)-1
            except ValueError:
                print("Invalid input, choose again.")
                continue

            if place_number in TTTobject.occupied:
                print("Occupied, choose again.")
            else:
                validity = False
                
        return place_number
      
#while not win
#make a move
#update state, occupied
#print the state
#check winner
#switch player