#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 19:55:36 2023

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
SRQ_cols = [col for col in alldata.columns if 'SRQ' in col]
ProlificID_cols = [col for col in alldata.columns if 'Prolific_' in col]


SRQ = alldata.filter(regex='SRQ_|Prolific_ID')


# %%
SRQ_clean = pd.DataFrame()

for i in range(0, len(SRQ)):
    if SRQ.loc[i,'Prolific_ID'] in participants['PROLIFIC_ID'].values:
       SRQ_clean[i] = SRQ.loc[i]    

finaldata = pd.DataFrame()


SRQ_clean = SRQ_clean.transpose()
SRQ_clean = SRQ_clean.reset_index()
finaldata['Prolific_ID'] = SRQ_clean['Prolific_ID']
SRQ_clean = SRQ_clean.drop(['index'], axis = 1)
SRQ_clean = SRQ_clean.drop(['Prolific_ID'], axis = 1)
SRQ_clean = SRQ_clean.fillna(0)
#%%

SRQ_admiration = pd.DataFrame()

SRQ_admiration['SRQ_1'] = SRQ_clean['SRQ_1']
SRQ_admiration['SRQ_7'] = SRQ_clean['SRQ_7']
SRQ_admiration['SRQ_11'] = SRQ_clean['SRQ_11']
SRQ_admiration['SRQ_18'] = SRQ_clean['SRQ_18']


SRQ_admiration= SRQ_admiration.astype(int)
SRQ_admiration["SRQ_admiration"] = SRQ_admiration.sum(axis=1)/4

#%%

SRQ_negsocpot = pd.DataFrame()

SRQ_negsocpot['SRQ_3'] = SRQ_clean['SRQ_3']
SRQ_negsocpot['SRQ_5'] = SRQ_clean['SRQ_5']
SRQ_negsocpot['SRQ_8'] = SRQ_clean['SRQ_8']
SRQ_negsocpot['SRQ_14'] = SRQ_clean['SRQ_14']
SRQ_negsocpot['SRQ_17'] = SRQ_clean['SRQ_17']


SRQ_negsocpot= SRQ_negsocpot.astype(int)
SRQ_negsocpot["SRQ_negsocpot"] = SRQ_negsocpot.sum(axis=1)/5

#%%

SRQ_passivity = pd.DataFrame()

SRQ_passivity['SRQ_12'] = SRQ_clean['SRQ_12']
SRQ_passivity['SRQ_21'] = SRQ_clean['SRQ_21']
SRQ_passivity['SRQ_23'] = SRQ_clean['SRQ_23']

SRQ_passivity= SRQ_passivity.astype(int)
SRQ_passivity["SRQ_passivity"] = SRQ_passivity.sum(axis=1)/3

#%%

SRQ_prosocint = pd.DataFrame()

SRQ_prosocint['SRQ_2'] = SRQ_clean['SRQ_2']
SRQ_prosocint['SRQ_6'] = SRQ_clean['SRQ_6']
SRQ_prosocint['SRQ_16'] = SRQ_clean['SRQ_16']
SRQ_prosocint['SRQ_19'] = SRQ_clean['SRQ_19']
SRQ_prosocint['SRQ_22'] = SRQ_clean['SRQ_22']


SRQ_prosocint= SRQ_prosocint.astype(int)
SRQ_prosocint["SRQ_prosocint"] = SRQ_prosocint.sum(axis=1)/5

#%%

SRQ_sexrel = pd.DataFrame()

SRQ_sexrel['SRQ_9'] = SRQ_clean['SRQ_9']
SRQ_sexrel['SRQ_13'] = SRQ_clean['SRQ_13']
SRQ_sexrel['SRQ_20'] = SRQ_clean['SRQ_20']

SRQ_sexrel= SRQ_sexrel.astype(int)
SRQ_sexrel["SRQ_sexrel"] = SRQ_sexrel.sum(axis=1)/3

#%%

SRQ_sociability = pd.DataFrame()

SRQ_sociability['SRQ_4'] = SRQ_clean['SRQ_4']
SRQ_sociability['SRQ_10'] = SRQ_clean['SRQ_10']
SRQ_sociability['SRQ_15'] = SRQ_clean['SRQ_15']

SRQ_sociability= SRQ_sociability.astype(int)
SRQ_sociability["SRQ_sociability"] = SRQ_sociability.sum(axis=1)/3

#%%

srq = pd.DataFrame()
srq['Prolific_ID'] = finaldata['Prolific_ID']
srq["SRQ_admiration"]= SRQ_admiration["SRQ_admiration"]
srq['SRQ_negsocpot'] = SRQ_negsocpot["SRQ_negsocpot"]
srq['SRQ_prosocint'] = SRQ_prosocint["SRQ_prosocint"]
srq['SRQ_sexrel'] = SRQ_sexrel["SRQ_sexrel"]
srq['SRQ_sociability'] = SRQ_sociability["SRQ_sociability"]
srq.to_csv('%s/srq.csv' %(path.parent), index=False)


# selfreportdata = pd.read_csv('%s/selfreportdata_master_DF.csv' %(path.parent))
# selfreportdata['SRQ_admiration'] = SRQ_admiration["SRQ_admiration"]
# selfreportdata['SRQ_negsocpot'] = SRQ_negsocpot["SRQ_negsocpot"]
# selfreportdata['SRQ_prosocint'] = SRQ_prosocint["SRQ_prosocint"]
# selfreportdata['SRQ_sexrel'] = SRQ_sexrel["SRQ_sexrel"]
# selfreportdata['SRQ_sociability'] = SRQ_sociability["SRQ_sociability"]
# selfreportdata.to_csv('%s/selfreportdata_master_DF.csv' %(path.parent), index=False)
