#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 12:03:22 2023

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
#%%

#columns list
DII_cols = [col for col in alldata.columns if 'DII_' in col]
ProlificID_cols = [col for col in alldata.columns if 'PROLIFIC_ID' in col]

DII = alldata.filter(regex='DII_|PROLIFIC_ID')

#%%
DII_clean = pd.DataFrame()


for i in range(0, len(DII)):
    if DII.loc[i,'PROLIFIC_ID'] in participants['PROLIFIC_ID'].values:
       DII_clean[i] = DII.loc[i]    

finaldata = pd.DataFrame()


DII_clean = DII_clean.transpose()
DII_clean = DII_clean.reset_index()
finaldata['Prolific_ID'] = DII_clean['PROLIFIC_ID']
DII_clean = DII_clean.drop(['index'], axis = 1)
DII_clean = DII_clean.drop(['PROLIFIC_ID'], axis = 1)
DII_clean = DII_clean.replace(np.nan, 0)
DII_clean = DII_clean.astype(int)
#%%
recode = [4, 7, 14]
for k in range(0, len(DII_clean)):
    for i in range (1,len(DII_clean.columns)+1):
        if i in recode:
            if DII_clean.loc[k, 'DII_' + str(i)] == 1:
                DII_clean['DII_' + str(i)][k] = 0
            elif DII_clean.loc[k, 'DII_' + str(i)] == 2:
                DII_clean['DII_' + str(i)][k] = 0
            elif DII_clean.loc[k, 'DII_' + str(i)] == 3:
                DII_clean['DII_' + str(i)][k] = 0
            elif DII_clean.loc[k, 'DII_' + str(i)] == 4:
                DII_clean['DII_' + str(i)][k] = 1
            elif DII_clean.loc[k, 'DII_' + str(i)] == 5:
                DII_clean['DII_' + str(i)][k] = 1
        else:
           DII_clean['DII_' +str(i)][k] = DII_clean.loc[k,'DII_'+ str(i)]
#%%
DII_score = pd.DataFrame(columns = DII_clean.columns, index = DII_clean.index)
#%%
functionalreverse = [2,3,8,11,12]
dysfunctionalreverse = [4,22,23]

for k in range(0, len(DII_clean)):
    for i in range (1,len(DII_clean.columns)+1):
        if i in functionalreverse:
            if DII_clean.loc[k,'DII_' + str(i)] == 0:
                DII_score['DII_' + str(i)][k] = 1
            elif DII_clean.loc[k,'DII_' + str(i)] == 1:
                 DII_score['DII_' + str(i)][k] = 0
        else:
            DII_score['DII_' +str(i)][k] = DII_clean.loc[k,'DII_'+ str(i)]
            
for k in range(0, len(DII_clean)):
    for i in range (1,len(DII_clean.columns)+1):
        if i in dysfunctionalreverse:
            if DII_clean.loc[k,'DII_' + str(i)] == 0:
                DII_score['DII_' + str(i)][k] = 1
            elif DII_clean.loc[k,'DII_' + str(i)] == 1:
                 DII_score['DII_' + str(i)][k] = 0
        else:
            DII_score['DII_' +str(i)][k] = DII_clean.loc[k,'DII_'+ str(i)]
        
DII_score = DII_score.astype(int)
# SRQ_negsocpot["SRQ_negsocpot"] = SRQ_negsocpot.sum(axis=1)/5
#%%
DII_functionalimpulsivity = pd.DataFrame()
DII_functionalimpulsivity['DII_2'] = DII_clean['DII_2']
DII_functionalimpulsivity['DII_3'] = DII_clean['DII_3']
DII_functionalimpulsivity['DII_8'] = DII_clean['DII_8']
DII_functionalimpulsivity['DII_11'] = DII_clean['DII_11']
DII_functionalimpulsivity['DII_12'] = DII_clean['DII_12']
DII_functionalimpulsivity['DII_5'] = DII_clean['DII_5']
DII_functionalimpulsivity['DII_19'] = DII_clean['DII_19']
DII_functionalimpulsivity['DII_15'] = DII_clean['DII_15']
DII_functionalimpulsivity['DII_6'] = DII_clean['DII_6']
DII_functionalimpulsivity['DII_16'] = DII_clean['DII_16']
DII_functionalimpulsivity['DII_20'] = DII_clean['DII_20']

DII_functionalimpulsivity = DII_functionalimpulsivity.astype(int)
DII_score["DII_functionalimpulsivity"] = DII_functionalimpulsivity.sum(axis=1)

#%%
DII_dysfuntionalimpulsivity = pd.DataFrame()
DII_dysfuntionalimpulsivity['DII_4'] = DII_clean['DII_4']
DII_dysfuntionalimpulsivity['DII_21'] = DII_clean['DII_21']
DII_dysfuntionalimpulsivity['DII_10'] = DII_clean['DII_10']
DII_dysfuntionalimpulsivity['DII_22'] = DII_clean['DII_22']
DII_dysfuntionalimpulsivity['DII_23'] = DII_clean['DII_23']
DII_dysfuntionalimpulsivity['DII_7'] = DII_clean['DII_7']
DII_dysfuntionalimpulsivity['DII_1'] = DII_clean['DII_1']
DII_dysfuntionalimpulsivity['DII_18'] = DII_clean['DII_18']
DII_dysfuntionalimpulsivity['DII_17'] = DII_clean['DII_17']
DII_dysfuntionalimpulsivity['DII_9'] = DII_clean['DII_9']
DII_dysfuntionalimpulsivity['DII_13'] = DII_clean['DII_13']

DII_dysfuntionalimpulsivity = DII_dysfuntionalimpulsivity.astype(int)
DII_score["DII_dysfuntionalimpulsivity"] = DII_dysfuntionalimpulsivity.sum(axis=1)

#%%

dii = pd.DataFrame()
dii['Prolific_ID'] = finaldata['Prolific_ID']
dii['DII_dysfuntionalimpulsivity']= DII_score["DII_dysfuntionalimpulsivity"]
dii['DII_functionalimpulsivity']= DII_score["DII_functionalimpulsivity"]
dii.to_csv('%s/DII.csv' %(path.parent), index=False)

#selfreportdata = pd.read_csv('%s/selfreportdata_master.csv' %(path.parent))
#selfreportdata['DII_functionalimpulsivity'] = DII_score["DII_functionalimpulsivity"]
#selfreportdata['DII_dysfunctionalimpulsivity'] = DII_score["DII_dysfuntionalimpulsivity"]
#selfreportdata.to_csv('%s/selfreportdata_master.csv' %(path.parent), index=False)
