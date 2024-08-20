#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 11:00:05 2023

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

# path = Path(r"%s"%(os.getcwd()))
# # read in participant list
# current_dir = os.getcwd()
# participants = pd.read_excel('%s/participantlist.xlsx'%(path.parent.parent))
# participants = participants.loc[
#     participants['PhotosUploaded? (y/n)'] == 'y'].reset_index()


# no_data = participants.loc[
#     participants['post-task survey'] == 0].reset_index()
# if len(no_data) > 1:
#     no_data = no_data[no_data['surveys_missing'].str.contains("RR")]
#     no_data = pd.DataFrame(data= no_data['PROLIFIC_ID'])

# participants = participants.loc[
#     participants['post-task survey'] == 1].reset_index()







#%%

#columns list
RR_cols = [col for col in alldata.columns if 'RR_' in col]
ProlificID_cols = [col for col in alldata.columns if 'PROLIFIC_ID' in col]

RR = alldata.filter(regex='RR_|PROLIFIC_ID')

#%%
RR_clean = pd.DataFrame()


for i in range(0, len(RR)):
    if RR.loc[i,'PROLIFIC_ID'] in participants['PROLIFIC_ID'].values:
       RR_clean[i] = RR.loc[i]    

finaldata = pd.DataFrame()


RR_clean = RR_clean.transpose()
RR_clean = RR_clean.reset_index()
finaldata['Prolific_ID'] = RR_clean['PROLIFIC_ID']
RR_clean = RR_clean.drop(['index'], axis = 1)
RR_clean = RR_clean.drop(['PROLIFIC_ID'], axis = 1)
RR_clean = RR_clean.replace(np.nan, 0)

#%%
RR_score = pd.DataFrame(columns = RR_clean.columns, index = RR_clean.index)


#%%
for k in range(0,len(RR_clean)):
    for i in range (0,len(RR_clean.columns)):
        RR_score[RR_clean.columns[i]][k] = RR_clean.loc[k,RR_clean.columns[i]]
        
RR_score= RR_score.astype(int)
RR_score["RR_totalscore"] = RR_score.sum(axis=1)
#those with no data needs a total score column too
# if len(no_data) > 1:
#     RR_score.loc[len(RR_score)+1] = '-'
#     participants.loc(len(RR_score)+1) = no_data['PROLIFIC_ID'] #!!!!!!!
# RR_score.insert(0, 'PROLIFIC_ID', participants)
#%%








#%%
rr = pd.DataFrame()
rr['Prolific_ID'] = finaldata['Prolific_ID']
rr['RR_score']= RR_score["RR_totalscore"]
rr.to_csv('%s/rr.csv' %(path.parent), index=False)

# selfreportdata = pd.read_csv('%s/selfreportdata_master.csv' %(path.parent))
# selfreportdata['RR'] = RR_score["RR_totalscore"]
# selfreportdata.to_csv('%s/selfreportdata_master.csv' %(path.parent), index=False)

