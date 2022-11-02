from database import ConnectionFromPool
import uuid

class Challenges:
    def __init__(self, gameParticipantId, details):
        self.id = uuid.uuid4()
        self.gameParticipantId = gameParticipantId
        self.details = details
        self.abilityUses = 0
        self.baronTakedowns = 0
        self.buffsStolen = 0
        self.controlWardTimeCoverageInRiverOrEnemyHalf = 0
        self.controlWardsPlaced = 0
        self.damagePerMinute = 0
        self.damageTakenOnTeamPercentage = 0
        self.dragonTakedowns = 0
        self.enemyJungleMonsterKills = 0
        self.takedownOnFirstTurret = 0
        self.firstTurretKilledTime = 0
        self.gameLength = 0
        self.goldPerMinute = 0
        self.initialBuffCount = 0
        self.initialCrabCount = 0
        self.jungleCsBefore10Minutes = 0
        self.kda = 0
        self.killAfterHiddenWithAlly = 0
        self.killParticipation = 0
        self.killsNearEnemyTurret = 0
        self.laneMinionsFirst10Minutes = 0
        self.legendaryCount = 0
        self.lostAnInhibitor = 0
        self.maxKillDeficit = 0
        self.moreEnemyJungleThanOpponent = 0
        self.perfectDragonSoulsTaken = 0
        self.pickKillWithAlly = 0
        self.quickFirstTurret = 0
        self.quickSoloKills = 0
        self.riftHeraldTakedowns = 0
        self.saveAllyFromDeath = 0
        self.scuttleCrabKills = 0
        self.soloKills = 0
        self.stealthWardsPlaced = 0
        self.takedowns = 0
        self.takedownsAfterGainingLevelAdvantage = 0
        self.teamBaronKills = 0
        self.teamDamagePercentage = 0
        self.teamElderDragonKills = 0
        self.teamRiftHeraldKills = 0
        self.tookLargeDamageSurvived = 0
        self.turretPlatesTaken = 0
        self.turretTakedowns = 0
        self.turretsTakenWithRiftHerald = 0
        self.visionScorePerMinute = 0
        self.wardTakedowns = 0
        self.wardTakedownsBefore20M = 0
        self.earliestDragonTakedown = 0
        self.killsOnLanersEarlyJungleAsJungler = 0
        self.junglerKillsEarlyJungle = 0
        self.killsOnOtherLanesEarlyJungleAsLaner = 0
        self.getTakedownsInAllLanesEarlyJungleAsLaner = 0
        self.json = {}

    def get_data(self):
        self.abilityUses = self.details["abilityUses"]
        self.baronTakedowns = self.details["baronTakedowns"]
        self.buffsStolen = self.details["buffsStolen"]
        self.controlWardsPlaced = self.details["controlWardsPlaced"]
        self.damageTakenOnTeamPercentage = self.details["damageTakenOnTeamPercentage"]
        self.dragonTakedowns = self.details["dragonTakedowns"]
        self.enemyJungleMonsterKills = self.details["enemyJungleMonsterKills"]
        self.takedownOnFirstTurret = self.details["takedownOnFirstTurret"]
        self.gameLength = self.details["gameLength"]
        self.goldPerMinute = self.details["goldPerMinute"]
        self.initialBuffCount = self.details["initialBuffCount"]
        self.initialCrabCount = self.details["initialCrabCount"]
        self.jungleCsBefore10Minutes = self.details["jungleCsBefore10Minutes"]
        self.kda = self.details["kda"]
        self.killsNearEnemyTurret = self.details["killsNearEnemyTurret"]
        self.laneMinionsFirst10Minutes = self.details["laneMinionsFirst10Minutes"]
        self.legendaryCount = self.details["legendaryCount"]
        self.lostAnInhibitor = self.details["lostAnInhibitor"]
        self.maxKillDeficit = self.details["maxKillDeficit"]
        self.moreEnemyJungleThanOpponent = self.details["moreEnemyJungleThanOpponent"]
        self.perfectDragonSoulsTaken = self.details["perfectDragonSoulsTaken"]
        self.quickFirstTurret = self.details["quickFirstTurret"]
        self.quickSoloKills = self.details["quickSoloKills"]
        self.riftHeraldTakedowns = self.details["riftHeraldTakedowns"]
        self.scuttleCrabKills = self.details["scuttleCrabKills"]
        self.soloKills = self.details["soloKills"]
        self.stealthWardsPlaced = self.details["stealthWardsPlaced"]
        self.takedowns = self.details["takedowns"]
        self.takedownsAfterGainingLevelAdvantage = self.details["takedownsAfterGainingLevelAdvantage"]
        self.teamBaronKills = self.details["teamBaronKills"]
        self.teamDamagePercentage = self.details["teamDamagePercentage"]
        self.teamElderDragonKills = self.details["teamElderDragonKills"]
        self.teamRiftHeraldKills = self.details["teamRiftHeraldKills"]
        self.turretPlatesTaken = self.details["turretPlatesTaken"]
        self.turretTakedowns = self.details["turretTakedowns"]
        self.turretsTakenWithRiftHerald = self.details["turretsTakenWithRiftHerald"]
        self.visionScorePerMinute = self.details["visionScorePerMinute"]
        self.wardTakedowns = self.details["wardTakedowns"]
        self.wardTakedownsBefore20M = self.details["wardTakedownsBefore20M"]

        # I found out that in older versions of the game, damagePerMinute shows way too big numbers, and dividing those
        # big numbers by 10 seemed like a good solution (well, at least not too complicated)
        if self.details["damagePerMinute"] < 1500:
            self.damagePerMinute = self.details["damagePerMinute"]
        else:
            self.damagePerMinute = self.details["damagePerMinute"]/10

        # First two keys are present in dictionary only for junglers, so we can assume that if those keys are not present
        # that means it must be a laner, so the latter two keys should be valid
        try:
            self.killsOnLanersEarlyJungleAsJungler = self.details["killsOnLanersEarlyJungleAsJungler"]
            self.junglerKillsEarlyJungle = self.details["junglerKillsEarlyJungle"]
        except KeyError:
            self.killsOnOtherLanesEarlyJungleAsLaner = self.details["killsOnOtherLanesEarlyJungleAsLaner"]
            self.getTakedownsInAllLanesEarlyJungleAsLaner = self.details["getTakedownsInAllLanesEarlyJungleAsLaner"]

        # EarliestDragonTakedown key is not always present in dictionary, therefore we use have to handle this exception
        try:
            self.earliestDragonTakedown = self.details["earliestDragonTakedown"]
        except KeyError:
            pass

        # Couldn't find out when this key should be present in dictionary. Let's just leave it like that
        try:
            self.controlWardTimeCoverageInRiverOrEnemyHalf = self.details["controlWardTimeCoverageInRiverOrEnemyHalf"]
        except KeyError:
            pass

        # Couldn't find out when this key should be present in dictionary. Let's just leave it like that
        try:
            self.firstTurretKilledTime = self.details["firstTurretKilledTime"]
        except KeyError:
            pass

        # Couldn't find out when this key should be present in dictionary. Let's just leave it like that
        try:
            self.killParticipation = self.details["killParticipation"]
        except KeyError:
            pass

        # Couldn't find out when this key should be present in dictionary. Let's just leave it like that
        try:
            self.killAfterHiddenWithAlly = self.details["killAfterHiddenWithAlly"]
        except KeyError:
            pass

        # Couldn't find out when this key should be present in dictionary. Let's just leave it like that
        try:
            self.pickKillWithAlly = self.details["pickKillWithAlly"]
        except KeyError:
            pass# Couldn't find out when this key should be present in dictionary. Let's just leave it like that

        # Couldn't find out when this key should be present in dictionary. Let's just leave it like that
        try:
            self.saveAllyFromDeath = self.details["saveAllyFromDeath"]
        except KeyError:
            pass

        # Couldn't find out when this key should be present in dictionary. Let's just leave it like that
        try:
            self.tookLargeDamageSurvived = self.details["tookLargeDamageSurvived"]
        except KeyError:
            pass

        self.json = {
            "id": str(self.id),
            "gameParticipantId": str(self.gameParticipantId),
            "abilityUses": self.abilityUses,
            "baronTakedowns": self.baronTakedowns,
            "buffsStolen": self.buffsStolen,
            "controlWardTimeCoverageInRiverOrEnemyHalf": self.controlWardTimeCoverageInRiverOrEnemyHalf,
            "controlWardsPlaced": self.controlWardsPlaced,
            "damagePerMinute": self.damagePerMinute,
            "damageTakenOnTeamPercentage": self.damageTakenOnTeamPercentage,
            "dragonTakedowns": self.dragonTakedowns,
            "enemyJungleMonsterKills": self.enemyJungleMonsterKills,
            "takedownOnFirstTurret": self.takedownOnFirstTurret,
            "firstTurretKilledTime": self.firstTurretKilledTime,
            "gameLength": self.gameLength,
            "goldPerMinute": self.goldPerMinute,
            "initialBuffCount": self.initialBuffCount,
            "initialCrabCount": self.initialCrabCount,
            "jungleCsBefore10Minutes": self.jungleCsBefore10Minutes,
            "kda": self.kda,
            "killAfterHiddenWithAlly": self.killAfterHiddenWithAlly,
            "killParticipation": self.killParticipation,
            "killsNearEnemyTurret": self.killsNearEnemyTurret,
            "laneMinionsFirst10Minutes": self.laneMinionsFirst10Minutes,
            "legendaryCount": self.legendaryCount,
            "lostAnInhibitor": self.lostAnInhibitor,
            "maxKillDeficit": self.maxKillDeficit,
            "moreEnemyJungleThanOpponent": self.moreEnemyJungleThanOpponent,
            "perfectDragonSoulsTaken": self.perfectDragonSoulsTaken,
            "pickKillWithAlly": self.pickKillWithAlly,
            "quickFirstTurret": self.quickFirstTurret,
            "quickSoloKills": self.quickSoloKills,
            "riftHeraldTakedowns": self.riftHeraldTakedowns,
            "saveAllyFromDeath": self.saveAllyFromDeath,
            "scuttleCrabKills": self.scuttleCrabKills,
            "soloKills": self.soloKills,
            "takedowns": self.takedowns,
            "takedownsAfterGainingLevelAdvantage": self.takedownsAfterGainingLevelAdvantage,
            "teamBaronKills": self.teamBaronKills,
            "teamDamagePercentage": self.teamDamagePercentage,
            "teamElderDragonKills": self.teamElderDragonKills,
            "teamRiftHeraldKills": self.teamRiftHeraldKills,
            "tookLargeDamageSurvived": self.tookLargeDamageSurvived,
            "turretPlatesTaken": self.turretPlatesTaken,
            "turretTakedowns": self.turretTakedowns,
            "turretsTakenWithRiftHerald": self.turretsTakenWithRiftHerald,
            "visionScorePerMinute": self.visionScorePerMinute,
            "wardTakedowns": self.wardTakedowns,
            "wardTakedownsBefore20M": self.wardTakedownsBefore20M,
            "earliestDragonTakedown": self.earliestDragonTakedown,
            "killsOnLanersEarlyJungleAsJungler": self.killsOnLanersEarlyJungleAsJungler,
            "junglerKillsEarlyJungle": self.junglerKillsEarlyJungle,
            "killsOnOtherLanesEarlyJungleAsLaner": self.killsOnOtherLanesEarlyJungleAsLaner,
            "getTakedownsInAllLanesEarlyJungleAsLaner": self.getTakedownsInAllLanesEarlyJungleAsLaner
        }


    def __repr__(self):
        return str(self.json)

    def insert_into_db(self):
        with ConnectionFromPool() as connection:
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO challenges (id, gameParticipantId, abilityUses, baronTakedowns, buffsStolen, "
                               "controlWardTimeCoverageInRiverOrEnemyHalf, controlWardsPlaced, damagePerMinute, "
                               "damageTakenOnTeamPercentage, dragonTakedowns, enemyJungleMonsterKills, "
                               "firstTurretKilledTime, gameLength, getTakedownsInAllLanesEarlyJungleAsLaner, "
                               "goldPerMinute, initialBuffCount, initialCrabCount, jungleCsBefore10Minutes, kda, "
                               "killAfterHiddenWithAlly, killParticipation, killsNearEnemyTurret, "
                               "killsOnOtherLanesEarlyJungleAsLaner, laneMinionsFirst10Minutes, legendaryCount, "
                               "lostAnInhibitor, maxKillDeficit, moreEnemyJungleThanOpponent, perfectDragonSoulsTaken, "
                               "pickKillWithAlly, quickFirstTurret, quickSoloKills, riftHeraldTakedowns, "
                               "saveAllyFromDeath, scuttleCrabKills, soloKill, stealthWardsPlaced, takedowns, "
                               "takedownsAfterGainingLevelAdvantage, teamBaronKills, teamDamagePercentage, "
                               "teamElderDragonKills, teamRiftHeraldKills, tookLargeDamageSurvived, turretPlatesTaken, "
                               "turretTakedowns, turretsTakenWithRiftHerald, visionScorePerMinute, wardTakedowns, "
                               "wardTakedownsBefore20M, earliestDragonTakedown, killsOnLanersEarlyJungleAsJungler, "
                               "junglerKillsEarlyJungle, takedownOnFirstTurret) "
                               "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, "
                               "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, "
                               "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                               (str(self.id), str(self.gameParticipantId), self.abilityUses, self.baronTakedowns,
                                self.buffsStolen, self.controlWardTimeCoverageInRiverOrEnemyHalf,
                                self.controlWardsPlaced, self.damagePerMinute, self.damageTakenOnTeamPercentage,
                                self.dragonTakedowns, self.enemyJungleMonsterKills, self.firstTurretKilledTime,
                                self.gameLength, self.getTakedownsInAllLanesEarlyJungleAsLaner, self.goldPerMinute,
                                self.initialBuffCount, self.initialCrabCount, self.jungleCsBefore10Minutes, self.kda,
                                self.killAfterHiddenWithAlly, self.killParticipation, self.killsNearEnemyTurret,
                                self.killsOnOtherLanesEarlyJungleAsLaner, self.laneMinionsFirst10Minutes,
                                self.legendaryCount, self.lostAnInhibitor, self.maxKillDeficit,
                                self.moreEnemyJungleThanOpponent, self.perfectDragonSoulsTaken, self.pickKillWithAlly,
                                self.quickFirstTurret, self.quickSoloKills, self.riftHeraldTakedowns,
                                self.saveAllyFromDeath, self.scuttleCrabKills, self.soloKills, self.stealthWardsPlaced,
                                self.takedowns, self.takedownsAfterGainingLevelAdvantage, self.teamBaronKills,
                                self.teamDamagePercentage, self.teamElderDragonKills, self.teamRiftHeraldKills,
                                self.tookLargeDamageSurvived, self.turretPlatesTaken, self.turretTakedowns,
                                self.turretsTakenWithRiftHerald, self.visionScorePerMinute, self.wardTakedowns,
                                self.wardTakedownsBefore20M, self.earliestDragonTakedown,
                                self.killsOnLanersEarlyJungleAsJungler, self.junglerKillsEarlyJungle,
                                self.takedownOnFirstTurret
                                ))
