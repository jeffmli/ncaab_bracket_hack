#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 15:24:38 2021

@author: ken
"""

import streamlit as st
import sim_pseudo_code as spc
import Team_Class as tc
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot  as plt 
plt.style.use('fivethirtyeight')

@st.cache
def load_data():
    by_team = pd.read_csv("./Data/teamlevel.csv")
    return by_team

df = load_data()

st.title('NCAAB Matchup Simulator Tool')
seasons = df.Season.unique()
seasons.sort()
year = st.selectbox('Year:', seasons)

t1 = st.selectbox('Team 1:', df[df['Season'] == year].TeamName.unique())
t2 = st.selectbox('Team 2:', df[df['Season'] == year].TeamName.unique())

team_1 = tc.Team(t1,df,year)
team_2 = tc.Team(t2,df,year)

sim_out = spc.sim_multiple(team_1,team_2,10000)

st.write(t1, ' Win Probability:', sim_out[0])


fig, ax = plt.subplots(1)
sns.kdeplot(sim_out[1], label = t1, ax=ax)
sns.kdeplot(sim_out[2], label = t2, ax=ax)
fig.suptitle("Projected Points Scored Distribution")
ax.legend()
st.pyplot(fig)