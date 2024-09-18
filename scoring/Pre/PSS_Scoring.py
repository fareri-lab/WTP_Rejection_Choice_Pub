#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 21:53:51 2023

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
PSS_cols = [col for col in alldata.columns if 'PerceivedStress_' in col]
PSS = alldata.filter(regex='PerceivedStress_|Prolific_ID')


# %%
PSS_clean = pd.DataFrame()

for i in range(0,len(PSS)):
    if PSS.loc[i,'Prolific_ID'] in participants['PROLIFIC_ID'].values:
       PSS_clean[i] = PSS.loc[i]    

finaldata = pd.DataFrame()


PSS_clean = PSS_clean.transpose()
PSS_clean = PSS_clean.reset_index()
finaldata['Prolific_ID'] = PSS_clean['Prolific_ID']
PSS_clean = PSS_clean.drop(['index'], axis = 1)
PSS_clean = PSS_clean.drop(['Prolific_ID'], axis = 1)
PSS_clean= PSS_clean.astype(int)
#%%
PSS_score = pd.DataFrame(columns = PSS_clean.columns, index = PSS_clean.index)
#%%
reverse_score= [4, 5, 7, 8,]

for k in range(0,len(PSS_clean)):
    for i in range (1,len(PSS_clean.columns)+1):
        if i in reverse_score:
            if PSS_clean.loc[k,'PerceivedStress_' + str(i)] == 4:
                PSS_score['PerceivedStress_' + str(i)][k] = 0
            elif PSS_clean.loc[k,'PerceivedStress_' + str(i)] == 3:
                PSS_score['PerceivedStress_' + str(i)][k] = 1
            elif PSS_clean.loc[k,'PerceivedStress_' + str(i)] == 2:
                PSS_score['PerceivedStress_' + str(i)][k] = 2
            elif PSS_clean.loc[k,'PerceivedStress_' + str(i)] == 1:
                PSS_score['PerceivedStress_' + str(i)][k] = 3
            elif PSS_clean.loc[k,'PerceivedStress_' + str(i)] == 0:
                PSS_score['PerceivedStress_' + str(i)][k] = 4
        else:
            PSS_score['PerceivedStress_' +str(i)][k] = PSS_clean.loc[k,'PerceivedStress_'+ str(i)]
PSS_score= PSS_score.astype(int)
#%%
PSS_score["PSS_score"] = PSS_score.sum(axis=1)
#%%
pss = pd.DataFrame()
pss['Prolific_ID'] = finaldata['Prolific_ID']
pss["PSS_score"]= PSS_score["PSS_score"]
pss.to_csv('%s/pss.csv' %(path.parent), index=False)


# selfreportdata = pd.read_csv('%s/selfreportdata_master_DF.csv' %(path.parent))
# selfreportdata['PSS'] = PSS_score["PSS_score"]
# selfreportdata.to_csv('%s/selfreportdata_master_DF.csv' %(path.parent), index=False)
