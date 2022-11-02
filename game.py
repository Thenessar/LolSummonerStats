from database import ConnectionFromPool
from riot_api import RiotAPI
import requests
import uuid


class Game:
    def __init__(self, matchId, region):
        self.matchId = matchId
        self.id = uuid.uuid4()
        self.region = region
        self.participantsDetails = []
        self.participants = []
        self.gameCreation = 0
        self.gameDuration = 0
        self.gameEndTimestamp = 0
        self.gameMode = ""
        self.gameName = ""
        self.gameStartTimestamp = 0
        self.gameType = ""
        self.gameVersion = ""
        self.mapId = 0
        self.queueId = 0
        self.teamsDetails = []
        self.teams = []
        self.json = {}

    def get_data(self):
        api = RiotAPI(self.region)
        url = api.get_match_by_id(self.matchId)
        response = requests.get(url).json()

        self.participantsDetails = response["info"]["participants"]
        self.participants = response["metadata"]["participants"]
        self.gameCreation = response["info"]["gameCreation"]
        self.gameDuration = response["info"]["gameDuration"]
        self.gameEndTimestamp = response["info"]["gameEndTimestamp"]
        self.gameMode = response["info"]["gameMode"]
        self.gameName = response["info"]["gameName"]
        self.gameStartTimestamp = response["info"]["gameStartTimestamp"]
        self.gameType = response["info"]["gameType"]
        self.gameVersion = response["info"]["gameVersion"]
        self.mapId = response["info"]["mapId"]
        self.queueId = response["info"]["queueId"]
        self.teamsDetails = response["info"]["teams"]

        for team in response["info"]["teams"]:
            self.teams.append(team["teamId"])

        self.json = {
            "id": str(self.id),
            "participants": self.participants,
            "gameCreation": self.gameCreation,
            "gameDuration": self.gameDuration,
            "gameEndTimestamp": self.gameEndTimestamp,
            "gameMode": self.gameMode,
            "gameName": self.gameName,
            "gameStartTimestamp": self.gameStartTimestamp,
            "gameType": self.gameType,
            "gameVersion": self.gameVersion,
            "mapId": self.mapId,
            "queueId": self.queueId,
            "teams": self.teams
        }

    def __repr__(self):
        return str(self.json)

    def insert_into_db(self):
        with ConnectionFromPool() as connection:
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO games (id, participants, gameCreation, gameDuration, gameEndTimestamp, "
                               "gameMode, gameName, gameStartTimestamp, gameType, gameVersion, mapId, queueId, teams) "
                               "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                               (str(self.id), self.participants, self.gameCreation, self.gameDuration,
                                self.gameEndTimestamp, self.gameMode, self.gameName, self.gameStartTimestamp,
                                self.gameType, self.gameVersion, self.mapId, self.queueId, self.teams
                                ))
