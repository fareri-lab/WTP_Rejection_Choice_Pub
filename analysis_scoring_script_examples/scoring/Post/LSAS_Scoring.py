#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 20:47:02 2023

@author: jordansiegel
"""

import pandas as pd
import os
import numpy as np
from pathlib import Path

path = Path(r"%s"%(os.getcwd()))
# read in participant list
current_dir = os.getcwd()
participants = pd.read_excel('%s/participantlist.xlsx'%(path.parent.parent))
participants = participants.loc[
    participants['PhotosUploaded? (y/n)'] == 'y'].reset_index()
participants = pd.DataFrame(data=participants['PROLIFIC_ID'])

posttask_survey = '%s/' %(str(path.parent.parent)) + [posttask for posttask in os.listdir(path.parent.parent) if posttask.startswith('RejectionChoice_PostTask')][0]
#read in raw qualtrics data
alldata = pd.read_csv(posttask_survey)
alldata = alldata.iloc[2:]
alldata = alldata.sort_values(by=['PROLIFIC_ID'])
alldata.pop("Attnchk")  # remove attention checks
alldata = alldata.reset_index()

# %%
#columns list
LSAS_avoidancecols = [col for col in alldata.columns if 'LSAS_1_' in col]
LSAS_fearcols = [col for col in alldata.columns if 'LSAS_2_' in col]
ProlificID_cols = [col for col in alldata.columns if 'PROLIFIC_ID' in col]


LSAS = alldata.filter(regex='LSAS_|PROLIFIC_ID')


# %%
LSAS_clean = pd.DataFrame()


for i in range(0, len(LSAS)):
    if LSAS.loc[i,'PROLIFIC_ID'] in participants['PROLIFIC_ID'].values:
       LSAS_clean[i] = LSAS.loc[i]

finaldata = pd.DataFrame()


LSAS_clean = LSAS_clean.transpose()
LSAS_clean = LSAS_clean.reset_index()
finaldata['Prolific_ID'] = LSAS_clean['PROLIFIC_ID']
LSAS_clean = LSAS_clean.drop(['index'], axis = 1)
LSAS_clean = LSAS_clean.drop(['PROLIFIC_ID'], axis = 1)
LSAS_clean = LSAS_clean.replace(np.nan, 0)
#%%

fear0 = LSAS_clean[LSAS_fearcols]
avoidance0 = LSAS_clean[LSAS_avoidancecols]

for k in range(0, len(fear0)):
    for i in range (1,len(fear0.columns)+1):
            if LSAS_clean.loc[k, 'LSAS_1_' + str(i)] == 1:
                LSAS_clean['LSAS_1_' + str(i)][k] = 0
            elif LSAS_clean.loc[k, 'LSAS_1_' + str(i)] == 2:
                LSAS_clean['LSAS_1_' + str(i)][k] = 1
            elif LSAS_clean.loc[k, 'LSAS_1_' + str(i)] == 3:
                LSAS_clean['LSAS_1_' + str(i)][k] = 2
            elif LSAS_clean.loc[k, 'LSAS_1_' + str(i)] == 4:
                LSAS_clean['LSAS_1_' + str(i)][k] = 3


for k in range(0, len(avoidance0)):
    for i in range (1,len(avoidance0.columns)+1):
            if LSAS_clean.loc[k, 'LSAS_2_' + str(i)] == 1:
                LSAS_clean['LSAS_2_' + str(i)][k] = 0
            elif LSAS_clean.loc[k, 'LSAS_2_' + str(i)] == 2:
                LSAS_clean['LSAS_2_' + str(i)][k] = 1
            elif LSAS_clean.loc[k, 'LSAS_2_' + str(i)] == 3:
                LSAS_clean['LSAS_2_' + str(i)][k] = 2
            elif LSAS_clean.loc[k, 'LSAS_2_' + str(i)] == 4:
                LSAS_clean['LSAS_2_' + str(i)][k] = 3
            #elif LSAS_clean.loc[k, 'DII_' + str(i)] == 5:
#%%
LSAS_score = pd.DataFrame(columns = LSAS_clean.columns, index = LSAS_clean.index)

#%%
LSAS_avoidance = pd.DataFrame()
LSAS_avoidance['LSAS_1_1'] = avoidance0['LSAS_1_1']
LSAS_avoidance['LSAS_1_2'] = avoidance0['LSAS_1_2']
LSAS_avoidance['LSAS_1_3'] = avoidance0['LSAS_1_3']
LSAS_avoidance['LSAS_1_4'] = avoidance0['LSAS_1_4']
LSAS_avoidance['LSAS_1_5'] = avoidance0['LSAS_1_5']
LSAS_avoidance['LSAS_1_6'] = avoidance0['LSAS_1_6']
LSAS_avoidance['LSAS_1_7'] = avoidance0['LSAS_1_7']
LSAS_avoidance['LSAS_1_8'] = avoidance0['LSAS_1_8']
LSAS_avoidance['LSAS_1_9'] = avoidance0['LSAS_1_9']
LSAS_avoidance['LSAS_1_10'] = avoidance0['LSAS_1_10']
LSAS_avoidance['LSAS_1_11'] = avoidance0['LSAS_1_11']
LSAS_avoidance['LSAS_1_12'] = avoidance0['LSAS_1_12']
LSAS_avoidance['LSAS_1_13'] = avoidance0['LSAS_1_13']
LSAS_avoidance['LSAS_1_14'] = avoidance0['LSAS_1_14']
LSAS_avoidance['LSAS_1_15'] = avoidance0['LSAS_1_15']
LSAS_avoidance['LSAS_1_16'] = avoidance0['LSAS_1_16']
LSAS_avoidance['LSAS_1_17'] = avoidance0['LSAS_1_17']
LSAS_avoidance['LSAS_1_18'] = avoidance0['LSAS_1_18']
LSAS_avoidance['LSAS_1_19'] = avoidance0['LSAS_1_19']
LSAS_avoidance['LSAS_1_20'] = avoidance0['LSAS_1_20']
LSAS_avoidance['LSAS_1_21'] = avoidance0['LSAS_1_21']
LSAS_avoidance['LSAS_1_22'] = avoidance0['LSAS_1_22']
LSAS_avoidance['LSAS_1_23'] = avoidance0['LSAS_1_23']
LSAS_avoidance['LSAS_1_24'] = avoidance0['LSAS_1_24']

LSAS_avoidance= LSAS_avoidance.astype(int)

#%%
LSAS_fear = pd.DataFrame()
LSAS_fear['LSAS_2_1'] = fear0['LSAS_2_1']
LSAS_fear['LSAS_2_2'] = fear0['LSAS_2_2']
LSAS_fear['LSAS_2_3'] = fear0['LSAS_2_3']
LSAS_fear['LSAS_2_4'] = fear0['LSAS_2_4']
LSAS_fear['LSAS_2_5'] = fear0['LSAS_2_5']
LSAS_fear['LSAS_2_6'] = fear0['LSAS_2_6']
LSAS_fear['LSAS_2_7'] = fear0['LSAS_2_7']
LSAS_fear['LSAS_2_8'] = fear0['LSAS_2_8']
LSAS_fear['LSAS_2_9'] = fear0['LSAS_2_9']
LSAS_fear['LSAS_2_10'] = fear0['LSAS_2_10']
LSAS_fear['LSAS_2_11'] = fear0['LSAS_2_11']
LSAS_fear['LSAS_2_12'] = fear0['LSAS_2_12']
LSAS_fear['LSAS_2_13'] = fear0['LSAS_2_13']
LSAS_fear['LSAS_2_14'] = fear0['LSAS_2_14']
LSAS_fear['LSAS_2_15'] = fear0['LSAS_2_15']
LSAS_fear['LSAS_2_16'] = fear0['LSAS_2_16']
LSAS_fear['LSAS_2_17'] = fear0['LSAS_2_17']
LSAS_fear['LSAS_2_18'] = fear0['LSAS_2_18']
LSAS_fear['LSAS_2_19'] = fear0['LSAS_2_19']
LSAS_fear['LSAS_2_20'] = fear0['LSAS_2_20']
LSAS_fear['LSAS_2_21'] = fear0['LSAS_2_21']
LSAS_fear['LSAS_2_22'] = fear0['LSAS_2_22']
LSAS_fear['LSAS_2_23'] = fear0['LSAS_2_23']
LSAS_fear['LSAS_2_24'] = fear0['LSAS_2_24']

LSAS_fear= LSAS_fear.astype(int)

#%%
LSAS_score =  pd.concat([LSAS_fear, LSAS_avoidance], axis=1)
LSAS_score["LSAS_avoidance"] = LSAS_avoidance.sum(axis=1)
LSAS_score["LSAS_fear"] = LSAS_fear.sum(axis=1)
LSAS_score["LSAS_total"] = LSAS_score['LSAS_avoidance'] + LSAS_score['LSAS_fear']

#%%
lsas = pd.DataFrame()
lsas['Prolific_ID'] = finaldata['Prolific_ID']
lsas['"LSAS_avoidance"']= LSAS_score["LSAS_avoidance"]
lsas['LSAS_fear']= LSAS_score["LSAS_fear"]
lsas['LSAS_total'] = LSAS_score['LSAS_total']
lsas.to_csv('%s/LSAS.csv' %(path.parent), index=False)
#selfreportdata = pd.read_csv('%s/selfreportdata_master.csv' %(path.parent))
#selfreportdata['LSAS_avoidance'] = LSAS_score["LSAS_avoidance"]
#selfreportdata['LSAS_fear'] = LSAS_score["LSAS_fear"]
#selfreportdata['LSAS_total'] = LSAS_score["LSAS_total"]
#selfreportdata.to_csv('%s/selfreportdata_master.csv' %(path.parent), index=False)
