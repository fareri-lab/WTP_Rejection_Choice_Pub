#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 13:43:58 2023

@author: melanieruiz
"""

import pandas as pd
import os
from pathlib import Path


path = Path(r"%s"%(os.getcwd()))
participants = pd.read_excel('%s/participantlist.xlsx'%(path.parent))
participants = participants.loc[
    participants['PhotosUploaded? (y/n)'] == 'y'].reset_index()
participants = pd.DataFrame(data=participants['PROLIFIC_ID'])
participants = participants.sort_values(by=['PROLIFIC_ID'])

selfreportdata = pd.read_csv('%s/selfreportdata_master_DF.csv' %(path))
selfreportdata['PROLIFIC_ID'] = participants["PROLIFIC_ID"]
selfreportdata.to_csv('%s/selfreportdata_master_DF.csv' %(path), index=False)

phase = input('Pre? Post? or Both? ')

#import pre-surveys

if phase == 'Pre': 
    os.chdir('%s/Pre' %(path))
    import AQ_Scoring, BRCS_Scoring, ERQ_Scoring, NTBS_Scoring, PSS_Scoring, RSQ_Scoring, SCS_Scoring, SRQ_Scoring
elif phase == 'Post':
    os.chdir('%s/Post' %(path))
    import DAST_Scoring, DII_Scoring, LSAS_Scoring, MSPSS_Scoring, RR_Scoring
elif phase == 'Both':
    os.chdir('%s/Pre' %(path))
    import AQ_Scoring, BRCS_Scoring, ERQ_Scoring, NTBS_Scoring, PSS_Scoring, RSQ_Scoring, SCS_Scoring, SRQ_Scoring
    os.chdir('%s/Post' %(path))
    import DAST_Scoring, DII_Scoring, MSPSS_Scoring, RR_Scoring, LSAS_Scoring
else:
    print('Please enter Pre, Post, or Both')
    


# if __name__ == "__main__":
#     for script in os.listdir(scoring_path):
#           if script.endswith('.py'):
#               os.system('python3 %s/%s' %(scoring_path,script))
