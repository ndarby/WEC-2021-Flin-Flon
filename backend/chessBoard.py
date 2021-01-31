from chessPiece import *


class chessBoard:

    piecesWhite = []  # Array of Pieces
    piecesBlack = []  # Array of Pieces
    size = 8
    whoseTurn = "White"
    gameID = 0
    whiteQueen = 5
    blackQueen = 5

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
            return False, ""

        if (self.size - 1 < location[0] < 0) or (self.size - 1 < location[1] < 0):
            return False, ""

        pcObj = self.findPiece(piece)
        if pcObj is None:
            return False, ""

        if self.whoseTurn == "White":
            madeMove = pcObj.makeMove(location, self.getWhiteLocations(), self.getBlackLocations())
            if "q" in pcObj.name:
                if self.whiteQueen < 5:
                    madeMove = False

        else:
            madeMove = pcObj.makeMove(location, self.getBlackLocations(), self.getWhiteLocations())

        if madeMove:

            if self.whoseTurn == "White":
                self.whiteQueen += 1
            elif self.whoseTurn == "Black":
                self.blackQueen += 1

            self.removeByLocation(location)
            pcObj.location = location

            if self.whoseTurn == "White":
                self.whoseTurn = "Black"
            else:
                self.whoseTurn = "White"

        # check for check/mate/draw

        return True, ""

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

        blackFront = [
            vanguard((0, 1), 0, "bv1", 8),
            pawn((1, 1), 1, "bp1", 8),
            pawn((2, 1), 2, "bp2", 8),
            pawn((3, 1), 3, "bp3", 8),
            pawn((4, 1), 4, "bp4", 8),
            pawn((5, 1), 5, "bp5", 8),
            pawn((6, 1), 6, "bp6", 8),
            vanguard((7, 1), 7, "bv2", 8)
        ]

        blackBack = [
            rook((0, 0), 8, "br1", 8),
            knight((1, 0), 9, "bk1", 8),
            bishop((2, 0), 10, "bb1", 8),
            queen((3, 0), 11, "bq1", 8),
            king((4, 0), 12, "bK1", 8),
            bishop((5, 0), 13, "bb2", 8),
            knight((6, 0), 14, "bk2", 8),
            rook((7, 0), 15, "br2", 8)
        ]

        whiteFront = [
            vanguard((0, 6), 16, "wv1", 8),
            pawn((1, 6), 17, "wp1", 8),
            pawn((2, 6), 18, "wp2", 8),
            pawn((3, 6), 19, "wp3", 8),
            pawn((4, 6), 20, "wp4", 8),
            pawn((5, 6), 21, "wp5", 8),
            pawn((6, 6), 22, "wp6", 8),
            vanguard((7, 6), 23, "wv2", 8)
        ]

        whiteBack = [
            rook((0, 7), 24, "wr1", 8),
            knight((1, 7), 25, "wk1", 8),
            bishop((2, 7), 26, "wb1", 8),
            queen((3, 7), 27, "wq1", 8),
            king((4, 7), 28, "wK1", 8),
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


# if __name__ == '__main__':
#     board = chessBoard(8)
#     board.printBoard()
#     board.makeMove("White", "wv1", (4, 4))
#     board.printBoard()
#     board.makeMove("Black", "bv1", (4, 4))
#     board.printBoard()
#     board.makeMove("White", "wv2", (4, 4))
#     board.printBoard()
#     board.makeMove("Black", "bv2", (4, 4))
#     board.printBoard()
    # board.makeMove("White", "wp1", (1, 4))
    # board.printBoard()
    # board.makeMove("Black", "bp1", (0, 6))
    # board.printBoard()
    # board.makeMove("White", "wr1", (0, 5))
    # board.printBoard()
    # board.makeMove("White", "wr1", (0, 6))
    # board.printBoard()
    # board.makeMove("Black", "bk1", (2, 3))
    # board.printBoard()

