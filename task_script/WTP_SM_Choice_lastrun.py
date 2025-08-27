#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.1),
    on Wed Jan  3 22:24:40 2024
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

import psychopy
psychopy.useVersion('2022.2.1')


# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Run 'Before Experiment' code from saliencyrating_code
saliencerating = ''
salienceratingtext=''
rating_forsalience = ''    

# Run 'Before Experiment' code from stresslevelslider
stresslevel = ''
stressleveltext = ''
rating_forstress = ''


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.1'
expName = 'RejectionTask_OneLoop'  # from the Builder filename that created this script
expInfo = {
    'participant': '',
    'session': '001',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s/%s_%s_%s' % (expInfo['participant'],expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/melanieruiz/Desktop/WTP_SM_Choice/WTP_SM_Choice_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1440, 900], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='norm')
win.mouseVisible = True
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}
ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='ptb')

# --- Initialize components for Routine "Welcome_Screen" ---
Welcome = visual.TextStim(win=win, name='Welcome',
    text='Welcome to the Instagram Sharing Task!\n\n\nToday you will have the opportunity to share some of your Instagram photos with other participants and receive feedback.\n\n\n\nPress space to continue.\n',
    font='Open Sans',
    pos=(0, 0), height=0.08, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
endwelcomescreen_keys = keyboard.Keyboard()
# Run 'Begin Experiment' code from spreadsheets
partnermatch = ''
partneravatar = ''
trialset = range(0,5)

# --- Initialize components for Routine "First_Instructions" ---
FirstInstructions = visual.TextStim(win=win, name='FirstInstructions',
    text='To begin, you will be assigned a partner at random by the computer. Next, your instagram photos will be shared with your partner. After each photo is shared, your partner will give you feedback on whether they liked or disliked your photo. You will have the chance to share your photos with 3 different partners during todays task.\n\n\nYou may be eligible throughout the task to participate in a lottery, which you may play yourself or have the computer play on your behalf. Further instructions about this task will be provided should you be eligible to participate.\n\n\nPress space to continue.',
    font='Open Sans',
    pos=(0,0), height=0.08, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
endinstructionscreen_keys = keyboard.Keyboard()

# --- Initialize components for Routine "partner_code" ---
# Run 'Begin Experiment' code from partnermatchcode
partnermatch = ''
partneravatar = ''


# --- Initialize components for Routine "WaitingToMatch" ---
Match_text = visual.TextStim(win=win, name='Match_text',
    text='You will now be matched with a game partner selected at random by the computer.',
    font='Open Sans',
    pos=(0, 0.3), height=0.08, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
syncing_text = visual.TextStim(win=win, name='syncing_text',
    text='Syncing…',
    font='Open Sans',
    pos=(0, 0.3), height=0.12, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
text_0 = visual.TextStim(win=win, name='text_0',
    text='0%',
    font='Open Sans',
    pos=(0, -0.2), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
Transparent = visual.Rect(
    win=win, name='Transparent',
    width=(1, 0.1)[0], height=(1, 0.1)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.2,     colorSpace='rgb',  lineColor='white', fillColor=[0.0000, 0.0000, 0.0000],
    opacity=None, depth=-4.0, interpolate=True)
Loading_25 = visual.Rect(
    win=win, name='Loading_25',
    width=(0.25, 0.1)[0], height=(0.25, 0.1)[1],
    ori=0.0, pos=(-0.375, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-5.0, interpolate=True)
text_25 = visual.TextStim(win=win, name='text_25',
    text='25%',
    font='Open Sans',
    pos=(0, -.2), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
Loading_50 = visual.Rect(
    win=win, name='Loading_50',
    width=(.5, 0.1)[0], height=(.5, 0.1)[1],
    ori=0.0, pos=(-0.25, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-7.0, interpolate=True)
text_50 = visual.TextStim(win=win, name='text_50',
    text='50%',
    font='Open Sans',
    pos=(0, -.2), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);
Loading_75 = visual.Rect(
    win=win, name='Loading_75',
    width=(0.75, 0.1)[0], height=(0.75, 0.1)[1],
    ori=0.0, pos=(-.125, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-9.0, interpolate=True)
text_75 = visual.TextStim(win=win, name='text_75',
    text='75%',
    font='Open Sans',
    pos=(0, -.2), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-10.0);
Loading_100 = visual.Rect(
    win=win, name='Loading_100',
    width=(1, 0.1)[0], height=(1, 0.1)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-11.0, interpolate=True)
text_100 = visual.TextStim(win=win, name='text_100',
    text='100%',
    font='Open Sans',
    pos=(0, -.2), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-12.0);

# --- Initialize components for Routine "Partner_Match" ---
Youhavematched = visual.TextStim(win=win, name='Youhavematched',
    text='',
    font='Open Sans',
    pos=(0, 0.6), height=0.08, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
partneremoji_image = visual.ImageStim(
    win=win,
    name='partneremoji_image', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.75),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
endpartnermatch_keys = keyboard.Keyboard()
PressToContinue = visual.TextStim(win=win, name='PressToContinue',
    text='Press space to continue.',
    font='Open Sans',
    pos=(0, -0.6), height=0.08, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);

# --- Initialize components for Routine "Photo_Share" ---
photobeingshared_text = visual.TextStim(win=win, name='photobeingshared_text',
    text='This photo is now being shared',
    font='Open Sans',
    pos=(0.0,0.6), height=0.09, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
waitforfeedback_text = visual.TextStim(win=win, name='waitforfeedback_text',
    text='Please wait for feedback.',
    font='Open Sans',
    pos=(0, -0.6), height=0.09, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
# Run 'Begin Experiment' code from initiatefeedbackresponses
feedbackresponses = ''
fdbkimage = ''
participantimage_image = visual.ImageStim(
    win=win,
    name='participantimage_image', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.75),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)

# --- Initialize components for Routine "Waitingforfeedback" ---
waiting_text = visual.TextStim(win=win, name='waiting_text',
    text='Waiting…',
    font='Open Sans',
    pos=(0, 0.0), height=0.15, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "feedback" ---
displayfeedback_text = visual.TextStim(win=win, name='displayfeedback_text',
    text='',
    font='Open Sans',
    pos=(0, 0.75), height=0.12, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
fdbkimage_image = visual.ImageStim(
    win=win,
    name='fdbkimage_image', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.75, 1.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
# Run 'Begin Experiment' code from initiatelottery_code
WTPlottery = ''

# --- Initialize components for Routine "continuesharing" ---
presstosharenextphoto_text = visual.TextStim(win=win, name='presstosharenextphoto_text',
    text='Press space to share your next photo.',
    font='Open Sans',
    pos=(0, 0), height=0.09, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
sharenextphoto_key = keyboard.Keyboard()

# --- Initialize components for Routine "WTP_Instructions1" ---
WTP_ins_text1 = visual.TextStim(win=win, name='WTP_ins_text1',
    text="In this part of the task, you will be choosing between two options.\n\nPlease indicate which option you would prefer by using your keyboard to press '1' for the choice on the left, or '2' for the choice on the right. \n\nEach option is associated with a price, which will be subtracted from your earnings from the previous task upon making a selection. \n\nPress SPACE to continue.",
    font='Open Sans',
    pos=(0, 0.3), height=0.07, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
WTP_ins_keys1 = keyboard.Keyboard()

# --- Initialize components for Routine "WTP_Instructions2" ---
WTP_ins_text2 = visual.TextStim(win=win, name='WTP_ins_text2',
    text='Imagine yourself actually doing the experiences shown on screen before making your decision.\n\nYou will have ten seconds to make a response after seeing the choices. \n\nWhen you make your choice, your selection will turn green. \n\nPress SPACE to start the task.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
WTP_ins_keys2 = keyboard.Keyboard()

# --- Initialize components for Routine "WTPTask" ---
Left_Experience = visual.TextStim(win=win, name='Left_Experience',
    text='',
    font='Open Sans',
    pos=(0.5, 0.1), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Right_Experience = visual.TextStim(win=win, name='Right_Experience',
    text='',
    font='Open Sans',
    pos=(-0.5, 0.1), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
Left_Price = visual.TextStim(win=win, name='Left_Price',
    text='',
    font='Open Sans',
    pos=(0.5, -0.5), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
Right_Price = visual.TextStim(win=win, name='Right_Price',
    text='',
    font='Open Sans',
    pos=(-0.5, -0.5), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
responses = keyboard.Keyboard()

# --- Initialize components for Routine "ITI" ---
ITI_text = visual.TextStim(win=win, name='ITI_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "Continue" ---
# Run 'Begin Experiment' code from code
resumetext = ''
Resume_keys = keyboard.Keyboard()
Resume_Text = visual.TextStim(win=win, name='Resume_Text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.12, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# --- Initialize components for Routine "SalienceRating" ---
# Run 'Begin Experiment' code from saliencyrating_code
salience_slider = visual.Slider(win=win, name='slider',
    startValue=999, size=(1.0, 0.1), pos=(0, -0.4), units=None,
    labels=(1, 2, 3, 4, 5), ticks=(1, 2, 3, 4, 5), granularity=0.0,
    style='rating', styleTweaks=('labels45', 'triangleMarker'), opacity=None,
    labelColor='white', markerColor='cornflowerblue', lineColor='white', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05, 
    flip=False, ori=0.0, depth=-5, readOnly=False)
saliencequestion_text = visual.TextStim(win=win, name='saliencequestion_text',
    text='',
    font='Open Sans',
    pos=(0, 0.6), height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp = keyboard.Keyboard()
salienceavatar_image = visual.ImageStim(
    win=win,
    name='salienceavatar_image', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.3, 0.55),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
saliencecontinue_text = visual.TextStim(win=win, name='saliencecontinue_text',
    text='Press space to enter rating and continue.',
    font='Open Sans',
    pos=(0, -0.8), height=0.07, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
displayrating_text = visual.TextStim(win=win, name='displayrating_text',
    text='',
    font='Open Sans',
    pos=(0, -0.65), height=0.065, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);

# --- Initialize components for Routine "StressLevel" ---
# Run 'Begin Experiment' code from stresslevelslider
stress_slider = visual.Slider(win=win, name='slider',
    startValue=999, size=(1.0, 0.1), pos=(0, -0.4), units=None,
    labels=(1, 2, 3, 4, 5, 6, 7, 8, 9), ticks=(1, 2, 3, 4, 5, 6, 7, 8, 9), granularity=0.0,
    style='rating', styleTweaks=('labels45', 'triangleMarker'), opacity=None,
    labelColor='white', markerColor='cornflowerblue', lineColor='white', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, ori=0.0, depth=-5, readOnly=False)
stresslevel_text = visual.TextStim(win=win, name='stresslevel_text',
    text='',
    font='Open Sans',
    pos=(0, 0.3), height=0.08, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
stresslevel_keypress = keyboard.Keyboard()
displaystressrating_text = visual.TextStim(win=win, name='displaystressrating_text',
    text='',
    font='Open Sans',
    pos=(0, -0.65), height=0.08, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "Welcome_Screen" ---
continueRoutine = True
# update component parameters for each repeat
endwelcomescreen_keys.keys = []
endwelcomescreen_keys.rt = []
_endwelcomescreen_keys_allKeys = []
# Run 'Begin Routine' code from spreadsheets
import pandas as pd

subid = expInfo['participant']
expdir = os.getcwd()
subjdir = '%s/Participant_Images/%s' % (expdir, subid)
trial_sheet = '%s/%s_trials.csv' %(subjdir,subid)
wtp_sheet = '%s/%s_WTP.xlsx' %(subjdir, subid)

#wtp_sheet = pd.read_csv('%s/%s_WTP.csv' %(subjdir, subid), encoding = 'unicode_escape')
partnermatch = ''
partneravatar = ''
# keep track of which components have finished
Welcome_ScreenComponents = [Welcome, endwelcomescreen_keys]
for thisComponent in Welcome_ScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Welcome_Screen" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Welcome* updates
    if Welcome.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Welcome.frameNStart = frameN  # exact frame index
        Welcome.tStart = t  # local t and not account for scr refresh
        Welcome.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Welcome, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'Welcome.started')
        Welcome.setAutoDraw(True)
    
    # *endwelcomescreen_keys* updates
    waitOnFlip = False
    if endwelcomescreen_keys.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        endwelcomescreen_keys.frameNStart = frameN  # exact frame index
        endwelcomescreen_keys.tStart = t  # local t and not account for scr refresh
        endwelcomescreen_keys.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(endwelcomescreen_keys, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'endwelcomescreen_keys.started')
        endwelcomescreen_keys.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(endwelcomescreen_keys.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(endwelcomescreen_keys.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if endwelcomescreen_keys.status == STARTED and not waitOnFlip:
        theseKeys = endwelcomescreen_keys.getKeys(keyList=['space'], waitRelease=False)
        _endwelcomescreen_keys_allKeys.extend(theseKeys)
        if len(_endwelcomescreen_keys_allKeys):
            endwelcomescreen_keys.keys = _endwelcomescreen_keys_allKeys[-1].name  # just the last key pressed
            endwelcomescreen_keys.rt = _endwelcomescreen_keys_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Welcome_ScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Welcome_Screen" ---
for thisComponent in Welcome_ScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if endwelcomescreen_keys.keys in ['', [], None]:  # No response was made
    endwelcomescreen_keys.keys = None
thisExp.addData('endwelcomescreen_keys.keys',endwelcomescreen_keys.keys)
if endwelcomescreen_keys.keys != None:  # we had a response
    thisExp.addData('endwelcomescreen_keys.rt', endwelcomescreen_keys.rt)
thisExp.nextEntry()
# the Routine "Welcome_Screen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "First_Instructions" ---
continueRoutine = True
# update component parameters for each repeat
endinstructionscreen_keys.keys = []
endinstructionscreen_keys.rt = []
_endinstructionscreen_keys_allKeys = []
# keep track of which components have finished
First_InstructionsComponents = [FirstInstructions, endinstructionscreen_keys]
for thisComponent in First_InstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "First_Instructions" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *FirstInstructions* updates
    if FirstInstructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        FirstInstructions.frameNStart = frameN  # exact frame index
        FirstInstructions.tStart = t  # local t and not account for scr refresh
        FirstInstructions.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(FirstInstructions, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'FirstInstructions.started')
        FirstInstructions.setAutoDraw(True)
    
    # *endinstructionscreen_keys* updates
    waitOnFlip = False
    if endinstructionscreen_keys.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        endinstructionscreen_keys.frameNStart = frameN  # exact frame index
        endinstructionscreen_keys.tStart = t  # local t and not account for scr refresh
        endinstructionscreen_keys.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(endinstructionscreen_keys, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'endinstructionscreen_keys.started')
        endinstructionscreen_keys.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(endinstructionscreen_keys.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(endinstructionscreen_keys.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if endinstructionscreen_keys.status == STARTED and not waitOnFlip:
        theseKeys = endinstructionscreen_keys.getKeys(keyList=['space'], waitRelease=False)
        _endinstructionscreen_keys_allKeys.extend(theseKeys)
        if len(_endinstructionscreen_keys_allKeys):
            endinstructionscreen_keys.keys = _endinstructionscreen_keys_allKeys[-1].name  # just the last key pressed
            endinstructionscreen_keys.rt = _endinstructionscreen_keys_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in First_InstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "First_Instructions" ---
for thisComponent in First_InstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if endinstructionscreen_keys.keys in ['', [], None]:  # No response was made
    endinstructionscreen_keys.keys = None
thisExp.addData('endinstructionscreen_keys.keys',endinstructionscreen_keys.keys)
if endinstructionscreen_keys.keys != None:  # we had a response
    thisExp.addData('endinstructionscreen_keys.rt', endinstructionscreen_keys.rt)
thisExp.nextEntry()
# the Routine "First_Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
entiretaskloop = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(trial_sheet),
    seed=None, name='entiretaskloop')
thisExp.addLoop(entiretaskloop)  # add the loop to the experiment
thisEntiretaskloop = entiretaskloop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisEntiretaskloop.rgb)
if thisEntiretaskloop != None:
    for paramName in thisEntiretaskloop:
        exec('{} = thisEntiretaskloop[paramName]'.format(paramName))

for thisEntiretaskloop in entiretaskloop:
    currentLoop = entiretaskloop
    # abbreviate parameter names if possible (e.g. rgb = thisEntiretaskloop.rgb)
    if thisEntiretaskloop != None:
        for paramName in thisEntiretaskloop:
            exec('{} = thisEntiretaskloop[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "partner_code" ---
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    partner_codeComponents = []
    for thisComponent in partner_codeComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "partner_code" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in partner_codeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "partner_code" ---
    for thisComponent in partner_codeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from partnermatchcode
    partnermatch = (f'You have matched with: {Partner}')
    if Partner == 'Sam':
        partneravatar='Images/nerdemoji_nobackground.png'
    elif Partner == 'Riley':
        partneravatar='Images/sunglassemoji_nobackground.png'
    elif Partner == 'Charlie':
        partneravatar='Images/smilingemoji.png'
    elif Partner == 'Alex':
        partneravatar='Images/cowboyemoji.png'
    elif Partner == 'Taylor':
        partneravatar='Images/huggingemoji.png'
    # the Routine "partner_code" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "WaitingToMatch" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from showloadingbar
    if TrialNumber not in [1, 31, 61]: # establishes two blocks per 32 trials
        continueRoutine = False # if not trial 31 or 63, skip routine completely
    # keep track of which components have finished
    WaitingToMatchComponents = [Match_text, syncing_text, text_0, Transparent, Loading_25, text_25, Loading_50, text_50, Loading_75, text_75, Loading_100, text_100]
    for thisComponent in WaitingToMatchComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "WaitingToMatch" ---
    while continueRoutine and routineTimer.getTime() < 9.25:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Match_text* updates
        if Match_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Match_text.frameNStart = frameN  # exact frame index
            Match_text.tStart = t  # local t and not account for scr refresh
            Match_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Match_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Match_text.started')
            Match_text.setAutoDraw(True)
        if Match_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Match_text.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                Match_text.tStop = t  # not accounting for scr refresh
                Match_text.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Match_text.stopped')
                Match_text.setAutoDraw(False)
        
        # *syncing_text* updates
        if syncing_text.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
            # keep track of start time/frame for later
            syncing_text.frameNStart = frameN  # exact frame index
            syncing_text.tStart = t  # local t and not account for scr refresh
            syncing_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(syncing_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'syncing_text.started')
            syncing_text.setAutoDraw(True)
        if syncing_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > syncing_text.tStartRefresh + 6.25-frameTolerance:
                # keep track of stop time/frame for later
                syncing_text.tStop = t  # not accounting for scr refresh
                syncing_text.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'syncing_text.stopped')
                syncing_text.setAutoDraw(False)
        
        # *text_0* updates
        if text_0.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
            # keep track of start time/frame for later
            text_0.frameNStart = frameN  # exact frame index
            text_0.tStart = t  # local t and not account for scr refresh
            text_0.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_0, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_0.started')
            text_0.setAutoDraw(True)
        if text_0.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_0.tStartRefresh + 1.25-frameTolerance:
                # keep track of stop time/frame for later
                text_0.tStop = t  # not accounting for scr refresh
                text_0.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_0.stopped')
                text_0.setAutoDraw(False)
        
        # *Transparent* updates
        if Transparent.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
            # keep track of start time/frame for later
            Transparent.frameNStart = frameN  # exact frame index
            Transparent.tStart = t  # local t and not account for scr refresh
            Transparent.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Transparent, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Transparent.started')
            Transparent.setAutoDraw(True)
        if Transparent.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Transparent.tStartRefresh + 6.25-frameTolerance:
                # keep track of stop time/frame for later
                Transparent.tStop = t  # not accounting for scr refresh
                Transparent.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Transparent.stopped')
                Transparent.setAutoDraw(False)
        
        # *Loading_25* updates
        if Loading_25.status == NOT_STARTED and tThisFlip >= 4.25-frameTolerance:
            # keep track of start time/frame for later
            Loading_25.frameNStart = frameN  # exact frame index
            Loading_25.tStart = t  # local t and not account for scr refresh
            Loading_25.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Loading_25, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Loading_25.started')
            Loading_25.setAutoDraw(True)
        if Loading_25.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Loading_25.tStartRefresh + 1.25-frameTolerance:
                # keep track of stop time/frame for later
                Loading_25.tStop = t  # not accounting for scr refresh
                Loading_25.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Loading_25.stopped')
                Loading_25.setAutoDraw(False)
        
        # *text_25* updates
        if text_25.status == NOT_STARTED and tThisFlip >= 4.25-frameTolerance:
            # keep track of start time/frame for later
            text_25.frameNStart = frameN  # exact frame index
            text_25.tStart = t  # local t and not account for scr refresh
            text_25.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_25, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_25.started')
            text_25.setAutoDraw(True)
        if text_25.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_25.tStartRefresh + 1.25-frameTolerance:
                # keep track of stop time/frame for later
                text_25.tStop = t  # not accounting for scr refresh
                text_25.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_25.stopped')
                text_25.setAutoDraw(False)
        
        # *Loading_50* updates
        if Loading_50.status == NOT_STARTED and tThisFlip >= 5.5-frameTolerance:
            # keep track of start time/frame for later
            Loading_50.frameNStart = frameN  # exact frame index
            Loading_50.tStart = t  # local t and not account for scr refresh
            Loading_50.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Loading_50, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Loading_50.started')
            Loading_50.setAutoDraw(True)
        if Loading_50.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Loading_50.tStartRefresh + 1.25-frameTolerance:
                # keep track of stop time/frame for later
                Loading_50.tStop = t  # not accounting for scr refresh
                Loading_50.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Loading_50.stopped')
                Loading_50.setAutoDraw(False)
        
        # *text_50* updates
        if text_50.status == NOT_STARTED and tThisFlip >= 5.5-frameTolerance:
            # keep track of start time/frame for later
            text_50.frameNStart = frameN  # exact frame index
            text_50.tStart = t  # local t and not account for scr refresh
            text_50.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_50, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_50.started')
            text_50.setAutoDraw(True)
        if text_50.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_50.tStartRefresh + 1.25-frameTolerance:
                # keep track of stop time/frame for later
                text_50.tStop = t  # not accounting for scr refresh
                text_50.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_50.stopped')
                text_50.setAutoDraw(False)
        
        # *Loading_75* updates
        if Loading_75.status == NOT_STARTED and tThisFlip >= 6.75-frameTolerance:
            # keep track of start time/frame for later
            Loading_75.frameNStart = frameN  # exact frame index
            Loading_75.tStart = t  # local t and not account for scr refresh
            Loading_75.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Loading_75, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Loading_75.started')
            Loading_75.setAutoDraw(True)
        if Loading_75.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Loading_75.tStartRefresh + 1.25-frameTolerance:
                # keep track of stop time/frame for later
                Loading_75.tStop = t  # not accounting for scr refresh
                Loading_75.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Loading_75.stopped')
                Loading_75.setAutoDraw(False)
        
        # *text_75* updates
        if text_75.status == NOT_STARTED and tThisFlip >= 6.75-frameTolerance:
            # keep track of start time/frame for later
            text_75.frameNStart = frameN  # exact frame index
            text_75.tStart = t  # local t and not account for scr refresh
            text_75.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_75, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_75.started')
            text_75.setAutoDraw(True)
        if text_75.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_75.tStartRefresh + 1.25-frameTolerance:
                # keep track of stop time/frame for later
                text_75.tStop = t  # not accounting for scr refresh
                text_75.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_75.stopped')
                text_75.setAutoDraw(False)
        
        # *Loading_100* updates
        if Loading_100.status == NOT_STARTED and tThisFlip >= 8-frameTolerance:
            # keep track of start time/frame for later
            Loading_100.frameNStart = frameN  # exact frame index
            Loading_100.tStart = t  # local t and not account for scr refresh
            Loading_100.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Loading_100, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Loading_100.started')
            Loading_100.setAutoDraw(True)
        if Loading_100.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Loading_100.tStartRefresh + 1.25-frameTolerance:
                # keep track of stop time/frame for later
                Loading_100.tStop = t  # not accounting for scr refresh
                Loading_100.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Loading_100.stopped')
                Loading_100.setAutoDraw(False)
        
        # *text_100* updates
        if text_100.status == NOT_STARTED and tThisFlip >= 8-frameTolerance:
            # keep track of start time/frame for later
            text_100.frameNStart = frameN  # exact frame index
            text_100.tStart = t  # local t and not account for scr refresh
            text_100.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_100, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_100.started')
            text_100.setAutoDraw(True)
        if text_100.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_100.tStartRefresh + 1.25-frameTolerance:
                # keep track of stop time/frame for later
                text_100.tStop = t  # not accounting for scr refresh
                text_100.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_100.stopped')
                text_100.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in WaitingToMatchComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "WaitingToMatch" ---
    for thisComponent in WaitingToMatchComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine
    routineTimer.addTime(-9.250000)
    
    # --- Prepare to start Routine "Partner_Match" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from showpartnermatch
    if TrialNumber not in [1, 31, 61]: # establishes two blocks per 32 trials
        continueRoutine = False # if not trial 31 or 63, skip routine completely
    Youhavematched.setText(partnermatch)
    partneremoji_image.setImage(partneravatar)
    endpartnermatch_keys.keys = []
    endpartnermatch_keys.rt = []
    _endpartnermatch_keys_allKeys = []
    # keep track of which components have finished
    Partner_MatchComponents = [Youhavematched, partneremoji_image, endpartnermatch_keys, PressToContinue]
    for thisComponent in Partner_MatchComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Partner_Match" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Youhavematched* updates
        if Youhavematched.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Youhavematched.frameNStart = frameN  # exact frame index
            Youhavematched.tStart = t  # local t and not account for scr refresh
            Youhavematched.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Youhavematched, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Youhavematched.started')
            Youhavematched.setAutoDraw(True)
        
        # *partneremoji_image* updates
        if partneremoji_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            partneremoji_image.frameNStart = frameN  # exact frame index
            partneremoji_image.tStart = t  # local t and not account for scr refresh
            partneremoji_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(partneremoji_image, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'partneremoji_image.started')
            partneremoji_image.setAutoDraw(True)
        
        # *endpartnermatch_keys* updates
        waitOnFlip = False
        if endpartnermatch_keys.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            endpartnermatch_keys.frameNStart = frameN  # exact frame index
            endpartnermatch_keys.tStart = t  # local t and not account for scr refresh
            endpartnermatch_keys.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(endpartnermatch_keys, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'endpartnermatch_keys.started')
            endpartnermatch_keys.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(endpartnermatch_keys.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(endpartnermatch_keys.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if endpartnermatch_keys.status == STARTED and not waitOnFlip:
            theseKeys = endpartnermatch_keys.getKeys(keyList=['space'], waitRelease=False)
            _endpartnermatch_keys_allKeys.extend(theseKeys)
            if len(_endpartnermatch_keys_allKeys):
                endpartnermatch_keys.keys = _endpartnermatch_keys_allKeys[-1].name  # just the last key pressed
                endpartnermatch_keys.rt = _endpartnermatch_keys_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *PressToContinue* updates
        if PressToContinue.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            PressToContinue.frameNStart = frameN  # exact frame index
            PressToContinue.tStart = t  # local t and not account for scr refresh
            PressToContinue.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(PressToContinue, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'PressToContinue.started')
            PressToContinue.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Partner_MatchComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Partner_Match" ---
    for thisComponent in Partner_MatchComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if endpartnermatch_keys.keys in ['', [], None]:  # No response was made
        endpartnermatch_keys.keys = None
    entiretaskloop.addData('endpartnermatch_keys.keys',endpartnermatch_keys.keys)
    if endpartnermatch_keys.keys != None:  # we had a response
        entiretaskloop.addData('endpartnermatch_keys.rt', endpartnermatch_keys.rt)
    # the Routine "Partner_Match" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Photo_Share" ---
    continueRoutine = True
    # update component parameters for each repeat
    participantimage_image.setImage(Photos)
    # keep track of which components have finished
    Photo_ShareComponents = [photobeingshared_text, waitforfeedback_text, participantimage_image]
    for thisComponent in Photo_ShareComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Photo_Share" ---
    while continueRoutine and routineTimer.getTime() < 3.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *photobeingshared_text* updates
        if photobeingshared_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            photobeingshared_text.frameNStart = frameN  # exact frame index
            photobeingshared_text.tStart = t  # local t and not account for scr refresh
            photobeingshared_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(photobeingshared_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'photobeingshared_text.started')
            photobeingshared_text.setAutoDraw(True)
        if photobeingshared_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > photobeingshared_text.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                photobeingshared_text.tStop = t  # not accounting for scr refresh
                photobeingshared_text.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'photobeingshared_text.stopped')
                photobeingshared_text.setAutoDraw(False)
        
        # *waitforfeedback_text* updates
        if waitforfeedback_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            waitforfeedback_text.frameNStart = frameN  # exact frame index
            waitforfeedback_text.tStart = t  # local t and not account for scr refresh
            waitforfeedback_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(waitforfeedback_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'waitforfeedback_text.started')
            waitforfeedback_text.setAutoDraw(True)
        if waitforfeedback_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > waitforfeedback_text.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                waitforfeedback_text.tStop = t  # not accounting for scr refresh
                waitforfeedback_text.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'waitforfeedback_text.stopped')
                waitforfeedback_text.setAutoDraw(False)
        
        # *participantimage_image* updates
        if participantimage_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            participantimage_image.frameNStart = frameN  # exact frame index
            participantimage_image.tStart = t  # local t and not account for scr refresh
            participantimage_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(participantimage_image, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'participantimage_image.started')
            participantimage_image.setAutoDraw(True)
        if participantimage_image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > participantimage_image.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                participantimage_image.tStop = t  # not accounting for scr refresh
                participantimage_image.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'participantimage_image.stopped')
                participantimage_image.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Photo_ShareComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Photo_Share" ---
    for thisComponent in Photo_ShareComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from initiatefeedbackresponses
    feedbackresponses = (f'{Partner} {Feedback} your photo')
    if Feedback == 'liked':
        fdbkimage ='Images/thumbsup.png'
    elif Feedback == 'did not like':
        fdbkimage ='Images/thumbsdown.png'
    # using non-slip timing so subtract the expected duration of this Routine
    routineTimer.addTime(-3.000000)
    
    # --- Prepare to start Routine "Waitingforfeedback" ---
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    WaitingforfeedbackComponents = [waiting_text]
    for thisComponent in WaitingforfeedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Waitingforfeedback" ---
    while continueRoutine and routineTimer.getTime() < 5.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *waiting_text* updates
        if waiting_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            waiting_text.frameNStart = frameN  # exact frame index
            waiting_text.tStart = t  # local t and not account for scr refresh
            waiting_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(waiting_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'waiting_text.started')
            waiting_text.setAutoDraw(True)
        if waiting_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > waiting_text.tStartRefresh + 5.0-frameTolerance:
                # keep track of stop time/frame for later
                waiting_text.tStop = t  # not accounting for scr refresh
                waiting_text.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'waiting_text.stopped')
                waiting_text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in WaitingforfeedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Waitingforfeedback" ---
    for thisComponent in WaitingforfeedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine
    routineTimer.addTime(-5.000000)
    
    # --- Prepare to start Routine "feedback" ---
    continueRoutine = True
    # update component parameters for each repeat
    displayfeedback_text.setText(feedbackresponses)
    fdbkimage_image.setImage(fdbkimage)
    # Run 'Begin Routine' code from initiatelottery_code
    if TrialNumber%5 == 0: # lottery should only appear every 5 trials and not on trial 0 
        startWTP = 1
    else: 
        startWTP = 0
    # keep track of which components have finished
    feedbackComponents = [displayfeedback_text, fdbkimage_image]
    for thisComponent in feedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "feedback" ---
    while continueRoutine and routineTimer.getTime() < 3.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *displayfeedback_text* updates
        if displayfeedback_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            displayfeedback_text.frameNStart = frameN  # exact frame index
            displayfeedback_text.tStart = t  # local t and not account for scr refresh
            displayfeedback_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(displayfeedback_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'displayfeedback_text.started')
            displayfeedback_text.setAutoDraw(True)
        if displayfeedback_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > displayfeedback_text.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                displayfeedback_text.tStop = t  # not accounting for scr refresh
                displayfeedback_text.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'displayfeedback_text.stopped')
                displayfeedback_text.setAutoDraw(False)
        
        # *fdbkimage_image* updates
        if fdbkimage_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fdbkimage_image.frameNStart = frameN  # exact frame index
            fdbkimage_image.tStart = t  # local t and not account for scr refresh
            fdbkimage_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fdbkimage_image, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fdbkimage_image.started')
            fdbkimage_image.setAutoDraw(True)
        if fdbkimage_image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fdbkimage_image.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                fdbkimage_image.tStop = t  # not accounting for scr refresh
                fdbkimage_image.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fdbkimage_image.stopped')
                fdbkimage_image.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "feedback" ---
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine
    routineTimer.addTime(-3.000000)
    
    # --- Prepare to start Routine "continuesharing" ---
    continueRoutine = True
    # update component parameters for each repeat
    sharenextphoto_key.keys = []
    sharenextphoto_key.rt = []
    _sharenextphoto_key_allKeys = []
    # Run 'Begin Routine' code from hidecontinuesharingroutine_code
    if startWTP == 1:
        continueRoutine = False
    else:
        continueRoutine = True 
    # keep track of which components have finished
    continuesharingComponents = [presstosharenextphoto_text, sharenextphoto_key]
    for thisComponent in continuesharingComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "continuesharing" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *presstosharenextphoto_text* updates
        if presstosharenextphoto_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            presstosharenextphoto_text.frameNStart = frameN  # exact frame index
            presstosharenextphoto_text.tStart = t  # local t and not account for scr refresh
            presstosharenextphoto_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(presstosharenextphoto_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'presstosharenextphoto_text.started')
            presstosharenextphoto_text.setAutoDraw(True)
        
        # *sharenextphoto_key* updates
        waitOnFlip = False
        if sharenextphoto_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sharenextphoto_key.frameNStart = frameN  # exact frame index
            sharenextphoto_key.tStart = t  # local t and not account for scr refresh
            sharenextphoto_key.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sharenextphoto_key, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'sharenextphoto_key.started')
            sharenextphoto_key.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(sharenextphoto_key.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(sharenextphoto_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if sharenextphoto_key.status == STARTED and not waitOnFlip:
            theseKeys = sharenextphoto_key.getKeys(keyList=['space'], waitRelease=False)
            _sharenextphoto_key_allKeys.extend(theseKeys)
            if len(_sharenextphoto_key_allKeys):
                sharenextphoto_key.keys = _sharenextphoto_key_allKeys[0].name  # just the first key pressed
                sharenextphoto_key.rt = _sharenextphoto_key_allKeys[0].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in continuesharingComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "continuesharing" ---
    for thisComponent in continuesharingComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if sharenextphoto_key.keys in ['', [], None]:  # No response was made
        sharenextphoto_key.keys = None
    entiretaskloop.addData('sharenextphoto_key.keys',sharenextphoto_key.keys)
    if sharenextphoto_key.keys != None:  # we had a response
        entiretaskloop.addData('sharenextphoto_key.rt', sharenextphoto_key.rt)
    # Run 'End Routine' code from hidecontinuesharingroutine_code
    trialset = [i+5 for i in trialset]
    # the Routine "continuesharing" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    startWTPloop = data.TrialHandler(nReps=startWTP, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='startWTPloop')
    thisExp.addLoop(startWTPloop)  # add the loop to the experiment
    thisStartWTPloop = startWTPloop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisStartWTPloop.rgb)
    if thisStartWTPloop != None:
        for paramName in thisStartWTPloop:
            exec('{} = thisStartWTPloop[paramName]'.format(paramName))
    
    for thisStartWTPloop in startWTPloop:
        currentLoop = startWTPloop
        # abbreviate parameter names if possible (e.g. rgb = thisStartWTPloop.rgb)
        if thisStartWTPloop != None:
            for paramName in thisStartWTPloop:
                exec('{} = thisStartWTPloop[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "WTP_Instructions1" ---
        continueRoutine = True
        # update component parameters for each repeat
        WTP_ins_keys1.keys = []
        WTP_ins_keys1.rt = []
        _WTP_ins_keys1_allKeys = []
        # keep track of which components have finished
        WTP_Instructions1Components = [WTP_ins_text1, WTP_ins_keys1]
        for thisComponent in WTP_Instructions1Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "WTP_Instructions1" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *WTP_ins_text1* updates
            if WTP_ins_text1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                WTP_ins_text1.frameNStart = frameN  # exact frame index
                WTP_ins_text1.tStart = t  # local t and not account for scr refresh
                WTP_ins_text1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(WTP_ins_text1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'WTP_ins_text1.started')
                WTP_ins_text1.setAutoDraw(True)
            
            # *WTP_ins_keys1* updates
            waitOnFlip = False
            if WTP_ins_keys1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                WTP_ins_keys1.frameNStart = frameN  # exact frame index
                WTP_ins_keys1.tStart = t  # local t and not account for scr refresh
                WTP_ins_keys1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(WTP_ins_keys1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'WTP_ins_keys1.started')
                WTP_ins_keys1.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(WTP_ins_keys1.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(WTP_ins_keys1.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if WTP_ins_keys1.status == STARTED and not waitOnFlip:
                theseKeys = WTP_ins_keys1.getKeys(keyList=['space'], waitRelease=False)
                _WTP_ins_keys1_allKeys.extend(theseKeys)
                if len(_WTP_ins_keys1_allKeys):
                    WTP_ins_keys1.keys = _WTP_ins_keys1_allKeys[-1].name  # just the last key pressed
                    WTP_ins_keys1.rt = _WTP_ins_keys1_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in WTP_Instructions1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "WTP_Instructions1" ---
        for thisComponent in WTP_Instructions1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if WTP_ins_keys1.keys in ['', [], None]:  # No response was made
            WTP_ins_keys1.keys = None
        startWTPloop.addData('WTP_ins_keys1.keys',WTP_ins_keys1.keys)
        if WTP_ins_keys1.keys != None:  # we had a response
            startWTPloop.addData('WTP_ins_keys1.rt', WTP_ins_keys1.rt)
        # the Routine "WTP_Instructions1" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "WTP_Instructions2" ---
        continueRoutine = True
        # update component parameters for each repeat
        WTP_ins_keys2.keys = []
        WTP_ins_keys2.rt = []
        _WTP_ins_keys2_allKeys = []
        # keep track of which components have finished
        WTP_Instructions2Components = [WTP_ins_text2, WTP_ins_keys2]
        for thisComponent in WTP_Instructions2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "WTP_Instructions2" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *WTP_ins_text2* updates
            if WTP_ins_text2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                WTP_ins_text2.frameNStart = frameN  # exact frame index
                WTP_ins_text2.tStart = t  # local t and not account for scr refresh
                WTP_ins_text2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(WTP_ins_text2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'WTP_ins_text2.started')
                WTP_ins_text2.setAutoDraw(True)
            
            # *WTP_ins_keys2* updates
            waitOnFlip = False
            if WTP_ins_keys2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                WTP_ins_keys2.frameNStart = frameN  # exact frame index
                WTP_ins_keys2.tStart = t  # local t and not account for scr refresh
                WTP_ins_keys2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(WTP_ins_keys2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'WTP_ins_keys2.started')
                WTP_ins_keys2.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(WTP_ins_keys2.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(WTP_ins_keys2.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if WTP_ins_keys2.status == STARTED and not waitOnFlip:
                theseKeys = WTP_ins_keys2.getKeys(keyList=['space'], waitRelease=False)
                _WTP_ins_keys2_allKeys.extend(theseKeys)
                if len(_WTP_ins_keys2_allKeys):
                    WTP_ins_keys2.keys = _WTP_ins_keys2_allKeys[-1].name  # just the last key pressed
                    WTP_ins_keys2.rt = _WTP_ins_keys2_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in WTP_Instructions2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "WTP_Instructions2" ---
        for thisComponent in WTP_Instructions2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if WTP_ins_keys2.keys in ['', [], None]:  # No response was made
            WTP_ins_keys2.keys = None
        startWTPloop.addData('WTP_ins_keys2.keys',WTP_ins_keys2.keys)
        if WTP_ins_keys2.keys != None:  # we had a response
            startWTPloop.addData('WTP_ins_keys2.rt', WTP_ins_keys2.rt)
        # the Routine "WTP_Instructions2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        WTPTaskLoop = data.TrialHandler(nReps=1.0, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions(wtp_sheet, selection=trialset),
            seed=None, name='WTPTaskLoop')
        thisExp.addLoop(WTPTaskLoop)  # add the loop to the experiment
        thisWTPTaskLoop = WTPTaskLoop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisWTPTaskLoop.rgb)
        if thisWTPTaskLoop != None:
            for paramName in thisWTPTaskLoop:
                exec('{} = thisWTPTaskLoop[paramName]'.format(paramName))
        
        for thisWTPTaskLoop in WTPTaskLoop:
            currentLoop = WTPTaskLoop
            # abbreviate parameter names if possible (e.g. rgb = thisWTPTaskLoop.rgb)
            if thisWTPTaskLoop != None:
                for paramName in thisWTPTaskLoop:
                    exec('{} = thisWTPTaskLoop[paramName]'.format(paramName))
            
            # --- Prepare to start Routine "WTPTask" ---
            continueRoutine = True
            # update component parameters for each repeat
            Left_Experience.setColor('white', colorSpace='rgb')
            Left_Experience.setText(Left_Exp)
            Right_Experience.setColor('white', colorSpace='rgb')
            Right_Experience.setText(Right_Exp)
            Left_Price.setText(leftmoney)
            Right_Price.setColor('white', colorSpace='rgb')
            Right_Price.setText(rightmoney)
            responses.keys = []
            responses.rt = []
            _responses_allKeys = []
            # keep track of which components have finished
            WTPTaskComponents = [Left_Experience, Right_Experience, Left_Price, Right_Price, responses]
            for thisComponent in WTPTaskComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "WTPTask" ---
            while continueRoutine and routineTimer.getTime() < 10.0:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *Left_Experience* updates
                if Left_Experience.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Left_Experience.frameNStart = frameN  # exact frame index
                    Left_Experience.tStart = t  # local t and not account for scr refresh
                    Left_Experience.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Left_Experience, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Left_Experience.started')
                    Left_Experience.setAutoDraw(True)
                if Left_Experience.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Left_Experience.tStartRefresh + 10-frameTolerance:
                        # keep track of stop time/frame for later
                        Left_Experience.tStop = t  # not accounting for scr refresh
                        Left_Experience.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'Left_Experience.stopped')
                        Left_Experience.setAutoDraw(False)
                
                # *Right_Experience* updates
                if Right_Experience.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Right_Experience.frameNStart = frameN  # exact frame index
                    Right_Experience.tStart = t  # local t and not account for scr refresh
                    Right_Experience.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Right_Experience, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Right_Experience.started')
                    Right_Experience.setAutoDraw(True)
                if Right_Experience.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Right_Experience.tStartRefresh + 10-frameTolerance:
                        # keep track of stop time/frame for later
                        Right_Experience.tStop = t  # not accounting for scr refresh
                        Right_Experience.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'Right_Experience.stopped')
                        Right_Experience.setAutoDraw(False)
                
                # *Left_Price* updates
                if Left_Price.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Left_Price.frameNStart = frameN  # exact frame index
                    Left_Price.tStart = t  # local t and not account for scr refresh
                    Left_Price.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Left_Price, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Left_Price.started')
                    Left_Price.setAutoDraw(True)
                if Left_Price.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Left_Price.tStartRefresh + 10-frameTolerance:
                        # keep track of stop time/frame for later
                        Left_Price.tStop = t  # not accounting for scr refresh
                        Left_Price.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'Left_Price.stopped')
                        Left_Price.setAutoDraw(False)
                
                # *Right_Price* updates
                if Right_Price.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Right_Price.frameNStart = frameN  # exact frame index
                    Right_Price.tStart = t  # local t and not account for scr refresh
                    Right_Price.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Right_Price, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Right_Price.started')
                    Right_Price.setAutoDraw(True)
                if Right_Price.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Right_Price.tStartRefresh + 10-frameTolerance:
                        # keep track of stop time/frame for later
                        Right_Price.tStop = t  # not accounting for scr refresh
                        Right_Price.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'Right_Price.stopped')
                        Right_Price.setAutoDraw(False)
                
                # *responses* updates
                waitOnFlip = False
                if responses.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    responses.frameNStart = frameN  # exact frame index
                    responses.tStart = t  # local t and not account for scr refresh
                    responses.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(responses, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'responses.started')
                    responses.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(responses.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(responses.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if responses.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > responses.tStartRefresh + 10-frameTolerance:
                        # keep track of stop time/frame for later
                        responses.tStop = t  # not accounting for scr refresh
                        responses.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'responses.stopped')
                        responses.status = FINISHED
                if responses.status == STARTED and not waitOnFlip:
                    theseKeys = responses.getKeys(keyList=['1','2'], waitRelease=False)
                    _responses_allKeys.extend(theseKeys)
                    if len(_responses_allKeys):
                        responses.keys = _responses_allKeys[0].name  # just the first key pressed
                        responses.rt = _responses_allKeys[0].rt
                # Run 'Each Frame' code from responses_code
                if responses.keys == '1':
                   Left_Experience.setColor('green')
                elif responses.keys =='2':
                   Right_Experience.setColor('green')
                    
                
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in WTPTaskComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "WTPTask" ---
            for thisComponent in WTPTaskComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # check responses
            if responses.keys in ['', [], None]:  # No response was made
                responses.keys = None
            WTPTaskLoop.addData('responses.keys',responses.keys)
            if responses.keys != None:  # we had a response
                WTPTaskLoop.addData('responses.rt', responses.rt)
            # Run 'End Routine' code from responses_code
            Left_Experience.setColor('white')
            Right_Experience.setColor('white')
            continueRoutine= False
            # using non-slip timing so subtract the expected duration of this Routine
            routineTimer.addTime(-10.000000)
            
            # --- Prepare to start Routine "ITI" ---
            continueRoutine = True
            # update component parameters for each repeat
            ITI_text.setText('+')
            # keep track of which components have finished
            ITIComponents = [ITI_text]
            for thisComponent in ITIComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "ITI" ---
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *ITI_text* updates
                if ITI_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    ITI_text.frameNStart = frameN  # exact frame index
                    ITI_text.tStart = t  # local t and not account for scr refresh
                    ITI_text.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ITI_text, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'ITI_text.started')
                    ITI_text.setAutoDraw(True)
                if ITI_text.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > ITI_text.tStartRefresh + ITI-frameTolerance:
                        # keep track of stop time/frame for later
                        ITI_text.tStop = t  # not accounting for scr refresh
                        ITI_text.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'ITI_text.stopped')
                        ITI_text.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in ITIComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "ITI" ---
            for thisComponent in ITIComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # the Routine "ITI" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed 1.0 repeats of 'WTPTaskLoop'
        
        
        # --- Prepare to start Routine "Continue" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code
        if TrialNumber%30 == 0: # needs to be set to 30 for actual run of task
            continueRoutine = False # if not trial 31 or 61, or 91 skip routine completely
        #if comprunOrNot ==0 and selfrunOrNot == 0:
        #    resumetext = 'You missed an opportunity to play the lottery. \n\n\n Please respond withtin 3 seconds on your next opportunity. \n\nPress space to continue.'
        #else:
        resumetext = 'Press space to resume sharing your photos.'
        Resume_keys.keys = []
        Resume_keys.rt = []
        _Resume_keys_allKeys = []
        Resume_Text.setText(resumetext)
        # keep track of which components have finished
        ContinueComponents = [Resume_keys, Resume_Text]
        for thisComponent in ContinueComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Continue" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Resume_keys* updates
            waitOnFlip = False
            if Resume_keys.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Resume_keys.frameNStart = frameN  # exact frame index
                Resume_keys.tStart = t  # local t and not account for scr refresh
                Resume_keys.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Resume_keys, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Resume_keys.started')
                Resume_keys.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(Resume_keys.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(Resume_keys.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if Resume_keys.status == STARTED and not waitOnFlip:
                theseKeys = Resume_keys.getKeys(keyList=['space'], waitRelease=False)
                _Resume_keys_allKeys.extend(theseKeys)
                if len(_Resume_keys_allKeys):
                    Resume_keys.keys = _Resume_keys_allKeys[0].name  # just the first key pressed
                    Resume_keys.rt = _Resume_keys_allKeys[0].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # *Resume_Text* updates
            if Resume_Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Resume_Text.frameNStart = frameN  # exact frame index
                Resume_Text.tStart = t  # local t and not account for scr refresh
                Resume_Text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Resume_Text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Resume_Text.started')
                Resume_Text.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ContinueComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Continue" ---
        for thisComponent in ContinueComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if Resume_keys.keys in ['', [], None]:  # No response was made
            Resume_keys.keys = None
        startWTPloop.addData('Resume_keys.keys',Resume_keys.keys)
        if Resume_keys.keys != None:  # we had a response
            startWTPloop.addData('Resume_keys.rt', Resume_keys.rt)
        # the Routine "Continue" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
    # completed startWTP repeats of 'startWTPloop'
    
    
    # --- Prepare to start Routine "SalienceRating" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from saliencyrating_code
    if not TrialNumber%30 == 0: # establishes two blocks per 32 trials
        continueRoutine = False # if not trial 31 or 63, skip routine completely
    salienceratingtext = (f'How likely are you to share photos with {Partner} in the future? \n\n Use your left and right arrows to move the arrow to your desired rating.' )
    event.clearEvents('keyboard')
    salience_slider.markerPos = 3
    saliencequestion_text.setText(salienceratingtext)
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    salienceavatar_image.setImage(partneravatar)
    displayrating_text.setText(rating_forsalience)
    # keep track of which components have finished
    SalienceRatingComponents = [saliencequestion_text, key_resp, salienceavatar_image, saliencecontinue_text, displayrating_text]
    for thisComponent in SalienceRatingComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "SalienceRating" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from saliencyrating_code
        salience_slider.draw()
        keys = event.getKeys()
        displayrating_text.setText(round(salience_slider.getMarkerPos(),1))
        if len(keys):
            if 'left' in keys:
                salience_slider.markerPos = salience_slider.markerPos - .1
                rating_forsalience = salience_slider.getRating()
                displayrating_text.setText(round(salience_slider.getMarkerPos(),1))
            elif 'right' in keys:
                salience_slider.markerPos = salience_slider.markerPos + .1
                rating_forsalience = salience_slider.getRating()
                displayrating_text.setText(round(salience_slider.getMarkerPos(),1))
        
        # *saliencequestion_text* updates
        if saliencequestion_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            saliencequestion_text.frameNStart = frameN  # exact frame index
            saliencequestion_text.tStart = t  # local t and not account for scr refresh
            saliencequestion_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(saliencequestion_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'saliencequestion_text.started')
            saliencequestion_text.setAutoDraw(True)
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp.started')
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *salienceavatar_image* updates
        if salienceavatar_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            salienceavatar_image.frameNStart = frameN  # exact frame index
            salienceavatar_image.tStart = t  # local t and not account for scr refresh
            salienceavatar_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(salienceavatar_image, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'salienceavatar_image.started')
            salienceavatar_image.setAutoDraw(True)
        
        # *saliencecontinue_text* updates
        if saliencecontinue_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            saliencecontinue_text.frameNStart = frameN  # exact frame index
            saliencecontinue_text.tStart = t  # local t and not account for scr refresh
            saliencecontinue_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(saliencecontinue_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'saliencecontinue_text.started')
            saliencecontinue_text.setAutoDraw(True)
        
        # *displayrating_text* updates
        if displayrating_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            displayrating_text.frameNStart = frameN  # exact frame index
            displayrating_text.tStart = t  # local t and not account for scr refresh
            displayrating_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(displayrating_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'displayrating_text.started')
            displayrating_text.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in SalienceRatingComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "SalienceRating" ---
    for thisComponent in SalienceRatingComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from saliencyrating_code
    #saliencerating = salience_slider.getRating()
    entiretaskloop.addData('salience_rating', round(salience_slider.getMarkerPos(),1))
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    entiretaskloop.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        entiretaskloop.addData('key_resp.rt', key_resp.rt)
    # the Routine "SalienceRating" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "StressLevel" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from stresslevelslider
    if not TrialNumber%30 == 0: # establishes two blocks per 32 trials
        continueRoutine = False # if not trial 31 or 63, skip routine completely
    stressleveltext = (f'Please rate your current stress level. \n\n\n Use your mouse or left and right arrows to move the arrow to your desired rating.' )
    event.clearEvents('keyboard')
    stress_slider.markerPos = 5
    
    stresslevel_text.setText(stressleveltext)
    stresslevel_keypress.keys = []
    stresslevel_keypress.rt = []
    _stresslevel_keypress_allKeys = []
    displaystressrating_text.setText(rating_forstress)
    # keep track of which components have finished
    StressLevelComponents = [stresslevel_text, stresslevel_keypress, displaystressrating_text]
    for thisComponent in StressLevelComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "StressLevel" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from stresslevelslider
        stress_slider.draw()
        keys = event.getKeys()
        displaystressrating_text.setText(round(stress_slider.getMarkerPos(),1))
        if len(keys):
            if 'left' in keys:
                stress_slider.markerPos = stress_slider.markerPos - .1
                rating_forstress = stress_slider.getRating()
                displayrating_text.setText(round(stress_slider.getMarkerPos(),1))
            elif 'right' in keys:
                stress_slider.markerPos = stress_slider.markerPos + .1
                rating_forstress = stress_slider.getRating()
                displayrating_text.setText(round(stress_slider.getMarkerPos(),1))
        
        # *stresslevel_text* updates
        if stresslevel_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            stresslevel_text.frameNStart = frameN  # exact frame index
            stresslevel_text.tStart = t  # local t and not account for scr refresh
            stresslevel_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stresslevel_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'stresslevel_text.started')
            stresslevel_text.setAutoDraw(True)
        
        # *stresslevel_keypress* updates
        waitOnFlip = False
        if stresslevel_keypress.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            stresslevel_keypress.frameNStart = frameN  # exact frame index
            stresslevel_keypress.tStart = t  # local t and not account for scr refresh
            stresslevel_keypress.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stresslevel_keypress, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'stresslevel_keypress.started')
            stresslevel_keypress.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(stresslevel_keypress.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(stresslevel_keypress.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if stresslevel_keypress.status == STARTED and not waitOnFlip:
            theseKeys = stresslevel_keypress.getKeys(keyList=['space'], waitRelease=False)
            _stresslevel_keypress_allKeys.extend(theseKeys)
            if len(_stresslevel_keypress_allKeys):
                stresslevel_keypress.keys = _stresslevel_keypress_allKeys[-1].name  # just the last key pressed
                stresslevel_keypress.rt = _stresslevel_keypress_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *displaystressrating_text* updates
        if displaystressrating_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            displaystressrating_text.frameNStart = frameN  # exact frame index
            displaystressrating_text.tStart = t  # local t and not account for scr refresh
            displaystressrating_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(displaystressrating_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'displaystressrating_text.started')
            displaystressrating_text.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in StressLevelComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "StressLevel" ---
    for thisComponent in StressLevelComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from stresslevelslider
    stresslevel = stress_slider.getRating()
    entiretaskloop.addData('stress_level', round(stress_slider.getMarkerPos(),1))
    # check responses
    if stresslevel_keypress.keys in ['', [], None]:  # No response was made
        stresslevel_keypress.keys = None
    entiretaskloop.addData('stresslevel_keypress.keys',stresslevel_keypress.keys)
    if stresslevel_keypress.keys != None:  # we had a response
        entiretaskloop.addData('stresslevel_keypress.rt', stresslevel_keypress.rt)
    # the Routine "StressLevel" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'entiretaskloop'


# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
