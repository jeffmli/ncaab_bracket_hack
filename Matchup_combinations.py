#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 14:53:09 2021

@author: ken
"""

import pandas as pd 
import itertools 
by_team = pd.read_csv("./Data/teamlevel.csv")

season_matchups = {}

szns = by_team.Season.unique()
szns.sort()

for i in szns:
    szn_yr = by_team[by_team['Season'] == i]
    all_teams = szn_yr.loc[:,'TeamName'].unique().tolist()
    season_matchups[str(i)] = (i,list(itertools.combinations(all_teams,2)))    

