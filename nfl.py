import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

nflCsv = pd.read_csv('nfl.csv')

#print (nflCsv.tail())
#print (nflCsv.columns)

#for index, row in nflCsv.iterrows():
#    print (index, row)

#print(nflCsv.loc[nflCsv["team"] == 'CLE'])

#nflCsv.columns = ["game_id","player_id","pos","player","team","pass_cmp","pass_att","pass_yds","pass_td","pass_int","pass_sacked","pass_sacked_yds","pass_long","pass_rating","rush_att","rush_yds","rush_td","rush_long","targets","rec","rec_yds","rec_td","rec_long","fumbles_lost","rush_scrambles","designed_rush_att","comb_pass_rush_play","comb_pass_play","comb_rush_play","Team_abbrev","Opponent_abbrev","two_point_conv","total_ret_td","offensive_fumble_recovery_td","pass_yds_bonus","rush_yds_bonus","rec_yds_bonus","Total_DKP","Off_DKP","Total_FDP","Off_FDP","Total_SDP","Off_SDP","pass_target_yds","pass_poor_throws","pass_blitzed","pass_hurried","rush_yds_before_contact","rush_yac","rush_broken_tackles","rec_air_yds","rec_yac","rec_drops","offense","off_pct","vis_team","home_team","vis_score","home_score","OT","Roof","Surface","Temperature","Humidity","Wind_Speed","Vegas_Line","Vegas_Favorite","Over_Under","game_date"]
#grouped = nflCsv.groupby('team')


#print(grouped.first('pass_yds'))
#nflCsv['Total'] = nflCsv['pass_yds'] + nflCsv['rush_yds']
#print(nflCsv.head(5))

#read headers
nflCsv.columns

#Read each column
#print(nflCsv[['player', 'pass_rating']])

#Read each row
#print (nflCsv.iloc[0:4])

#Read a specific location
#print (nflCsv.iloc[0,3])

print(nflCsv.loc[nflCsv['pos'] == 'QB'])