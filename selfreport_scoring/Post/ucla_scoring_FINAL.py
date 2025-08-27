#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 12:44:49 2025

@author: jordansiegel
"""

import pandas as pd
import os
from pathlib import Path

path = Path(r"%s" % (os.getcwd()))

# Read in participant list
current_dir = os.getcwd()
participants = pd.read_excel('%s/participantlist.xlsx' % (path.parent.parent))
participants = participants.loc[participants['PhotosUploaded? (y/n)'] == 'y'].reset_index()
participants = pd.DataFrame(data=participants['PROLIFIC_ID'])

# Read in raw Qualtrics data
posttask_survey = '%s/' % (str(path.parent.parent)) + [posttask for posttask in os.listdir(path.parent.parent) if posttask.startswith('WTP_PostTask')][0]
alldata = pd.read_csv(posttask_survey)
alldata = alldata.iloc[2:]  # Remove Qualtrics metadata rows
alldata = alldata.sort_values(by=['PROLIFIC_ID'])
alldata.pop("Attnchk")  # Remove attention checks
alldata = alldata.reset_index(drop=True)

# Select UCLA columns
UCLA_cols = [col for col in alldata.columns if 'UCLA-' in col]
UCLA = alldata.filter(regex='UCLA-|Prolific_ID')

# Filter by participants
UCLA_clean = UCLA[UCLA['Prolific_ID'].isin(participants['PROLIFIC_ID'])].copy()

# Convert to numeric, handling NaNs
UCLA_clean.set_index('Prolific_ID', inplace=True)
UCLA_clean = UCLA_clean.apply(pd.to_numeric, errors='coerce').fillna(0).astype(int)

# Compute UCLA Score
UCLA_score = UCLA_clean.copy()
UCLA_score["UCLA_score"] = UCLA_clean.sum(axis=1)  # Sum UCLA items row-wise

# Save to CSV
ucla = pd.DataFrame()
ucla['Prolific_ID'] = UCLA_clean.index  # Restore Prolific_ID
ucla['UCLA_score'] = UCLA_score["UCLA_score"].values

print(ucla.head())  # Debugging step

ucla.to_csv('%s/ucla.csv' % (path.parent), index=False)
