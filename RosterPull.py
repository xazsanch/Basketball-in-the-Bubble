from basketball_reference_scraper.teams import get_roster, get_team_stats, get_opp_stats, get_roster_stats, get_team_misc
import pandas as pd


teams = ['ATL','BOS','BRK','CHI','CHO','CLE','DAL','DEN','DET','GSW','HOU',
'IND','LAC','LAL','MEM','MIA','MIL','MIN','NOP','NYK','OKC','ORL','PHI','PHO','POR','SAC','SAS','TOR','UTA','WAS']
playoffs2019 = ['BOS','BRK','DEN','DET','GSW','HOU','IND','LAC','MIL','OKC','ORL','PHI','POR','SAS','TOR','UTA']
playoffs2020 = ['BOS','BRK','DAL','DEN','HOU','IND','LAC','LAL','MIA','MIL','OKC','ORL','PHI','POR','TOR','UTA']
years = [2020,2019]

# Loop for pulling roster data
output = []

#for year in years:
for team in playoffs2020:
    # For Reg Season
    #df1 = get_roster(team, 2021)
    
    # For Playoffs
    df1 = get_roster_stats(team, 2020, data_format='PER_GAME', playoffs=False)
    #df1 = df1[['PLAYER','TEAM']]

    #Team Misc
    #df1 = get_team_misc(team,2019)
    #df1 = df1.to_frame().T
    output.append(df1)
    print(team)
#print(year)
results = pd.concat(output,ignore_index=True)
#results.drop_duplicates(subset=['PLAYER'],keep='last',inplace=True)
#results['TS%'] = round(results['PTS']/(2*(results['FGA']+0.44*results['FTA'])),3)
results.to_csv('2020 Regular Season Avgs (Playoff Teams).csv')

#Print Testing
# data_format = 'TOTALS'|'PER_GAME'|'PER_MINUTE'|'PER_POSS'|'ADVANCED'
#print(get_roster_stats('LAL', 2020, data_format='PER_POSS', playoffs=True))

#df = get_team_misc('LAL',2020)
#df = df.to_frame().T
#print(df)