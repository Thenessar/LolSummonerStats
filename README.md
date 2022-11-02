
# LolSummonerStats

The project is for anyone that would like to analyse League of Legends in-game data for the
chosen player. Personally, I used the project to analyse my friends' gameplay. Such
analysis might be a great tool used to find weaknesses and strengths of a player, resulting
in improvements of gameplay.

When launched, the app will ask the user about summoner name, his region, number of games
to import to the database and index number (which lets us ommit last X games played by the
summoner). Based on them, the app will send requests to Riot Games API servers, getting the
data about matches that our summoner played and inserting them into the database. Later we
can use that information to analyse the player, plot charts or set goals for the player that
would result in improving his playstyle.

## Notes
Before you run the app, you will have to create database, preferably using postgresql.
DDL script for tables, indexes and view are located in a file [LolSummonerStatsDDL](https://github.com/Thenessar/LolSummonerStats/blob/main/LolSummonerStatsDDL.sql).

Secondly, you will have to edit database.py and tell the app how to connect to your database.

Finally, head to the https://developer.riotgames.com/ to generate your own API key and save it in riot_api.py file.

Sample player report (created in PowerBI desktop) can be found [here](https://github.com/Thenessar/LolSummonerStats/blob/main/sample_player_report.pdf).

## API Documentation

[Riot Games API](https://developer.riotgames.com/apis)


## Authors

- [@Thenessar](https://github.com/Thenessar)


## License

[GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/)

