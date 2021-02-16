#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 10:39:07 2021

@author: ken
"""
import random as rd


#if points are the same then rerun code 
def sim_once(team1,team2):
    score_team1= rd.gauss(team1.getPointsScored().mean(),team1.getPointsScored().std())
    score_team2= rd.gauss(team2.getPointsScored().mean(),team2.getPointsScored().std())
    score_against_team1= rd.gauss(team1.getPointsAllowed().mean(),team1.getPointsAllowed().std())
    score_against_team2= rd.gauss(team2.getPointsAllowed().mean(),team2.getPointsAllowed().std())
    final_score_t1 = (score_team1+score_against_team2)/2
    final_score_t2 = (score_team2+score_against_team1)/2
    if final_score_t1 == final_score_t2:
        sim_once(team1,team2)
    return (final_score_t1,final_score_t2, final_score_t1 > final_score_t2)
    

def sim_multiple(team1,team2,n=100):
    t1_points = []
    t2_points = []
    w_l = []
    for i in range(n):
        sim = sim_once(team1,team2)
        t1_points.append(sim[0])
        t2_points.append(sim[1])
        w_l.append(sim[2])
    return (sum(w_l)/n, t1_points, t2_points, w_l)
