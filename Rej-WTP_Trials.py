#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 21:27:39 2023

@author: melanieruiz
"""

import os
import pandas as pd
from itertools import product

completedparticipantlist = pd.read_excel('participantlist.xlsx')
completedparticipantlist = completedparticipantlist.loc[
    completedparticipantlist['PhotosUploaded? (y/n)'] == 'n']
completedparticipantlist = completedparticipantlist['PROLIFIC_ID'].reset_index()
completedparticipantlist= completedparticipantlist.drop(['index'], axis=1)
exp = pd.read_csv('WTP-Rej_Experiences_103024.csv', encoding = 'latin1')

clean = exp.filter(regex='ocial_A')
clean.insert(0, 'PROLIFIC_PID', exp['PROLIFIC_PID'])

path = os.getcwd()
# parent = Path(path).parents[1]

# sub_data = clean[clean["dem_ID"].str.contains(sub)]



#%%
template = pd.read_excel('WTP_trials_template.xlsx')

sub_folders= path + '/Participant_Images/'
for sub in completedparticipantlist['PROLIFIC_ID']:
    if not sub.endswith('.DS_Store'): 
        if not sub.startswith('101'): #we do not want DS store or blank file
            sub_exp = clean.loc[
            clean['PROLIFIC_PID'] == sub]
            all_exp= pd.DataFrame()
            sub_path= sub_folders + sub
            #get nonsocial activities
            nonsocial = sub_exp.filter(regex='Nonsocial_A')
            nonsocial=nonsocial.T.reset_index(0)
            nonsocial= nonsocial.drop(['index'], axis=1)
            nonsocial.columns.values[0] = "nonsocial"
    
            # nonsocial= nonsocial.rename(columns={5: "nonsocial"}) #change column number
            nonsocial['type'] =0
            all_exp['nonsocial'] = nonsocial['nonsocial']
            # nonsocial.to_csv('%s/%s_nonsocial.csv'%(subdir,sub), index= False)
            # nonsocial=nonsocial.loc[nonsocial.index.repeat(10)]
            # nonsocial.insert(0, 'trial', range(1,len(nonsocial)+1))
            # nonsocial.insert(1, 'exp_type', nonsocial.rename('NS_{}'.format).index)
            # nonsocial['nonsocial_left'] = np.where(nonsocial.trial % 2, 1, 0)
            # nonsocial.columns.values[0] = "experience"
    
    
    
            #get social activities
            social = sub_exp.filter(regex='Social_A')
            social=social.T.reset_index()
            social= social.drop(['index'], axis=1)
            # social= social.rename(columns={5: "social"}) #change column number
            social.columns.values[0] = "social"
            social['type'] =1
        
            all_exp['social'] = social['social']
    
            #dataframe to split up the experiences on different sides
    
            
            preshuffle = pd.DataFrame(list(product(all_exp['nonsocial'], all_exp['social'])), columns=['right', 'left'])
         
            preshuffle =  preshuffle.sample(frac = 1).reset_index(drop=True)
            preshuffle['social_left'] = 1
            wtp = pd.DataFrame(preshuffle[0:50], index= range(0,100))
            wtp['right'][50:100]= preshuffle['left'][50:100]
            wtp['left'][50:100]= preshuffle['right'][50:100]
            wtp['social_left'][50:100] = 0
            wtp =  wtp.sample(frac = 1).reset_index(drop=True)

            wtp.insert(0,'TrialNumber',range(1,101))
            wtp.insert(3, 'leftmoney', template['LeftPrice'])
            wtp.insert(4, 'rightmoney', template['RightPrice'])
            wtp.insert(5,'WTP_ITI', template['ITI'])
            wtp.to_csv(sub_path + '/%s_WTP.csv' %(sub), index=False)
    
    
    
    # new_wtp.to_csv('')