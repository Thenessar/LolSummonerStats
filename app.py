from game_participant import GameParticipant
from challenges import Challenges
from summoner import Summoner
from game_team import GameTeam
from riot_api import RiotAPI
from game import Game
import requests
import time

# Input data
summoner_name = input("Insert summoner's name: ")
summoner_region = input("Insert summoner's region: ")
quantity = int(input("Insert number of games to import: "))

# To skip last X games, type in X
start_index = int(input("Insert start index: "))

# Create summoner based on name and region, whose games will be imported to the database
summoner = Summoner(summoner_name, summoner_region)

# Get basic data provided by Riot about our summoner
summoner.get_data()

# If number of games to import is bigger than 5, the app will crash because of Riot API limitations. The limit is 100
# requests per 2 minutes and the app sends around 20 requests for each game, so to get around that limit I use
# {start_index} variable to cycle through more than 5 games, thanks to putting the app to sleep after every 5 games
while start_index < quantity-1:

    # Using RiotAPI, we get last {quantity} games played by our summoner
    api = RiotAPI(summoner_region)
    url = api.get_matches_by_puuid(summoner.puuid, quantity, start_index)
    response = requests.get(url).json()

    # For every match in a list, insert its details to the database
    for count, match_id in enumerate(response):
        print(f"Processing game {match_id} ({count+1}/{quantity})...")
        game = Game(match_id, summoner_region)
        game.get_data()
        game.insert_into_db()

        # For every participant in a game, create new summoner - if it doesn't exist already
        for summoner_puuid in game.participants:
            new_summoner_name = requests.get(api.get_summoner_by_puuid(summoner_puuid)).json()["name"]
            check_summoner = Summoner.check_if_summoner_exists(new_summoner_name)
            if check_summoner:
                pass
            else:
                new_summoner = Summoner(new_summoner_name, summoner_region)
                new_summoner.get_data()
                new_summoner.insert_into_db()

        # For every team in a game, insert its details to the database
        for team in game.teamsDetails:
            game_team = GameTeam(game.id, team)
            game_team.get_data()
            game_team.insert_into_db()

            team_participants = list(team_participant["puuid"] for team_participant in game.participantsDetails if team_participant["teamId"] == game_team.team["teamId"])

            # For every participant (player) in a team, insert its details to the database
            for participant in team_participants:
                participant_details = list(filter(lambda details: details["puuid"] == participant, game.participantsDetails))[0]
                game_participant = GameParticipant(game_team.id, participant_details)
                game_participant.get_data()
                game_participant.insert_into_db()

                participant_challenge = Challenges(game_participant.id, game_participant.challengesDetails)
                participant_challenge.get_data()
                participant_challenge.insert_into_db()

    start_index += 5

    # Just to make sure we do not waste 2 minutes by putting app to sleep after all the games have been imported
    if start_index < quantity-1:
        print("Sleeping...")
        time.sleep(121)
    else:
        print("All games have been imported to the database.")


