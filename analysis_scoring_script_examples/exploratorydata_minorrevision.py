#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 12:02:31 2024

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
columns = ['PROLIFIC_ID']
participants =participants[columns]
participants = pd.DataFrame(data = participants.sort_values(by='PROLIFIC_ID').reset_index(drop=True))

#%%


path = Path(r"%s"%(os.getcwd()))
p = Path('%s/data' %(path))
exploratory_cols = ['PROLIFIC_ID', 'choice', 'condition', 'condition_recode', 'trialnumber', 'feedback_words', 'feedbackvalue', 'overall_subblock_feedback']
exploratory_data= pd.DataFrame(columns = exploratory_cols)
#%%
#exploratory_df = pd.DataFrame(index=participants.index, columns = exploratory_cols)


current_dir = os.getcwd()
participants = pd.read_excel('participantlist.xlsx')
participants = participants.loc[participants['PhotosUploaded? (y/n)'] == 'y'].reset_index()
participants = participants[['PROLIFIC_ID']].sort_values(by='PROLIFIC_ID').reset_index(drop=True)

# Define the data path
#%%
data_path = os.getcwd()+'/data/'


# Define the data path
data_path = os.path.join(os.getcwd(), 'data')

# Initialize the final DataFrame
exploratory_df = pd.DataFrame()


#%%

# Iterate through each CSV file in the data directory
for csv in sorted(os.listdir(data_path)):
    # Iterate through each participant in the participants DataFrame
    for sub in range(len(participants)):
        # Check if the CSV file starts with the PROLIFIC_ID of the current participant
        if csv.startswith(participants['PROLIFIC_ID'][sub]):
            # Read the CSV file into a DataFrame
            participantdata = pd.read_csv(os.path.join(data_path, csv))
            
            # Ensure 'PROLIFIC_ID' column exists in participantdata
            if 'PROLIFIC_ID' not in participantdata.columns:
                participantdata['PROLIFIC_ID'] = participants['PROLIFIC_ID'][sub]
            else:
                participantdata['PROLIFIC_ID'] = participantdata['PROLIFIC_ID'].fillna(participants['PROLIFIC_ID'][sub])
            
            # Prepare a DataFrame for the current participant's data
            participantdata = pd.DataFrame({
                'PROLIFIC_ID': participants['PROLIFIC_ID'][sub],
                'trialnumber': participantdata['TrialNumber'].replace(np.nan, 'remove'),
                'choice': participantdata['playlottery'],
                'condition': participantdata['Condition'].replace(np.nan, 'remove'),
                'feedback_words': participantdata['Feedback'].replace(np.nan, 'remove')
                
            })
            
        
            
            if participantdata.at[7,'choice'] == 999:
                 participantdata.loc[[6,5,4,3,8],'choice']= 999
            elif participantdata.at[7,'choice'] == 1:
                 participantdata.loc[[6,5,4,3,8],'choice']= 1
            elif participantdata.at[7,'choice'] == 0:
                 participantdata.loc[[6,5,4,3,8],'choice']= 0
                     
             #fill in choice column for trials 6-10 with the correct value
             
            if participantdata.at[13,'choice'] == 999:
                 participantdata.loc[[9,10,11,12,14],'choice']= 999
            elif participantdata.at[13,'choice'] == 1:
                 participantdata.loc[[9,10,11,12,14],'choice']= 1
            elif participantdata.at[13,'choice'] == 0:
                 participantdata.loc[[9,10,11,12,14],'choice']= 0
                 
             #trials 11-15
                 
            if participantdata.at[19,'choice'] == 999:
                 participantdata.loc[[15,16,17,18,20],'choice']= 999
            elif participantdata.at[19,'choice'] == 1:
                 participantdata.loc[[15,16,17,18,20],'choice']= 1
            elif participantdata.at[19,'choice'] == 0:
                 participantdata.loc[[15,16,17,18,20],'choice']= 0
                 
             #trials 16-20   
             
            if participantdata.at[25,'choice'] == 999:
                 participantdata.loc[[21,22,23,24,26],'choice']= 999
            elif participantdata.at[25,'choice'] == 1:
                 participantdata.loc[[21,22,23,24,26],'choice']= 1
            elif participantdata.at[25,'choice'] == 0:
                 participantdata.loc[[21,22,23,24,26],'choice']= 0
                 
              #trials 21-25 
              
            if participantdata.at[31,'choice'] == 999:
                 participantdata.loc[[27,28,29,30,32],'choice']= 999
            elif participantdata.at[31,'choice'] == 1:
                 participantdata.loc[[27,28,29,30,32],'choice']= 1
            elif participantdata.at[31,'choice'] == 0:
                 participantdata.loc[[27,28,29,30,32],'choice']= 0
                  
              #trials 26-30 
              
            if participantdata.at[37,'choice'] == 999:
                participantdata.loc[[33,34,35,36,38],'choice']= 999
            elif participantdata.at[37,'choice'] == 1:
                participantdata.loc[[33,34,35,36,38],'choice']= 1
            elif participantdata.at[37,'choice'] == 0:
                participantdata.loc[[33,34,35,36,38],'choice']= 0
             
             #trials 31-35 
             
            if participantdata.at[43,'choice'] == 999:
                 participantdata.loc[[39,40,41,42,44],'choice']= 999
            elif participantdata.at[43,'choice'] == 1:
                 participantdata.loc[[39,40,41,42,44],'choice']= 1
            elif participantdata.at[43,'choice'] == 0:
                 participantdata.loc[[39,40,41,42,44],'choice']= 0
                 
             #trials 36-40 
              
            if participantdata.at[49,'choice'] == 999:
                 participantdata.loc[[45,46,47,48,50],'choice']= 999
            elif participantdata.at[49,'choice'] == 1:
                participantdata.loc[[45,46,47,48,50],'choice']= 1
            elif participantdata.at[49,'choice'] == 0:
                participantdata.loc[[45,46,47,48,50],'choice']= 0
             
             #trials 41-45 
             
            if participantdata.at[55,'choice'] == 999:
                participantdata.loc[[51,52,53,54,56],'choice']= 999
            elif participantdata.at[55,'choice'] == 1:
                participantdata.loc[[51,52,53,54,56],'choice']= 1
            elif participantdata.at[55,'choice'] == 0:
                participantdata.loc[[51,52,53,54,56],'choice']= 0
                
            #trials 46-50 
            
            if participantdata.at[61,'choice'] == 999:
               participantdata.loc[[57,58,59,60,62],'choice']= 999
            elif participantdata.at[61,'choice'] == 1:
               participantdata.loc[[57,58,59,60,62],'choice']= 1
            elif participantdata.at[61,'choice'] == 0:
               participantdata.loc[[57,58,59,60,62],'choice']= 0
               
             #trials 51-55 
             
            if participantdata.at[67,'choice'] == 999:
                participantdata.loc[[63,64,65,66,68],'choice']= 999
            elif participantdata.at[67,'choice'] == 1:
                participantdata.loc[[63,64,65,66,68],'choice']= 1
            elif participantdata.at[67,'choice'] == 0:
                participantdata.loc[[63,64,65,66,68],'choice']= 0
                
             #trials 56-60 
             
            if participantdata.at[73,'choice'] == 999:
                participantdata.loc[[69,70,71,72,74],'choice']= 999
            elif participantdata.at[73,'choice'] == 1:
                participantdata.loc[[69,70,71,72,74],'choice']= 1
            elif participantdata.at[73,'choice'] == 0:
                participantdata.loc[[69,70,71,72,74],'choice']= 0
                
              #trials 61-65 
              
            if participantdata.at[79,'choice'] == 999:
                 participantdata.loc[[75,76,77,78,80],'choice']= 999
            elif participantdata.at[79,'choice'] == 1:
                 participantdata.loc[[75,76,77,78,80],'choice']= 1
            elif participantdata.at[79,'choice'] == 0:
                 participantdata.loc[[75,76,77,78,80],'choice']= 0
                 
             #trials 66-70 
             
            if participantdata.at[85,'choice'] == 999:
                participantdata.loc[[81,82,83,84,86],'choice']= 999
            elif participantdata.at[85,'choice'] == 1:
                participantdata.loc[[81,82,83,84,86],'choice']= 1
            elif participantdata.at[85,'choice'] == 0:
                participantdata.loc[[81,82,83,84,86],'choice']= 0
                
              #trials 76-80 
              
            if participantdata.at[91,'choice'] == 999:
                 participantdata.loc[[87,88,89,90,92],'choice']= 999
            elif participantdata.at[91,'choice'] == 1:
                 participantdata.loc[[87,88,89,90,92],'choice']= 1
            elif participantdata.at[91,'choice'] == 0:
                 participantdata.loc[[87,88,89,90,92],'choice']= 0
                 
             #trials 81-85 
             
            if participantdata.at[97,'choice'] == 999:
                participantdata.loc[[93,94,95,96,98],'choice']= 999
            elif participantdata.at[97,'choice'] == 1:
                participantdata.loc[[93,94,95,96,98],'choice']= 1
            elif participantdata.at[97,'choice'] == 0:
                participantdata.loc[[93,94,95,96,98],'choice']= 0
                
              #trials 86-90 
              
            if participantdata.at[103,'choice'] == 999:
                 participantdata.loc[[99,100,101,102,104],'choice']= 999
            elif participantdata.at[103,'choice'] == 1:
                 participantdata.loc[[99,100,101,102,104],'choice']= 1
            elif participantdata.at[103,'choice'] == 0:
                 participantdata.loc[[99,100,101,102,104],'choice']= 0
                 
             #trials 91-95 
             
            if participantdata.at[109,'choice'] == 999:
                participantdata.loc[[105,106,107,108,110],'choice']= 999
            elif participantdata.at[109,'choice'] == 1:
                participantdata.loc[[105,106,107,108,110],'choice']= 1
            elif participantdata.at[109,'choice'] == 0:
                participantdata.loc[[105,106,107,108,110],'choice']= 0
                
              #trials 96-100 
              
            if participantdata.at[115,'choice'] == 999:
                 participantdata.loc[[111,112,113,114,116],'choice']= 999
            elif participantdata.at[115,'choice'] == 1:
                 participantdata.loc[[111,112,113,114,116],'choice']= 1
            elif participantdata.at[115,'choice'] == 0:
                 participantdata.loc[[111,112,113,114,116],'choice']= 0
                 
             #trials 101-105 
             
            if participantdata.at[121,'choice'] == 999:
                participantdata.loc[[117,118,119,120,122],'choice']= 999
            elif participantdata.at[121,'choice'] == 1:
                participantdata.loc[[117,118,119,120,122],'choice']= 1
            elif participantdata.at[121,'choice'] == 0:
                participantdata.loc[[117,118,119,120,122],'choice']= 0
                
              #trials 106-110 
               
            if participantdata.at[127,'choice'] == 999:
                  participantdata.loc[[123,124,125,126,128],'choice']= 999
            elif participantdata.at[127,'choice'] == 1:
                  participantdata.loc[[123,124,125,126,128],'choice']= 1
            elif participantdata.at[127,'choice'] == 0:
                  participantdata.loc[[123,124,125,126,128],'choice']= 0
                  
             #trials 111-115 
             
            if participantdata.at[133,'choice'] == 999:
                participantdata.loc[[129,130,131,132,134],'choice']= 999
            elif participantdata.at[133,'choice'] == 1:
                participantdata.loc[[129,130,131,132,134],'choice']= 1
            elif participantdata.at[133,'choice'] == 0:
                participantdata.loc[[129,130,131,132,134],'choice']= 0
                
               #trials 116-120
               
            if participantdata.at[139,'choice'] == 999:
                  participantdata.loc[[135,136,137,138,140],'choice']= 999
            elif participantdata.at[139,'choice'] == 1:
                  participantdata.loc[[135,136,137,138,140],'choice']= 1
            elif participantdata.at[139,'choice'] == 0:
                  participantdata.loc[[135,136,137,138,140],'choice']= 0
                  
             #trials 121-125 
             
            if participantdata.at[145,'choice'] == 999:
                participantdata.loc[[141,142,143,144,146],'choice']= 999
            elif participantdata.at[145,'choice'] == 1:
                participantdata.loc[[141,142,143,144,146],'choice']= 1
            elif participantdata.at[145,'choice'] == 0:
                participantdata.loc[[141,142,143,144,146],'choice']= 0
                
              #trials 126-130 
              
            if participantdata.at[151,'choice'] == 999:
                 participantdata.loc[[147,148,149,150,152],'choice']= 999
            elif participantdata.at[151,'choice'] == 1:
                 participantdata.loc[[147,148,149,150,152],'choice']= 1
            elif participantdata.at[151,'choice'] == 0:
                 participantdata.loc[[147,148,149,150,152],'choice']= 0
                 
              #trials 131-135 
              
            if participantdata.at[157,'choice'] == 999:
                 participantdata.loc[[153,154,155,156,158],'choice']= 999
            elif participantdata.at[157,'choice'] == 1:
                 participantdata.loc[[153,154,155,156,158],'choice']= 1
            elif participantdata.at[157,'choice'] == 0:
                 participantdata.loc[[153,154,155,156,158],'choice']= 0
                 
              #trials 136-140 
              
            if participantdata.at[163,'choice'] == 999:
                 participantdata.loc[[159,160,161,162,164],'choice']= 999
            elif participantdata.at[163,'choice'] == 1:
                 participantdata.loc[[159,160,161,162,164],'choice']= 1
            elif participantdata.at[163,'choice'] == 0:
                 participantdata.loc[[159,160,161,162,164],'choice']= 0
                 
             #trials141-145 
             
            if participantdata.at[169,'choice'] == 999:
                participantdata.loc[[165,166,167,168,170],'choice']= 999
            elif participantdata.at[169,'choice'] == 1:
                participantdata.loc[[165,166,167,168,170],'choice']= 1
            elif participantdata.at[169,'choice'] == 0:
                participantdata.loc[[165,166,167,168,170],'choice']= 0
                
               #trials 146-150
               
            if participantdata.at[175,'choice'] == 999:
                  participantdata.loc[[171,172,173,174,176],'choice']= 999
            elif participantdata.at[175,'choice'] == 1:
                  participantdata.loc[[171,172,173,174,176],'choice']= 1
            elif participantdata.at[175,'choice'] == 0:
                  participantdata.loc[[171,172,173,174,176],'choice']= 0
                  
                  
            if participantdata.at[181,'choice'] == 999:
                  participantdata.loc[[177,178,179,180,182],'choice']= 999
            elif participantdata.at[181,'choice'] == 1:
                  participantdata.loc[[177,178,179,180,182],'choice']= 1
            elif participantdata.at[181,'choice'] == 0:
                  participantdata.loc[[177,178,179,180,182],'choice']= 0
            
            
            exploratory_df = pd.concat([exploratory_df, participantdata], ignore_index=True)
exploratorydf_cleaned = exploratory_df[exploratory_df['trialnumber'] != 'remove'].reset_index(drop=True)

            
           
            
            
#%%            
exploratorydf_cleaned['condition_recode']=''            
exploratorydf_cleaned['feedbackvalue']=''         

condition_mapping = {'Rej': 1, 'Acc': -1, 'Neutral': 0}

# Create 'condition_recode' column
exploratorydf_cleaned['condition_recode'] = exploratorydf_cleaned['condition'].map(condition_mapping)

#create feedbackvalue column

feedback_mapping ={'liked': -1, 'did not like': 1,}

exploratorydf_cleaned['feedbackvalue'] = exploratorydf_cleaned['feedback_words'].map(feedback_mapping)

# Process in chunks of 5 trials
chunk_size = 5
for i in range(0, len(exploratorydf_cleaned), chunk_size):
    chunk = exploratorydf_cleaned.iloc[i:i + chunk_size]
    # Count the number of 1s and -1s in the chunk
    count_1 = (chunk['feedbackvalue'] == 1).sum()
    count_minus_1 = (chunk['feedbackvalue'] == -1).sum()
    
    # Determine the aggregated value for the chunk
    if count_1 >= 3:
        aggregated_value = 1
    elif count_minus_1 >= 3:
        aggregated_value = -1
    else:
        aggregated_value = 0  # If neither condition is met, assign 0 (or handle it as needed)
    
    # Assign the aggregated value to the corresponding rows in the new column
    exploratorydf_cleaned.loc[i:i + chunk_size - 1, 'aggregated_value'] = aggregated_value
    
  

#%%

exploratorydata_foranalysis = pd.DataFrame()

# Define the chunk size
chunk_size = 5

# Initialize lists to store the results for the new DataFrame
condition_recodes = []
aggregated_values = []
prolific_ids = []
choice =[]

for i in range(0, len(exploratorydf_cleaned), chunk_size):
    chunk = exploratorydf_cleaned.iloc[i:i + chunk_size]
    # Count the number of 1s and -1s in the chunk
    count_1 = (chunk['feedbackvalue'] == 1).sum()
    count_minus_1 = (chunk['feedbackvalue'] == -1).sum()
    
    # Determine the aggregated value for the chunk
    if count_1 >= 3:
        aggregated_value = 1
    elif count_minus_1 >= 3:
        aggregated_value = -1
    else:
        aggregated_value = 0  # If neither condition is met, assign 0 (or handle it as needed)
    
    
    # Store the aggregated value and the condition recode (arbitrary choice: use first row's condition recode)
    condition_recodes.append(chunk['condition_recode'].iloc[0])
    choice.append(chunk['choice'].iloc[0])
    prolific_ids.append(chunk['PROLIFIC_ID'].iloc[0])
    aggregated_values.append(aggregated_value)
   

# Create the new DataFrame
exploratorydata_foranalysis = pd.DataFrame({
    'PROLIFIC_ID': prolific_ids,
    'condition_recode': condition_recodes,
    'aggregated_value': aggregated_values,
    'choice': choice
    
})

#%%

exploratory_rej = pd.DataFrame()
exploratory_acc = pd.DataFrame()
exploratory_neu = pd.DataFrame()
learningdata = pd.DataFrame()

exploratory_rej = exploratorydata_foranalysis.loc[(exploratorydata_foranalysis['condition_recode'] == 1)]
exploratory_rej = exploratory_rej.reset_index(drop = True)

exploratory_acc = exploratorydata_foranalysis.loc[(exploratorydata_foranalysis['condition_recode'] == -1)]
exploratory_acc = exploratory_acc.reset_index(drop = True)

exploratory_neu = exploratorydata_foranalysis.loc[(exploratorydata_foranalysis['condition_recode'] == 0)]
exploratory_neu = exploratory_neu.reset_index(drop = True)

num_rows = len(exploratory_rej)
exploratory_rej['chunk'] = [(i % 12) + 1 for i in range(num_rows)]

num_rows = len(exploratory_acc)
exploratory_acc['chunk'] = [(i % 12) + 1 for i in range(num_rows)]

num_rows = len(exploratory_neu)
exploratory_neu['chunk'] = [(i % 6) + 1 for i in range(num_rows)]

learningdata = pd.concat([exploratory_rej, exploratory_acc, exploratory_neu], ignore_index=True)


learningdata.to_csv('learningdata.csv', index=False)     
exploratorydf_cleaned.to_csv('exploratorydf_cleaned.csv', index=False)     
exploratorydata_foranalysis.to_csv('exploratorydata_foranalysis.csv', index=False)        

  
              
        
                
            
                 
            
                
                
                
        