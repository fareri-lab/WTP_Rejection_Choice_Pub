#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 14:57:05 2023

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
columns = ['PROLIFIC_ID','afterstresschange']
participants =participants[columns]
participants = pd.DataFrame(data = participants.sort_values(by='PROLIFIC_ID').reset_index(drop=True))




#%%

#read in csvs containing task data
shortformtaskdata = pd.read_csv('Updatedtaskdata_3.2.23.csv')
longformtaskdata = pd.read_csv('RejChoice_MasterData.csv')

#%%


path = Path(r"%s"%(os.getcwd()))
p = Path('%s/data' %(path))

cols = ['PROLIFIC_ID', 'choice', 'condition', 'salience', 'stress', 'afterstresschange', 'rej-acc', 'ifnegvalue']
columns2 = ['PROLIFIC_ID', 'condition_recode', 'afterstresschange','salience_mean', 'stress_mean', 'recoded_stress', 'choice','rej-acc', 'ifnegvalue']
shortform_data= pd.DataFrame(columns = columns2)
#%%

#make rejection data frame
rej_df = pd.DataFrame(index=participants.index, columns = cols)


#%%

#make acceptance data frame
acc_df = pd.DataFrame(index=participants.index, columns = cols)

#%%

#make neutral data frame
neu_df = pd.DataFrame(index=participants.index, columns = cols)
#%%

stressdiffscore = pd.DataFrame(index=participants.index, columns= ['PROLIFIC_ID', 'rejstress', 'accstress', 'difference', 'ifnegvalue'])

#%%
data_path = os.getcwd()+'/data/'
for csv in sorted(os.listdir(data_path)):
    for sub in range(0,len(participants)):
        if csv.startswith(participants['PROLIFIC_ID'][sub]):
            participantdata = pd.read_csv(data_path+csv)
            participantdata['PROLIFIC_ID']=participantdata['PROLIFIC_ID'][0]
            print(participantdata['PROLIFIC_ID'][0])
#participantdata = pd.read_csv('/users/jordansiegel/Documents/GitHub/Rejection_Choice/data/5a4636c92f91ec0001dcba07_RejTask_2022-11-21_17h24.19.149.csv')

#%%
            participantdata['Condition'] = participantdata['Condition'].replace(np.nan,'Empty',regex = True)

#%%
            for row in range(0,len(participantdata)):
                if participantdata['playlottery'][row] == 0 or  participantdata['playlottery'][row] == 1 or  participantdata['playlottery'][row] == 999:
                    if row < 183:
                        if participantdata.loc[row+1,'Condition']== 'Rej':
                            participantdata['Condition'][row] =  participantdata['Condition'][row].replace('Empty', 'Rej')
                        elif participantdata.loc[row+1,'Condition']== 'Neutral':
                             participantdata['Condition'][row] =  participantdata['Condition'][row].replace('Empty', 'Neutral')
                        elif participantdata.loc[row+1,'Condition']== 'Acc':
                            participantdata['Condition'][row] =  participantdata['Condition'][row].replace('Empty', 'Acc')
        
            #%%
                rej_df = participantdata.loc[(participantdata['Condition'] == 'Rej')]
                rej_df = rej_df.reset_index(drop = True)
                
                acc_df= participantdata.loc[(participantdata['Condition'] == 'Acc')]
                acc_df = acc_df.reset_index(drop = True)
                
                neu_df= participantdata.loc[(participantdata['Condition'] == 'Neutral')]
                neu_df = neu_df.reset_index(drop = True)
                
                #recoding condition strings to numbers in subsectioned dataframes
                acc_df['condition_recode'] = 2
                neu_df['condition_recode'] = 0
                rej_df['condition_recode'] = 1 
                
           
                #%%
                rej_df['afterstresschange'] = participants['afterstresschange'][sub]
                acc_df['afterstresschange'] = participants['afterstresschange'][sub]
                neu_df['afterstresschange'] =  participants['afterstresschange'][sub]
                
                #calculate mean salience rating across rejection condition for one participant
                rejection_salience = pd.DataFrame()
                rejection_salience['salience_rating'] = rej_df['salience_rating']
                
                #drop nans and empty spaces to make cumulative sum possible
                rejection_salience= rejection_salience.replace('NAN', np.nan,regex = True)
                rejection_salience = rejection_salience.dropna()
                
                rejection_salience= rejection_salience.astype(int)
                rejection_saliencemean = rejection_salience['salience_rating'].mean()
                # print(rejection_saliencemean)
                
                rejection_salience = rejection_salience.reset_index(drop = True)
                rej_df['salience_mean'] = rejection_saliencemean
                
                #%%
                
                rejection_stress = pd.DataFrame()
                rejection_stress['stress'] = rej_df['stress_level']
                
                rejection_stress= rejection_stress.replace('NAN', np.nan,regex = True)
                rejection_stress = rejection_stress.dropna()
                
                rejection_stress= rejection_stress.astype(int)
                rejection_stressmean = rejection_stress['stress'].mean()
                # print(rejection_stressmean)
                
                rej_df['stress_mean'] = rejection_stressmean
                rej_df['recoded_stress'] = ''
           
                
                
                #%%
                rejection_choice = pd.DataFrame()
                rejection_choice['choice'] = rej_df['playlottery']
                rejection_choice = rejection_choice.dropna()
                rejection_choice.drop(rejection_choice[(rejection_choice['choice'] == 999)].index, inplace = True)
                rejection_choice = rejection_choice.reset_index(drop = True)
                
                rejection_choicemean = rejection_choice['choice'].mean()
                # print(rejection_choicemean)
                
                rej_df['choice'] = rejection_choicemean
                
                #%%
                #calculate mean salience rating across acceptance condition for one participant
                acceptance_salience = pd.DataFrame()
                acceptance_salience['salience_rating'] = acc_df['salience_rating']
                
                #drop nans and empty spaces to make cumulative sum possible
                acceptance_salience= acceptance_salience.replace('NAN', np.nan,regex = True)
                acceptance_salience = acceptance_salience.dropna()
                
                acceptance_salience= acceptance_salience.astype(int)
                acceptance_saliencemean = acceptance_salience['salience_rating'].mean()
                # print(acceptance_saliencemean)
                
                acc_df['salience_mean'] = acceptance_saliencemean
                
                #%%
                
                acceptance_stress = pd.DataFrame()
                acceptance_stress['stress'] = acc_df['stress_level']
                
                acceptance_stress= acceptance_stress.replace('NAN', np.nan,regex = True)
                acceptance_stress = acceptance_stress.dropna()
                
                acceptance_stress= acceptance_stress.astype(int)
                acceptance_stressmean = acceptance_stress['stress'].mean()
                # print(acceptance_stressmean)
                
                acc_df['stress_mean'] = acceptance_stressmean
            
                acc_df['recoded_stress'] = ''
         
                
                #%%
                
                acceptance_choice = pd.DataFrame()
                acceptance_choice['choice'] = acc_df['playlottery']
                acceptance_choice = acceptance_choice.dropna()
                acceptance_choice.drop(acceptance_choice[(acceptance_choice['choice'] == 999)].index, inplace = True)
                acceptance_choice = acceptance_choice.reset_index(drop = True)
                
                acceptance_choicemean = acceptance_choice['choice'].mean()
                # print(acceptance_choicemean)
                
                acc_df['choice'] = acceptance_choicemean
                
                #%%
                #calculate mean salience rating across neutral condition for one participant
                neutral_salience = pd.DataFrame()
                neutral_salience['salience_rating'] = neu_df['salience_rating']
                
                #drop nans and empty spaces to make cumulative sum possible
                neutral_salience= neutral_salience.replace('NAN', np.nan,regex = True)
                neutral_salience = neutral_salience.dropna()
                
                neutral_salience= neutral_salience.astype(int)
                neutral_saliencemean = neutral_salience['salience_rating'].mean()
                # print(neutral_saliencemean)
                
                neu_df['salience_mean'] = neutral_saliencemean
                
                #%%
                
                neutral_stress = pd.DataFrame()
                neutral_stress['stress'] = neu_df['stress_level']
                
                neutral_stress= neutral_stress.replace('NAN', np.nan,regex = True)
                neutral_stress = neutral_stress.dropna()
                
                neutral_stress= neutral_stress.astype(int)
                neutral_stressmean = neutral_stress['stress'].mean()
                # print(neutral_stressmean)
                
                neu_df['stress_mean'] = neutral_stressmean
             
                neu_df['recoded_stress'] = ''
            
                
                
                #%%
                
                neutral_choice = pd.DataFrame()
                neutral_choice['choice'] = neu_df['playlottery']
                neutral_choice = neutral_choice.dropna()
                neutral_choice.drop(neutral_choice[(neutral_choice['choice'] == 999)].index, inplace = True)
                neutral_choice = neutral_choice.reset_index(drop = True)
                
                neutral_choicemean = neutral_choice['choice'].mean()
                # print(neutral_choicemean)
                
                neu_df['choice'] = neutral_choicemean
                #%%
                # stressdiffscore['PROLIFIC_ID'] [sub]= rej_df['PROLIFIC_ID'][sub]
        
           
                
               
                # recode values in rejection
                for i in range(0,len(rej_df)):
                 if rej_df.loc[i,'afterstresschange'] == 0:
                     if rej_df.loc[i,'stress_mean'] == 9:
                         rej_df['recoded_stress' ][i] = 1
                         
                     elif rej_df.loc[i,'stress_mean'] == 8.5:
                         rej_df['recoded_stress'][i] = 1.5
                          
                     elif rej_df.loc[i,'stress_mean'] == 8:
                         rej_df['recoded_stress'][i] = 2
                     
                     elif rej_df.loc[i,'stress_mean'] == 7.5:
                         rej_df['recoded_stress'][i] = 2.5
                         
                     elif rej_df.loc[i,'stress_mean'] == 7:
                         rej_df['recoded_stress'][i] = 3
                     
                     elif rej_df.loc[i,'stress_mean'] == 6.5:
                         rej_df['recoded_stress'][i] = 3.5
                         
                     elif rej_df.loc[i,'stress_mean'] == 6:
                         rej_df['recoded_stress'][i] = 4
                     
                     elif rej_df.loc[i,'stress_mean'] == 5.5:
                         rej_df['recoded_stress'][i] = 4.5
                         
                     elif rej_df.loc[i,'stress_mean'] == 5:
                         rej_df['recoded_stress'][i] = 5
                 
                     elif rej_df.loc[i,'stress_mean'] == 4.5:
                         rej_df['recoded_stress'][i] = 5.5
                         
                     elif rej_df.loc[i,'stress_mean'] == 4:
                         rej_df['recoded_stress'][i] = 6
                         
                     elif rej_df.loc[i,'stress_mean'] == 3.5:
                         rej_df['recoded_stress'][i] = 6.5
                         
                     elif rej_df.loc[i,'stress_mean'] == 3:
                         rej_df['recoded_stress'][i] = 7
                     
                     elif rej_df.loc[i,'stress_mean'] == 2.5:
                         rej_df['recoded_stress'][i] = 7.5
                         
                     elif rej_df.loc[i,'stress_mean'] == 2:
                         rej_df['recoded_stress'][i] = 8
                         
                     elif rej_df.loc[i,'stress_mean'] == 1.5:
                         rej_df['recoded_stress'][i] = 8.5 
                    
                     elif rej_df.loc[i,'stress_mean'] == 1:
                         rej_df['recoded_stress'][i] = 9 
                         
                 elif rej_df.loc[i,'afterstresschange'] == 1:
                     rej_df['recoded_stress' ][i] = rej_df['stress_mean' ][i]
                    
            #recode values in acceptance
                for i in range(0,len(acc_df)):
                 if acc_df.loc[i,'afterstresschange'] == 0:
                     if acc_df.loc[i,'stress_mean'] == 9:
                         acc_df['recoded_stress' ][i] = 1
                         
                     elif acc_df.loc[i,'stress_mean'] == 8.5:
                         acc_df['recoded_stress'][i] = 1.5
                          
                     elif acc_df.loc[i,'stress_mean'] == 8:
                         acc_df['recoded_stress'][i] = 2
                     
                     elif acc_df.loc[i,'stress_mean'] == 7.5:
                         acc_df['recoded_stress'][i] = 2.5
                         
                     elif acc_df.loc[i,'stress_mean'] == 7:
                         acc_df['recoded_stress'][i] = 3
                     
                     elif acc_df.loc[i,'stress_mean'] == 6.5:
                         acc_df['recoded_stress'][i] = 3.5
                         
                     elif acc_df.loc[i,'stress_mean'] == 6:
                         acc_df['recoded_stress'][i] = 4
                     
                     elif acc_df.loc[i,'stress_mean'] == 5.5:
                         acc_df['recoded_stress'][i] = 4.5
                         
                     elif acc_df.loc[i,'stress_mean'] == 5:
                         acc_df['recoded_stress'][i] = 5
                 
                     elif acc_df.loc[i,'stress_mean'] == 4.5:
                         acc_df['recoded_stress'][i] = 5.5
                         
                     elif acc_df.loc[i,'stress_mean'] == 4:
                         acc_df['recoded_stress'][i] = 6
                         
                     elif acc_df.loc[i,'stress_mean'] == 3.5:
                         acc_df['recoded_stress'][i] = 6.5
                         
                     elif acc_df.loc[i,'stress_mean'] == 3:
                         acc_df['recoded_stress'][i] = 7
                     
                     elif acc_df.loc[i,'stress_mean'] == 2.5:
                         acc_df['recoded_stress'][i] = 7.5
                         
                     elif acc_df.loc[i,'stress_mean'] == 2:
                         acc_df['recoded_stress'][i] = 8
                         
                     elif acc_df.loc[i,'stress_mean'] == 1.5:
                         acc_df['recoded_stress'][i] = 8.5
                         
                     elif acc_df.loc[i,'stress_mean'] == 1:
                         acc_df['recoded_stress'][i] = 9
                         
                
                 elif acc_df.loc[i,'afterstresschange'] == 1:
                     acc_df['recoded_stress' ][i] =   acc_df['stress_mean' ][i]
                     
                #recode values in neutral 
                for i in range(0,len(neu_df)):
                     if neu_df.loc[i,'afterstresschange'] == 0:
                         if neu_df.loc[i,'stress_mean'] == 9:
                             neu_df['recoded_stress' ][i] = 1
                             
                         elif neu_df.loc[i,'stress_mean'] == 8.5:
                             neu_df['recoded_stress'][i] = 1.5
                              
                         elif neu_df.loc[i,'stress_mean'] == 8:
                             neu_df['recoded_stress'][i] = 2
                         
                         elif neu_df.loc[i,'stress_mean'] == 7.5:
                             neu_df['recoded_stress'][i] = 2.5
                             
                         elif neu_df.loc[i,'stress_mean'] == 7:
                             neu_df['recoded_stress'][i] = 3
                         
                         elif neu_df.loc[i,'stress_mean'] == 6.5:
                             neu_df['recoded_stress'][i] = 3.5
                             
                         elif neu_df.loc[i,'stress_mean'] == 6:
                             neu_df['recoded_stress'][i] = 4
                         
                         elif neu_df.loc[i,'stress_mean'] == 5.5:
                             neu_df['recoded_stress'][i] = 4.5
                             
                         elif neu_df.loc[i,'stress_mean'] == 5:
                             neu_df['recoded_stress'][i] = 5
                     
                         elif neu_df.loc[i,'stress_mean'] == 4.5:
                             neu_df['recoded_stress'][i] = 5.5
                             
                         elif neu_df.loc[i,'stress_mean'] == 4:
                             neu_df['recoded_stress'][i] = 6
                             
                         elif neu_df.loc[i,'stress_mean'] == 3.5:
                             neu_df['recoded_stress'][i] = 6.5
                             
                         elif neu_df.loc[i,'stress_mean'] == 3:
                             neu_df['recoded_stress'][i] = 7
                         
                         elif neu_df.loc[i,'stress_mean'] == 2.5:
                             neu_df['recoded_stress'][i] = 7.5
                             
                         elif neu_df.loc[i,'stress_mean'] == 2:
                             neu_df['recoded_stress'][i] = 8
                             
                         elif neu_df.loc[i,'stress_mean'] == 1.5:
                             neu_df['recoded_stress'][i] = 8.5
                             
                         elif neu_df.loc[i,'stress_mean'] == 1:
                             neu_df['recoded_stress'][i] = 9
                             
                     elif neu_df.loc[i,'afterstresschange'] == 1:
                         neu_df['recoded_stress' ][i] =   neu_df['stress_mean' ][i]
                         
            difference = float(rej_df['recoded_stress'][0]) - float(acc_df['recoded_stress'][0])
           
            rej_df['rej-acc'] = difference
            acc_df['rej-acc'] = difference
            neu_df['rej-acc'] = difference
            rej_df['ifnegvalue']= ''
            neu_df['ifnegvalue'] = ''
            acc_df['ifnegvalue'] = ''
               
            
            shortform_data = shortform_data.append(rej_df[columns2].iloc[[0]].append(neu_df[columns2].iloc[[0]]).append(acc_df[columns2].iloc[[0]])).reset_index(drop=True) 

#%%

for i in range(0,len(shortform_data)):
    if shortform_data.loc[i, 'rej-acc'] < 0:
        shortform_data['ifnegvalue'][i] = 1 
    else:
        shortform_data['ifnegvalue'][i] = 0                            
#%%
shortform_data=shortform_data.sort_values(['PROLIFIC_ID', 'condition_recode']).reset_index(drop=True)
shortform_data.to_csv('shortformdata_DF.csv', index=False)                   

#%%





# acceptance_recoded  = shortform_data.loc[
#     shortform_data['condition'] == 2].reset_index(drop=True)
# rejection_recoded  = shortform_data.loc[
#     shortform_data['condition'] == 1].reset_index(drop=True)
# neutral_recoded  = shortform_data.loc[
#     shortform_data['condition'] == 0].reset_index(drop=True)

