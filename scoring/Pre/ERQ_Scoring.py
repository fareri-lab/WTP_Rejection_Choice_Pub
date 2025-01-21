#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 19:18:14 2023

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


pretask_survey = '%s/' %(str(path.parent.parent)) + [pretask for pretask in os.listdir(path.parent.parent) if pretask.startswith('WTP_Pretask')][0]
#read in raw qualtrics data
alldata = pd.read_csv(pretask_survey)

alldata = alldata.iloc[4:]
alldata = alldata.sort_values(by=['Prolific_ID'])
alldata.pop("attnchk")  # remove attention checks
alldata = alldata.reset_index()

# %%
#columns list
ERQ_cols = [col for col in alldata.columns if 'ERQ' in col]
ProlificID_cols = [col for col in alldata.columns if 'Prolific_' in col]


ERQ = alldata.filter(regex='ERQ_|Prolific_ID')


# %%
ERQ_clean = pd.DataFrame()

for i in range(0, len(ERQ)):
    if ERQ.loc[i,'Prolific_ID'] in participants['PROLIFIC_ID'].values:
       ERQ_clean[i] = ERQ.loc[i]    

finaldata = pd.DataFrame()


ERQ_clean = ERQ_clean.transpose()
ERQ_clean = ERQ_clean.reset_index()
finaldata['Prolific_ID'] = ERQ_clean['Prolific_ID']
ERQ_clean = ERQ_clean.drop(['index'], axis = 1)
ERQ_clean = ERQ_clean.drop(['Prolific_ID'], axis = 1)
# %%
ERQ_score = pd.DataFrame(columns = ERQ_clean.columns, index = ERQ_clean.index)

#%%
ERQ_cogreappraisal = pd.DataFrame()

ERQ_cogreappraisal['ERQ_1'] = ERQ_clean['ERQ_1']
ERQ_cogreappraisal['ERQ_3'] = ERQ_clean['ERQ_12']
ERQ_cogreappraisal['ERQ_5'] = ERQ_clean['ERQ_14']
ERQ_cogreappraisal['ERQ_7'] = ERQ_clean['ERQ_16']
ERQ_cogreappraisal['ERQ_8'] = ERQ_clean['ERQ_17']
ERQ_cogreappraisal['ERQ_10'] = ERQ_clean['ERQ_19']

ERQ_cogreappraisal= ERQ_cogreappraisal.astype(int)
ERQ_cogreappraisal["ERQ_cogreappraisal"] = ERQ_cogreappraisal.sum(axis=1)/6

#%%

ERQ_emosuppression = pd.DataFrame()
ERQ_emosuppression['ERQ_2'] = ERQ_clean['ERQ_11']
ERQ_emosuppression['ERQ_4'] = ERQ_clean['ERQ_13']
ERQ_emosuppression['ERQ_6'] = ERQ_clean['ERQ_15']
ERQ_emosuppression['ERQ_9'] = ERQ_clean['ERQ_18']


ERQ_emosuppression= ERQ_emosuppression.astype(int)
ERQ_emosuppression["ERQ_emosuppression"] = ERQ_emosuppression.sum(axis=1)/4

#%%

erq = pd.DataFrame()
erq['Prolific_ID'] = finaldata['Prolific_ID']
erq['ERQ_emosuppression']= ERQ_emosuppression["ERQ_emosuppression"]
erq['ERQ_cogreappraisal'] = ERQ_cogreappraisal["ERQ_cogreappraisal"]
erq.to_csv('%s/erq.csv' %(path.parent), index=False)


# selfreportdata = pd.read_csv('%s/selfreportdata_master_DF.csv' %(path.parent))
# selfreportdata['ERQ_emosuppression'] = ERQ_emosuppression["ERQ_emosuppression"]
# selfreportdata['ERQ_cogreappraisal'] = ERQ_cogreappraisal["ERQ_cogreappraisal"]
# selfreportdata.to_csv('%s/selfreportdata_master_DF.csv' %(path.parent), index=False)
