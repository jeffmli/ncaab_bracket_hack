#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 14:02:39 2021

@author: ken
"""
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

class Team:
    def __init__(self, team_name, data, season):
        self.team_name = team_name
        self.data = data[(data['TeamName'] == self.team_name)&
                         (data['Season'] == season)].copy()
    
    def getPointsScored(self):
        return self.data['PtScored'].values

    def getPointsAllowed(self):
        return self.data['PtAllowed'].values
    
    def getAttributes(self):
        self.attributes = dict()
        for col in self.data.columns:
            self.attributes[col] = self.data[col].values
        return self.attributes
    
