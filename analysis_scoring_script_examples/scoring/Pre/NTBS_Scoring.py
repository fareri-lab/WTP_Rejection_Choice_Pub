#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 19:48:26 2023

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


pretask_survey = '%s/' %(str(path.parent.parent)) + [pretask for pretask in os.listdir(path.parent.parent) if pretask.startswith('RejectionChoice_PreTask')][0]
#read in raw qualtrics data
alldata = pd.read_csv(pretask_survey)
alldata = alldata.iloc[4:]
alldata = alldata.sort_values(by=['Prolific_ID'])
alldata.pop("attnchk")  # remove attention checks
alldata = alldata.reset_index()

# %%
#columns list
NTBS_cols = [col for col in alldata.columns if 'NTBS' in col]
ProlificID_cols = [col for col in alldata.columns if 'Prolific_' in col]


NTBS = alldata.filter(regex='NTBS|Prolific_ID')


# %%
NTBS_clean = pd.DataFrame()

for i in range(0, len(NTBS)):
    if NTBS.loc[i,'Prolific_ID'] in participants['PROLIFIC_ID'].values:
       NTBS_clean[i] = NTBS.loc[i]    

finaldata = pd.DataFrame()


NTBS_clean = NTBS_clean.transpose()
NTBS_clean = NTBS_clean.reset_index()
finaldata['Prolific_ID'] = NTBS_clean['Prolific_ID']
NTBS_clean = NTBS_clean.drop(['index'], axis = 1)
NTBS_clean = NTBS_clean.drop(['Prolific_ID'], axis = 1)
# %%
NTBS_score = pd.DataFrame(columns = NTBS_clean.columns, index = NTBS_clean.index)

for k in range(0,len(NTBS_clean)):
    for i in range (0,len(NTBS_clean.columns)):
        NTBS_score[NTBS_clean.columns[i]][k] = NTBS_clean.loc[k,NTBS_clean.columns[i]]
        
NTBS_score= NTBS_score.astype(int)
NTBS_score["NTBS"] = NTBS_score.sum(axis=1)
#%%
ntbs = pd.DataFrame()
ntbs['Prolific_ID'] = finaldata['Prolific_ID']
ntbs['NTBS_score']= NTBS_score["NTBS"]
ntbs.to_csv('%s/ntbs.csv' %(path.parent), index=False)

# selfreportdata = pd.read_csv('%s/selfreportdata_master_DF.csv' %(path.parent))
# selfreportdata['NTBS'] = NTBS_score["NTBS"]
# selfreportdata.to_csv('%s/selfreportdata_master_DF.csv' %(path.parent), index=False)
