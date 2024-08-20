#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 11:31:15 2023

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
BRCS_cols = [col for col in alldata.columns if 'BRCS_' in col]
ProlificID_cols = [col for col in alldata.columns if 'Prolific_' in col]


BRCS = alldata.filter(regex='BRCS_|Prolific_ID')


# %%
BRCS_clean = pd.DataFrame()

for i in range(0,len(BRCS)):
    if BRCS.loc[i,'Prolific_ID'] in participants['PROLIFIC_ID'].values:
       BRCS_clean[i] = BRCS.loc[i]    

finaldata = pd.DataFrame()


BRCS_clean = BRCS_clean.transpose()
BRCS_clean = BRCS_clean.reset_index()
finaldata['Prolific_ID'] = BRCS_clean['Prolific_ID']
BRCS_clean = BRCS_clean.drop(['index'], axis = 1)
BRCS_clean = BRCS_clean.drop(['Prolific_ID'], axis = 1)

#%%
BRCS_score = pd.DataFrame(columns = BRCS_clean.columns, index = BRCS_clean.index)

for k in range(0,len(BRCS_clean)):
    for i in range (0,len(BRCS_clean.columns)):
        BRCS_score[BRCS_clean.columns[i]][k] = BRCS_clean.loc[k,BRCS_clean.columns[i]]
        
BRCS_score= BRCS_score.astype(int)
BRCS_score["BRCS_total_score"] = BRCS_score.sum(axis=1)

#%%

brcs = pd.DataFrame()
brcs['Prolific_ID'] = finaldata['Prolific_ID']
brcs['BCRS_total_score']= BRCS_score["BRCS_total_score"]
brcs.to_csv('%s/brcs.csv' %(path.parent), index=False)

# selfreportdata = pd.read_csv('%s/selfreportdata_master_DF.csv' %(path.parent))
# selfreportdata['BRCS'] = BRCS_score["BRCS_total_score"]
# selfreportdata.to_csv('%s/selfreportdata_master_DF.csv' %(path.parent), index=False)


