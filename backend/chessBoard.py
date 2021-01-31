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
            return False, "Not your turn"

        if (self.size - 1 < location[0] < 0) or (self.size - 1 < location[1] < 0):
            return False, "Invalid location"

        pcObj = self.findPiece(piece)
        if pcObj is None:
            return False, "No Piece Found"

        kMustMove = False
        if self.isCheck(0):
            kMustMove = True

        if self.whoseTurn == "White":
            madeMove = pcObj.makeMove(location, self.getWhiteLocations(), self.getBlackLocations())
            if "q" in pcObj.name:
                if self.whiteQueen < 5:
                    madeMove = False

        else:
            madeMove = pcObj.makeMove(location, self.getBlackLocations(), self.getWhiteLocations())

        if madeMove and kMustMove:
            if self.isCheck(0):
                madeMove = False
                return False, "In check"
        elif madeMove and self.isCheck(0):
            madeMove = False
            return False, "Cannot Move into Check"

        if self.isCheck(0):
            # check if mate
            gameOver = self.isMate()

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

        king = None
        kingLoc = ()
        if self.whoseTurn == "Black":
            king = self.findPiece("bK1")

        elif self.whoseTurn == "White":
            king = self.findPiece('wK1')

        offsets = [-1, 0, 1]
        offsets2 = [1, 0, -1]
        allMoves = [(kingLoc[0] + off, kingLoc[1]) for off in offsets]
        allMoves.extend([(kingLoc[0], kingLoc[1] + off) for off in offsets])
        allMoves.extend([(kingLoc[0] + offsets, kingLoc[1] + offsets2) for i in range(3)])

        oneValid = False
        for move in allMoves:

            if self.size <= move[0] < 0:
                continue
            if self.size <= move[1] < 0:
                continue

            if self.whoseTurn == "Black":
                if king.makeMove(move, self.getBlackLocations(), self.getWhiteLocations()):
                    oneValid = not self.isCheck(move)

            elif self.whoseTurn == "White":
                if king.makeMove(move, self.getBlackLocations(), self.getWhiteLocations()):
                    oneValid = not self.isCheck(move)

        return not oneValid

    def isCheck(self, position):
        # is king targeted?

        # Is our king threatened?
        isThreat = False
        if self.whoseTurn == "Black":

            if position == 0:
                position = self.findPiece("bK1").location

            for piece in self.piecesWhite:
                isThreat = piece.makeMove(position, self.getBlackLocations(), self.getWhiteLocations())

        elif self.whoseTurn == "White":

            if position == 0:
                position = self.findPiece("wK1").location

            for piece in self.piecesBlack:
                isThreat = piece.makeMove(position, self.getWhiteLocations(), self.getBlackLocations())

        # find valid moves?

        # Iterate through opponent pieces, try and makeMove to king square
        # if True, in check

        return isThreat


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
        size = 8
        blackFront = [
            vanguard((0, 1), 0, "bv1", size),
            pawn((1, 1), 1, "bp1", size),
            pawn((2, 1), 2, "bp2", size),
            pawn((3, 1), 3, "bp3", size),
            pawn((4, 1), 4, "bp4", size),
            pawn((5, 1), 5, "bp5", size),
            pawn((6, 1), 6, "bp6", size),
            vanguard((7, 1), 7, "bv2", 8)
        ]

        blackBack = [
            rook((0, 0), 8, "br1", size),
            knight((1, 0), 9, "bk1", size),
            bishop((2, 0), 10, "bb1", size),
            queen((3, 0), 11, "bq1", size),
            king((4, 0), 12, "bK1", size),
            bishop((5, 0), 13, "bb2", size),
            knight((6, 0), 14, "bk2", size),
            rook((7, 0), 15, "br2", 8)
        ]

        whiteFront = [
            vanguard((0, 6), 16, "wv1", size),
            pawn((1, 6), 17, "wp1", size),
            pawn((2, 6), 18, "wp2", size),
            pawn((3, 6), 19, "wp3", size),
            pawn((4, 6), 20, "wp4", size),
            pawn((5, 6), 21, "wp5", size),
            pawn((6, 6), 22, "wp6", size),
            vanguard((7, 6), 23, "wv2", 8)
        ]

        whiteBack = [
            rook((0, 7), 24, "wr1", size),
            knight((1, 7), 25, "wk1", size),
            bishop((2, 7), 26, "wb1", size),
            queen((3, 7), 27, "wq1", size),
            king((4, 7), 28, "wK1", size),
            bishop((5, 7), 29, "wb2", size),
            knight((6, 7), 30, "wk2", size),
            rook((7, 7), 31, "wr2", 8)
        ]

        whiteBack.extend(whiteFront)
        self.piecesWhite = whiteBack

        blackBack.extend(blackFront)
        self.piecesBlack = blackBack

        return

    def initSizeTen(self):

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
        size = 10
        blackFront = [
            vanguard((0, 1), 0, "bv1", size),
            pawn((1, 1), 1, "bp1", size),
            pawn((2, 1), 2, "bp2", size),
            pawn((3, 1), 3, "bp3", size),
            pawn((4, 1), 4, "bp4", size),
            pawn((5, 1), 5, "bp5", size),
            pawn((6, 1), 6, "bp6", size),
            pawn((7, 1), 7, "bp7", size),
            pawn((8, 1), 8, "bp8", size),
            vanguard((7, 1), 9, "bv2", 8)
        ]

        blackBack = [
            rook((0, 0), 10, "br1", size),
            knight((1, 0), 11, "bk1", size),
            knight((2, 0), 12, "bk2", size),
            bishop((3, 0), 13, "bb1", size),
            queen((4, 0), 14, "bq1", size),
            king((5, 0), 15, "bK1", size),
            bishop((6, 0), 16, "bb2", size),
            knight((7, 0), 17, "bk3", size),
            knight((8, 0), 18, "bk4", size),
            rook((9, 0), 19, "br2", 8)
        ]

        whiteFront = [
            vanguard((0, 8), 20, "wv1", size),
            pawn((1, 8), 21, "wp1", size),
            pawn((2, 8), 22, "wp2", size),
            pawn((3, 8), 23, "wp3", size),
            pawn((4, 8), 24, "wp4", size),
            pawn((5, 8), 25, "wp5", size),
            pawn((6, 8), 26, "wp6", size),
            pawn((7, 8), 27, "wp7", size),
            pawn((8, 8), 28, "wp8", size),
            vanguard((7, 8), 29, "wv2", 8)
        ]

        whiteBack = [
            rook((0, 9), 30, "wr1", size),
            knight((1, 9), 31, "wk1", size),
            knight((2, 9), 32, "wk2", size),
            bishop((3, 9), 33, "wb1", size),
            queen((4, 9), 34, "wq1", size),
            king((5, 9), 35, "wK1", size),
            bishop((6, 9), 36, "wb2", size),
            knight((7, 9), 37, "wk3", size),
            knight((8, 9), 38, "wk4", size),
            rook((9, 9), 39, "wr2", 8)
        ]

        whiteBack.extend(whiteFront)
        self.piecesWhite = whiteBack

        blackBack.extend(blackFront)
        self.piecesBlack = blackBack

        return

    def initSizeTwelve(self):

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
        size = 12
        blackFront = [
            vanguard((0, 1), 0, "bv1", size),
            pawn((1, 1), 1, "bp1", size),
            pawn((2, 1), 2, "bp2", size),
            pawn((3, 1), 3, "bp3", size),
            pawn((4, 1), 4, "bp4", size),
            pawn((5, 1), 5, "bp5", size),
            pawn((6, 1), 6, "bp6", size),
            pawn((7, 1), 7, "bp7", size),
            pawn((8, 1), 8, "bp8", size),
            pawn((9, 1), 9, "bp9", size),
            vanguard((10, 1), 10, "bv2", size),
            vanguard((11, 1), 11, "bv3", 8)
        ]

        blackBack = [
            rook((0, 0), 12, "br1", size),
            knight((1, 0), 13, "bk1", size),
            knight((2, 0), 14, "bk2", size),
            bishop((3, 0), 15, "bb1", size),
            bishop((3, 0), 16, "bb2", size),
            queen((4, 0), 17, "bq1", size),
            king((5, 0), 18, "bK1", size),
            bishop((6, 0), 19, "bb3", size),
            bishop((3, 0), 20, "bb4", size),
            knight((7, 0), 21, "bk3", size),
            knight((8, 0), 22, "bk4", size),
            rook((9, 0), 23, "br2", 8)
        ]

        whiteFront = [
            vanguard((0, 10), 24, "wv1", size),
            pawn((1, 10), 25, "wp1", size),
            pawn((2, 10), 26, "wp2", size),
            pawn((3, 10), 27, "wp3", size),
            pawn((4, 10), 28, "wp4", size),
            pawn((5, 10), 29, "wp5", size),
            pawn((6, 10), 30, "wp6", size),
            pawn((7, 10), 31, "wp7", size),
            pawn((8, 10), 32, "wp8", size),
            pawn((9, 10), 33, "wp9", size),
            vanguard((10, 10), 34, "wv2", size),
            vanguard((11, 10), 35, "wv3", 8)
        ]

        whiteBack = [
            rook((0, 11), 36, "wr1", size),
            knight((1, 11), 37, "wk1", size),
            knight((2, 11), 38, "wk1", size),
            bishop((3, 11), 39, "wb1", size),
            bishop((4, 11), 40, "wb2", size),
            queen((5, 11), 41, "wq1", size),
            king((6, 11), 42, "wK1", size),
            bishop((7, 11), 43, "wb3", size),
            bishop((8, 11), 44, "wb4", size),
            knight((9, 11), 45, "wk2", size),
            knight((10, 11), 46, "wk1", size),
            rook((11, 11), 47, "wr2", 8)
        ]

        whiteBack.extend(whiteFront)
        self.piecesWhite = whiteBack

        blackBack.extend(blackFront)
        self.piecesBlack = blackBack

        return

    def initSizeFourteen(self):

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
        size = 14
        blackFront = [
            vanguard((0, 1), 0, "bv1", size),
            pawn((1, 1), 1, "bp1", size),
            pawn((2, 1), 2, "bp2", size),
            pawn((3, 1), 3, "bp3", size),
            pawn((4, 1), 4, "bp4", size),
            pawn((5, 1), 5, "bp5", size),
            pawn((6, 1), 6, "bp6", size),
            pawn((7, 1), 7, "bp7", size),
            pawn((8, 1), 8, "bp8", size),
            pawn((9, 1), 9, "bp9", size),
            pawn((10, 1), 10, "bp10", size),
            pawn((11, 1), 11, "bp11", size),
            vanguard((12, 1), 12, "bv2", size),
            vanguard((13, 1), 13, "bv3", 8)
        ]

        blackBack = [
            rook((0, 0), 14, "br1", size),
            rook((1, 0), 15, "br2", size),
            knight((2, 0), 16, "bk1", size),
            knight((3, 0), 17, "bk2", size),
            bishop((4, 0), 18, "bb1", size),
            bishop((5, 0), 19, "bb2", size),
            queen((6, 0), 20, "bq1", size),
            king((7, 0), 21, "bK1", size),
            bishop((8, 0), 22, "bb3", size),
            bishop((9, 0), 23, "bb4", size),
            knight((10, 0), 24, "bk3", size),
            knight((11, 0), 25, "bk4", size),
            rook((12, 0), 26, "br3", size),
            rook((13, 0), 27, "br4", size),
        ]

        whiteFront = [
            vanguard((0, 12), 28, "wv1", size),
            pawn((1, 12), 29, "wp1", size),
            pawn((2, 12), 30, "wp2", size),
            pawn((3, 12), 31, "wp3", size),
            pawn((4, 12), 32, "wp4", size),
            pawn((5, 12), 33, "wp5", size),
            pawn((6, 12), 34, "wp6", size),
            pawn((7, 12), 35, "wp7", size),
            pawn((8, 12), 36, "wp8", size),
            pawn((9, 12), 37, "wp9", size),
            pawn((10, 12), 38, "wp9", size),
            pawn((11, 12), 39, "wp9", size),
            vanguard((12, 12), 40, "wv2", size),
            vanguard((13, 12), 41, "wv3", 8)
        ]

        whiteBack = [
            rook((0, 13), 42, "wr1", size),
            rook((1, 13), 43, "wr2", size),
            knight((2, 13), 44, "wk1", size),
            knight((3, 13), 45, "wk1", size),
            bishop((4, 13), 46, "wb1", size),
            bishop((5, 13), 47, "wb2", size),
            queen((6, 13), 48, "wq1", size),
            king((7, 13), 49, "wK1", size),
            bishop((8, 13), 50, "wb3", size),
            bishop((9, 13), 51, "wb4", size),
            knight((10, 13), 52, "wk2", size),
            knight((11, 13), 53, "wk1", size),
            rook((12, 13), 54, "wr3", size),
            rook((13, 13), 55, "wr4", 8)
        ]

        whiteBack.extend(whiteFront)
        self.piecesWhite = whiteBack

        blackBack.extend(blackFront)
        self.piecesBlack = blackBack

        return

    def initSizeSixteen(self):

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
        size = 16
        blackFront = [
            vanguard((0, 1), 0, "bv1", size),
            vanguard((1, 1), 1, "bv2", size),
            pawn((2, 1), 2, "bp1", size),
            pawn((3, 1), 3, "bp2", size),
            pawn((4, 1), 4, "bp3", size),
            pawn((5, 1), 5, "bp4", size),
            pawn((6, 1), 6, "bp5", size),
            pawn((7, 1), 7, "bp6", size),
            pawn((8, 1), 8, "bp7", size),
            pawn((9, 1), 9, "bp8", size),
            pawn((10, 1), 10, "bp9", size),
            pawn((11, 1), 11, "bp10", size),
            pawn((12, 1), 12, "bp11", size),
            vanguard((13, 1), 13, "bv3", size),
            vanguard((14, 1), 14, "bv4", size),
            vanguard((15, 1), 15, "bv5", size),
        ]

        blackBack = [
            rook((0, 0), 16, "br1", size),
            rook((1, 0), 17, "br2", size),
            knight((2, 0), 18, "bk1", size),
            knight((3, 0), 19, "bk2", size),
            bishop((4, 0), 20, "bb1", size),
            bishop((5, 0), 21, "bb2", size),
            queen((6, 0), 22, "bq1", size),
            queen((7, 0), 23, "bq2", size),
            king((8, 0), 24, "bK1", size),
            queen((9, 0), 25, "bq3", size),
            bishop((10, 0), 26, "bb3", size),
            bishop((11, 0), 27, "bb4", size),
            knight((12, 0), 28, "bk3", size),
            knight((13, 0), 29, "bk4", size),
            rook((14, 0), 30, "br3", size),
            rook((15, 0), 31, "br4", size),
        ]

        whiteFront = [
            vanguard((0, 14), 32, "wv1", size),
            vanguard((1, 14), 33, "wv2", size),
            pawn((2, 14), 34, "wp1", size),
            pawn((3, 14), 35, "wp2", size),
            pawn((4, 14), 36, "wp3", size),
            pawn((5, 14), 37, "wp4", size),
            pawn((6, 14), 38, "wp5", size),
            pawn((7, 14), 39, "wp6", size),
            pawn((8, 14), 40, "wp7", size),
            pawn((9, 14), 41, "wp8", size),
            pawn((10, 14), 42, "wp9", size),
            pawn((11, 14), 43, "wp9", size),
            pawn((12, 14), 44, "wp9", size),
            vanguard((13, 14), 45, "wv3", size),
            vanguard((14, 14), 46, "wv4", size),
            vanguard((15, 14), 47, "wv5", size),
        ]

        whiteBack = [
            rook((0, 15), 42, "wr1", size),
            rook((1, 15), 43, "wr2", size),
            knight((2, 15), 44, "wk1", size),
            knight((3, 15), 45, "wk1", size),
            bishop((4, 15), 46, "wb1", size),
            bishop((5, 15), 47, "wb2", size),
            queen((6, 15), 48, "wq1", size),
            queen((7, 15), 49, "wq2", size),
            king((8, 15), 50, "wK1", size),
            queen((9, 15), 51, "wq3", size),
            bishop((10, 15), 52, "wb3", size),
            bishop((11, 15), 53, "wb4", size),
            knight((12, 15), 54, "wk2", size),
            knight((13, 15), 55, "wk1", size),
            rook((14, 15), 56, "wr3", size),
            rook((15, 15), 57, "wr4", size)
        ]

        whiteBack.extend(whiteFront)
        self.piecesWhite = whiteBack

        blackBack.extend(blackFront)
        self.piecesBlack = blackBack

        return


if __name__ == '__main__':
    board = chessBoard(8)
    board.printBoard()
    board.makeMove("White", "wp4", (4, 4))
    board.printBoard()
    board.makeMove("Black", "bv1", (4, 4))
    board.printBoard()
    # board.makeMove("White", "wp2", (2, 4))
    # board.printBoard()
    # board.makeMove("Black", "bp2", (2, 2))
    # board.printBoard()
    # board.makeMove("White", "wk1", (3, 5))
    # board.printBoard()
    # board.makeMove("Black", "bp1", (0, 6))
    # board.printBoard()
    # board.makeMove("White", "wr1", (0, 5))
    # board.printBoard()
    # board.makeMove("White", "wr1", (0, 6))
    # board.printBoard()
    # board.makeMove("Black", "bk1", (2, 3))
    # board.printBoard()

