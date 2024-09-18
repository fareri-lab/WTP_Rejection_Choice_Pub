#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 22:23:09 2023

@author: jordansiegel
"""

import pandas as pd
import os
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
DAST_cols = [col for col in alldata.columns if 'DAST_' in col]
ProlificID_cols = [col for col in alldata.columns if 'PROLIFIC_ID' in col]


DAST = alldata.filter(regex='DAST_|post_task')
#%%
DAST_clean = pd.DataFrame()

for i in range(0,len(DAST)):
    if DAST.loc[i,'post_task'] in participants['PROLIFIC_ID'].values:
       DAST_clean[i] = DAST.loc[i]    

finaldata = pd.DataFrame()


DAST_clean = DAST_clean.transpose()
DAST_clean = DAST_clean.reset_index()
finaldata['Prolific_ID'] = DAST_clean['post_task']
DAST_clean = DAST_clean.drop(['index'], axis = 1)
DAST_clean = DAST_clean.drop(['post_task'], axis = 1)
DAST_clean= DAST_clean.astype(int)
#%%
DAST_score = pd.DataFrame(columns = DAST_clean.columns, index = DAST_clean.index)

#%%
reverse_score= [4, 5, 7]

for k in range(0,len(DAST_clean)):
    for i in range (1,len(DAST_clean.columns)+1):
        if i in reverse_score:
            if DAST_clean.loc[k,'DAST_' + str(i)] == 0:
                DAST_score['DAST_' + str(i)][k] = 1
            elif DAST_clean.loc[k,'DAST_'+ str(i)] == 1:
                DAST_score['DAST_' + str(i)][k] = 0
            
        else:
            DAST_score['DAST_' +str(i)][k] = DAST_clean.loc[k,'DAST_'+ str(i)]
DAST_score= DAST_score.astype(int)
DAST_score["DAST"] = DAST_score.sum(axis=1)
#%%
dast = pd.DataFrame()
dast['Prolific_ID'] = finaldata['Prolific_ID']
dast['DAST_score']= DAST_score["DAST"]
dast.to_csv('%s/dast.csv' %(path.parent), index=False)

#selfreportdata = pd.read_csv('%s/selfreportdata_master_DF.csv' %(path.parent))
#selfreportdata['DAST'] = DAST_score["DAST"]
#selfreportdata.to_csv('%s/selfreportdata_master_DF.csv' %(path.parent), index=False)
