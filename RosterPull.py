from basketball_reference_scraper.teams import get_roster, get_team_stats, get_opp_stats, get_roster_stats, get_team_misc
import pandas as pd


teams = ['ATL','BOS','BRK','CHI','CHO','CLE','DAL','DEN','DET','GSW','HOU',
'IND','LAC','LAL','MEM','MIA','MIL','MIN','NOP','NYK','OKC','ORL','PHI','PHO','POR','SAC','SAS','TOR','UTA','WAS']
playoffs2019 = ['BOS','BRK','DEN','DET','GSW','HOU','IND','LAC','MIL','OKC','ORL','PHI','POR','SAS','TOR','UTA']
playoffs2020 = ['BOS','BRK','DAL','DEN','HOU','IND','LAC','LAL','MIA','MIL','OKC','ORL','PHI','POR','TOR','UTA']

# Loop for pulling roster data
output = []

for team in playoffs2020:
    # For Reg Season
    #df1 = get_roster(team, 2021)
    
    # For Playoffs
    df1 = get_roster_stats(team, 2020, data_format='PER_GAME', playoffs=True)
    df1 = df1[['PLAYER','TEAM']]
    output.append(df1)
results = pd.concat(output,ignore_index=True)
results.drop_duplicates(subset=['PLAYER'],keep='last',inplace=True)
results.to_csv('2020 Playoff Roster.csv')

