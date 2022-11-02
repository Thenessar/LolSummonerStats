from database import ConnectionFromPool
from riot_api import RiotAPI
import requests
import uuid


class Summoner:
    def __init__(self, name, region):
        self.name = name
        self.region = region
        self.id = uuid.uuid4()
        self.puuid = ""
        self.accountId = ""
        self.profileIconId = 0
        self.summonerLevel = 0
        self.revisionDate = 0
        self.json = {}

    def get_data(self):
        api = RiotAPI(self.region)
        url = api.get_summoner_by_name(self.name)
        response = requests.get(url).json()

        self.puuid = response["puuid"]
        self.accountId = response["accountId"]
        self.profileIconId = response["profileIconId"]
        self.name = response["name"]
        self.summonerLevel = response["summonerLevel"]
        self.revisionDate = response["revisionDate"]
        self.json = {
            "id": str(self.id),
            "puuid": self.puuid,
            "accountId": self.accountId,
            "profileIconId": self.profileIconId,
            "name": self.name,
            "summonerLevel": self.summonerLevel,
            "revisionDate": self.revisionDate
        }

    def __repr__(self):
        return str(self.json)

    def insert_into_db(self):
        with ConnectionFromPool() as connection:
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO summoners (id, puuid, accountId, profileIconId, name, summonerLevel, "
                               "revisionDate) "
                               "VALUES (%s, %s, %s, %s, %s, %s, %s)",
                               (str(self.id), self.puuid, self.accountId, self.profileIconId, self.name,
                                self.summonerLevel, self.revisionDate)
                               )

    @classmethod
    def check_if_summoner_exists(cls, name):
        with ConnectionFromPool() as connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT 1 FROM summoners WHERE name = %s LIMIT 1", (name,))
                summoner_exists = cursor.fetchone()
                return summoner_exists
