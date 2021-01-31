from chessBoard import chessBoard
from random import randint
import Services


class chessGame:

    gameID = 0
    chessBoard = 0
    blackPlayer = ""
    whitePlayer = ""
    completed = False
    winner = ""



    def __init__(self, email, color, size):

        self.gameID = randint(100000, 999999)
        # while not Services.GameService.check_game_id_unused(self.gameID):
        #     self.gameID = randint(100000, 999999)

        self.chessBoard = chessBoard(size)
        if color.lower() == "white":
            self.whitePlayer = email
        elif color.lower() == "black":
            self.blackPlayer = email
        else:
            self.whitePlayer = email

        return

    def __init__(self):
        pass

    def playerJoin(self, email):

        if self.whitePlayer == "":
            self.whitePlayer = email
        elif self.blackPlayer == "":
            self.blackPlayer = email
        else:
            return False

        return True

    def gameEnd(self, playerWin):

        self.completed = True
        self.winner = playerWin

        if playerWin == self.whitePlayer:
            player = "White"
        elif playerWin == self.blackPlayer:
            player = "Black"

        return

    def makeMove(self, email, ID, location):

        player = ""
        if email == self.whitePlayer:
            player = "White"
        elif email == self.blackPlayer:
            player = "Black"
        else:
            return -1

        return self.chessBoard.makeMove(player, ID, location)

    def playerResign(self, email):

        if self.completed:
            return False

        if self.whitePlayer == email:
            self.completed = True
            self.winner = self.blackPlayer
            return True

        elif self.blackPlayer == email:
            self.completed = True
            self.winner = self.whitePlayer
            return True

        return False

    def getGameBoard(self, email):

        player = ""
        if email == self.whitePlayer:
            player = "White"
        elif email == self.blackPlayer:
            player = "Black"
        else:
            return -1

        return [self.chessBoard, self.chessBoard.size, self.chessBoard.whoseTurn, player]

    def todict(self):
        return {'gameID': self.gameID, 'chessBoard': self.chessBoard.todict(), 'blackPlayer': self.blackPlayer, 'whitePlayer': self.whitePlayer, 'completed': self.completed, 'winner': self.winner}

