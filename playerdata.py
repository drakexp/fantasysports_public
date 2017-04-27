from nba_py import team, player

202738


player.PlayerGameLogs(202738, league_id='00', season='2016-17', season_type='Playoffs')

def gameLog(id):
   i=0
   player_now = player.PlayerGameLogs(202738, league_id='00', season='2016-17', season_type='Playoffs')
   if(player_now):
      player_now = player_now.info()
      for row, column in player_now.iterrows():
         
      
   player_now = player.PlayerGameLogs(id, league_id='00', season='2016-17', season_type='Regular Season')
   return player_now

team_id = {"Atlanta Hawks":1610612737, "Boston Celtics": 1610612738, "Brooklyn Nets": 1610612751, \
                  "Charlotte Hornets" : 1610612766, "Chicago Bulls" : 1610612741, "Cleveland Cavaliers": 1610612739, \
                  "Dallas Mavericks" : 1610612742, "Denver Nuggets" : 1610612743, "Detroit Pistons" : 1610612765, \
                  "Golden State Warriors" : 1610612744, "Houston Rockets" : 1610612745, "Indiana Pacers": 1610612754, \
                  "Los Angeles Clippers" : 1610612746, "Los Angeles Lakers": 1610612747, "Memphis Grizzlies" : 1610612763, \
                  "Miami Heat" :1610612748, "Milwaukee Bucks" : 1610612749, "Minnesota Timberwolves" : 1610612750, \
                  "New Orleans Pelicans"	: 1610612740, "New York Knicks":	1610612752,  "Oklahoma City Thunder":	1610612760, \
                  "Orlando Magic" : 1610612753,  "Philadelphia 76ers" :	1610612755, "Phoenix Suns" :	1610612756, \
                  "Portland Trail Blazers" :	1610612757, "Sacramento Kings" : 1610612758, "San Antonio Spurs" :	1610612759, \
                  "Toronto Raptors" :	1610612761, "Utah Jazz" :	1610612762, "Washington Wizards" :	1610612764
               }
               
players = player.PlayerList(league_id='00', season='2016-17', only_current=1)
               
# for key, value in team_id.items():
   # print(value)

player_name = input('Enter a player\'s full name: ')
print("Retrieving " + player_name + "'s data...")

player_found = False
players = players.info()
for row, column in players.iterrows():
   if(column["DISPLAY_FIRST_LAST"] == player_name):
      player_id = column["PERSON_ID"]
      player_found = True
      break
if(not player_found):
   print("Player not found!")
   exit()
   
   subset = players.loc[:,("DISPLAY_FIRST_LAST", "PERSON_ID")]
else:
   print("Player found! Calculating data...")
   gameLog(player_id)

# player_found = False
# for key, value in team_id.items():
   # team_this = team.TeamCommonRoster(value, season='2016-17')
   # roster = team_this.roster()
   # for p in roster["PLAYER"]:
      # if(p == player):
         # print("Player found!")
         # player_found = True
         # break
   # if(player_found):
      # break
   
# if(not player_found):
   # print("Player not found!")
   # exit()
# else:
   # print("Player found!")
