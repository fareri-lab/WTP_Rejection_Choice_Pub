#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 15:11:17 2025

@author: jordansiegel
"""

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

posttask_survey = '%s/' %(str(path.parent.parent)) + [posttask for posttask in os.listdir(path.parent.parent) if posttask.startswith('WTP_PostTask')][0]
#read in raw qualtrics data
alldata = pd.read_csv(posttask_survey)
alldata = alldata.iloc[2:]
alldata = alldata.sort_values(by=['PROLIFIC_ID'])
alldata.pop("Attnchk")  # remove attention checks
alldata = alldata.reset_index()


# %%
#columns list
UCLA_cols = [col for col in alldata.columns if 'UCLA_' in col]
ProlificID_cols = [col for col in alldata.columns if 'PROLIFIC_ID' in col]


UCLA = alldata.filter(regex='UCLA_|post_task')
#%%
UCLA_clean = pd.DataFrame()

for i in range(0,len(UCLA)):
    if UCLA.loc[i,'post_task'] in participants['PROLIFIC_ID'].values:
       UCLA_clean[i] = UCLA.loc[i]    

finaldata = pd.DataFrame()


UCLA_clean = UCLA_clean.transpose()
UCLA_clean = UCLA_clean.reset_index()
finaldata['Prolific_ID'] = UCLA_clean['post_task']
UCLA_clean = UCLA_clean.drop(['index'], axis = 1)
UCLA_clean = UCLA_clean.drop(['post_task'], axis = 1)
UCLA_clean= UCLA_clean.astype(int)
#%%
UCLA_score = pd.DataFrame(columns = UCLA_clean.columns, index = UCLA_clean.index)

#%%

UCLA_score= UCLA_score.astype(int)
UCLA_score["UCLA"] = UCLA_score.sum(axis=1)
#%%
ucla = pd.DataFrame()
ucla['Prolific_ID'] = finaldata['Prolific_ID']
ucla['UCLA_score']= UCLA_score["UCLA"]
ucla.to_csv('%s/ucla.csv' %(path.parent), index=False)

#selfreportdata = pd.read_csv('%s/selfreportdata_master_DF.csv' %(path.parent))
#selfreportdata['DAST'] = DAST_score["DAST"]
#selfreportdata.to_csv('%s/selfreportdata_master_DF.csv' %(path.parent), index=False)
