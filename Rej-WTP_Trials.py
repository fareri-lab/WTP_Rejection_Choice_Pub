#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 21:27:39 2023

@author: melanieruiz
"""

import pandas as pd
import os
from itertools import product



sub = 106
# os.chdir('/Users/dfareri/Documents/GitHub/r15-WTP/stimuli/Scan-Thinking/event-related/params/sub-9999')
wtp = pd.read_csv('/Users/dfareri/Dropbox/Dominic/Github/fareri-lab/r15-WTP/WTP_exp.csv')

# wtp = pd.DataFrame(data=wtp1.append(wtp2))


# wtp['Left_Exp']= wtp1['Left_Exp']
# wtp['Right_Exp']= wtp1['Right_Exp']

new_wtp = pd.DataFrame(list(product(wtp['exp1'], wtp['exp2'])), columns=['Right', 'Left'])
new_wtp['TrialNumber']= range(1,101)

path= '/Users/dfareri/Dropbox/Dominic/Github/fareri-lab/r15-WTP/stimuli/Scan-WTP/event-related/params/'
os.chdir(path)
subdir = path + '/sub-9998/'
os.makedirs(subdir, exist_ok=True)
print('Directory for subject %s has been created' %(sub))

run1 = new_wtp[(new_wtp["TrialNumber"] < 26)]
run1.to_csv(subdir+ 'sub-9998_run-1_design.csv')

run2 = new_wtp[(new_wtp["TrialNumber"] > 25) & (new_wtp["TrialNumber"] < 51)]
run2.to_csv(subdir+'sub-9998_run-2_design.csv')

run3 = new_wtp[(new_wtp["TrialNumber"] > 50) & (new_wtp["TrialNumber"] < 76)]
run3.to_csv(subdir+ 'sub-9998_run-3_design.csv')


run4 = new_wtp[(new_wtp["TrialNumber"] > 75) & (new_wtp["TrialNumber"] < 101)]
run4.to_csv(subdir+ 'sub-9998_run-4_design.csv')

# new_wtp.to_csv('')
