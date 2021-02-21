# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd 

def get_merged_data(results_data_path,team_names_path,team_conf_path):
    df = pd.read_csv(results_data_path)
    df_wteams = pd.read_csv(team_names_path)
    df_lteams = pd.read_csv(team_names_path)
    df_wteams.columns = ['w_'+i for i in df_wteams.columns]
    df_lteams.columns = ['l_'+i for i in df_lteams.columns]
    
    df_wconf = pd.read_csv(team_conf_path)
    df_lconf = pd.read_csv(team_conf_path)
    
    df_wconf.columns = ['w_'+i for i in df_wconf.columns]
    df_lconf.columns = ['l_'+i for i in df_lconf.columns]
    
    df_team_names = pd.merge(pd.merge(df, df_wteams, left_on = 'WTeamID', right_on = 'w_TeamID'), df_lteams, left_on = 'LTeamID',right_on='l_TeamID')
    
    df_tn_conf = pd.merge(pd.merge(df_team_names, df_wconf, left_on = ['w_TeamID','Season'], right_on = ['w_TeamID','w_Season']), df_lconf,left_on = ['l_TeamID','Season'], right_on = ['l_TeamID','l_Season'])
    
    return df_tn_conf