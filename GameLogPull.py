from basketball_reference_scraper.teams import get_roster, get_team_stats, get_opp_stats, get_roster_stats, get_team_misc
from basketball_reference_scraper.players import get_stats, get_game_logs
import pandas as pd

#Read Roster CSV
df = pd.read_csv('2019 Playoff Roster.csv', index_col = 0)
# for Keep, we want last, because a player could have been traded to another team. They would only play for Playoffs for that last team
df.drop_duplicates(subset=['PLAYER'],keep='last',inplace=True)
#pd.set_option('display.max_rows', df.shape[0]+1)
#print(df.duplicated())

df = list(df['PLAYER'])

#df = df[50:]
#print(get_game_logs('Jayson Tatum','2019-04-13', '2019-06-13', playoffs=True))

for i,player in enumerate(df):
    if i == 0:
        game_log = get_game_logs(player, '2018-10-16', '2019-04-10', playoffs=False)
    df_to_add = get_game_logs(player, '2018-10-16', '2019-04-10', playoffs=False)
    game_log = pd.concat([game_log, df_to_add])

game_log.to_csv('2018-2019 Game Log.csv')
