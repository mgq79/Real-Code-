from Game import Game

class Player(object):

    def __init__(self):
        self.game = Game()

    def play(self):
        while(True): #TODO add a check for game over
            print(self.game.boardString())
            print(self.game.currPlayer + " to move")
            for i in range(len(self.game.moves())):
                print(str(i)+": "+self.game.moves()[i])
            success = False
            while(not success):
                try:
                    response = input()
                    if(response == "exit"):
                        print("bye")
                        return None
                    moveNum = int(response)
                    success = True
                except:
                    print("Please enter a number (or exit)")
            self.game.makeMove(self.game.moves()[moveNum])
            self.game.currPlayer = Game.otherPlayer(self.game.currPlayer)
