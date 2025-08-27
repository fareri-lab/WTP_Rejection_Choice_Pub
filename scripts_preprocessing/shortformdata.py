#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 19:58:57 2024

@author: jordansiegel
"""

from pathlib import Path
import pandas as pd 
import numpy as np
import os

#read in participant list
current_dir = os.getcwd()

#participants = pd.read_excel('participantlist.xlsx')
participants = pd.read_excel('/Users/jordansiegel/Documents/GitHub/WTP_rejection_choice/participantlist.xlsx')

#toberecoded = participants.loc[participants['afterstresschange']== 0].reset_index(drop=True)
participants = participants.loc[
    participants['PhotosUploaded? (y/n)'] == 'y'].reset_index()
columns = ['PROLIFIC_ID','timebetween','sex','age']
participants =participants[columns]
participants = pd.DataFrame(data = participants.sort_values(by='PROLIFIC_ID').reset_index(drop=True))
participants['order'] = ''
order = ''

#%%


path = Path(r"%s"%(os.getcwd()))
p = Path('%s/data' %(path))

cols = ['PROLIFIC_ID','Condition', 'salience_rating', 'stress_level', 'decision_price', 'responses.keys', 'social_left', 'rej-acc', 'ifnegvalue','choicertmean','timebetween', 'age', 'sex','order', 'overallaffect', 'socialchoice', 'prop_socialchoice']
columns2 = ['participant', 'condition_recode','salience_mean', 'choice', 'stress_mean', 'stress_mean','rej-acc', 'ifnegvalue','choicertmean', 'timebetween', 'age', 'sex', 'order','overallaffect', 'socialchoice','prop_socialchoice', 'social_left', 'social_decisionprice_mean', 'nonsocial_decisionprice_mean']
shortform_data= pd.DataFrame(columns=columns2)

#%%

#make rejection data frame
rej_df = pd.DataFrame(index=participants.index, columns = cols)


#%%

#make acceptance data frame
acc_df = pd.DataFrame(index=participants.index, columns = cols)

#%%
stressdiffscore = pd.DataFrame(index=participants.index, columns= ['PROLIFIC_ID', 'rejstress', 'accstress', 'difference', 'ifnegvalue'])

#%%
data_path = os.getcwd()+'/data/'

#calcuate the order of conditions for each participant 
for csv in sorted(os.listdir(data_path)):
    for sub in range(0,len(participants)):
        if csv.startswith(participants['PROLIFIC_ID'][sub]):
            participantdata = pd.read_csv(data_path+csv)
            participantdata['participant']=participantdata['participant'][0]
            print(participantdata['participant'][0])
            if participantdata.loc[3,'TrialNumber'] == 1:
                if participantdata.loc[3,'Condition'] == 'Rej':
                    order= 12
                elif participantdata.loc[3,'Condition'] == 'Acc':
                    order= 21
            if order == 12 or order == 21:
                 participants['order'][sub] = int(order)
            elif order == '' or order == 0:
              if participantdata.loc[39,'TrialNumber'] == 31:
                  if participantdata.loc[39,'Condition'] == 'Rej':
                      order= 12 
                  elif participantdata.loc[39,'Condition'] == 'Acc':
                      order= 21   
            if order == 12 or order == 21:
                   participants['order'][sub] = int(order)
            elif order == '' or order == 0: 
                    if participantdata.loc[75,'TrialNumber'] == 61:
                        if participantdata.loc[39,'Condition'] == 'Rej':
                            order= 12 
                        elif participantdata.loc[39,'Condition'] == 'Acc':
                            order= 21 
            if order == 12 or order == 21:
                    participants['order'][sub] = int(order)  
#%%
#replace the nan with Empty so to change them to the correct values below
            participantdata['Condition'] = participantdata['Condition'].replace(np.nan,'Empty',regex = True)

       #%%              
            #for row in range(0,len(participantdata)):
                #if participantdata['responses.keys'][row] == 2 or  participantdata['responses.keys'][row] == 1:
                 #   if row < 203:
                  #      if participantdata.loc[row+3,'Condition']== 'Rej':
                   #         participantdata['Condition'][row] =  participantdata['Condition'][row].replace('Empty', 'Rej')
                    #        participantdata['Condition'][row] =  participantdata['Condition'][row].replace('Empty', 'Rej')
                     #   elif participantdata.loc[row+3,'Condition']== 'Acc':
                      #      participantdata['Condition'][row] =  participantdata['Condition'][row].replace('Empty', 'Acc')
                            
                 #%%  
                 
                 #fill in missing values for condition column in data frame
            for row in range(len(participantdata)):
    # Ensure the row is valid and row+3 does not exceed the DataFrame length
                if participantdata['responses.keys'][row] in [1, 2] and (row + 3) < len(participantdata):
                    if participantdata.loc[row + 3, 'Condition'] == 'Rej':
                        participantdata.loc[row, 'Condition'] = participantdata.loc[row, 'Condition'].replace('Empty', 'Rej')
                    elif participantdata.loc[row + 3, 'Condition'] == 'Acc':
                        participantdata.loc[row, 'Condition'] = participantdata.loc[row, 'Condition'].replace('Empty', 'Acc')
            #%%
            #separate participant data according to the two conditions
                rej_df = participantdata.loc[(participantdata['Condition'] == 'Rej')]
                rej_df = rej_df.reset_index(drop = True)
                
                acc_df= participantdata.loc[(participantdata['Condition'] == 'Acc')]
                acc_df = acc_df.reset_index(drop = True)
                
                #recoding condition strings to numbers in subsectioned dataframes
                acc_df['condition_recode'] = 2
                rej_df['condition_recode'] = 1 
                

                
                #%%

                # Drop NaNs in columns relevant to the calculation of 'socialchoice'
                #rej_df = rej_df.dropna(subset=['social_left', 'responses.keys']).copy()
                #acc_df = acc_df.dropna(subset=['social_left', 'responses.keys']).copy()
                                
 
                # Initialize 'socialchoice' and calculate based on conditions
                rej_df['socialchoice'] = 999
                
                rej_df.loc[(rej_df['responses.keys'] == 1) & (rej_df['social_left'] == 1),'socialchoice'] = 1
                rej_df.loc[(rej_df['responses.keys'] == 2) & (rej_df['social_left'] == 1),'socialchoice'] = 0
                rej_df.loc[(rej_df['responses.keys'] == 1) & (rej_df['social_left'] == 0),'socialchoice'] = 0
                rej_df.loc[(rej_df['responses.keys'] == 2) & (rej_df['social_left'] == 0),'socialchoice'] = 1
               
                
                acc_df['socialchoice'] = 999
                
                acc_df.loc[(acc_df['responses.keys'] == 1) & (acc_df['social_left'] == 1),'socialchoice'] = 1
                acc_df.loc[(acc_df['responses.keys'] == 2) & (acc_df['social_left'] == 1),'socialchoice'] = 0
                acc_df.loc[(rej_df['responses.keys'] == 1) & (acc_df['social_left'] == 0),'socialchoice'] = 0
                acc_df.loc[(rej_df['responses.keys'] == 2) & (acc_df['social_left'] == 0),'socialchoice'] = 1
                
                #%%
               
                # Calculate proportion of social choices
                
                rejection_prop_social = pd.DataFrame()
                rejection_prop_social['socialchoice'] = rej_df['socialchoice']
                
                rejection_prop_social = rejection_prop_social[rejection_prop_social['socialchoice'] != 999].copy()
                
            
                rejection_prop_social_mean= rejection_prop_social['socialchoice'].mean()
                rej_df['prop_socialchoice'] = rejection_prop_social_mean
                
                #%%
                
                acceptance_prop_social = pd.DataFrame()
                acceptance_prop_social['socialchoice'] = acc_df['socialchoice']
                
                acceptance_prop_social = acceptance_prop_social[acceptance_prop_social['socialchoice'] != 999].copy()
                
            
                acceptance_prop_social_mean= acceptance_prop_social['socialchoice'].mean()
                acc_df['prop_socialchoice'] =  acceptance_prop_social_mean
                
            
                #%%
               
                
                rej_df['timebetween'] = participants['timebetween'][sub]
                acc_df['timebetween'] = participants['timebetween'][sub]
                
                    
                rej_df['age'] = participants['age'][sub]
                acc_df['age'] = participants['age'][sub]
                
                    
                rej_df['sex'] = participants['sex'][sub]
                acc_df['sex'] = participants['sex'][sub]
               
                rej_df['order'] = participants['order'][sub]
                acc_df['order'] = participants['order'][sub]
            
           #%%
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
             
                
                #%%
                rejection_choice = pd.DataFrame()
                rejection_choice['choice'] = rej_df['responses.keys']
                rejection_choice = rejection_choice.dropna()
                rejection_choice.drop(rejection_choice[(rejection_choice['choice'] == 999)].index, inplace = True)
                rejection_choice = rejection_choice.reset_index(drop = True)
                
                rejection_choicemean = rejection_choice['choice'].mean()
                # print(rejection_choicemean)
                
                rej_df['choice'] = rejection_choicemean
                
                #%%
                
           
                
                rejection_decisionprice_social = pd.DataFrame()
                rejection_decisionprice_social = rej_df.loc[(rej_df['socialchoice']) == 1].copy()
                rejection_decisionprice_social_mean = rejection_decisionprice_social['decision_price'].mean()
                
                rejection_decisionprice_nonsocial = pd.DataFrame()
                rejection_decisionprice_nonsocial = rej_df.loc[(rej_df['socialchoice']) == 0].copy()
                rejection_decisionprice_nonsocial_mean = rejection_decisionprice_nonsocial['decision_price'].mean()
                
                rej_df['social_decisionprice_mean'] = rejection_decisionprice_social_mean
                rej_df['nonsocial_decisionprice_mean'] = rejection_decisionprice_nonsocial_mean
                
            
                
                #%%
                
                 
                acceptance_decisionprice = pd.DataFrame()
                acceptance_decisionprice['decision_price'] = acc_df['decision_price']
                
                acceptance_decisionprice_social = pd.DataFrame()
                acceptance_decisionprice_social = acc_df.loc[(acc_df['socialchoice']) == 1].copy()
                acceptance_decisionprice_social_mean = acceptance_decisionprice_social['decision_price'].mean()
                
                acceptance_decisionprice_nonsocial = pd.DataFrame()
                acceptance_decisionprice_nonsocial = acc_df.loc[(acc_df['socialchoice']) == 0].copy()
                acceptance_decisionprice_nonsocial_mean = acceptance_decisionprice_nonsocial['decision_price'].mean()
                
                acc_df['social_decisionprice_mean'] = acceptance_decisionprice_social_mean
                acc_df['nonsocial_decisionprice_mean'] = acceptance_decisionprice_nonsocial_mean
                
                
                #%%
                
                rejection_choice = pd.DataFrame()
                rejection_choice['choice'] = rej_df['responses.keys']
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
                
               
                
                
                #%%
                
                acceptance_choice = pd.DataFrame()
                acceptance_choice['choice'] = acc_df['responses.keys']
                acceptance_choice = acceptance_choice.dropna()
                acceptance_choice.drop(acceptance_choice[(acceptance_choice['choice'] == 999)].index, inplace = True)
                acceptance_choice = acceptance_choice.reset_index(drop = True)
                
                acceptance_choicemean = acceptance_choice['choice'].mean()
                # print(acceptance_choicemean)
                
                acc_df['choice'] = acceptance_choicemean
            
                
             #%%
             
                rejection_choicert = pd.DataFrame()
                rejection_choicert['choicert'] = rej_df['responses.rt']
             
                rejection_choicert= rejection_choicert.replace('NAN', np.nan,regex = True)
                rejection_choicert = rejection_choicert.dropna()
             
                rejection_choicert= rejection_choicert.astype(int)
                rejection_choicertmean = rejection_choicert['choicert'].mean()
             # print(rejection_stressmean)
             
                rej_df['choicertmean'] = rejection_choicertmean
            
             #%%
             
                   
                acceptance_choicert =acceptance_choicert = pd.DataFrame()
                acceptance_choicert['choicert'] = acc_df['responses.rt']
             
                acceptance_choicert= acceptance_choicert.replace('NAN', np.nan,regex = True)
                acceptance_choicert = acceptance_choicert.dropna()
             
                acceptance_choicert= acceptance_choicert.astype(int)
                acceptance_choicertmean = acceptance_choicert['choicert'].mean()
             # print(acceptance_stressmean)
             
                acc_df['choicertmean'] = acceptance_choicertmean
             
               #%% 
            overallaffect = overallaffect = pd.DataFrame()
            overallaffect['acc'] = acc_df['stress_mean']
            overallaffect['rej'] = rej_df['stress_mean']
            overallaffect_sum = acc_df['stress_mean'] + rej_df['stress_mean']
            overallaffect['overall_mean'] = overallaffect_sum/2
   
       
               
            acc_df['overallaffect'] = overallaffect['overall_mean']
            rej_df['overallaffect'] = overallaffect['overall_mean']
            #calculate difference between affect rating following rejection conditions and affect ratings during acceptance condition             
            difference = float(rej_df['stress_mean'][0]) - float(acc_df['stress_mean'][0])
      
           
            rej_df['rej-acc'] = difference
            acc_df['rej-acc'] = difference
           
            rej_df['ifnegvalue']= ''
            
            acc_df['ifnegvalue'] = ''
            
            #%%
               
            
            shortform_data = shortform_data.append(rej_df[columns2].iloc[[0]].append(acc_df[columns2].iloc[[0]])).reset_index(drop=True) 
            
                        # Combine rows from rej_df and acc_df for the specified columns
            #new_rows = pd.concat([rej_df[columns2].iloc[[0]], acc_df[columns2].iloc[[0]]], ignore_index=True)
            
            # Append to shortform_data and reset index
            #shortform_data = pd.concat([shortform_data, new_rows], ignore_index=True)


    #%%

    for i in range(0,len(shortform_data)):
        if shortform_data.loc[i, 'rej-acc'] < 0:
            shortform_data['ifnegvalue'][i] = 1 
        else:
            shortform_data['ifnegvalue'][i] = 0                            
    #%%

    shortform_data=shortform_data.sort_values(['participant','condition_recode']).reset_index(drop=True)
    output_path = '/Users/jordansiegel/documents/GitHub/WTP_rejection_choice/shortformdata.csv'
    shortform_data.to_csv(output_path, index=False)    
             
