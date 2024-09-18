#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 12:27:47 2022

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
RSQ_cols = [col for col in alldata.columns if 'RSQ_' in col]
ProlificID_cols = [col for col in alldata.columns if 'Prolific_' in col]


RSQ = alldata.filter(regex='RSQ_|Prolific_ID')


# %%
RSQ_clean = pd.DataFrame()

for i in range(0, len(RSQ)):
    if RSQ.loc[i,'Prolific_ID'] in participants['PROLIFIC_ID'].values:
       RSQ_clean[i] = RSQ.loc[i]    

finaldata = pd.DataFrame()


RSQ_clean = RSQ_clean.transpose()
RSQ_clean = RSQ_clean.reset_index()
finaldata['Prolific_ID'] = RSQ_clean['Prolific_ID']
RSQ_clean = RSQ_clean.drop(['index'], axis = 1)
RSQ_clean = RSQ_clean.drop(['Prolific_ID'], axis = 1)

#%%
RSQ_score = pd.DataFrame(columns = RSQ_clean.columns, index = RSQ_clean.index)
reverse_score = [col for col in RSQ_clean.columns if 'b' in col]
noreverse_score = [col for col in RSQ_clean.columns if 'a' in col]

for k in range(0,len(RSQ_clean)):
    for i in range (0,len(RSQ_clean.columns)):

        if RSQ_clean.columns[i] in reverse_score:
            if RSQ_clean.loc[k,RSQ_clean.columns[i]] == '6':
                RSQ_score[RSQ_clean.columns[i]][k] = 1
            elif RSQ_clean.loc[k,RSQ_clean.columns[i]] == '5':
                RSQ_score[RSQ_clean.columns[i]][k] = 2
            elif RSQ_clean.loc[k,RSQ_clean.columns[i]] == '4':
                RSQ_score[RSQ_clean.columns[i]][k] = 3
            elif RSQ_clean.loc[k,RSQ_clean.columns[i]] == '3':
                RSQ_score[RSQ_clean.columns[i]][k] = 4
            elif RSQ_clean.loc[k,RSQ_clean.columns[i]] == '2':
                RSQ_score[RSQ_clean.columns[i]][k] = 5
            elif RSQ_clean.loc[k,RSQ_clean.columns[i]] == '1':
                RSQ_score[RSQ_clean.columns[i]][k] = 6
        else:
            RSQ_score[RSQ_clean.columns[i]][k] = RSQ_clean.loc[k,RSQ_clean.columns[i]]

RSQ_score= RSQ_score.astype(int)
#%%
RSQ_average = pd.DataFrame()

RSQ_average['RS_1'] = RSQ_score['RSQ_1a']* RSQ_score['RSQ_1b']
RSQ_average['RS_2'] = RSQ_score['RSQ_2a']* RSQ_score['RSQ_2b']
RSQ_average['RS_3'] = RSQ_score['RSQ_3a']* RSQ_score['RSQ_3b']
RSQ_average['RS_4'] = RSQ_score['RSQ_4a']* RSQ_score['RSQ_4b']
RSQ_average['RS_5'] = RSQ_score['RSQ_5a']* RSQ_score['RSQ_5b']
RSQ_average['RS_6'] = RSQ_score['RSQ_6a']* RSQ_score['RSQ_6b']
RSQ_average['RS_7'] = RSQ_score['RSQ_7a']* RSQ_score['RSQ_7b']
RSQ_average['RS_8'] = RSQ_score['RSQ_8a']* RSQ_score['RSQ_8b']

RSQ_average['RSQ_finalscore'] = RSQ_average.sum(axis=1)/8
#%%

rsq = pd.DataFrame()
rsq['Prolific_ID'] = finaldata['Prolific_ID']
rsq["RSQ_finalscore"]= RSQ_average['RSQ_finalscore']
rsq.to_csv('%s/rsq.csv' %(path.parent), index=False)

# selfreportdata = pd.read_csv('%s/selfreportdata_master_DF.csv' %(path.parent))
# selfreportdata['RSQ'] = RSQ_average["RSQ_finalscore"]
# selfreportdata.to_csv('%s/selfreportdata_master_DF.csv' %(path.parent), index=False)

