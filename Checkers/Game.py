import copy

# Base Game Class
# Requirements:
#   moves:
#     returns a list of all valid moves given a board state
#   getStart:
#     starting board state (empty)
#   makeMove:
#     takes a move and a board and returns a new board with the given
#     move applied
#
#

class Game(object):
    #Python doesn't actually have interfaces afaik
    #TODO find out about abstract classes/interfaces in python


    @staticmethod
    def getStart():
        raise Exception("Unimplemented Method: getStart")

    @staticmethod
    def moveToString(move):
        raise Exception("Unimplemented Method: moveToString")

    @staticmethod
    def previewMove(board, move):
        raise Exception("Unimplemented Method: previewMove")

    @staticmethod
    def boardToString(board):
        raise Exception("Unimplemented Method: boardToString")

    def moves(self):
        raise Exception("Unimplemented Method: moves")

    def makeMove(self, move):
        raise Exception("Unimplemented Method: makeMove")


