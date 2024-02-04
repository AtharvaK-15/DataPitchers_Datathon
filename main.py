from understatapi import UnderstatClient
import json

# Create an instance of the UnderstatAPI class
understat = UnderstatClient()

# team_match_data = understat.team(team="Chelsea").get_match_data(season="2023")
# league_player_data = understat.league(league="EPL").get_player_data(season="2022")
# EPL league data:
league_data = understat.league(league="EPL").season(season="2022")

# Convert the data to JSON format
json_data = json.dumps(league_data, indent=2)

# Save the JSON data to a file
with open('league_data_22.json', 'w') as json_file:
    json.dump(league_data, json_file, indent=2)

# Print a message indicating that the data has been saved
print('Team match data saved to league_data.json')
