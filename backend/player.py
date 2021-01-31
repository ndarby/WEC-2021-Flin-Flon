class Player:

    email = ""
    screenName = ""
    wins = 0
    losses = 0
    totalGamesPlayed = 0

    def __init__(self, email, screenName):

        self.email = email
        self.screenName = screenName
        self.wins = 0
        self.losses = 0
        self.totalGamesPlayed = 0

        return

    def playerWin(self):

        self.wins += 1
        self.totalGamesPlayed += 1

        return

    def playerLose(self):

        self.losses += 1
        self.totalGamesPlayed += 1

        return

    def changeScreenName(self, newName):

        self.screenName = newName

        return
