from basketball_reference_scraper.teams import get_roster, get_team_stats, get_opp_stats, get_roster_stats, get_team_misc
from basketball_reference_scraper.players import get_stats, get_game_logs
import pandas as pd

#df = get_game_logs('LeBron James', '2010-01-19', '2014-01-20', playoffs=False)
#print(df)

teams = ['ATL','BOS','BRK','CHI','CHO','CLE','DAL','DEN','DET','GSW','HOU',
'IND','LAC','LAL','MEM','MIL','MIN','NOP','NYK','OKC','ORL','PHI','PHO','POR','SAC','SAS','TOR','UTA','WAS']

# Loop for pulling roster data
'''
output = []

for team in teams:
    df1 = get_roster(team, 2021)
    df1 = df1[['PLAYER','POS']]
    df1['TEAM'] = team
    output.append(df1)
results = pd.concat(output,ignore_index=True)
results.to_csv('2021 Roster.csv')
'''

df = pd.read_csv('2020 Playoff Roster.csv', index_col = 0)
df.drop_duplicates(subset=['PLAYER'],keep='first',inplace=True)
df = list(df['PLAYER'])
#df = df[165:]


#print(get_game_logs('Joel Embiid','2020-08-01', '2020-10-11', playoffs=True))


for i,player in enumerate(df):
    if i == 0:
        game_log = get_game_logs(player, '2020-08-01', '2020-10-11', playoffs=True)
    df_to_add = get_game_logs(player, '2020-08-01', '2020-10-11', playoffs=True)
    game_log = pd.concat([game_log, df_to_add])

game_log.to_csv('2019-2020 Game Log Playoffs.csv')
