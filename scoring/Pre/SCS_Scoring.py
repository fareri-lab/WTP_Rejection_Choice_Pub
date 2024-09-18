#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 12:33:50 2023

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

#columns list
SCS_cols = [col for col in alldata.columns if 'SCS_' in col]
SCS = alldata.filter(regex='SCS_|Prolific_ID')


# %%
SCS_clean = pd.DataFrame()

for i in range(0,len(SCS)):
    if SCS.loc[i,'Prolific_ID'] in participants['PROLIFIC_ID'].values:
       SCS_clean[i] = SCS.loc[i]    

finaldata = pd.DataFrame()


SCS_clean = SCS_clean.transpose()
SCS_clean = SCS_clean.reset_index()
finaldata['Prolific_ID'] = SCS_clean['Prolific_ID']
SCS_clean = SCS_clean.drop(['index'], axis = 1)
SCS_clean = SCS_clean.drop(['Prolific_ID'], axis = 1)
SCS_clean= SCS_clean.astype(int)
#%%
SCS_score = pd.DataFrame(columns = SCS_clean.columns, index = SCS_clean.index)
#%%
reverse_score = [1, 2, 3, 4, 5, 6, 8, 10, 15, 18]

for k in range(0,len(SCS_clean)):
    for i in range (1,len(SCS_clean.columns)+1):
        if i in reverse_score:
            if SCS_clean.loc[k,'SCS_' + str(i)] == 6:
                SCS_score['SCS_' + str(i)][k] = 1
            elif SCS_clean.loc[k,'SCS_' + str(i)] == 5:
                SCS_score['SCS_' + str(i)][k] = 2
            elif SCS_clean.loc[k,'SCS_' + str(i)] == 4:
                SCS_score['SCS_' + str(i)][k] = 3
            elif SCS_clean.loc[k,'SCS_' + str(i)] == 3:
                SCS_score['SCS_' + str(i)][k] = 4
            elif SCS_clean.loc[k,'SCS_' + str(i)] == 2:
                SCS_score['SCS_' + str(i)][k] = 5
            elif SCS_clean.loc[k,'SCS_' + str(i)] == 1:
                SCS_score['SCS_' + str(i)][k] = 6
        else:
            SCS_score['SCS_' +str(i)][k] = SCS_clean.loc[k,'SCS_'+ str(i)]

SCS_score= SCS_score.astype(int)

        
SCS_score= SCS_score.astype(int)
SCS_score["SCS_score"] = SCS_score.sum(axis=1)
#%%
scs = pd.DataFrame()
scs['Prolific_ID'] = finaldata['Prolific_ID']
scs["SCS_score"]= SCS_score["SCS_score"]
scs.to_csv('%s/scs.csv' %(path.parent), index=False)

# selfreportdata = pd.read_csv('%s/selfreportdata_master_DF.csv' %(path.parent))
# selfreportdata['SCS'] = SCS_score["SCS_score"]
# selfreportdata.to_csv('%s/selfreportdata_master_DF.csv' %(path.parent), index=False)

