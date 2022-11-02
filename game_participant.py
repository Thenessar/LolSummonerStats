from database import ConnectionFromPool
import uuid


class GameParticipant:
    def __init__(self, gameTeamId, details):
        self.id = uuid.uuid4()
        self.gameTeamId = gameTeamId
        self.details = details
        self.puuid = ""
        self.assists = 0
        self.baronKills = 0
        self.bountyLevel = 0
        self.challengesDetails = self.details["challenges"]
        self.champExperience = 0
        self.champLevel = 0
        self.championId = 0
        self.championName = ""
        self.championTransform = 0
        self.consumablesPurchased = 0
        self.damageDealtToBuildings = 0
        self.damageDealtToObjectives = 0
        self.damageDealtToTurrets = 0
        self.damageSelfMitigated = 0
        self.deaths = 0
        self.detectorWardsPlaced = 0
        self.doubleKills = 0
        self.dragonKills = 0
        self.firstBloodAssist = 0
        self.firstBloodKill = 0
        self.firstTowerAssist = 0
        self.firstTowerKill = 0
        self.gameEndedInEarlySurrender = 0
        self.gameEndedInSurrender = 0
        self.goldEarned = 0
        self.goldSpent = 0
        self.individualPosition = 0
        self.inhibitorKills = 0
        self.inhibitorTakedowns = 0
        self.inhibitorsLost = 0
        self.item0 = 0
        self.item1 = 0
        self.item2 = 0
        self.item3 = 0
        self.item4 = 0
        self.item5 = 0
        self.item6 = 0
        self.itemsPurchased = 0
        self.killingSprees = 0
        self.kills = 0
        self.lane = ""
        self.largestCriticalStrike = 0
        self.largestKillingSpree = 0
        self.largestMultiKill = 0
        self.longestTimeSpentLiving = 0
        self.magicDamageDealt = 0
        self.magicDamageDealtToChampions = 0
        self.magicDamageTaken = 0
        self.neutralMinionsKilled = 0
        self.nexusKills = 0
        self.nexusTakedowns = 0
        self.nexusLost = 0
        self.objectivesStolen = 0
        self.objectivesStolenAssists = 0
        self.participantId = 0
        self.pentaKills = 0
        self.physicalDamageDealt = 0
        self.physicalDamageDealtToChampions = 0
        self.physicalDamageTaken = 0
        self.profileIcon = 0
        self.quadraKills = 0
        self.riotIdName = ""
        self.riotIdTagline = ""
        self.role = ""
        self.sightWardsBoughtInGame = 0
        self.spell1Casts = 0
        self.spell2Casts = 0
        self.spell3Casts = 0
        self.spell4Casts = 0
        self.summoner1Casts = 0
        self.summoner1Id = 0
        self.summoner2Casts = 0
        self.summoner2Id = 0
        self.summonerId = ""
        self.summonerLevel = 0
        self.summonerName = ""
        self.teamEarlySurrendered = ""
        self.teamId = 0
        self.teamPosition = ""
        self.timeCCingOthers = 0
        self.timePlayed = 0
        self.totalDamageDealt = 0
        self.totalDamageDealtToChampions = 0
        self.totalDamageShieldedOnTeammates = 0
        self.totalDamageTaken = 0
        self.totalHeal = 0
        self.totalHealsOnTeammates = 0
        self.totalMinionsKilled = 0
        self.totalTimeCCDealt = 0
        self.totalTimeSpentDead = 0
        self.totalUnitsHealed = 0
        self.tripleKills = 0
        self.trueDamageDealt = 0
        self.trueDamageDealtToChampions = 0
        self.trueDamageTaken = 0
        self.turretKills = 0
        self.turretTakedowns = 0
        self.turretsLost = 0
        self.unrealKills = 0
        self.visionScore = 0
        self.visionWardsBoughtInGame = 0
        self.wardsKilled = 0
        self.wardsPlaced = 0
        self.win = ""
        self.json = {}

    def get_data(self):
        self.puuid = self.details["puuid"]
        self.assists = self.details["assists"]
        self.baronKills = self.details["baronKills"]
        self.bountyLevel = self.details["bountyLevel"]
        self.champExperience = self.details["champExperience"]
        self.champLevel = self.details["champLevel"]
        self.championId = self.details["championId"]
        self.championName = self.details["championName"]
        self.championTransform = self.details["championTransform"]
        self.consumablesPurchased = self.details["consumablesPurchased"]
        self.damageDealtToBuildings = self.details["damageDealtToBuildings"]
        self.damageDealtToObjectives = self.details["damageDealtToObjectives"]
        self.damageDealtToTurrets = self.details["damageDealtToTurrets"]
        self.damageSelfMitigated = self.details["damageSelfMitigated"]
        self.deaths = self.details["deaths"]
        self.detectorWardsPlaced = self.details["detectorWardsPlaced"]
        self.doubleKills = self.details["doubleKills"]
        self.dragonKills = self.details["dragonKills"]
        self.firstBloodAssist = self.details["firstBloodAssist"]
        self.firstBloodKill = self.details["firstBloodKill"]
        self.firstTowerAssist = self.details["firstTowerAssist"]
        self.firstTowerKill = self.details["firstTowerKill"]
        self.gameEndedInEarlySurrender = self.details["gameEndedInEarlySurrender"]
        self.gameEndedInSurrender = self.details["gameEndedInSurrender"]
        self.goldEarned = self.details["goldEarned"]
        self.goldSpent = self.details["goldSpent"]
        self.individualPosition = self.details["individualPosition"]
        self.inhibitorKills = self.details["inhibitorKills"]
        self.inhibitorTakedowns = self.details["inhibitorTakedowns"]
        self.inhibitorsLost = self.details["inhibitorsLost"]
        self.item0 = self.details["item0"]
        self.item1 = self.details["item1"]
        self.item2 = self.details["item2"]
        self.item3 = self.details["item3"]
        self.item4 = self.details["item4"]
        self.item5 = self.details["item5"]
        self.item6 = self.details["item6"]
        self.itemsPurchased = self.details["itemsPurchased"]
        self.killingSprees = self.details["killingSprees"]
        self.kills = self.details["kills"]
        self.lane = self.details["lane"]
        self.largestCriticalStrike = self.details["largestCriticalStrike"]
        self.largestKillingSpree = self.details["largestKillingSpree"]
        self.largestMultiKill = self.details["largestMultiKill"]
        self.longestTimeSpentLiving = self.details["longestTimeSpentLiving"]
        self.magicDamageDealt = self.details["magicDamageDealt"]
        self.magicDamageDealtToChampions = self.details["magicDamageDealtToChampions"]
        self.magicDamageTaken = self.details["magicDamageTaken"]
        self.neutralMinionsKilled = self.details["neutralMinionsKilled"]
        self.nexusKills = self.details["nexusKills"]
        self.nexusTakedowns = self.details["nexusTakedowns"]
        self.nexusLost = self.details["nexusLost"]
        self.objectivesStolen = self.details["objectivesStolen"]
        self.objectivesStolenAssists = self.details["objectivesStolenAssists"]
        self.participantId = self.details["participantId"]
        self.pentaKills = self.details["pentaKills"]
        self.physicalDamageDealt = self.details["physicalDamageDealt"]
        self.physicalDamageDealtToChampions = self.details["physicalDamageDealtToChampions"]
        self.physicalDamageTaken = self.details["physicalDamageTaken"]
        self.profileIcon = self.details["profileIcon"]
        self.quadraKills = self.details["quadraKills"]
        self.riotIdName = self.details["riotIdName"]
        self.riotIdTagline = self.details["riotIdTagline"]
        self.role = self.details["role"]
        self.sightWardsBoughtInGame = self.details["sightWardsBoughtInGame"]
        self.spell1Casts = self.details["spell1Casts"]
        self.spell2Casts = self.details["spell2Casts"]
        self.spell3Casts = self.details["spell3Casts"]
        self.spell4Casts = self.details["spell4Casts"]
        self.summoner1Casts = self.details["summoner1Casts"]
        self.summoner1Id = self.details["summoner1Id"]
        self.summoner2Casts = self.details["summoner2Casts"]
        self.summoner2Id = self.details["summoner2Id"]
        self.summonerLevel = self.details["summonerLevel"]
        self.summonerName = self.details["summonerName"]
        self.summonerId = GameParticipant.get_summoner_id_from_puuid(self.puuid)
        self.teamEarlySurrendered = self.details["teamEarlySurrendered"]
        self.teamId = self.details["teamId"]
        self.teamPosition = self.details["teamPosition"]
        self.timeCCingOthers = self.details["timeCCingOthers"]
        self.timePlayed = self.details["timePlayed"]
        self.totalDamageDealt = self.details["totalDamageDealt"]
        self.totalDamageDealtToChampions = self.details["totalDamageDealtToChampions"]
        self.totalDamageShieldedOnTeammates = self.details["totalDamageShieldedOnTeammates"]
        self.totalDamageTaken = self.details["totalDamageTaken"]
        self.totalHeal = self.details["totalHeal"]
        self.totalHealsOnTeammates = self.details["totalHealsOnTeammates"]
        self.totalMinionsKilled = self.details["totalMinionsKilled"]
        self.totalTimeCCDealt = self.details["totalTimeCCDealt"]
        self.totalTimeSpentDead = self.details["totalTimeSpentDead"]
        self.totalUnitsHealed = self.details["totalUnitsHealed"]
        self.tripleKills = self.details["tripleKills"]
        self.trueDamageDealt = self.details["trueDamageDealt"]
        self.trueDamageDealtToChampions = self.details["trueDamageDealtToChampions"]
        self.trueDamageTaken = self.details["trueDamageTaken"]
        self.turretKills = self.details["turretKills"]
        self.turretTakedowns = self.details["turretTakedowns"]
        self.turretsLost = self.details["turretsLost"]
        self.unrealKills = self.details["unrealKills"]
        self.visionScore = self.details["visionScore"]
        self.visionWardsBoughtInGame = self.details["visionWardsBoughtInGame"]
        self.wardsKilled = self.details["wardsKilled"]
        self.wardsPlaced = self.details["wardsPlaced"]
        self.win = self.details["win"]
        self.json = {
            "id": str(self.id),
            "gameTeamId": str(self.gameTeamId),
            "puuid": self.puuid,
            "assists": self.assists,
            "baronKills": self.baronKills,
            "bountyLevel": self.bountyLevel,
            "champExperience": self.champExperience,
            "champLevel": self.champLevel,
            "championId": self.championId,
            "championName": self.championName,
            "championTransform": self.championTransform,
            "consumablesPurchased": self.consumablesPurchased,
            "damageDealtToBuildings": self.damageDealtToBuildings,
            "damageDealtToObjectives": self.damageDealtToObjectives,
            "damageDealtToTurrets": self.damageDealtToTurrets,
            "damageSelfMitigated": self.damageSelfMitigated,
            "deaths": self.deaths,
            "detectorWardsPlaced": self.detectorWardsPlaced,
            "doubleKills": self.doubleKills,
            "dragonKills": self.dragonKills,
            "firstBloodAssist": self.firstBloodAssist,
            "firstBloodKill": self.firstBloodKill,
            "firstTowerAssist": self.firstTowerAssist,
            "firstTowerKill": self.firstTowerKill,
            "gameEndedInEarlySurrender": self.gameEndedInEarlySurrender,
            "gameEndedInSurrender": self.gameEndedInSurrender,
            "goldEarned": self.goldEarned,
            "goldSpent": self.goldSpent,
            "individualPosition": self.individualPosition,
            "inhibitorKills": self.inhibitorKills,
            "inhibitorTakedowns": self.inhibitorTakedowns,
            "inhibitorsLost": self.inhibitorsLost,
            "item0": self.item0,
            "item1": self.item1,
            "item2": self.item2,
            "item3": self.item3,
            "item4": self.item4,
            "item5": self.item5,
            "item6": self.item6,
            "itemsPurchased": self.itemsPurchased,
            "killingSprees": self.killingSprees,
            "kills": self.kills,
            "lane": self.lane,
            "largestCriticalStrike": self.largestCriticalStrike,
            "largestKillingSpree": self.largestKillingSpree,
            "largestMultiKill": self.largestMultiKill,
            "longestTimeSpentLiving": self.longestTimeSpentLiving,
            "magicDamageDealt": self.magicDamageDealt,
            "magicDamageDealtToChampions": self.magicDamageDealtToChampions,
            "magicDamageTaken": self.magicDamageTaken,
            "neutralMinionsKilled": self.neutralMinionsKilled,
            "nexusKills": self.nexusKills,
            "nexusTakedowns": self.nexusTakedowns,
            "nexusLost": self.nexusLost,
            "objectivesStolen": self.objectivesStolen,
            "objectivesStolenAssists": self.objectivesStolenAssists,
            "participantId": self.participantId,
            "pentaKills": self.pentaKills,
            "physicalDamageDealt": self.physicalDamageDealt,
            "physicalDamageDealtToChampions": self.physicalDamageDealtToChampions,
            "physicalDamageTaken": self.physicalDamageTaken,
            "profileIcon": self.profileIcon,
            "quadraKills": self.quadraKills,
            "riotIdName": self.riotIdName,
            "riotIdTagline": self.riotIdTagline,
            "role": self.role,
            "sightWardsBoughtInGame": self.sightWardsBoughtInGame,
            "spell1Casts": self.spell1Casts,
            "spell2Casts": self.spell2Casts,
            "spell3Casts": self.spell3Casts,
            "spell4Casts": self.spell4Casts,
            "summoner1Casts": self.summoner1Casts,
            "summoner1Id": self.summoner1Id,
            "summoner2Casts": self.summoner2Casts,
            "summoner2Id": self.summoner2Id,
            "summonerId": str(self.summonerId),
            "summonerLevel": self.summonerLevel,
            "summonerName": self.summonerName,
            "teamEarlySurrendered": self.teamEarlySurrendered,
            "teamId": self.teamId,
            "teamPosition": self.teamPosition,
            "timeCCingOthers": self.timeCCingOthers,
            "timePlayed": self.timePlayed,
            "totalDamageDealt": self.totalDamageDealt,
            "totalDamageDealtToChampions": self.totalDamageDealtToChampions,
            "totalDamageShieldedOnTeammates": self.totalDamageShieldedOnTeammates,
            "totalDamageTaken": self.totalDamageTaken,
            "totalHeal": self.totalHeal,
            "totalHealsOnTeammates": self.totalHealsOnTeammates,
            "totalMinionsKilled": self.totalMinionsKilled,
            "totalTimeCCDealt": self.totalTimeCCDealt,
            "totalTimeSpentDead": self.totalTimeSpentDead,
            "totalUnitsHealed": self.totalUnitsHealed,
            "tripleKills": self.tripleKills,
            "trueDamageDealt": self.trueDamageDealt,
            "trueDamageDealtToChampions": self.trueDamageDealtToChampions,
            "trueDamageTaken": self.trueDamageTaken,
            "turretKills": self.turretKills,
            "turretTakedowns": self.turretTakedowns,
            "turretsLost": self.turretsLost,
            "unrealKills": self.unrealKills,
            "visionScore": self.visionScore,
            "visionWardsBoughtInGame": self.visionWardsBoughtInGame,
            "wardsKilled": self.wardsKilled,
            "wardsPlaced": self.wardsPlaced,
            "win": self.win
        }

    def __repr__(self):
        return str(self.json)

    def insert_into_db(self):
        with ConnectionFromPool() as connection:
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO game_participants (id, gameTeamId, puuid, assists, baronKills, bountyLevel,"
                               "champExperience, champLevel, championId, championName, championTransform, "
                               "consumablesPurchased, damageDealtToBuildings, damageDealtToObjectives, "
                               "damageDealtToTurrets, damageSelfMitigated, deaths, detectorWardsPlaced, doubleKills, "
                               "dragonKills, firstBloodAssist, firstBloodKill, firstTowerAssist, firstTowerKill, "
                               "gameEndedInEarlySurrender, gameEndedInSurrender, goldEarned, goldSpent, "
                               "individualPosition, inhibitorKills, inhibitorTakedowns, inhibitorsLost, item0, item1, "
                               "item2, item3, item4, item5, item6, itemsPurchased, killingSprees, kills, lane, "
                               "largestCriticalStrike, largestKillingSpree, largestMultiKill, longestTimeSpentLiving, "
                               "magicDamageDealt, magicDamageDealtToChampions, magicDamageTaken, neutralMinionsKilled, "
                               "nexusKills, nexusTakedowns, nexusLost, objectivesStolen, objectivesStolenAssists, "
                               "participantId, pentaKills, physicalDamageDealt, physicalDamageDealtToChampions, "
                               "physicalDamageTaken, profileIcon, quadraKills, riotIdName, riotIdTagline, role, "
                               "sightWardsBoughtInGame, spell1Casts, spell2Casts, spell3Casts, spell4Casts, "
                               "summoner1Casts, summoner1Id, summoner2Casts, summoner2Id, summonerId, summonerLevel, "
                               "summonerName, teamEarlySurrendered, teamId, teamPosition, timeCCingOthers, timePlayed, "
                               "totalDamageDealt, totalDamageDealtToChampions, totalDamageShieldedOnTeammates, "
                               "totalDamageTaken, totalHeal, totalHealsOnTeammates, totalMinionsKilled, "
                               "totalTimeCCDealt, " "totalTimeSpentDead, totalUnitsHealed, tripleKills, "
                               "trueDamageDealt, trueDamageDealtToChampions, trueDamageTaken, turretKills, "
                               "turretTakedowns, turretsLost, unrealKills, visionScore, visionWardsBoughtInGame, "
                               "wardsKilled, wardsPlaced, win) "
                               "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, "
                               "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, "
                               "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, "
                               "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, "
                               "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, "
                               "%s, %s, %s)",
                               (str(self.id), str(self.gameTeamId), self.puuid, self.assists, self.baronKills,
                                self.bountyLevel, self.champExperience, self.champLevel, self.championId,
                                self.championName, self.championTransform, self.consumablesPurchased,
                                self.damageDealtToBuildings, self.damageDealtToObjectives, self.damageDealtToTurrets,
                                self.damageSelfMitigated, self.deaths, self.detectorWardsPlaced, self.doubleKills,
                                self.dragonKills, self.firstBloodAssist, self.firstBloodKill, self.firstTowerAssist,
                                self.firstTowerKill, self.gameEndedInEarlySurrender, self.gameEndedInSurrender,
                                self.goldEarned, self.goldSpent, self.individualPosition, self.inhibitorKills,
                                self.inhibitorTakedowns, self.inhibitorsLost, self.item0, self.item1, self.item2,
                                self.item3, self.item4, self.item5, self.item6, self.itemsPurchased, self.killingSprees,
                                self.kills, self.lane, self.largestCriticalStrike, self.largestKillingSpree,
                                self.largestMultiKill, self.longestTimeSpentLiving, self.magicDamageDealt,
                                self.magicDamageDealtToChampions, self.magicDamageTaken, self.neutralMinionsKilled,
                                self.nexusKills, self.nexusTakedowns, self.nexusLost, self.objectivesStolen,
                                self.objectivesStolenAssists, self.participantId, self.pentaKills,
                                self.physicalDamageDealt, self.physicalDamageDealtToChampions, self.physicalDamageTaken,
                                self.profileIcon, self.quadraKills, self.riotIdName, self.riotIdTagline, self.role,
                                self.sightWardsBoughtInGame, self.spell1Casts, self.spell2Casts, self.spell3Casts,
                                self.spell4Casts, self.summoner1Casts, self.summoner1Id, self.summoner2Casts,
                                self.summoner2Id, str(self.summonerId), self.summonerLevel, self.summonerName,
                                self.teamEarlySurrendered, self.teamId, self.teamPosition, self.timeCCingOthers,
                                self.timePlayed, self.totalDamageDealt, self.totalDamageDealtToChampions,
                                self.totalDamageShieldedOnTeammates, self.totalDamageTaken, self.totalHeal,
                                self.totalHealsOnTeammates, self.totalMinionsKilled, self.totalTimeCCDealt,
                                self.totalTimeSpentDead, self.totalUnitsHealed, self.tripleKills, self.trueDamageDealt,
                                self.trueDamageDealtToChampions, self.trueDamageTaken, self.turretKills,
                                self.turretTakedowns, self.turretsLost, self.unrealKills, self.visionScore,
                                self.visionWardsBoughtInGame, self.wardsKilled, self.wardsPlaced, self.win
                                ))

    @classmethod
    def get_summoner_id_from_puuid(cls, puuid):
        with ConnectionFromPool() as connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT id FROM summoners WHERE puuid = %s LIMIT 1", (puuid,))
                summoner_id = cursor.fetchone()
                return summoner_id[0]
