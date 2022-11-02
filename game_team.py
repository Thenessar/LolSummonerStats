from database import ConnectionFromPool
import uuid


class GameTeam:
    def __init__(self, gameId, details):
        self.gameId = gameId
        self.team = details
        self.id = uuid.uuid4()
        self.side = ""
        self.firstBaron = 0
        self.firstChampion = 0
        self.firstDragon = 0
        self.firstInhibitor = 0
        self.firstRiftHerald = 0
        self.firstTower = 0
        self.baronKills = 0
        self.championKills = 0
        self.dragonKills = 0
        self.inhibitorKills = 0
        self.riftHeraldKills = 0
        self.towerKills = 0
        self.win = 0
        self.json = {}

    def get_data(self):
        self.firstBaron = self.team["objectives"]["baron"]["first"]
        self.firstChampion = self.team["objectives"]["champion"]["first"]
        self.firstDragon = self.team["objectives"]["dragon"]["first"]
        self.firstInhibitor = self.team["objectives"]["inhibitor"]["first"]
        self.firstRiftHerald = self.team["objectives"]["riftHerald"]["first"]
        self.firstTower = self.team["objectives"]["tower"]["first"]
        self.baronKills = self.team["objectives"]["baron"]["kills"]
        self.championKills = self.team["objectives"]["champion"]["kills"]
        self.dragonKills = self.team["objectives"]["dragon"]["kills"]
        self.inhibitorKills = self.team["objectives"]["inhibitor"]["kills"]
        self.riftHeraldKills = self.team["objectives"]["riftHerald"]["kills"]
        self.towerKills = self.team["objectives"]["tower"]["kills"]
        self.win = self.team["win"]

        if self.team["teamId"] == 100:
            self.side = "blue"
        else:
            self.side = "red"

        self.json = {
            "gameId": self.gameId,
            "id": self.id,
            "side": self.side,
            "firstBaron": self.firstBaron,
            "firstChampion": self.firstChampion,
            "firstDragon": self.firstDragon,
            "firstInhibitor": self.firstInhibitor,
            "firstRiftHerald": self.firstRiftHerald,
            "firstTower": self.firstTower,
            "baronKills": self.baronKills,
            "championKills": self.championKills,
            "dragonKills": self.dragonKills,
            "inhibitorKills": self.inhibitorKills,
            "riftHeraldKills": self.riftHeraldKills,
            "towerKills": self.towerKills,
            "win": self.win
        }

    def __repr__(self):
        return str(self.json)

    def insert_into_db(self):
        with ConnectionFromPool() as connection:
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO game_teams (id, gameId, firstBaron, firstChampion, firstDragon, "
                               "firstInhibitor, firstRiftHerald, firstTower, baronKills, championKills, dragonKills, "
                               "inhibitorKills, riftHeraldKills, towerKills, win, side) "
                               "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                               (str(self.id), str(self.gameId), self.firstBaron, self.firstChampion, self.firstDragon,
                                self.firstInhibitor, self.firstRiftHerald, self.firstTower, self.baronKills,
                                self.championKills, self.dragonKills, self.inhibitorKills, self.riftHeraldKills,
                                self.towerKills, self.win, self.side)
                               )
