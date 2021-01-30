class chessBoard:

    piecesWhite = []  # Array of Pieces
    piecesBlack = []  # Array of Pieces
    size = 0
    whoseTurn = "White"
    gameID = 0

    # 8 - 16 square

    def __init__(self):

        return

    def initBoard(self):
        return

    def makeMove(self, player, piece, location):

        # Check with piece if can make move

        # If player = black
        # but whoseTurn = White
        # Move not possible

        # Is move possible by piece
        # Is move valid on board



        return True

    def isMoveBlocked(self):
        return

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