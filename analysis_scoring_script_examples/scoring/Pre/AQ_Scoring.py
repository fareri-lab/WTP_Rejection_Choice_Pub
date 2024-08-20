#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 21:39:19 2023

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
AQ_cols = [col for col in alldata.columns if 'AQ_' in col]
AQ = alldata.filter(regex='AQ_|Prolific_ID')


# %%
AQ_clean = pd.DataFrame()

for i in range(0,len(AQ)):
    if AQ.loc[i,'Prolific_ID'] in participants['PROLIFIC_ID'].values:
       AQ_clean[i] = AQ.loc[i]    

finaldata = pd.DataFrame()


AQ_clean = AQ_clean.transpose()
AQ_clean = AQ_clean.reset_index()
finaldata['Prolific_ID'] = AQ_clean['Prolific_ID']
AQ_clean = AQ_clean.drop(['index'], axis = 1)
AQ_clean = AQ_clean.drop(['Prolific_ID'], axis = 1)
AQ_clean= AQ_clean.astype(int)
#%%
AQ_score = pd.DataFrame(columns = AQ_clean.columns, index = AQ_clean.index)
#%%

#List of items to be reverse scored
reverse_score= [2, 4, 5, 6, 7, 9, 12, 13, 16, 18, 19, 20, 21, 22, 23, 26, 33, 35, 39, 41, 42, 43, 45, 46]


#Recode each response according to score rules
for k in range(0,len(AQ_clean)):
    for i in range (1,len(AQ_clean.columns)+1):

        if i in reverse_score:
            if AQ_clean.loc[k,'AQ_'+ str(i)] == 1 or AQ_clean.loc[k,'AQ_'+ str(i)] == 2:
                AQ_score['AQ_' +str(i)][k] = 1
            else:
                AQ_score['AQ_'+str(i)][k] = 0
        else:
            if AQ_clean.loc[k,'AQ_'+ str(i)] == 3 or AQ_clean.loc[k,'AQ_'+ str(i)] == 4:
                AQ_score['AQ_' +str(i)][k] = 1
            else:
                AQ_score['AQ_'+str(i)][k] = 0
#%%
AQ_score["AQ_score"] = AQ_score.sum(axis=1)


aq = pd.DataFrame()
aq['Prolific_ID'] = finaldata['Prolific_ID']
aq['AQ']= AQ_score['AQ_score']
aq.to_csv('%s/aq.csv' %(path.parent), index=False)
#AQ_score["AQ_score"].to_CSV('%/aq.csv')%(path.parent), index = False)
#%%
#selfreportdata = pd.read_csv('%s/selfreportdata_master_DF.csv' %(path.parent))
#selfreportdata['AQ'] = AQ_score["AQ_score"]

# aq=pd.DataFrame()
# aq['AQ'] = AQ_score["AQ_score"]
# aq['AQ_score'].to_csv('%s/aq.csv' %(path.parent), index=False)
