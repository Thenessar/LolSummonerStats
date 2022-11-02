servers = {
            "BR1": "AMERICAS",
            "EUN1": "EUROPE",
            "JP1": "ASIA",
            "KR": "ASIA",
            "LA1": "AMERICAS",
            "LA2": "AMERICAS",
            "NA1": "AMERICAS",
            "OC1": "SEA",
            "RU": "EUROPE",
            "TR1": "EUROPE",
        }


class RiotAPI:
    def __init__(self, region):
        self.apiKey = ""  # "GET YOUR API KEY HERE: https://developer.riotgames.com/"
        self.region = region

    def get_summoner_by_name(self, name):
        return f"https://{self.region}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{name}?api_key={self.apiKey}"

    def get_summoner_by_puuid(self, puuid):
        return f"https://eun1.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/{puuid}?api_key={self.apiKey}"

    def get_matches_by_puuid(self, puuid, quantity, start_index):
        return f"https://{servers[self.region]}.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?type=ranked&start={start_index}&count={quantity}&api_key={self.apiKey}"

    def get_match_by_id(self, gameId):
        return f"https://{servers[self.region]}.api.riotgames.com/lol/match/v5/matches/{gameId}?api_key={self.apiKey}"



