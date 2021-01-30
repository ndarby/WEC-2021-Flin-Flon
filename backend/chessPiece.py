class chessPiece:

    location = (0, 0)
    id = ""
    name = ""
    boardSize = 8

    def __init__(self, location, id, name, size):
        self.location = location
        self.id = id
        self.name = name
        self.boardSize = size
        return

    def pieceType(self):
        return self.name[1]

    def  makeMove(self, position, myLocations, oppLocations):
        return True

    def checkMove(self, toCheck, position, myLocations, oppLocations):

        if position in myLocations:
            return False

        if position in toCheck:
            toCheck.remove(position)
        mineSafe = not any(check in myLocations for check in toCheck)
        oppSafe = not any(check in oppLocations for check in toCheck)
        return mineSafe and oppSafe



class vanguard (chessPiece):

    def makeMove(self, position, myLocations, oppLocations):
        # Check if position fits inside definition of piece

        toCheck = []

        lowX = min(position[0], self.location[0])
        lowY = min(position[1], self.location[1])
        maxX = max(position[0], self.location[0])
        maxY = max(position[1], self.location[1])

        if (maxY - lowY) > (maxX - lowX):
            # Vertical Long
            toCheck = [(self.location[0], y) for y in range(lowY, maxY)]
        elif (maxX - lowX) > (maxY - lowY):
            toCheck = [(self.location[1]) for x in range(lowX, maxX)]
            # Horizontal Long
        else:
            return False

        return self.checkMove(toCheck, position, myLocations, oppLocations)



class pawn (chessPiece):

    def makeMove(self, position, myLocations, oppLocations):
        # Check if position fits inside definition of piece
        toCheck = []

        if abs(position[1] - self.location[1]) > 3:
            return False

        if "w" in self.name:
            # White
            toCheck = [(position[0], self.location[1] - n) for n in range(1, self.location[1] - position[1])]

        else:
            # Black
            toCheck = [(position[0], self.location[1] + n) for n in range(1, position[1] - self.location[1])]

        if position[0] == self.location[0]:
            # Straight Line
            if position in oppLocations or position in myLocations:
                return False
            return self.checkMove(toCheck, position, myLocations, oppLocations)

        if (self.location[0], position[1]) not in oppLocations:
            return False

        return self.checkMove(toCheck, position, myLocations, oppLocations)



class bishop (chessPiece):

    def makeMove(self, position, myLocations, oppLocations):
        # Check if position fits inside definition of piece
        toCheck = []

        if abs(self.location[0] - position[0]) == abs(self.location[1] - position[1]):

            startX = 0
            startY = 0

            if position[0] > self.location[0] and position[1] > self.location[1]:
                startX = self.location[0]
                startY = self.location[1]

            elif position[0] < self.location[0] and position[1] < self.location[1]:
                startX = position[0]
                startY = position[1]

            elif position[0] < self.location[0] and position[1] > self.location[1]:
                startX = position[0]
                startY = position[1]

            elif position[0] > self.location[0] and position[1] < self.location[1]:
                startX = self.location[0]
                startY = self.location[1]

            offset = abs(self.location[0] - position[0])

            toCheck = [(startX + off, startY + off) for off in range(0, offset + 1)]

            toCheck.remove(self.location)

            return self.checkMove(toCheck, position, myLocations, oppLocations)

        return False



class knight (chessPiece):

    def makeMove(self, position, myLocations, oppLocations):
        # Check if position fits inside definition of piece
        # Knight can hop
        toCheck = []

        # Is X position same?
        if position[0] == self.location[0]:
            # How far is request move?
            yLength = abs(position[1] - self.location[1])
            return 2 <= yLength <= 4 and (position not in myLocations)

        # Is Y position same?
        if position[1] == self.location[1]:
            # How far is request move?
            xLength = abs(position[0] - self.location[0])
            return 2 <= xLength <= 4 and (position not in myLocations)

        if abs(self.location[0] - position[0]) == abs(self.location[1] - position[1]):

            offset = abs(self.location[0] - position[0])
            return 2 <= offset <= 4 and (position not in myLocations)

        return False



class rook (chessPiece):

    def makeMove(self, position, myLocations, oppLocations):
        # Check if position fits inside definition of piece
        toCheck = []

        if position[0] == self.location[0]:
            # x = x

            low = min(position[1], self.location[1])
            high = max(position[1], self.location[1])

            toCheck = [(position[0], y) for y in range(low, high + 1)]
            toCheck.remove(self.location)

            return self.checkMove(toCheck, position, myLocations, oppLocations)

        if position[1] == self.location[1]:
            # y = y

            low = min(position[0], self.location[0])
            high = max(position[0], self.location[0])

            toCheck = [(x, position[1]) for x in range(low, high + 1)]
            toCheck.remove(self.location)

            return self.checkMove(toCheck, position, myLocations, oppLocations)

        return False



class queen (chessPiece):

    def makeMove(self, position, myLocations, oppLocations):
        # Check if position fits inside definition of piece
        toCheck = []

        if "w" in self.name:
            # White
            if position[1] < (self.boardSize/2):
                return False

        else:
            # Black
            if position[1] >= (self.boardSize / 2):
                return False

        # how do we check if blocked in??

        return self.checkMove([], position, myLocations, oppLocations)



class king(chessPiece):

    def makeMove(self, position, myLocations, oppLocations):
        # Check if position fits inside definition of piece
        toCheck = []

        if position[0] == self.location[0] and abs(position[0] - self.location[0]) == 1:
            return position not in myLocations
        if position[0] == self.location[0] and abs(position[1] - self.location[1]) == 1:
            return position not in myLocations

        if abs(self.location[0] - position[0]) == abs(self.location[1] - position[1]):
            return abs(self.location[0] - position[0]) == 1 and position not in myLocations

        return False

