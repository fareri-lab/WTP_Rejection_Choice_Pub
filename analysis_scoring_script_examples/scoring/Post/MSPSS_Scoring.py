#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 11:14:21 2023

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
MSPSS_cols = [col for col in alldata.columns if 'MSPSS_' in col]
ProlificID_cols = [col for col in alldata.columns if 'PROLIFIC_ID' in col]

MSPSS = alldata.filter(regex='MSPSS_|PROLIFIC_ID')

#%%
MSPSS_clean = pd.DataFrame()


for i in range(0, len(MSPSS)):
    if MSPSS.loc[i,'PROLIFIC_ID'] in participants['PROLIFIC_ID'].values:
       MSPSS_clean[i] = MSPSS.loc[i]    

finaldata = pd.DataFrame()


MSPSS_clean = MSPSS_clean.transpose()
MSPSS_clean = MSPSS_clean.reset_index()
finaldata['Prolific_ID'] = MSPSS_clean['PROLIFIC_ID']
MSPSS_clean = MSPSS_clean.drop(['index'], axis = 1)
MSPSS_clean = MSPSS_clean.drop(['PROLIFIC_ID'], axis = 1)
MSPSS_clean = MSPSS_clean.replace(np.nan, 0)
MSPSS_clean = MSPSS_clean.astype(int)

#%%
MSPSS_score = pd.DataFrame(columns = MSPSS_clean.columns, index = MSPSS_clean.index)

#%%

for k in range(0,len(MSPSS_clean)):
    for i in range (1,len(MSPSS_clean.columns)+1):

        MSPSS_score['MSPSS_' +str(i)][k] = MSPSS_clean.loc[k,'MSPSS_'+ str(i)]


MSPSS_score["MSPSS_totalscore"] = MSPSS_score.sum(axis=1)/12

#%%

mspss = pd.DataFrame()
mspss['Prolific_ID'] = finaldata['Prolific_ID']
mspss['MSPSS_score']= MSPSS_score["MSPSS_totalscore"]
mspss.to_csv('%s/mspss.csv' %(path.parent), index=False)

# selfreportdata = pd.read_csv('%s/selfreportdata_master.csv' %(path.parent))
# selfreportdata['MSPSS'] = MSPSS_score["MSPSS_totalscore"]
# selfreportdata.to_csv('%s/selfreportdata_master.csv' %(path.parent), index=False)
