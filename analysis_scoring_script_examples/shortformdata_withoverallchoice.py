#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 13:59:55 2023

@author: jordansiegel
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 16:45:54 2023

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

#read in csvs containing task data
shortformtaskdata = pd.read_csv('Updatedtaskdata_3.2.23.csv')
longformtaskdata = pd.read_csv('RejChoice_MasterData.csv')

#%%


path = Path(r"%s"%(os.getcwd()))
p = Path('%s/data' %(path))

cols = ['PROLIFIC_ID', 'choice', 'condition', 'salience', 'stress', 'afterstresschange', 'rej-acc', 'ifnegvalue','choicertmean','timebetween', 'age', 'sex','order', 'overallchoice', 'overallaffect']
columns2 = ['PROLIFIC_ID', 'condition_recode', 'afterstresschange','salience_mean', 'stress_mean', 'recoded_stress', 'choice','rej-acc', 'ifnegvalue','choicertmean', 'timebetween', 'age', 'sex', 'order', 'choicedifference_rejneu', 'overallchoice','overallaffect']
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
            if participantdata.loc[3,'TrialNumber'] == 1:
                if participantdata.loc[3,'Condition'] == 'Neutral':
                    order = 0
                elif participantdata.loc[3,'Condition'] == 'Rej':
                    order= 12
                elif participantdata.loc[3,'Condition'] == 'Acc':
                    order= 21
            if order == 12 or order == 21:
                 participants['order'][sub] = int(order)
            elif order == '' or order == 0:
              if participantdata.loc[39,'TrialNumber'] == 31:
                  if participantdata.loc[39,'Condition'] == 'Neutral':
                      order = 0
                  elif participantdata.loc[39,'Condition'] == 'Rej':
                      order= 12 
                  elif participantdata.loc[39,'Condition'] == 'Acc':
                      order= 21    
            if order == 12 or order == 21:
                   participants['order'][sub] = int(order)
            elif order == '' or order == 0: 
                    if participantdata.loc[75,'TrialNumber'] == 61:
                        if participantdata.loc[75,'Condition'] == 'Neutral':
                            order = 0
                        elif participantdata.loc[75,'Condition'] == 'Rej':
                            order= 12               
                        elif participantdata.loc[75,'Condition'] == 'Acc':
                            order= 21
            if order == 12 or order == 21:
                    participants['order'][sub] = int(order)
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
                
                rej_df['timebetween'] = participants['timebetween'][sub]
                acc_df['timebetween'] = participants['timebetween'][sub]
                neu_df['timebetween'] =  participants['timebetween'][sub]
                
                    
                rej_df['age'] = participants['age'][sub]
                acc_df['age'] = participants['age'][sub]
                neu_df['age'] =  participants['age'][sub]
                
                    
                rej_df['sex'] = participants['sex'][sub]
                acc_df['sex'] = participants['sex'][sub]
                neu_df['sex'] = participants['sex'][sub]
               
                rej_df['order'] = participants['order'][sub]
                acc_df['order'] = participants['order'][sub]
                neu_df['order'] =  participants['order'][sub]
                 
               
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
                
                rejection_choicert = pd.DataFrame()
                rejection_choicert['choicert'] = rej_df['choice_keys.rt']
                
                rejection_choicert= rejection_choicert.replace('NAN', np.nan,regex = True)
                rejection_choicert = rejection_choicert.dropna()
                
                rejection_choicert= rejection_choicert.astype(int)
                rejection_choicertmean = rejection_choicert['choicert'].mean()
                # print(rejection_stressmean)
                
                rej_df['choicertmean'] = rejection_choicertmean
              
                #%%
                
                      
                acceptance_choicert =acceptance_choicert = pd.DataFrame()
                acceptance_choicert['choicert'] = acc_df['choice_keys.rt']
                
                acceptance_choicert= acceptance_choicert.replace('NAN', np.nan,regex = True)
                acceptance_choicert = acceptance_choicert.dropna()
                
                acceptance_choicert= acceptance_choicert.astype(int)
                acceptance_choicertmean = acceptance_choicert['choicert'].mean()
                # print(acceptance_stressmean)
                
                acc_df['choicertmean'] = acceptance_choicertmean
                
            #%%
            
                neutral_choicert = neutral_choicert = pd.DataFrame()
                neutral_choicert['choicert'] = neu_df['choice_keys.rt']

                neutral_choicert= neutral_choicert.replace('NAN', np.nan,regex = True)
                neutral_choicert = neutral_choicert.dropna()

                neutral_choicert= neutral_choicert.astype(int)
                neutral_choicertmean = neutral_choicert['choicert'].mean()
                # print(neutral_stressmean)

                neu_df['choicertmean'] = neutral_choicertmean
                #%%
                
                neutral_overallchoice = neutral_overallchoice = pd.DataFrame()
                neutral_overallchoice['overallchoice'] = participantdata['playlottery']

                neutral_overallchoice= neutral_overallchoice.replace('NAN', np.nan,regex = True)
                neutral_overallchoice = neutral_overallchoice.dropna()

                neutral_overallchoice= neutral_overallchoice.replace(999, np.nan,regex = True)
                neutral_overallchoice = neutral_overallchoice.dropna()

                neutral_overallchoice = neutral_overallchoice.astype(int)
                neutral_overallchoicemean = neutral_overallchoice['overallchoice'].mean()
                # print(neutral_stressmean)

                neu_df['overallchoice'] = neutral_overallchoicemean
                acc_df['overallchoice'] = neutral_overallchoicemean
                rej_df['overallchoice'] = neutral_overallchoicemean
                   
                #%%
             
       
               # acceptance_overallchoice = acceptance_overallchoice = pd.DataFrame()
                # acceptance_overallchoice['overallchoice'] = participantdata['playlottery']

                # acceptance_overallchoice= acceptance_overallchoice.replace('NAN', np.nan,regex = True)
                # acceptance_overallchoice = acceptance_overallchoice.dropna()

                # acceptance_overallchoice= acceptance_overallchoice.replace(999, np.nan,regex = True)
                # acceptance_overallchoice = acceptance_overallchoice.dropna()

                # acceptance_overallchoice = acceptance_overallchoice.astype(int)
                # acceptance_overallchoicemean = acceptance_overallchoice['overallchoice'].mean()
                # # print(neutral_stressmean)

                # acc_df['overallchoice'] = acceptance_overallchoicemean
                
                #%%
                
                # rejection_overallchoice = rejection_overallchoice = pd.DataFrame()
                # rejection_overallchoice['overallchoice'] = participantdata['playlottery']

                # rejection_overallchoice= rejection_overallchoice.replace('NAN', np.nan,regex = True)
                # rejection_overallchoice = rejection_overallchoice.dropna()

                # rejection_overallchoice= rejection_overallchoice.replace(999, np.nan,regex = True)
                # rejection_overallchoice = rejection_overallchoice.dropna()

                # rejection_overallchoice = rejection_overallchoice.astype(int)
                # rejection_overallchoicemean = rejection_overallchoice['overallchoice'].mean()
                # # print(neutral_stressmean)

                # rej_df['overallchoice'] = rejection_overallchoicemean
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
                         
            overallaffect = overallaffect = pd.DataFrame()
            overallaffect['neu'] = neu_df['recoded_stress']
            overallaffect['acc'] = acc_df['recoded_stress']
            overallaffect['rej'] = rej_df['recoded_stress']
            overallaffect_sum = neu_df['recoded_stress'] + acc_df['recoded_stress'] + rej_df['recoded_stress']
            overallaffect['overall_mean'] = overallaffect_sum/3
   
   
            neu_df['overallaffect'] = overallaffect['overall_mean']
            acc_df['overallaffect'] = overallaffect['overall_mean']
            rej_df['overallaffect'] = overallaffect['overall_mean']
            #calculate difference between affect rating following rejection conditions and affect ratings during acceptance condition             
            difference = float(rej_df['recoded_stress'][0]) - float(acc_df['recoded_stress'][0])
            #caldulate percentage difference for each participant of self-choice during rejection compared to neutral
            choicedifference_rejneu =float(rej_df['choice'][0]) - float(neu_df['choice'][0])
           
            rej_df['rej-acc'] = difference
            acc_df['rej-acc'] = difference
            neu_df['rej-acc'] = difference
            rej_df['choicedifference_rejneu'] = choicedifference_rejneu
            acc_df['choicedifference_rejneu'] = choicedifference_rejneu
            neu_df['choicedifference_rejneu'] = choicedifference_rejneu
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


