from chessPiece import *


class chessBoard:

    piecesWhite = []  # Array of Pieces
    piecesBlack = []  # Array of Pieces
    size = 8
    whoseTurn = "White"
    gameID = 0

    # 8 - 16 square

    def __init__(self, size):
        self.size = size
        self.initBoard()
        return

    def initBoard(self):

        if self.size == 8:
            self.initSizeEight()
        elif self.size == 10:
            self.initSizeTen()
        elif self.size == 12:
            self.initSizeTwelve()
        elif self.size == 14:
            self.initSizeFourteen()
        elif self.size == 16:
            self.initSizeSixteen()

        return

    def makeMove(self, player, piece, location):

        if player != self.whoseTurn:
            return False

        if (self.size - 1 < location[0] < 0) or (self.size - 1 < location[1] < 0):
            return False

        pcObj = self.findPiece(piece)
        if pcObj is None:
            return False

        if self.whoseTurn == "White":
            madeMove = pcObj.makeMove(location, self.getWhiteLocations(), self.getBlackLocations())
        else:
            madeMove = pcObj.makeMove(location, self.getBlackLocations(), self.getWhiteLocations())

        if madeMove:
            self.removeByLocation(location)
            pcObj.location = location

            if self.whoseTurn == "White":
                self.whoseTurn = "Black"
            else:
                self.whoseTurn = "White"

        # check for check/mate/draw

        return True

    def isMate(self):
        # isCheck()
        # AND king cannot move - is every valid square around kind in danger
        return

    def isCheck(self):
        # is king targeted?
        return

    def isDraw(self):
        # King not targeted, no valid king or other moves
        return

    def isRepition(self):
        return

    def findPiece(self, piece):

        if self.whoseTurn == "White":

            found = [pc for pc in self.piecesWhite if pc.name == piece]
            if len(found) > 0: return found[0]

        if self.whoseTurn == "Black":

            found = [pc for pc in self.piecesBlack if pc.name == piece]
            if len(found) > 0: return found[0]

        return None

    def getWhiteLocations(self):
        locations = []
        for piece in self.piecesWhite:
            locations.append(piece.location)
        return locations

    def getBlackLocations(self):
        locations = []
        for piece in self.piecesBlack:
            locations.append(piece.location)
        return locations

    def removeByLocation(self, location):

        for pc in self.piecesWhite:
            if pc.location == location:
                self.piecesWhite.remove(pc)
        for pc in self.piecesBlack:
            if pc.location == location:
                self.piecesBlack.remove(pc)

        return

    def printBoard(self):

        board = [[0] * 8 for i in range(8)]

        for piece in self.piecesBlack:
            board[piece.location[1]][piece.location[0]] = piece.pieceType()

        for piece in self.piecesWhite:
            board[piece.location[1]][piece.location[0]] = piece.pieceType().upper()

        out = ""
        for col in board:
            for c in col:
                out += str(c)
            out += "\n"
        print(out)
        return

    def initSizeEight(self):


        # Front Row
        # 8 -> VPPPPPPV
        # 10-> VPPPPPPPPV
        # 12-> VPPPPPPPPPVV
        # 14-> VPPPPPPPPPPPVV
        # 16-> VVPPPPPPPPPPPVVV

        # Back Row
        # 8 -> RKBQKBKR
        # 10-> RKKBQKBKKR
        # 12-> RKKBBQKBBKKR
        # 14-> RRKKBBQKBBKKRR
        # 16-> RRKKBBQQKQBBKKRR

        idCount = 0
        blackFront = [pawn((i, 1), idCount + i, "bp{}".format(i + 1), 8) for i in range(0, 8)]

        blackBack = [
            rook((0, 0), 8, "br1", 8),
            knight((1, 0), 9, "bk1", 8),
            bishop((2, 0), 10, "bb1", 8),
            queen((3, 0), 11, "bq1", 8),
            king((4, 0), 12, "bk1", 8),
            bishop((5, 0), 13, "bb2", 8),
            knight((6, 0), 14, "bk2", 8),
            rook((7, 0), 15, "br2", 8)
        ]

        idCount = 16
        whiteFront = [pawn((i, 6), idCount + i, "wp{}".format(i + 1), 8) for i in range(0, 8)]

        whiteBack = [
            rook((0, 7), 24, "wr1", 8),
            knight((1, 7), 25, "wk1", 8),
            bishop((2, 7), 26, "wwb1", 8),
            queen((3, 7), 27, "wq1", 8),
            king((4, 7), 28, "wk1", 8),
            bishop((5, 7), 29, "wb2", 8),
            knight((6, 7), 30, "wk2", 8),
            rook((7, 7), 31, "wr2", 8)
        ]

        whiteBack.extend(whiteFront)
        self.piecesWhite = whiteBack

        blackBack.extend(blackFront)
        self.piecesBlack = blackBack

        return

    def initSizeTen(self):
        return

    def initSizeTwelve(self):
        return

    def initSizeFourteen(self):
        return

    def initSizeSixteen(self):
        return


if __name__ == '__main__':
    board = chessBoard(8)
    board.printBoard()
    board.makeMove("White", "wp1", (0, 5))
    board.printBoard()
    board.makeMove("Black", "bp1", (0, 4))
    board.printBoard()
    board.makeMove("White", "wp4", (3, 4))
    board.printBoard()
    board.makeMove("Black", "bp2", (1, 4))
    board.printBoard()
    board.makeMove("White", "wp1", (1, 4))
    board.printBoard()
    board.makeMove("Black", "bp1", (0, 6))
    board.printBoard()
    board.makeMove("White", "wr1", (0, 5))
    board.printBoard()
    board.makeMove("White", "wr1", (0, 5))
    board.printBoard()

