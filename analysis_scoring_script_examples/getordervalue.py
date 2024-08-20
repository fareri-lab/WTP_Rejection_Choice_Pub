#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 13:31:24 2023

@author: jordansiegel
"""


from pathlib import Path
import pandas as pd 
import numpy as np
import os

#read in participant list
current_dir = os.getcwd()

participants = pd.read_excel('participantlist.xlsx')

#toberecoded = participants.loc[participants['afterstresschange']== 0].reset_index(drop=True)
participants = participants.loc[
    participants['PhotosUploaded? (y/n)'] == 'y'].reset_index()
columns = ['PROLIFIC_ID','afterstresschange','timebetween','sex','age']
participants =participants[columns]
participants = pd.DataFrame(data = participants.sort_values(by='PROLIFIC_ID').reset_index(drop=True))

participants['order'] = ''
order = ''
#%%

data_path = os.getcwd()+'/data/'
for csv in sorted(os.listdir(data_path)):
    for sub in range(0,len(participants)):
        if csv.startswith(participants['PROLIFIC_ID'][sub]):
            participantdata = pd.read_csv(data_path+csv)
            participantdata['PROLIFIC_ID']=participantdata['PROLIFIC_ID'][0]
            if participantdata.loc[3,'TrialNumber'] == 1:
                if participantdata.loc[3,'Condition'] == 'Neutral':
                    order = 0
                elif participantdata.loc[3,'Condition'] == 'Rej':
                    order= 12
                elif participantdata.loc[3,'Condition'] == 'Acc':
                    order= 21
            if order == 12 or order == 21:
                 participants['order'][sub] = order
            elif order == '' or order == 0:
              if participantdata.loc[39,'TrialNumber'] == 31:
                  if participantdata.loc[39,'Condition'] == 'Neutral':
                      order = 0
                  elif participantdata.loc[39,'Condition'] == 'Rej':
                      order= 12 
                  elif participantdata.loc[39,'Condition'] == 'Acc':
                      order= 21    
            if order == 12 or order == 21:
                   participants['order'][sub] = order
            elif order == '' or order == 0: 
                    if participantdata.loc[75,'TrialNumber'] == 61:
                        if participantdata.loc[75,'Condition'] == 'Neutral':
                            order = 0
                        elif participantdata.loc[75,'Condition'] == 'Rej':
                            order= 12               
                        elif participantdata.loc[75,'Condition'] == 'Acc':
                            order= 21
            if order == 12 or order == 21:
                    participants['order'][sub] = order
                
       
