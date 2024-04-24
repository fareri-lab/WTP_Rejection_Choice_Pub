/***************************** 
 * Wtp_Sm_Choice_Legacy Test *
 *****************************/

import { core, data, sound, util, visual, hardware } from './lib/psychojs-2022.2.1.js';
const { PsychoJS } = core;
const { TrialHandler, MultiStairHandler } = data;
const { Scheduler } = util;
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;
const { round } = util;



// store info about the experiment session:
let expName = 'WTP_SM_Choice';  // from the Builder filename that created this script
let expInfo = {
    'participant': ''
};


// add info from the URL:
util.addInfoFromUrl(expInfo);
console.log(expInfo['participant'])


// Start code blocks for 'Before Experiment'
// Run 'Before Experiment' code from saliencyrating_code
var saliencerating;
var salienceratingtext;
var rating_forsalience;
saliencerating = "";
salienceratingtext = "";
rating_forsalience = "";

// Run 'Before Experiment' code from stresslevelslider

var stresslevel;
var stressleveltext;
var rating_forstress;

stresslevel = "";
stressleveltext = "";
rating_forstress = "";




// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),
  units: 'norm',
  waitBlanking: true
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(Welcome_ScreenRoutineBegin());
flowScheduler.add(Welcome_ScreenRoutineEachFrame());
flowScheduler.add(Welcome_ScreenRoutineEnd());
flowScheduler.add(First_InstructionsRoutineBegin());
flowScheduler.add(First_InstructionsRoutineEachFrame());
flowScheduler.add(First_InstructionsRoutineEnd());
const entiretaskloopLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(entiretaskloopLoopBegin(entiretaskloopLoopScheduler));
flowScheduler.add(entiretaskloopLoopScheduler);
flowScheduler.add(entiretaskloopLoopEnd);
flowScheduler.add(End_ScreenRoutineBegin());
flowScheduler.add(End_ScreenRoutineEachFrame());
flowScheduler.add(End_ScreenRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);
var participantID;
participantID = expInfo["participant"];

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [

    {'name': `Participant_Images/${participantID}/${participantID}_WTP.csv`, 'path': `Participant_Images/${participantID}/${participantID}_WTP.csv`},
    {'name': `Participant_Images/${participantID}/${participantID}_trials.csv`, 'path': `Participant_Images/${participantID}/${participantID}_trials.csv`},
    {'name': 'Images/facedown_card.png', 'path': 'Images/facedown_card.png'},
    {'name': 'Images/facedown_card.png', 'path': 'Images/facedown_card.png'},
    {'name': 'Images/nerdemoji_nobackground.png', 'path': 'Images/nerdemoji_nobackground.png'},
    {'name': 'Images/smilingemoji.png', 'path': 'Images/smilingemoji.png'},
    {'name': 'Images/sunglassemoji_nobackground.png', 'path': 'Images/sunglassemoji_nobackground.png'},
    {'name': 'Images/thumbsdown.png', 'path': 'Images/thumbsdown.png'},
    {'name': 'Images/thumbsup.png', 'path': 'Images/thumbsup.png'},
    {'name': 'Images/cowboyemoji.png', 'path': 'Images/cowboyemoji.png'},
    {'name': 'Images/huggingemoji.png', 'path': 'Images/huggingemoji.png'},

    {'name': `Participant_Images/${expInfo["participant"]}/${expInfo["participant"]}_Images/${expInfo["participant"]}_Image_5.jpeg`, 'path': `Participant_Images/${expInfo["participant"]}/${expInfo["participant"]}_Images/${expInfo["participant"]}_Image_5.jpeg` ,},
    {'name': `Participant_Images/${expInfo["participant"]}/${expInfo["participant"]}_Images/${expInfo["participant"]}_Image_13.jpeg`, 'path': `Participant_Images/${expInfo["participant"]}/${expInfo["participant"]}_Images/${expInfo["participant"]}_Image_13.jpeg` ,},
    {'name': `Participant_Images/${expInfo["participant"]}/${expInfo["participant"]}_Images/${expInfo["participant"]}_Image_12.jpeg`, 'path': `Participant_Images/${expInfo["participant"]}/${expInfo["participant"]}_Images/${expInfo["participant"]}_Image_12.jpeg` ,},
    {'name': `Participant_Images/${expInfo["participant"]}/${expInfo["participant"]}_Images/${expInfo["participant"]}_Image_4.jpeg`, 'path': `Participant_Images/${expInfo["participant"]}/${expInfo["participant"]}_Images/${expInfo["participant"]}_Image_4.jpeg` ,},
    {'name': `Participant_Images/${expInfo["participant"]}/${expInfo["participant"]}_Images/${expInfo["participant"]}_Image_6.jpeg`, 'path': `Participant_Images/${expInfo["participant"]}/${expInfo["participant"]}_Images/${expInfo["participant"]}_Image_6.jpeg` ,},
    {'name': `Participant_Images/${expInfo["participant"]}/${expInfo["participant"]}_Images/${expInfo["participant"]}_Image_10.jpeg`, 'path': `Participant_Images/${expInfo["participant"]}/${expInfo["participant"]}_Images/${expInfo["participant"]}_Image_10.jpeg` ,},
    {'name': `Participant_Images/${expInfo["participant"]}/${expInfo["participant"]}_Images/${expInfo["participant"]}_Image_11.jpeg`, 'path': `Participant_Images/${expInfo["participant"]}/${expInfo["participant"]}_Images/${expInfo["participant"]}_Image_11.jpeg` ,},
    {'name': `Participant_Images/${expInfo["participant"]}/${expInfo["participant"]}_Images/${expInfo["participant"]}_Image_7.jpeg`, 'path': `Participant_Images/${expInfo["participant"]}/${expInfo["participant"]}_Images/${expInfo["participant"]}_Image_7.jpeg` ,},
    {'name': `Participant_Images/${expInfo["participant"]}/${expInfo["participant"]}_Images/${expInfo["participant"]}_Image_3.jpeg`, 'path': `Participant_Images/${expInfo["participant"]}/${expInfo["participant"]}_Images/${expInfo["participant"]}_Image_3.jpeg` ,},
    {'name': `Participant_Images/${expInfo["participant"]}/${expInfo["participant"]}_Images/${expInfo["participant"]}_Image_15.jpeg`, 'path': `Participant_Images/${expInfo["participant"]}/${expInfo["participant"]}_Images/${expInfo["participant"]}_Image_15.jpeg` ,},
    {'name': `Participant_Images/${expInfo["participant"]}/${expInfo["participant"]}_Images/${expInfo["participant"]}_Image_14.jpeg`, 'path': `Participant_Images/${expInfo["participant"]}/${expInfo["participant"]}_Images/${expInfo["participant"]}_Image_14.jpeg` ,},
    {'name': `Participant_Images/${expInfo["participant"]}/${expInfo["participant"]}_Images/${expInfo["participant"]}_Image_2.jpeg`, 'path': `Participant_Images/${expInfo["participant"]}/${expInfo["participant"]}_Images/${expInfo["participant"]}_Image_2.jpeg` ,},
    {'name': `Participant_Images/${expInfo["participant"]}/${expInfo["participant"]}_Images/${expInfo["participant"]}_Image_16.jpeg`, 'path': `Participant_Images/${expInfo["participant"]}/${expInfo["participant"]}_Images/${expInfo["participant"]}_Image_16.jpeg` ,},
    {'name': `Participant_Images/${expInfo["participant"]}/${expInfo["participant"]}_Images/${expInfo["participant"]}_Image_17.jpeg`, 'path': `Participant_Images/${expInfo["participant"]}/${expInfo["participant"]}_Images/${expInfo["participant"]}_Image_17.jpeg` ,},
    {'name': `Participant_Images/${expInfo["participant"]}/${expInfo["participant"]}_Images/${expInfo["participant"]}_Image_1.jpeg`, 'path': `Participant_Images/${expInfo["participant"]}/${expInfo["participant"]}_Images/${expInfo["participant"]}_Image_1.jpeg` ,},
    {'name': `Participant_Images/${expInfo["participant"]}/${expInfo["participant"]}_Images/${expInfo["participant"]}_Image_19.jpeg`, 'path': `Participant_Images/${expInfo["participant"]}/${expInfo["participant"]}_Images/${expInfo["participant"]}_Image_19.jpeg` ,},
    {'name': `Participant_Images/${expInfo["participant"]}/${expInfo["participant"]}_Images/${expInfo["participant"]}_Image_25.jpeg`, 'path': `Participant_Images/${expInfo["participant"]}/${expInfo["participant"]}_Images/${expInfo["participant"]}_Image_25.jpeg` ,},
    {'name': `Participant_Images/${expInfo["participant"]}/${expInfo["participant"]}_Images/${expInfo["participant"]}_Image_24.jpeg`, 'path': `Participant_Images/${expInfo["participant"]}/${expInfo["participant"]}_Images/${expInfo["participant"]}_Image_24.jpeg` ,},
    {'name': `Participant_Images/${expInfo["participant"]}/${expInfo["participant"]}_Images/${expInfo["participant"]}_Image_18.jpeg`, 'path': `Participant_Images/${expInfo["participant"]}/${expInfo["participant"]}_Images/${expInfo["participant"]}_Image_18.jpeg` ,},
    {'name': `Participant_Images/${expInfo["participant"]}/${expInfo["participant"]}_Images/${expInfo["participant"]}_Image_20.jpeg`, 'path': `Participant_Images/${expInfo["participant"]}/${expInfo["participant"]}_Images/${expInfo["participant"]}_Image_20.jpeg` ,},
    {'name': `Participant_Images/${expInfo["participant"]}/${expInfo["participant"]}_Images/${expInfo["participant"]}_Image_21.jpeg`, 'path': `Participant_Images/${expInfo["participant"]}/${expInfo["participant"]}_Images/${expInfo["participant"]}_Image_21.jpeg` ,},
    {'name': `Participant_Images/${expInfo["participant"]}/${expInfo["participant"]}_Images/${expInfo["participant"]}_Image_9.jpeg`, 'path': `Participant_Images/${expInfo["participant"]}/${expInfo["participant"]}_Images/${expInfo["participant"]}_Image_9.jpeg` ,},
    {'name': `Participant_Images/${expInfo["participant"]}/${expInfo["participant"]}_Images/${expInfo["participant"]}_Image_23.jpeg`, 'path': `Participant_Images/${expInfo["participant"]}/${expInfo["participant"]}_Images/${expInfo["participant"]}_Image_23.jpeg` ,},
    {'name': `Participant_Images/${expInfo["participant"]}/${expInfo["participant"]}_Images/${expInfo["participant"]}_Image_22.jpeg`, 'path': `Participant_Images/${expInfo["participant"]}/${expInfo["participant"]}_Images/${expInfo["participant"]}_Image_22.jpeg` ,},
    {'name': `Participant_Images/${expInfo["participant"]}/${expInfo["participant"]}_Images/${expInfo["participant"]}_Image_8.jpeg`, 'path': `Participant_Images/${expInfo["participant"]}/${expInfo["participant"]}_Images/${expInfo["participant"]}_Image_8.jpeg` ,},
    {'name': `Participant_Images/${expInfo["participant"]}/${expInfo["participant"]}_Images/${expInfo["participant"]}_Image_8.jpeg`, 'path': `Participant_Images/${expInfo["participant"]}/${expInfo["participant"]}_Images/${expInfo["participant"]}_Image_8.jpeg` ,}
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);

var currentLoop;
var frameDur;
async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2022.2.1';
  expInfo['OS'] = window.navigator.platform;

  psychoJS.experiment.dataFileName = (("." + "/") + `data/${expInfo["participant"]}/${expInfo["participant"]}_${expName}_${expInfo["date"]}`);

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  
  return Scheduler.Event.NEXT;
}

var prac_subtract_bonus = 0;
var subtract_bonus=0;
var conditionalBlank;
var globalClock;
var Welcome_ScreenClock;
var Welcome;
var routineTimer;
var FirstInstructions;
var First_InstructionsClock;
var endwelcomescreen_keys;
var partnermatch;
var partneravatar;
var trialset;

var First_InstructionsClock;
var First_Instructions;
var endinstructionscreen_keys;
var partner_codeClock;
var partnermatch;
var partneravatar;
var WaitingToMatchClock;
var Match_text;
var syncing_text;
var text_0;
var Transparent;
var Loading_25;
var text_25;
var Loading_50;
var text_50;
var Loading_75;
var text_75;
var Loading_100;
var text_100;
var Partner_MatchClock;
var Youhavematched;
var partneremoji_image;
var endpartnermatch_keys;
var PressToContinue;
var Photo_ShareClock;
var photobeingshared_text;
var waitforfeedback_text;
var feedbackresponses;
var fdbkimage;
var participantimage_image;
var WaitingforfeedbackClock;
var waiting_text;
var feedbackClock;
var displayfeedback_text;
var fdbkimage_image;
var WTPlottery;
var continuesharingClock;
var presstosharenextphoto_text;
var sharenextphoto_key;
var WTP_Instructions1Clock;
var WTP_ins_text1;
var WTP_ins_keys1;
var WTP_Instructions2Clock;
var WTP_ins_text2;
var WTP_ins_keys2;
var WTPTaskClock;
var Left_Experience;
var Right_Experience;
var Left_Price;
var Right_Price;
var responses;
var ITIClock;
var ITI_text;
var ContinueClock;
var resumetext;
var Resume_keys;
var Resume_Text;
// salience slider
var userMouse;
var mouseClock;
var SalienceRatingClock;
var salience_slider;
var saliencequestion_text;
var key_resp;
var salienceavatar_image;
var saliencecontinue_text;
var Salience_Button;
var displayrating_text;
// salience slider
var userMouse;
var mouseClock;
var StressLevelClock;
var stress_slider;
var stresslevel_text;
var stresslevel_keypress;
var Stress_Button;
var stresscontinue_text;

var displaystressrating_text;
var weblink;
weblink = `https://adelphiderner.qualtrics.com/jfe/form/SV_2bF7lXuTQzoEIGq?PROLIFIC_PID=${expInfo["participant"]}`;
console.log(weblink);
//end screen
var end_screen;
var end_screenclock;
var end_screen_keys;





async function experimentInit() {
  // Initialize components for Routine "Welcome_Screen"

  //test changes by changing font color here
  Welcome_ScreenClock = new util.Clock();
  Welcome = new visual.TextStim({
    win: psychoJS.window,
    name: 'Welcome',
    text: 'Welcome to the Instagram Sharing Task!\n\n\nToday you will have the opportunity to share some of your Instagram photos with other participants and receive feedback.\n\n\n\nPress space to continue.\n',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.08,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('pink'),  opacity: undefined,
    depth: 0.0 
  }); //change font color here to test changes 
  
  endwelcomescreen_keys = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});


  conditionalBlank = new visual.TextStim({
   win: psychoJS.window,
   name: 'conditionalconditionalBlank',
   text: '',
   font: 'Arial',
   pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
   color: new util.Color('blue'),  opacity: 1,
   depth: -6.0
 });

  
  // Run 'Begin Experiment' code from spreadsheets
  partnermatch = "";
  partneravatar = "";
  trialset = util.range(0, 5);

  

  // Initialize components for Routine "First_Instructions"
  First_InstructionsClock = new util.Clock();
  FirstInstructions = new visual.TextStim({
    win: psychoJS.window,
    name: 'FirstInstructions',
    text: 'To begin, you will be assigned a partner at random by the computer. Next, your instagram photos will be shared with your partner. After each photo is shared, your partner will give you feedback on whether they liked or disliked your photo. You will have the chance to share your photos with 4 different partners during todays task.\n\n\nYou may be eligible throughout the task to participate in a decision-making task, where you may be eligible to earn a bonus. Further instructions about this task will be provided should you be eligible to participate.\n\n\nPress space to continue.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.08,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  endinstructionscreen_keys = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "partner_code"
  partner_codeClock = new util.Clock();
  // Run 'Begin Experiment' code from partnermatchcode
  partnermatch = "";
  partneravatar = "";
  
  // Initialize components for Routine "WaitingToMatch"
  WaitingToMatchClock = new util.Clock();
  Match_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'Match_text',
    text: 'You will now be matched with a game partner selected at random by the computer.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.3], height: 0.08,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  syncing_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'syncing_text',
    text: 'Syncing…',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.3], height: 0.12,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  text_0 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_0',
    text: '0%',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.2)], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -3.0 
  });
  
  Transparent = new visual.Rect ({
    win: psychoJS.window, name: 'Transparent', 
    width: [1, 0.1][0], height: [1, 0.1][1],
    ori: 0.0, pos: [0, 0],
    lineWidth: 1.2, lineColor: new util.Color('white'),
    fillColor: new util.Color([0.0, 0.0, 0.0]),
    opacity: undefined, depth: -4, interpolate: true,
  });
  
  Loading_25 = new visual.Rect ({
    win: psychoJS.window, name: 'Loading_25', 
    width: [0.25, 0.1][0], height: [0.25, 0.1][1],
    ori: 0.0, pos: [(- 0.375), 0],
    lineWidth: 1.0, lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: undefined, depth: -5, interpolate: true,
  });
  
  text_25 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_25',
    text: '25%',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.2)], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -6.0 
  });
  
  Loading_50 = new visual.Rect ({
    win: psychoJS.window, name: 'Loading_50', 
    width: [0.5, 0.1][0], height: [0.5, 0.1][1],
    ori: 0.0, pos: [(- 0.25), 0],
    lineWidth: 1.0, lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: undefined, depth: -7, interpolate: true,
  });
  
  text_50 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_50',
    text: '50%',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.2)], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -8.0 
  });
  
  Loading_75 = new visual.Rect ({
    win: psychoJS.window, name: 'Loading_75', 
    width: [0.75, 0.1][0], height: [0.75, 0.1][1],
    ori: 0.0, pos: [(- 0.125), 0],
    lineWidth: 1.0, lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: undefined, depth: -9, interpolate: true,
  });
  
  text_75 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_75',
    text: '75%',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.2)], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -10.0 
  });
  
  Loading_100 = new visual.Rect ({
    win: psychoJS.window, name: 'Loading_100', 
    width: [1, 0.1][0], height: [1, 0.1][1],
    ori: 0.0, pos: [0, 0],
    lineWidth: 1.0, lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: undefined, depth: -11, interpolate: true,
  });
  
  text_100 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_100',
    text: '100%',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.2)], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -12.0 
  });
  
  // Initialize components for Routine "Partner_Match"
  Partner_MatchClock = new util.Clock();
  Youhavematched = new visual.TextStim({
    win: psychoJS.window,
    name: 'Youhavematched',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.6], height: 0.08,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  partneremoji_image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'partneremoji_image', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.5, 0.75],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  endpartnermatch_keys = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  PressToContinue = new visual.TextStim({
    win: psychoJS.window,
    name: 'PressToContinue',
    text: 'Press space to continue.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.6)], height: 0.08,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -4.0 
  });
  
  // Initialize components for Routine "Photo_Share"
  Photo_ShareClock = new util.Clock();
  photobeingshared_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'photobeingshared_text',
    text: 'This photo is now being shared',
    font: 'Open Sans',
    units: undefined, 
    pos: [0.0, 0.6], height: 0.09,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  waitforfeedback_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'waitforfeedback_text',
    text: 'Please wait for feedback.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.6)], height: 0.09,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  // Run 'Begin Experiment' code from initiatefeedbackresponses
  feedbackresponses = "";
  fdbkimage = "";
  
  participantimage_image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'participantimage_image', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.5, 0.75],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  // Initialize components for Routine "Waitingforfeedback"
  WaitingforfeedbackClock = new util.Clock();
  waiting_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'waiting_text',
    text: 'Waiting…',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.0], height: 0.15,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Initialize components for Routine "feedback"
  feedbackClock = new util.Clock();
  displayfeedback_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'displayfeedback_text',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.75], height: 0.12,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  fdbkimage_image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'fdbkimage_image', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.75, 1.25],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  // Run 'Begin Experiment' code from initiatelottery_code
  WTPlottery = "";
  
  // Initialize components for Routine "continuesharing"
  continuesharingClock = new util.Clock();
  presstosharenextphoto_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'presstosharenextphoto_text',
    text: 'Press space to share your next photo.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.09,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  sharenextphoto_key = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "WTP_Instructions1"
  WTP_Instructions1Clock = new util.Clock();
  WTP_ins_text1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'WTP_ins_text1',
    text: "In this part of the task, you will be choosing between two options.\n\nPlease indicate which option you would prefer by using your keyboard to press '1' for the choice on the left, or '2' for the choice on the right. \n\nEach option is associated with a price, which will be subtracted from your earnings of $6 from the previous task upon making a selection. \n\nPress SPACE to continue.",
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.3], height: 0.07,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  WTP_ins_keys1 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "WTP_Instructions2"
  WTP_Instructions2Clock = new util.Clock();
  WTP_ins_text2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'WTP_ins_text2',
    text: 'Imagine yourself actually doing the experiences shown on screen before making your decision.\n\nYou will have ten seconds to make a response after seeing the choices. \n\nWhen you make your choice, your selection will turn green. \n\nPress SPACE to start the task.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  WTP_ins_keys2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "WTPTask"
  WTPTaskClock = new util.Clock();
  Left_Experience = new visual.TextStim({
    win: psychoJS.window,
    name: 'Left_Experience',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [(- 0.5), 0.1], height: 0.08,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  Right_Experience = new visual.TextStim({
    win: psychoJS.window,
    name: 'Right_Experience',
    text: 'undefined',
    font: 'Open Sans',
    units: undefined, 
    pos: [0.5, 0.1], height: 0.08,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  Left_Price = new visual.TextStim({
    win: psychoJS.window,
    name: 'Left_Price',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [-0.5, (- 0.5)], height: 0.08,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  Right_Price = new visual.TextStim({
    win: psychoJS.window,
    name: 'Right_Price',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [(0.5), (- 0.5)], height: 0.08,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -3.0 
  });
  
  responses = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "ITI"
  ITIClock = new util.Clock();
  ITI_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'ITI_text',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.09,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Initialize components for Routine "Continue"
  ContinueClock = new util.Clock();
  // Run 'Begin Experiment' code from code
  resumetext = "";
  
  Resume_keys = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  Resume_Text = new visual.TextStim({
    win: psychoJS.window,
    name: 'Resume_Text',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.12,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });

  mouseClock =  new util.Clock();
  userMouse = new core.Mouse({
    win: psychoJS.window,
    name: 'userMouse',
  });
  // Initialize components for Routine "SalienceRating"
  SalienceRatingClock = new util.Clock();
  // Run 'Begin Experiment' code from saliencyrating_code
  salience_slider = new visual.Slider({
    win: psychoJS.window,
    name: "slider",
    size: [1.0, 0.1],
    pos: [0, -0.2], //[0, (- 0.4)]
    units: null,
    labels: [1, 2, 3, 4, 5],
    ticks: [1, 2, 3, 4, 5],
    granularity: 0.0,
    opacity: null,
    style: [visual.Slider.Style.RATING],
    labelColor: "white",
    markerColor: "cornflowerblue",
    lineColor: "white",
    colorSpace: "rgb",
    font: "Open Sans",
    labelHeight: 0.05,
    flip: false,
    ori: 0.0,
    depth: (- 5),
    readOnly: false,
    autoDraw: false});
    
  saliencequestion_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'saliencequestion_text',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.7], height: 0.06,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  salienceavatar_image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'salienceavatar_image', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0.2], size : [0.3, 0.60],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  saliencecontinue_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'saliencecontinue_text',
    text: 'To continue, click the square when your desired rating appears',
    font: 'Open Sans',
    units: undefined,
    pos: [0, (- 0.8)], //[0, (- 0.8)]
    height: 0.045, //0.07
     wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -4.0
  });

  Salience_Button = new visual.Rect ({
   win: psychoJS.window, name: 'polygon',
   width: [0.25, 0.25][0], height: [0.25, 0.25][1],
   ori: 0, pos: [0, (- 0.6)],
   lineWidth: 1, lineColor: new util.Color('white'),
   fillColor: undefined,
   opacity: 1, depth: -1, interpolate: true,
 });
 
  displayrating_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'displayrating_text',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.60)], height: 0.065,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -5.0 
  });

  
  Stress_Button = new visual.Rect ({
     win: psychoJS.window, name: 'polygon',
     width: [0.25, 0.25][0], height: [0.25, 0.25][1],
     ori: 0, pos: [0, (- 0.6)],
     lineWidth: 1, lineColor: new util.Color('white'),
     fillColor: undefined,
     opacity: 1, depth: -1, interpolate: true,
   });
  
  // Initialize components for Routine "StressLevel"
  StressLevelClock = new util.Clock();
  // Run 'Begin Experiment' code from stresslevelslider
  stresscontinue_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'stresscontinue_text',
    text: 'To continue, click the square when your desired rating appears',
    font: 'Open Sans',
    units: undefined,
    pos: [0, (- 0.8)], //[0, (- 0.8)]
    height: 0.045, //0.07
     wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -4.0
  });
  stresslevel_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'stresslevel_text',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.3], height: 0.08,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  stress_slider = new visual.Slider({
    win: psychoJS.window,
    name: "slider",
    size: [1.0, 0.1],
    pos: [0, -0.2], //[0,(-0.4)]
    units: null,
    labels: ['1 (Bad)', '2', '3', '4', '5','6','7','8','9 (Good)'],
    ticks: [1, 2, 3, 4, 5,6,7,8,9],
    granularity: 0.0,
    opacity: null,
    style: [visual.Slider.Style.RATING],
    labelColor: "white",
    markerColor: "cornflowerblue",
    lineColor: "white",
    colorSpace: "rgb",
    font: "Open Sans",
    labelHeight: 0.05,
    flip: false,
    ori: 0.0,
    depth: (- 5),
    readOnly: false});
    
  stresslevel_keypress = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  displaystressrating_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'displaystressrating_text',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.65)], height: 0.08,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -3.0 

    
  });

  end_screenclock = new util.Clock();
  end_screen = new visual.TextStim({
    win: psychoJS.window,
    name: 'end_screen',
    text: 'You have now reached the end of the task. \n\n\nPress space to be redirected to complete the post-task survey.\n',
    font: 'Open Sans',
    units: undefined,
    pos: [0, 0], height: 0.08,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0
  });
  end_screen_keys = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  endwelcomescreen_keys = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});


  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}
var t;
var frameN;
var continueRoutine;
var _endwelcomescreen_keys_allKeys;
var subid;
var subjdir;
var trial_sheet;
var wtp_sheet;
var partnermatch;
var partneravatar;
var endwelcomescreen_keys;
var Welcome_ScreenComponents;
function Welcome_ScreenRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Welcome_Screen' ---
    t = 0;
    Welcome_ScreenClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    endwelcomescreen_keys.keys = undefined;
    endwelcomescreen_keys.rt = undefined;
    _endwelcomescreen_keys_allKeys = [];
    // Run 'Begin Routine' code from spreadsheets
    subid = expInfo["participant"];
    subjdir = `Participant_Images/${subid}`;
    trial_sheet = `${subjdir}/${subid}_trials.csv`;
    wtp_sheet = `${subjdir}/${subid}_WTP.csv`;
    partnermatch = "";
    partneravatar = "";
    
    // keep track of which components have finished
    Welcome_ScreenComponents = [];
    Welcome_ScreenComponents.push(Welcome);
    Welcome_ScreenComponents.push(endwelcomescreen_keys);
    
    for (const thisComponent of Welcome_ScreenComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function Welcome_ScreenRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Welcome_Screen' ---
    // get current time
    t = Welcome_ScreenClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Welcome* updates
    if (t >= 0.0 && Welcome.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Welcome.tStart = t;  // (not accounting for frame time here)
      Welcome.frameNStart = frameN;  // exact frame index
      
      Welcome.setAutoDraw(true);
    }

    
    // *endwelcomescreen_keys* updates
    if (t >= 0.0 && endwelcomescreen_keys.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      endwelcomescreen_keys.tStart = t;  // (not accounting for frame time here)
      endwelcomescreen_keys.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { endwelcomescreen_keys.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { endwelcomescreen_keys.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { endwelcomescreen_keys.clearEvents(); });
    }

    if (endwelcomescreen_keys.status === PsychoJS.Status.STARTED) {
      let theseKeys = endwelcomescreen_keys.getKeys({keyList: ['space'], waitRelease: false});
      _endwelcomescreen_keys_allKeys = _endwelcomescreen_keys_allKeys.concat(theseKeys);
      if (_endwelcomescreen_keys_allKeys.length > 0) {
        endwelcomescreen_keys.keys = _endwelcomescreen_keys_allKeys[_endwelcomescreen_keys_allKeys.length - 1].name;  // just the last key pressed
        endwelcomescreen_keys.rt = _endwelcomescreen_keys_allKeys[_endwelcomescreen_keys_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of Welcome_ScreenComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function Welcome_ScreenRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Welcome_Screen' ---
    for (const thisComponent of Welcome_ScreenComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(endwelcomescreen_keys.corr, level);
    }
    psychoJS.experiment.addData('endwelcomescreen_keys.keys', endwelcomescreen_keys.keys);
    if (typeof endwelcomescreen_keys.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('endwelcomescreen_keys.rt', endwelcomescreen_keys.rt);
        routineTimer.reset();
        }
    
    endwelcomescreen_keys.stop();
    // the Routine "Welcome_Screen" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

var _endinstructionscreen_keys_allKeys;
var First_InstructionsComponents;
function First_InstructionsRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'First_Instructions' ---
    t = 0;
    First_InstructionsClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    endinstructionscreen_keys.keys = undefined;
    endinstructionscreen_keys.rt = undefined;
    _endinstructionscreen_keys_allKeys = [];
    // keep track of which components have finished
    First_InstructionsComponents = [];
    First_InstructionsComponents.push(FirstInstructions);
    First_InstructionsComponents.push(endinstructionscreen_keys);
    
    for (const thisComponent of First_InstructionsComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function First_InstructionsRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'First_Instructions' ---
    // get current time
    t = First_InstructionsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *FirstInstructions* updates
    if (t >= 0.0 && FirstInstructions.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      FirstInstructions.tStart = t;  // (not accounting for frame time here)
      FirstInstructions.frameNStart = frameN;  // exact frame index
      
      FirstInstructions.setAutoDraw(true);
    }

    
    // *endinstructionscreen_keys* updates
    if (t >= 0.0 && endinstructionscreen_keys.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      endinstructionscreen_keys.tStart = t;  // (not accounting for frame time here)
      endinstructionscreen_keys.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { endinstructionscreen_keys.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { endinstructionscreen_keys.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { endinstructionscreen_keys.clearEvents(); });
    }

    if (endinstructionscreen_keys.status === PsychoJS.Status.STARTED) {
      let theseKeys = endinstructionscreen_keys.getKeys({keyList: ['space'], waitRelease: false});
      _endinstructionscreen_keys_allKeys = _endinstructionscreen_keys_allKeys.concat(theseKeys);
      if (_endinstructionscreen_keys_allKeys.length > 0) {
        endinstructionscreen_keys.keys = _endinstructionscreen_keys_allKeys[_endinstructionscreen_keys_allKeys.length - 1].name;  // just the last key pressed
        endinstructionscreen_keys.rt = _endinstructionscreen_keys_allKeys[_endinstructionscreen_keys_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of First_InstructionsComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function First_InstructionsRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'First_Instructions' ---
    for (const thisComponent of First_InstructionsComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(endinstructionscreen_keys.corr, level);
    }
    psychoJS.experiment.addData('endinstructionscreen_keys.keys', endinstructionscreen_keys.keys);
    if (typeof endinstructionscreen_keys.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('endinstructionscreen_keys.rt', endinstructionscreen_keys.rt);
        routineTimer.reset();
        }
    
    endinstructionscreen_keys.stop();
    // the Routine "First_Instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

var trial_nums;
var WTPloop;
var WTP_trial;
var entiretaskloop;
var subtract_bonus = 0;
function entiretaskloopLoopBegin(entiretaskloopLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    entiretaskloop = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: trial_sheet,
      seed: undefined, name: 'entiretaskloop'
    });
    psychoJS.experiment.addLoop(entiretaskloop); // add the loop to the experiment
    currentLoop = entiretaskloop;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisEntiretaskloop of entiretaskloop) {
      snapshot = entiretaskloop.getSnapshot();
      entiretaskloopLoopScheduler.add(importConditions(snapshot));
      entiretaskloopLoopScheduler.add(partner_codeRoutineBegin(snapshot));
      entiretaskloopLoopScheduler.add(partner_codeRoutineEachFrame());
      entiretaskloopLoopScheduler.add(partner_codeRoutineEnd(snapshot));
      entiretaskloopLoopScheduler.add(WaitingToMatchRoutineBegin(snapshot));
      entiretaskloopLoopScheduler.add(WaitingToMatchRoutineEachFrame());
      entiretaskloopLoopScheduler.add(WaitingToMatchRoutineEnd(snapshot));
      entiretaskloopLoopScheduler.add(Partner_MatchRoutineBegin(snapshot));
      entiretaskloopLoopScheduler.add(Partner_MatchRoutineEachFrame());
      entiretaskloopLoopScheduler.add(Partner_MatchRoutineEnd(snapshot));
      entiretaskloopLoopScheduler.add(Photo_ShareRoutineBegin(snapshot));
      entiretaskloopLoopScheduler.add(Photo_ShareRoutineEachFrame());
      entiretaskloopLoopScheduler.add(Photo_ShareRoutineEnd(snapshot));
      entiretaskloopLoopScheduler.add(WaitingforfeedbackRoutineBegin(snapshot));
      entiretaskloopLoopScheduler.add(WaitingforfeedbackRoutineEachFrame());
      entiretaskloopLoopScheduler.add(WaitingforfeedbackRoutineEnd(snapshot));
      entiretaskloopLoopScheduler.add(feedbackRoutineBegin(snapshot));
      entiretaskloopLoopScheduler.add(feedbackRoutineEachFrame());
      entiretaskloopLoopScheduler.add(feedbackRoutineEnd(snapshot));
      entiretaskloopLoopScheduler.add(continuesharingRoutineBegin(snapshot));
      entiretaskloopLoopScheduler.add(continuesharingRoutineEachFrame());
      entiretaskloopLoopScheduler.add(continuesharingRoutineEnd(snapshot));
      const startWTPloopLoopScheduler = new Scheduler(psychoJS);
      entiretaskloopLoopScheduler.add(startWTPloopLoopBegin(startWTPloopLoopScheduler, snapshot));
      entiretaskloopLoopScheduler.add(startWTPloopLoopScheduler);
      entiretaskloopLoopScheduler.add(startWTPloopLoopEnd);
      entiretaskloopLoopScheduler.add(SalienceRatingRoutineBegin(snapshot));
      entiretaskloopLoopScheduler.add(SalienceRatingRoutineEachFrame());
      entiretaskloopLoopScheduler.add(SalienceRatingRoutineEnd(snapshot));
      entiretaskloopLoopScheduler.add(StressLevelRoutineBegin(snapshot));
      entiretaskloopLoopScheduler.add(StressLevelRoutineEachFrame());
      entiretaskloopLoopScheduler.add(StressLevelRoutineEnd(snapshot));
      entiretaskloopLoopScheduler.add(entiretaskloopLoopEndIteration(entiretaskloopLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}
// var Right_Exp;
// var Left_Exp;
// var leftmoney;
// var rightmoney;
var startWTPloop;
// var social_left;
// var left;
// var right;
// var WTP_ITI;
// var left_more_than_right;
// var matching_prices;
// var social_worthmore;
function startWTPloopLoopBegin(startWTPloopLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    startWTPloop = new TrialHandler({
      psychoJS: psychoJS,
      nReps: startWTP, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'startWTPloop'
    });
    psychoJS.experiment.addLoop(startWTPloop); // add the loop to the experiment
    currentLoop = startWTPloop;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisStartWTPloop of startWTPloop) {
      snapshot = startWTPloop.getSnapshot();
      startWTPloopLoopScheduler.add(importConditions(snapshot));
      startWTPloopLoopScheduler.add(WTP_Instructions1RoutineBegin(snapshot));
      startWTPloopLoopScheduler.add(WTP_Instructions1RoutineEachFrame());
      startWTPloopLoopScheduler.add(WTP_Instructions1RoutineEnd(snapshot));
      startWTPloopLoopScheduler.add(WTP_Instructions2RoutineBegin(snapshot));
      startWTPloopLoopScheduler.add(WTP_Instructions2RoutineEachFrame());
      startWTPloopLoopScheduler.add(WTP_Instructions2RoutineEnd(snapshot));
      const WTPTaskLoopLoopScheduler = new Scheduler(psychoJS);
      startWTPloopLoopScheduler.add(WTPTaskLoopLoopBegin(WTPTaskLoopLoopScheduler, snapshot));
      startWTPloopLoopScheduler.add(WTPTaskLoopLoopScheduler);
      startWTPloopLoopScheduler.add(WTPTaskLoopLoopEnd);
      startWTPloopLoopScheduler.add(ContinueRoutineBegin(snapshot));
      startWTPloopLoopScheduler.add(ContinueRoutineEachFrame());
      startWTPloopLoopScheduler.add(ContinueRoutineEnd(snapshot));
      startWTPloopLoopScheduler.add(startWTPloopLoopEndIteration(startWTPloopLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}

var WTPTaskLoop;

function WTPTaskLoopLoopBegin(WTPTaskLoopLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    WTPTaskLoop = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: TrialHandler.importConditions(psychoJS.serverManager, wtp_sheet, trialset),
      seed: undefined, name: 'WTPTaskLoop'
    });
    psychoJS.experiment.addLoop(WTPTaskLoop); // add the loop to the experiment
    currentLoop = WTPTaskLoop;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisWTPTaskLoop of WTPTaskLoop) {
      snapshot = WTPTaskLoop.getSnapshot();
      WTPTaskLoopLoopScheduler.add(importConditions(snapshot));
      WTPTaskLoopLoopScheduler.add(WTPTaskRoutineBegin(snapshot));
      WTPTaskLoopLoopScheduler.add(WTPTaskRoutineEachFrame());
      WTPTaskLoopLoopScheduler.add(WTPTaskRoutineEnd(snapshot));
      WTPTaskLoopLoopScheduler.add(ITIRoutineBegin(snapshot));
      WTPTaskLoopLoopScheduler.add(ITIRoutineEachFrame());
      WTPTaskLoopLoopScheduler.add(ITIRoutineEnd(snapshot));
      WTPTaskLoopLoopScheduler.add(WTPTaskLoopLoopEndIteration(WTPTaskLoopLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}

async function WTPTaskLoopLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(WTPTaskLoop);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}

function WTPTaskLoopLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}

async function startWTPloopLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(startWTPloop);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}

function startWTPloopLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      }
    return Scheduler.Event.NEXT;
    }
  };
}

async function entiretaskloopLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(entiretaskloop);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}

function entiretaskloopLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}
var partner_codeComponents;
function partner_codeRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'partner_code' ---
    t = 0;
    partner_codeClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // keep track of which components have finished
    partner_codeComponents = [];
    
    for (const thisComponent of partner_codeComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function partner_codeRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'partner_code' ---
    // get current time
    t = partner_codeClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of partner_codeComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function partner_codeRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'partner_code' ---
    for (const thisComponent of partner_codeComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Run 'End Routine' code from partnermatchcode
    partnermatch = `You have matched with: ${Partner}`;
    if ((Partner === "Sam")) {
        partneravatar = "Images/nerdemoji_nobackground.png";
    } else {
        if ((Partner === "Riley")) {
            partneravatar = "Images/sunglassemoji_nobackground.png";
        } else {
            if ((Partner === "Charlie")) {
                partneravatar = "Images/smilingemoji.png";
            } else {
                if ((Partner === "Alex")) {
                    partneravatar = "Images/cowboyemoji.png";
                // } else {
                //     if ((Partner === "Taylor")) {
                //         partneravatar = "Images/huggingemoji.png";
                //     }
                }
            }
        }
    }
    
    // the Routine "partner_code" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}
var _pj;
var continueRoutine;
var frameRemains;
var t;
var WaitingToMatchComponents;
function WaitingToMatchRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'WaitingToMatch' ---
    t = 0;
    WaitingToMatchClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(9.250000);
    // update component parameters for each repeat
    // Run 'Begin Routine' code from showloadingbar
    var _pj;
    function _pj_snippets(container) {
        function in_es6(left, right) {
            if (((right instanceof Array) || ((typeof right) === "string"))) {
                return (right.indexOf(left) > (- 1));
            } else {
                if (((right instanceof Map) || (right instanceof Set) || (right instanceof WeakMap) || (right instanceof WeakSet))) {
                    return right.has(left);
                } else {
                    return (left in right);
                }
            }
        }
        container["in_es6"] = in_es6;
        return container;
    }
    _pj = {};
    _pj_snippets(_pj);
    if ((! _pj.in_es6(TrialNumber, [1, 26, 51,76]))) {
        continueRoutine = false;
    }
    
    // keep track of which components have finished
    WaitingToMatchComponents = [];
    WaitingToMatchComponents.push(Match_text);
    WaitingToMatchComponents.push(syncing_text);
    WaitingToMatchComponents.push(text_0);
    WaitingToMatchComponents.push(Transparent);
    WaitingToMatchComponents.push(Loading_25);
    WaitingToMatchComponents.push(text_25);
    WaitingToMatchComponents.push(Loading_50);
    WaitingToMatchComponents.push(text_50);
    WaitingToMatchComponents.push(Loading_75);
    WaitingToMatchComponents.push(text_75);
    WaitingToMatchComponents.push(Loading_100);
    WaitingToMatchComponents.push(text_100);
    
    for (const thisComponent of WaitingToMatchComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}
var continueRoutine;
var frameRemains;
var t;
function WaitingToMatchRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'WaitingToMatch' ---
    // get current time
    t = WaitingToMatchClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Match_text* updates
    if (t >= 0.0 && Match_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Match_text.tStart = t;  // (not accounting for frame time here)
      Match_text.frameNStart = frameN;  // exact frame index
      
      Match_text.setAutoDraw(true);
    }

    frameRemains = 0.0 + 3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (Match_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Match_text.setAutoDraw(false);
    }
    
    // *syncing_text* updates
    if (t >= 3 && syncing_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      syncing_text.tStart = t;  // (not accounting for frame time here)
      syncing_text.frameNStart = frameN;  // exact frame index
      
      syncing_text.setAutoDraw(true);
    }

    frameRemains = 3 + 6.25 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (syncing_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      syncing_text.setAutoDraw(false);
    }
    
    // *text_0* updates
    if (t >= 3 && text_0.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_0.tStart = t;  // (not accounting for frame time here)
      text_0.frameNStart = frameN;  // exact frame index
      
      text_0.setAutoDraw(true);
    }

    frameRemains = 3 + 1.25 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_0.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_0.setAutoDraw(false);
    }
    
    // *Transparent* updates
    if (t >= 3 && Transparent.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Transparent.tStart = t;  // (not accounting for frame time here)
      Transparent.frameNStart = frameN;  // exact frame index
      
      Transparent.setAutoDraw(true);
    }

    frameRemains = 3 + 6.25 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (Transparent.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Transparent.setAutoDraw(false);
    }
    
    // *Loading_25* updates
    if (t >= 4.25 && Loading_25.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Loading_25.tStart = t;  // (not accounting for frame time here)
      Loading_25.frameNStart = frameN;  // exact frame index
      
      Loading_25.setAutoDraw(true);
    }

    frameRemains = 4.25 + 1.25 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (Loading_25.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Loading_25.setAutoDraw(false);
    }
    
    // *text_25* updates
    if (t >= 4.25 && text_25.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_25.tStart = t;  // (not accounting for frame time here)
      text_25.frameNStart = frameN;  // exact frame index
      
      text_25.setAutoDraw(true);
    }

    frameRemains = 4.25 + 1.25 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_25.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_25.setAutoDraw(false);
    }
    
    // *Loading_50* updates
    if (t >= 5.5 && Loading_50.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Loading_50.tStart = t;  // (not accounting for frame time here)
      Loading_50.frameNStart = frameN;  // exact frame index
      
      Loading_50.setAutoDraw(true);
    }

    frameRemains = 5.5 + 1.25 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (Loading_50.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Loading_50.setAutoDraw(false);
    }
    
    // *text_50* updates
    if (t >= 5.5 && text_50.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_50.tStart = t;  // (not accounting for frame time here)
      text_50.frameNStart = frameN;  // exact frame index
      
      text_50.setAutoDraw(true);
    }

    frameRemains = 5.5 + 1.25 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_50.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_50.setAutoDraw(false);
    }
    
    // *Loading_75* updates
    if (t >= 6.75 && Loading_75.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Loading_75.tStart = t;  // (not accounting for frame time here)
      Loading_75.frameNStart = frameN;  // exact frame index
      
      Loading_75.setAutoDraw(true);
    }

    frameRemains = 6.75 + 1.25 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (Loading_75.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Loading_75.setAutoDraw(false);
    }
    
    // *text_75* updates
    if (t >= 6.75 && text_75.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_75.tStart = t;  // (not accounting for frame time here)
      text_75.frameNStart = frameN;  // exact frame index
      
      text_75.setAutoDraw(true);
    }

    frameRemains = 6.75 + 1.25 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_75.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_75.setAutoDraw(false);
    }
    
    // *Loading_100* updates
    if (t >= 8 && Loading_100.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Loading_100.tStart = t;  // (not accounting for frame time here)
      Loading_100.frameNStart = frameN;  // exact frame index
      
      Loading_100.setAutoDraw(true);
    }

    frameRemains = 8 + 1.25 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (Loading_100.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Loading_100.setAutoDraw(false);
    }
    
    // *text_100* updates
    if (t >= 8 && text_100.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_100.tStart = t;  // (not accounting for frame time here)
      text_100.frameNStart = frameN;  // exact frame index
      
      text_100.setAutoDraw(true);
    }

    frameRemains = 8 + 1.25 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_100.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_100.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of WaitingToMatchComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function WaitingToMatchRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'WaitingToMatch' ---
    for (const thisComponent of WaitingToMatchComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}
var _endpartnermatch_keys_allKeys;
var Partner_MatchComponents;
function Partner_MatchRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Partner_Match' ---
    t = 0;
    Partner_MatchClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // Run 'Begin Routine' code from showpartnermatch
    var _pj;
    function _pj_snippets(container) {
        function in_es6(left, right) {
            if (((right instanceof Array) || ((typeof right) === "string"))) {
                return (right.indexOf(left) > (- 1));
            } else {
                if (((right instanceof Map) || (right instanceof Set) || (right instanceof WeakMap) || (right instanceof WeakSet))) {
                    return right.has(left);
                } else {
                    return (left in right);
                }
            }
        }
        container["in_es6"] = in_es6;
        return container;
    }
    _pj = {};
    _pj_snippets(_pj);
    if ((! _pj.in_es6(TrialNumber, [1, 26, 51,76]))) {
        continueRoutine = false;
    }
    
    Youhavematched.setText(partnermatch);
    partneremoji_image.setImage(partneravatar);
    endpartnermatch_keys.keys = undefined;
    endpartnermatch_keys.rt = undefined;
    _endpartnermatch_keys_allKeys = [];
    // keep track of which components have finished
    Partner_MatchComponents = [];
    Partner_MatchComponents.push(Youhavematched);
    Partner_MatchComponents.push(partneremoji_image);
    Partner_MatchComponents.push(endpartnermatch_keys);
    Partner_MatchComponents.push(PressToContinue);
    
    for (const thisComponent of Partner_MatchComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function Partner_MatchRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Partner_Match' ---
    // get current time
    t = Partner_MatchClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Youhavematched* updates
    if (t >= 0.0 && Youhavematched.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Youhavematched.tStart = t;  // (not accounting for frame time here)
      Youhavematched.frameNStart = frameN;  // exact frame index
      
      Youhavematched.setAutoDraw(true);
    }

    
    // *partneremoji_image* updates
    if (t >= 0.0 && partneremoji_image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      partneremoji_image.tStart = t;  // (not accounting for frame time here)
      partneremoji_image.frameNStart = frameN;  // exact frame index
      
      partneremoji_image.setAutoDraw(true);
    }

    
    // *endpartnermatch_keys* updates
    if (t >= 0.0 && endpartnermatch_keys.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      endpartnermatch_keys.tStart = t;  // (not accounting for frame time here)
      endpartnermatch_keys.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { endpartnermatch_keys.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { endpartnermatch_keys.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { endpartnermatch_keys.clearEvents(); });
    }

    if (endpartnermatch_keys.status === PsychoJS.Status.STARTED) {
      let theseKeys = endpartnermatch_keys.getKeys({keyList: ['space'], waitRelease: false});
      _endpartnermatch_keys_allKeys = _endpartnermatch_keys_allKeys.concat(theseKeys);
      if (_endpartnermatch_keys_allKeys.length > 0) {
        endpartnermatch_keys.keys = _endpartnermatch_keys_allKeys[_endpartnermatch_keys_allKeys.length - 1].name;  // just the last key pressed
        endpartnermatch_keys.rt = _endpartnermatch_keys_allKeys[_endpartnermatch_keys_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *PressToContinue* updates
    if (t >= 0.0 && PressToContinue.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      PressToContinue.tStart = t;  // (not accounting for frame time here)
      PressToContinue.frameNStart = frameN;  // exact frame index
      
      PressToContinue.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of Partner_MatchComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function Partner_MatchRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Partner_Match' ---
    for (const thisComponent of Partner_MatchComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(endpartnermatch_keys.corr, level);
    }
    psychoJS.experiment.addData('endpartnermatch_keys.keys', endpartnermatch_keys.keys);
    if (typeof endpartnermatch_keys.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('endpartnermatch_keys.rt', endpartnermatch_keys.rt);
        routineTimer.reset();
        }
    
    endpartnermatch_keys.stop();
    // the Routine "Partner_Match" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}
var continueRoutine;
var frameRemains;
var t;
var Photo_ShareComponents;
function Photo_ShareRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Photo_Share' ---
    t = 0;
    Photo_ShareClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(3.000000);
    // update component parameters for each repeat
    participantimage_image.setImage(Photos);
    // keep track of which components have finished
    Photo_ShareComponents = [];
    Photo_ShareComponents.push(photobeingshared_text);
    Photo_ShareComponents.push(waitforfeedback_text);
    Photo_ShareComponents.push(participantimage_image);
    
    for (const thisComponent of Photo_ShareComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function Photo_ShareRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Photo_Share' ---
    // get current time
    t = Photo_ShareClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *photobeingshared_text* updates
    if (t >= 0.0 && photobeingshared_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      photobeingshared_text.tStart = t;  // (not accounting for frame time here)
      photobeingshared_text.frameNStart = frameN;  // exact frame index
      
      photobeingshared_text.setAutoDraw(true);
    }

    frameRemains = 0.0 + 3.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (photobeingshared_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      photobeingshared_text.setAutoDraw(false);
    }
    
    // *waitforfeedback_text* updates
    if (t >= 0.0 && waitforfeedback_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      waitforfeedback_text.tStart = t;  // (not accounting for frame time here)
      waitforfeedback_text.frameNStart = frameN;  // exact frame index
      
      waitforfeedback_text.setAutoDraw(true);
    }

    frameRemains = 0.0 + 3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (waitforfeedback_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      waitforfeedback_text.setAutoDraw(false);
    }
    
    // *participantimage_image* updates
    if (t >= 0.0 && participantimage_image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      participantimage_image.tStart = t;  // (not accounting for frame time here)
      participantimage_image.frameNStart = frameN;  // exact frame index
      
      participantimage_image.setAutoDraw(true);
    }

    frameRemains = 0.0 + 3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (participantimage_image.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      participantimage_image.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of Photo_ShareComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function Photo_ShareRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Photo_Share' ---
    for (const thisComponent of Photo_ShareComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Run 'End Routine' code from initiatefeedbackresponses
    feedbackresponses = `${Partner} ${Feedback} your photo`;
    if ((Feedback === "liked")) {
        fdbkimage = "Images/thumbsup.png";
    } else {
        if ((Feedback === "did not like")) {
            fdbkimage = "Images/thumbsdown.png";
        }
    }
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

var WaitingforfeedbackComponents;
function WaitingforfeedbackRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Waitingforfeedback' ---
    t = 0;
    WaitingforfeedbackClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(5.000000);
    // update component parameters for each repeat
    // keep track of which components have finished
    WaitingforfeedbackComponents = [];
    WaitingforfeedbackComponents.push(waiting_text);
    
    for (const thisComponent of WaitingforfeedbackComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function WaitingforfeedbackRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Waitingforfeedback' ---
    // get current time
    t = WaitingforfeedbackClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *waiting_text* updates
    if (t >= 0.0 && waiting_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      waiting_text.tStart = t;  // (not accounting for frame time here)
      waiting_text.frameNStart = frameN;  // exact frame index
      
      waiting_text.setAutoDraw(true);
    }

    frameRemains = 0.0 + 5.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (waiting_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      waiting_text.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of WaitingforfeedbackComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function WaitingforfeedbackRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Waitingforfeedback' ---
    for (const thisComponent of WaitingforfeedbackComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}
var startWTP;
var feedbackComponents;
function feedbackRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'feedback' ---
    t = 0;
    feedbackClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(3.000000);
    // update component parameters for each repeat
    displayfeedback_text.setText(feedbackresponses);
    fdbkimage_image.setImage(fdbkimage);
    // Run 'Begin Routine' code from initiatelottery_code
    if (((TrialNumber % 5) === 0)) {
        startWTP = 1;
    } else {
        startWTP = 0;
    }
    
    // keep track of which components have finished
    feedbackComponents = [];
    feedbackComponents.push(displayfeedback_text);
    feedbackComponents.push(fdbkimage_image);
    
    for (const thisComponent of feedbackComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function feedbackRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'feedback' ---
    // get current time
    t = feedbackClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *displayfeedback_text* updates
    if (t >= 0.0 && displayfeedback_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      displayfeedback_text.tStart = t;  // (not accounting for frame time here)
      displayfeedback_text.frameNStart = frameN;  // exact frame index
      
      displayfeedback_text.setAutoDraw(true);
    }

    frameRemains = 0.0 + 3.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (displayfeedback_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      displayfeedback_text.setAutoDraw(false);
    }
    
    // *fdbkimage_image* updates
    if (t >= 0.0 && fdbkimage_image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fdbkimage_image.tStart = t;  // (not accounting for frame time here)
      fdbkimage_image.frameNStart = frameN;  // exact frame index
      
      fdbkimage_image.setAutoDraw(true);
    }

    frameRemains = 0.0 + 3.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (fdbkimage_image.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      fdbkimage_image.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of feedbackComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function feedbackRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'feedback' ---
    for (const thisComponent of feedbackComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

var _sharenextphoto_key_allKeys;
var sharenextphoto_key_allKeys;
var continuesharingComponents;
function continuesharingRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'continuesharing' ---
    t = 0;
    continuesharingClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    sharenextphoto_key.keys = undefined;
    sharenextphoto_key.rt = undefined;
    _sharenextphoto_key_allKeys = [];
    // Run 'Begin Routine' code from hidecontinuesharingroutine_code
    if ((startWTP === 1)) {
        continueRoutine = false;
    } else {
        continueRoutine = true;
    }
    
    // keep track of which components have finished
    continuesharingComponents = [];
    continuesharingComponents.push(presstosharenextphoto_text);
    continuesharingComponents.push(sharenextphoto_key);
    
    for (const thisComponent of continuesharingComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function continuesharingRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'continuesharing' ---
    // get current time
    t = continuesharingClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *presstosharenextphoto_text* updates
    if (t >= 0.0 && presstosharenextphoto_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      presstosharenextphoto_text.tStart = t;  // (not accounting for frame time here)
      presstosharenextphoto_text.frameNStart = frameN;  // exact frame index
      
      presstosharenextphoto_text.setAutoDraw(true);
    }

    
    // *sharenextphoto_key* updates
    if (t >= 0.0 && sharenextphoto_key.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      sharenextphoto_key.tStart = t;  // (not accounting for frame time here)
      sharenextphoto_key.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { sharenextphoto_key.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { sharenextphoto_key.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { sharenextphoto_key.clearEvents(); });
    }

    if (sharenextphoto_key.status === PsychoJS.Status.STARTED) {
      let theseKeys = sharenextphoto_key.getKeys({keyList: ['space'], waitRelease: false});
      _sharenextphoto_key_allKeys = _sharenextphoto_key_allKeys.concat(theseKeys);
      if (_sharenextphoto_key_allKeys.length > 0) {
        sharenextphoto_key.keys = _sharenextphoto_key_allKeys[0].name;  // just the first key pressed
        sharenextphoto_key.rt = _sharenextphoto_key_allKeys[0].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of continuesharingComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function continuesharingRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'continuesharing' ---
    for (const thisComponent of continuesharingComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(sharenextphoto_key.corr, level);
    }
    psychoJS.experiment.addData('sharenextphoto_key.keys', sharenextphoto_key.keys);
    if (typeof sharenextphoto_key.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('sharenextphoto_key.rt', sharenextphoto_key.rt);
        routineTimer.reset();
        }
  
    
    sharenextphoto_key.stop();
    // Run 'End Routine' code from hidecontinuesharingroutine_code

    
    // the Routine "continuesharing" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

var _WTP_ins_keys1_allKeys;
var WTP_ins_keys1_allKeys;
var WTP_Instructions1Components;
function WTP_Instructions1RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date

    //--- Prepare to start Routine 'WTP_Instructions1' ---
    t = 0;
    WTP_Instructions1Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    WTP_ins_keys1.keys = undefined;
    WTP_ins_keys1.rt = undefined;
    _WTP_ins_keys1_allKeys = [];
    // keep track of which components have finished
    WTP_Instructions1Components = [];
    WTP_Instructions1Components.push(WTP_ins_text1);
    WTP_Instructions1Components.push(WTP_ins_keys1);
    
    for (const thisComponent of WTP_Instructions1Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;

    
  }
}

function WTP_Instructions1RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'WTP_Instructions1' ---
    // get current time
    t = WTP_Instructions1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *WTP_ins_text1* updates
    if (t >= 0.0 && WTP_ins_text1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      WTP_ins_text1.tStart = t;  // (not accounting for frame time here)
      WTP_ins_text1.frameNStart = frameN;  // exact frame index
      
      WTP_ins_text1.setAutoDraw(true);
    }

    
    // *WTP_ins_keys1* updates
    if (t >= 0.0 && WTP_ins_keys1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      WTP_ins_keys1.tStart = t;  // (not accounting for frame time here)
      WTP_ins_keys1.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { WTP_ins_keys1.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { WTP_ins_keys1.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { WTP_ins_keys1.clearEvents(); });
    }

    if (WTP_ins_keys1.status === PsychoJS.Status.STARTED) {
      let theseKeys = WTP_ins_keys1.getKeys({keyList: ['space'], waitRelease: false});
      _WTP_ins_keys1_allKeys = _WTP_ins_keys1_allKeys.concat(theseKeys);
      if (_WTP_ins_keys1_allKeys.length > 0) {
        WTP_ins_keys1.keys = _WTP_ins_keys1_allKeys[_WTP_ins_keys1_allKeys.length - 1].name;  // just the last key pressed
        WTP_ins_keys1.rt = _WTP_ins_keys1_allKeys[_WTP_ins_keys1_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of WTP_Instructions1Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function WTP_Instructions1RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'WTP_Instructions1' ---
    for (const thisComponent of WTP_Instructions1Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(WTP_ins_keys1.corr, level);
    }
    psychoJS.experiment.addData('WTP_ins_keys1.keys', WTP_ins_keys1.keys);
    if (typeof WTP_ins_keys1.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('WTP_ins_keys1.rt', WTP_ins_keys1.rt);
        routineTimer.reset();
        }
    
    WTP_ins_keys1.stop();
    // the Routine "WTP_Instructions1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

var _WTP_ins_keys2_allKeys;
var WTP_ins_keys2_allKeys;
var WTP_Instructions2Components;
function WTP_Instructions2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'WTP_Instructions2' ---
    t = 0;
    WTP_Instructions2Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    WTP_ins_keys2.keys = undefined;
    WTP_ins_keys2.rt = undefined;
    _WTP_ins_keys2_allKeys = [];
    // keep track of which components have finished
    WTP_Instructions2Components = [];
    WTP_Instructions2Components.push(WTP_ins_text2);
    WTP_Instructions2Components.push(WTP_ins_keys2);
    
    for (const thisComponent of WTP_Instructions2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function WTP_Instructions2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'WTP_Instructions2' ---
    // get current time
    t = WTP_Instructions2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *WTP_ins_text2* updates
    if (t >= 0.0 && WTP_ins_text2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      WTP_ins_text2.tStart = t;  // (not accounting for frame time here)
      WTP_ins_text2.frameNStart = frameN;  // exact frame index
      
      WTP_ins_text2.setAutoDraw(true);
    }

    
    // *WTP_ins_keys2* updates
    if (t >= 0.0 && WTP_ins_keys2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      WTP_ins_keys2.tStart = t;  // (not accounting for frame time here)
      WTP_ins_keys2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { WTP_ins_keys2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { WTP_ins_keys2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { WTP_ins_keys2.clearEvents(); });
    }

    if (WTP_ins_keys2.status === PsychoJS.Status.STARTED) {
      let theseKeys = WTP_ins_keys2.getKeys({keyList: ['space'], waitRelease: false});
      _WTP_ins_keys2_allKeys = _WTP_ins_keys2_allKeys.concat(theseKeys);
      if (_WTP_ins_keys2_allKeys.length > 0) {
        WTP_ins_keys2.keys = _WTP_ins_keys2_allKeys[_WTP_ins_keys2_allKeys.length - 1].name;  // just the last key pressed
        WTP_ins_keys2.rt = _WTP_ins_keys2_allKeys[_WTP_ins_keys2_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of WTP_Instructions2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function WTP_Instructions2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'WTP_Instructions2' ---
    for (const thisComponent of WTP_Instructions2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(WTP_ins_keys2.corr, level);
    }
    psychoJS.experiment.addData('WTP_ins_keys2.keys', WTP_ins_keys2.keys);
    if (typeof WTP_ins_keys2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('WTP_ins_keys2.rt', WTP_ins_keys2.rt);
        routineTimer.reset();
        }
    
    WTP_ins_keys2.stop();
    // the Routine "WTP_Instructions2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

var _responses_allKeys;
var responses_allKeys;
var WTPTaskComponents;

function WTPTaskRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'WTPTask' ---
    t = 0;
    conditionalBlank.setText('');
    WTPTaskClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(10.000000);
    // update component parameters for each repeat

    Left_Experience.setColor(new util.Color('white'));
    Left_Experience.setText(left);
    Right_Experience.setColor(new util.Color('white'));
    Right_Experience.setText(right);
    Left_Price.setText('$'+leftmoney);
    Right_Price.setColor(new util.Color('white'));
    Right_Price.setText('$'+leftmoney);
    responses.keys = undefined;
    responses.rt = undefined;
    _responses_allKeys = [];
    // keep track of which components have finished
    WTPTaskComponents = [];
    WTPTaskComponents.push(Left_Experience);
    WTPTaskComponents.push(Right_Experience);
    WTPTaskComponents.push(Left_Price);
    WTPTaskComponents.push(Right_Price);
    WTPTaskComponents.push(responses);
    WTPTaskComponents.push(conditionalBlank);
    
    for (const thisComponent of WTPTaskComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}
var continueRoutine;
var frameRemains;
var t;
function WTPTaskRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'WTPTask' ---
    // get current time
    t = WTPTaskClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Left_Experience* updates
    if (t >= 0.0 && Left_Experience.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Left_Experience.tStart = t;  // (not accounting for frame time here)
      Left_Experience.frameNStart = frameN;  // exact frame index
      
      Left_Experience.setAutoDraw(true);
    }

    frameRemains = 0.0 + 10 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (Left_Experience.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Left_Experience.setAutoDraw(false);
    }
    
    // *Right_Experience* updates
    if (t >= 0.0 && Right_Experience.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Right_Experience.tStart = t;  // (not accounting for frame time here)
      Right_Experience.frameNStart = frameN;  // exact frame index
      
      Right_Experience.setAutoDraw(true);
    }

    frameRemains = 0.0 + 10 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (Right_Experience.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Right_Experience.setAutoDraw(false);
    }
    
    // *Left_Price* updates
    if (t >= 0.0 && Left_Price.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Left_Price.tStart = t;  // (not accounting for frame time here)
      Left_Price.frameNStart = frameN;  // exact frame index
      
      Left_Price.setAutoDraw(true);
    }

    frameRemains = 0.0 + 10 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (Left_Price.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Left_Price.setAutoDraw(false);
    }
    
    // *Right_Price* updates
    if (t >= 0.0 && Right_Price.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Right_Price.tStart = t;  // (not accounting for frame time here)
      Right_Price.frameNStart = frameN;  // exact frame index
      
      Right_Price.setAutoDraw(true);
    }

    frameRemains = 0.0 + 10 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (Right_Price.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Right_Price.setAutoDraw(false);
    }
    
    // *responses* updates
    if (t >= 0.0 && responses.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      responses.tStart = t;  // (not accounting for frame time here)
      responses.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { responses.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { responses.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { responses.clearEvents(); });
    }

    frameRemains = 0.0 + 10 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (responses.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      responses.status = PsychoJS.Status.FINISHED;
  }

    if (responses.status === PsychoJS.Status.STARTED) {
      let theseKeys = responses.getKeys({keyList: ['1', '2'], waitRelease: false});
      _responses_allKeys = _responses_allKeys.concat(theseKeys);
      if (_responses_allKeys.length > 0) {
        responses.keys = _responses_allKeys[0].name;  // just the first key pressed
        responses.rt = _responses_allKeys[0].rt;
      }
    }
    
    // Run 'Each Frame' code from responses_code
    if ((responses.keys === "1")) {
        Left_Experience.setColor("green");
        Left_Price.setColor("green");

        
    } else {
        if ((responses.keys === "2")) {
            Right_Experience.setColor("green");
            Right_Price.setColor("green");
        }
    }

    
    // *conditionalBlank* updates
    if (responses.keys > 0 && conditionalBlank.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      conditionalBlank.tStart = t;  // (not accounting for frame time here)
      conditionalBlank.frameNStart = frameN;  // exact frame index
      conditionalBlank.setAutoDraw(true);
    }

    if (conditionalBlank.status === PsychoJS.Status.STARTED && t >= (conditionalBlank.tStart + 2.0)) {
    conditionalBlank.setAutoDraw(false);
    }

  //   show the response for 2 seconds, then move on to next trial
    if (conditionalBlank.status == PsychoJS.Status.FINISHED){
    
  
       continueRoutine = false;
     }


    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of WTPTaskComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}
var subtract_bonus;
function WTPTaskRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'WTPTask' ---
    // original placement of trialset re-numbering

  
    continueRoutine = false;
    for (const thisComponent of WTPTaskComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    if ((responses.keys === "1")) {
      psychoJS.experiment.addData('decision_price', leftmoney);
      subtract_bonus =  subtract_bonus + leftmoney;

        
    } else {
        if ((responses.keys === "2")) {
          psychoJS.experiment.addData('decision_price', rightmoney);
          subtract_bonus =  subtract_bonus + rightmoney;
        }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(responses.corr, level);
    }
    psychoJS.experiment.addData('responses.keys', responses.keys);
    if (typeof responses.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('responses.rt', responses.rt);
        }
    
    responses.stop();
    // Run 'Each Frame' code from responses_code
  

    // Run 'End Routine' code from responses_code
    Left_Experience.setColor("white");
    Right_Experience.setColor("white");
    Left_Price.setColor("white");
    Right_Price.setColor("white");

    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}
var ITIComponents; 
function ITIRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'ITI' ---
    t = 0;
    ITIClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    ITI_text.setText('+');
    // keep track of which components have finished
    ITIComponents = [];
    ITIComponents.push(ITI_text);
    
    for (const thisComponent of ITIComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}
var continueRoutine;
var frameRemains;
var t;

function ITIRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'ITI' ---
    // get current time
    t = ITIClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *ITI_text* updates
    if (t >= 0.0 && ITI_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ITI_text.tStart = t;  // (not accounting for frame time here)
      ITI_text.frameNStart = frameN;  // exact frame index
      
      ITI_text.setAutoDraw(true);
    }

    frameRemains = 0.0 + WTP_ITI - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (ITI_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      ITI_text.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of ITIComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function ITIRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'ITI' ---
    for (const thisComponent of ITIComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "ITI" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

var continueRoutine;
var frameRemains;
var t;
var _Resume_keys_allKeys;
var ContinueComponents;
function ContinueRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Continue' ---
    t = 0;
    ContinueClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // Run 'Begin Routine' code from code
    console.log(TrialNumber)
    const trials = [25,50,75,100]
    
        if (trials.includes(TrialNumber) == true) {
          continueRoutine = true;
          console.log('ok')
        } else {
          continueRoutine = false;
          console.log('nope')
        }

    resumetext = "Press space to resume.";
    trialset = function () {
        var _pj_a = [], _pj_b = trialset;
        for (var _pj_c = 0, _pj_d = _pj_b.length; (_pj_c < _pj_d); _pj_c += 1) {
            var i = _pj_b[_pj_c];
            _pj_a.push((i + 5));
        }
        return _pj_a;
    }
    .call(this);
    Resume_keys.keys = undefined;
    Resume_keys.rt = undefined;
    _Resume_keys_allKeys = [];
    Resume_Text.setText(resumetext);
    // keep track of which components have finished
    ContinueComponents = [];
    ContinueComponents.push(Resume_keys);
    ContinueComponents.push(Resume_Text);
    
    for (const thisComponent of ContinueComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function ContinueRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Continue' ---
    // get current time
    t = ContinueClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Resume_keys* updates
    if (t >= 0.0 && Resume_keys.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Resume_keys.tStart = t;  // (not accounting for frame time here)
      Resume_keys.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { Resume_keys.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { Resume_keys.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { Resume_keys.clearEvents(); });
    }

    if (Resume_keys.status === PsychoJS.Status.STARTED) {
      let theseKeys = Resume_keys.getKeys({keyList: ['space'], waitRelease: false});
      _Resume_keys_allKeys = _Resume_keys_allKeys.concat(theseKeys);
      if (_Resume_keys_allKeys.length > 0) {
        Resume_keys.keys = _Resume_keys_allKeys[0].name;  // just the first key pressed
        Resume_keys.rt = _Resume_keys_allKeys[0].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *Resume_Text* updates
    if (t >= 0.0 && Resume_Text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Resume_Text.tStart = t;  // (not accounting for frame time here)
      Resume_Text.frameNStart = frameN;  // exact frame index
      
      Resume_Text.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of ContinueComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function ContinueRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Continue' ---
    for (const thisComponent of ContinueComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(Resume_keys.corr, level);
    }
    psychoJS.experiment.addData('Resume_keys.keys', Resume_keys.keys);
    if (typeof Resume_keys.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('Resume_keys.rt', Resume_keys.rt);
        routineTimer.reset();
        }
    
    Resume_keys.stop();
    // the Routine "Continue" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

var salienceratingtext;
var _key_resp_allKeys;
var SalienceRatingComponents;
var continueRoutine;
var salience_slider;
var SalienceRatingClock;
var mouserec;
var prevButtonState;
var key_resp_allKeys;
var SalienceRatingComponents;
function SalienceRatingRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date

    //--- Prepare to start Routine 'SalienceRating' ---
    t = 0;
    SalienceRatingClock.reset(); // clock
    frameN = -1;
    //continueRoutine = true; // until we're told otherwise

    const trials = [25,50,75,100]

    if (trials.includes(TrialNumber) == true) {
      continueRoutine = true;

    } else {
      continueRoutine = false;
    }
    // update component parameters for each repeat
    // Run 'Begin Routine' code from saliencyrating_code
    
    // console.log(TrialNumber)
    // const trials = [30,60,90,120,150]
    // 
    //     if (trials.includes(TrialNumber) == true) {
    //       continueRoutine = true;
    //       console.log('ok')
    //     } else {
    //       continueRoutine = false;
    //       console.log('nope')
    //     }
  

    salienceratingtext = `How likely are you to share photos with ${Partner} in the future?
    
    Use your left and right arrows to move the arrow to your desired rating.`
    ;
    psychoJS.eventManager.clearEvents("keyboard");
    salience_slider.markerPos = 3;
    
    saliencequestion_text.setText(salienceratingtext);
    key_resp.keys = undefined;
    key_resp.rt = undefined;
    _key_resp_allKeys = [];
    salienceavatar_image.setImage(partneravatar);
    displayrating_text.setText(rating_forsalience);
    userMouse.clickReset();
    mouseClock.reset()
    mouserec = userMouse.getPos();
    userMouse.x = [];
    userMouse.y = [];
    userMouse.leftButton = [];
    userMouse.midButton = [];
    userMouse.rightButton = [];
    userMouse.time=[];
    prevButtonState = userMouse.getPressed();
    salience_slider.reset();
    displayrating_text.setText('Click line');
    
    // keep track of which components have finished
    SalienceRatingComponents = [];
    SalienceRatingComponents.push(saliencequestion_text);
    SalienceRatingComponents.push(key_resp);
    SalienceRatingComponents.push(salienceavatar_image);
    SalienceRatingComponents.push(saliencecontinue_text);
    SalienceRatingComponents.push(displayrating_text);
    SalienceRatingComponents.push(salience_slider);
    SalienceRatingComponents.push(SalienceRatingClock);
    SalienceRatingComponents.push(Salience_Button);
    
    for (const thisComponent of SalienceRatingComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}
var keys;
var rating_forsalience;
var salience_ratingvalue;
var gotValidClick;
var marker_pos;
var ratingvalue;
var buttonpress;
var finalmouseRT;
function SalienceRatingRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'SalienceRating' ---
    // get current time
    t = SalienceRatingClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // Run 'Each Frame' code from saliencyrating_code
    // var _pj;
    // function _pj_snippets(container) {
    //     function in_es6(left, right) {
    //         if (((right instanceof Array) || ((typeof right) === "string"))) {
    //             return (right.indexOf(left) > (- 1));
    //         } else {
    //             if (((right instanceof Map) || (right instanceof Set) || (right instanceof WeakMap) || (right instanceof WeakSet))) {
    //                 return right.has(left);
    //             } else {
    //                 return (left in right);
    //             }
    //         }
    //     }
    //     container["in_es6"] = in_es6;
    //     return container;
    // }
    // _pj = {};
    // _pj_snippets(_pj);
    // salience_slider.draw();
    // keys = psychoJS.eventManager.getKeys();
    // displayrating_text.setText(Math.round(salience_slider.getMarkerPos(), 1));
    // if (keys.length) {
    //     if (_pj.in_es6("left", keys)) {
    //         salience_slider.markerPos = (salience_slider.markerPos - 0.1);
    //         rating_forsalience = salience_slider.getRating();
    //         displayrating_text.setText(Math.round(salience_slider.getMarkerPos(), 1));
    //     } else {
    //         if (_pj.in_es6("right", keys)) {
    //             salience_slider.markerPos = (salience_slider.markerPos + 0.1);
    //             rating_forsalience = salience_slider.getRating();
    //             displayrating_text.setText(Math.round(salience_slider.getMarkerPos(), 1));
    //         }
    //     }
    // }
    // 
    // 
    let buttonpress = userMouse.getPressed(); // read mouse state
      const xys = userMouse.getPos();
      userMouse.x.push(xys[0]); // add mouse coordinates to x/y list, in principle for data storage, but not implemented right now
      userMouse.y.push(xys[1]);
      userMouse.leftButton.push(buttonpress[0]); // store buttons in button list, likewise for storage
      userMouse.midButton.push(buttonpress[1]);
      userMouse.rightButton.push(buttonpress[2]);
    // *saliencequestion_text* updates
    if (t >= 0.0 && saliencequestion_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      saliencequestion_text.tStart = t;  // (not accounting for frame time here)
      saliencequestion_text.frameNStart = frameN;  // exact frame index
      
      saliencequestion_text.setAutoDraw(true);
    }

    
    // *key_resp* updates
    if (t >= 0.0 && key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp.tStart = t;  // (not accounting for frame time here)
      key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp.clearEvents(); });
    }

    if (key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_allKeys = _key_resp_allKeys.concat(theseKeys);
      if (_key_resp_allKeys.length > 0) {
        key_resp.keys = _key_resp_allKeys[_key_resp_allKeys.length - 1].name;  // just the last key pressed
        key_resp.rt = _key_resp_allKeys[_key_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *salienceavatar_image* updates
    if (t >= 0.0 && salienceavatar_image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      salienceavatar_image.tStart = t;  // (not accounting for frame time here)
      salienceavatar_image.frameNStart = frameN;  // exact frame index
      
      salienceavatar_image.setAutoDraw(true);
    }

    
    // *saliencecontinue_text* updates
    if (t >= 0.0 && saliencecontinue_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      saliencecontinue_text.tStart = t;  // (not accounting for frame time here)
      saliencecontinue_text.frameNStart = frameN;  // exact frame index
      
      saliencecontinue_text.setAutoDraw(true);
      Salience_Button.setAutoDraw(true);
      displayrating_text.setText('Click line');
      displayrating_text.setAutoDraw(true);
    }

    
    // *displayrating_text* updates
    if (t >= 0.0 && displayrating_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      displayrating_text.tStart = t;  // (not accounting for frame time here)
      displayrating_text.frameNStart = frameN;  // exact frame index
      
      displayrating_text.setAutoDraw(true);
    }
    
    // // *salience_slider* updates
    if (t >= 0.0 && salience_slider.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      salience_slider.tStart = t;  // (not accounting for frame time here)
      salience_slider.frameNStart = frameN;  // exact frame index

      salience_slider.setAutoDraw(true);
    }

    var _pj;
      function _pj_snippets(container) {
          function in_es6(left, right) {
              if (((right instanceof Array) || ((typeof right) === "string"))) {
                  return (right.indexOf(left) > (- 1));
              } else {
                  if (((right instanceof Map) || (right instanceof Set) || (right instanceof WeakMap) || (right instanceof WeakSet))) {
                      return right.has(left);
                  } else {
                      return (left in right);
                  }
              }
          }
          container["in_es6"] = in_es6;
          return container;
      }
      _pj = {};
      _pj_snippets(_pj);

      const validclicks = [1,2,3,4,5]
        ratingvalue = salience_slider.getMarkerPos();
          if (1 < ratingvalue && ratingvalue < 1.5) {
                salience_slider.setMarkerPos(1)
                salience_slider.setRating(1)
                displayrating_text.setText(1);
                displayrating_text.setAutoDraw(true);

          }

          else if (1.5 < ratingvalue && ratingvalue < 2.5) {
                salience_slider.setMarkerPos(2)
                salience_slider.setRating(2)
                displayrating_text.setText(2);
                displayrating_text.setAutoDraw(true);

          }
            else if (2.5 < ratingvalue && ratingvalue < 3.5) {
                salience_slider.setMarkerPos(3)
                salience_slider.setRating(3)
                displayrating_text.setText(3);
                displayrating_text.setAutoDraw(true);

          }
          else if (3.5 < ratingvalue && ratingvalue < 4.5) {
              salience_slider.setMarkerPos(4)
              salience_slider.setRating(4)
              displayrating_text.setText(4);
              displayrating_text.setAutoDraw(true);
            }
          else if (4.5 < ratingvalue && ratingvalue < 5) {
              salience_slider.setMarkerPos(5)
              salience_slider.setRating(5)
              displayrating_text.setText(5);
              displayrating_text.setAutoDraw(true);

        }
            finalmouseRT = mouseClock.getTime(); // get mouse time, again for storage that is not implemented
            if (!buttonpress.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
              prevButtonState = buttonpress; //button state as of last frame, makes sure holding mouse down has not affected anything
              //debug code
              //console.log('new button state detected');
              if (buttonpress.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
                // check if the mouse was inside our 'clickable' objects
                gotValidClick = false;
                if (Salience_Button.contains(userMouse) && ratingvalue > 0) {
                  {gotValidClick = true};
                }
                if (gotValidClick === true) { // abort routine on response
                    continueRoutine = false;
                }
              }
            }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of SalienceRatingComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function SalienceRatingRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'SalienceRating' ---
    for (const thisComponent of SalienceRatingComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    function financial(x) {
                  return Number.parseFloat(x).toFixed(2);
                }
    // Run 'End Routine' code from saliencyrating_code
    entiretaskloop.addData("salience_rating", Math.round(salience_slider.getMarkerPos(), 1));
    
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp.corr, level);
    }
    psychoJS.experiment.addData('key_resp.keys', key_resp.keys);
    if (typeof key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp.rt', key_resp.rt);
        routineTimer.reset();
        }
    
    key_resp.stop();
    // the Routine "SalienceRating" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

var stressleveltext;
var _stresslevel_keypress_allKeys;
var StressLevelComponents;
var stress_slider;
var continueRoutine;
var StressLevelClock;
var mouserec;
var prevButtonState;
var stresslevel_keypress_allKeys;
var StressLevelComponents;
function StressLevelRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'StressLevel' ---
    t = 0;
    StressLevelClock.reset(); // clock
    frameN = -1;
//    continueRoutine = true; // until we're told otherwise
    const trials = [25,50,75,100]

    if (trials.includes(TrialNumber) == true) {
      continueRoutine = true;

    } else {
      continueRoutine = false;
    }
    // update component parameters for each repeat
    // Run 'Begin Routine' code from stresslevelslider
    // var _pj;
    // _pj = {};
    // _pj_snippets(_pj);
    // if ((! _pj.in_es6(TrialNumber, [30,60,90,120,150]))) {
    //     continueRoutine = false;
    // }
    // console.log(TrialNumber)
    // console.log(trials.includes(TrialNumber))
    // const trials = [30,60,90,120,150]
    // 
    //     if (trials.includes(TrialNumber) == true) {
    //       continueRoutine = true;
    //       console.log('ok')
    //     } else {
    //       continueRoutine = false;
    //       console.log('nope')
    //     }

    stressleveltext = `Please rate your current stress level.
    
    
    Use your mouse or left and right arrows to move the arrow to your desired rating.`
    ;
    psychoJS.eventManager.clearEvents("keyboard");
    
    stress_slider.markerPos = 5;
    stresslevel_text.setText(stressleveltext);
    stresslevel_keypress.keys = undefined;
    stresslevel_keypress.rt = undefined;
    _stresslevel_keypress_allKeys = [];
    userMouse.clickReset();
    mouseClock.reset()
    mouserec = userMouse.getPos();
    userMouse.x = [];
    userMouse.y = [];
    userMouse.leftButton = [];
    userMouse.midButton = [];
    userMouse.rightButton = [];
    userMouse.time=[];
    prevButtonState = userMouse.getPressed();
    stress_slider.reset();
    displaystressrating_text.setText(rating_forstress);
    // keep track of which components have finished
    StressLevelComponents = [];
    StressLevelComponents.push(stresslevel_text);
    StressLevelComponents.push(stresslevel_keypress);
    StressLevelComponents.push(displaystressrating_text);
    StressLevelComponents.push(stress_slider);
    StressLevelComponents.push(StressLevelClock);
    StressLevelComponents.push(userMouse);
    StressLevelComponents.push(Stress_Button);
    StressLevelComponents.push(stresscontinue_text);
    
    for (const thisComponent of StressLevelComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

var keys;
var rating_forstress;
var stress_ratingvalue;
var gotValidClick;
var marker_pos;
var ratingvalue;
var buttonpress;
var finalmouseRT;
function StressLevelRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'StressLevel' ---
    // get current time
    t = StressLevelClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // Run 'Each Frame' code from stresslevelslider
    let buttonpress = userMouse.getPressed(); // read mouse state
      const xys = userMouse.getPos();
      userMouse.x.push(xys[0]); // add mouse coordinates to x/y list, in principle for data storage, but not implemented right now
      userMouse.y.push(xys[1]);
      userMouse.leftButton.push(buttonpress[0]); // store buttons in button list, likewise for storage
      userMouse.midButton.push(buttonpress[1]);
      userMouse.rightButton.push(buttonpress[2]);
    // var _pj;
    // function _pj_snippets(container) {
    //     function in_es6(left, right) {
    //         if (((right instanceof Array) || ((typeof right) === "string"))) {
    //             return (right.indexOf(left) > (- 1));
    //         } else {
    //             if (((right instanceof Map) || (right instanceof Set) || (right instanceof WeakMap) || (right instanceof WeakSet))) {
    //                 return right.has(left);
    //             } else {
    //                 return (left in right);
    //             }
    //         }
    //     }
    //     container["in_es6"] = in_es6;
    //     return container;
    // }
    // _pj = {};
    // _pj_snippets(_pj);
    // stress_slider.draw();
    // keys = psychoJS.eventManager.getKeys();
    // displaystressrating_text.setText(Math.round(stress_slider.getMarkerPos(), 1));
    // if (keys.length) {
    //     if (_pj.in_es6("left", keys)) {
    //         stress_slider.markerPos = (stress_slider.markerPos - 0.1);
    //         rating_forstress = stress_slider.getRating();
    //         displayrating_text.setText(Math.round(stress_slider.getMarkerPos(), 1));
    //     } else {
    //         if (_pj.in_es6("right", keys)) {
    //             stress_slider.markerPos = (stress_slider.markerPos + 0.1);
    //             rating_forstress = stress_slider.getRating();
    //             displayrating_text.setText(Math.round(stress_slider.getMarkerPos(), 1));
    //         }
    //     }
    // }
    // 
    
    // *stresslevel_text* updates
    if (t >= 0.0 && stresslevel_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      stresslevel_text.tStart = t;  // (not accounting for frame time here)
      stresslevel_text.frameNStart = frameN;  // exact frame index
      
      stresslevel_text.setAutoDraw(true);
    }

    
    // *stresslevel_keypress* updates
    if (t >= 0.0 && stresslevel_keypress.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      stresslevel_keypress.tStart = t;  // (not accounting for frame time here)
      stresslevel_keypress.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { stresslevel_keypress.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { stresslevel_keypress.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { stresslevel_keypress.clearEvents(); });
    }

    // if (stresslevel_keypress.status === PsychoJS.Status.STARTED) {
    //   let theseKeys = stresslevel_keypress.getKeys({keyList: ['space'], waitRelease: false});
    //   _stresslevel_keypress_allKeys = _stresslevel_keypress_allKeys.concat(theseKeys);
    //   if (_stresslevel_keypress_allKeys.length > 0) {
    //     stresslevel_keypress.keys = _stresslevel_keypress_allKeys[_stresslevel_keypress_allKeys.length - 1].name;  // just the last key pressed
    //     stresslevel_keypress.rt = _stresslevel_keypress_allKeys[_stresslevel_keypress_allKeys.length - 1].rt;
    //     // a response ends the routine
    //     continueRoutine = false;
    //   }
    // }
    // 
    
    // // *displaystressrating_text* updates
    // if (t >= 0.0 && displaystressrating_text.status === PsychoJS.Status.NOT_STARTED) {
    //   // keep track of start time/frame for later
    //   displaystressrating_text.tStart = t;  // (not accounting for frame time here)
    //   displaystressrating_text.frameNStart = frameN;  // exact frame index
    // 
    //   displaystressrating_text.setAutoDraw(true);
    // }
    // *stresscontinue_text* updates
    //  if (t >= 0.0 && stresscontinue_text.status === PsychoJS.Status.NOT_STARTED) {
    if (stresslevel_keypress.status === PsychoJS.Status.STARTED && stresscontinue_text.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        stresscontinue_text.tStart = t;  // (not accounting for frame time here)
        stresscontinue_text.frameNStart = frameN;  // exact frame index

        stresscontinue_text.setAutoDraw(true);
        Stress_Button.setAutoDraw(true);
        displaystressrating_text.setText('Click line');
        displaystressrating_text.setAutoDraw(true);
    }
    // // *stress_slider* updates
    if (t >= 0.0 && stress_slider.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      stress_slider.tStart = t;  // (not accounting for frame time here)
      stress_slider.frameNStart = frameN;  // exact frame index

      stress_slider.setAutoDraw(true);
    }

    var _pj;
      function _pj_snippets(container) {
          function in_es6(left, right) {
              if (((right instanceof Array) || ((typeof right) === "string"))) {
                  return (right.indexOf(left) > (- 1));
              } else {
                  if (((right instanceof Map) || (right instanceof Set) || (right instanceof WeakMap) || (right instanceof WeakSet))) {
                      return right.has(left);
                  } else {
                      return (left in right);
                  }
              }
          }
          container["in_es6"] = in_es6;
          return container;
      }
      _pj = {};
      _pj_snippets(_pj);


      const validclicks = [1,2,3,4,5,6,7,8,9]
        ratingvalue = stress_slider.getMarkerPos();
          if (1 < ratingvalue && ratingvalue < 1.5) {
                stress_slider.setMarkerPos(1)
                stress_slider.setRating(1)
                displaystressrating_text.setText(1);
                displaystressrating_text.setAutoDraw(true);

          }

          else if (1.5 < ratingvalue && ratingvalue < 2.5) {
                stress_slider.setMarkerPos(2)
                stress_slider.setRating(2)
                displaystressrating_text.setText(2);
                displaystressrating_text.setAutoDraw(true);

          }
            else if (2.5 < ratingvalue && ratingvalue < 3.5) {
                stress_slider.setMarkerPos(3)
                stress_slider.setRating(3)
                displaystressrating_text.setText(3);
                displaystressrating_text.setAutoDraw(true);

          }
          else if (3.5 < ratingvalue && ratingvalue < 4.5) {
              stress_slider.setMarkerPos(4)
              stress_slider.setRating(4)
              displaystressrating_text.setText(4);
              displaystressrating_text.setAutoDraw(true);
            }
          else if (4.5 < ratingvalue && ratingvalue < 5.5) {
              stress_slider.setMarkerPos(5)
              stress_slider.setRating(5)
              displaystressrating_text.setText(5);
              displaystressrating_text.setAutoDraw(true);

        }
        else if (5.5 < ratingvalue && ratingvalue < 6.5) {
            stress_slider.setMarkerPos(6)
            stress_slider.setRating(6)
            displaystressrating_text.setText(6);
            displaystressrating_text.setAutoDraw(true);

      }
      else if (6.5 < ratingvalue && ratingvalue < 7.5) {
          stress_slider.setMarkerPos(7)
          stress_slider.setRating(7)
          displaystressrating_text.setText(7);
          displaystressrating_text.setAutoDraw(true);

    }
    else if (7.5 < ratingvalue && ratingvalue < 8.5) {
        stress_slider.setMarkerPos(8)
        stress_slider.setRating(8)
        displaystressrating_text.setText(8);
        displaystressrating_text.setAutoDraw(true);

  }
  else if (8.5 < ratingvalue && ratingvalue < 9) {
      stress_slider.setMarkerPos(9)
      stress_slider.setRating(9)
      displaystressrating_text.setText(9);
      displaystressrating_text.setAutoDraw(true);

}

            finalmouseRT = mouseClock.getTime(); // get mouse time, again for storage that is not implemented
            if (!buttonpress.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
              prevButtonState = buttonpress; //button state as of last frame, makes sure holding mouse down has not affected anything
              //debug code
              //console.log('new button state detected');
              if (buttonpress.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
                // check if the mouse was inside our 'clickable' objects
                gotValidClick = false;
                if (Stress_Button.contains(userMouse) && ratingvalue > 0) {
                  {gotValidClick = true};
                }
                if (gotValidClick === true) { // abort routine on response
                    continueRoutine = false;
                }
              }
            }


    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of StressLevelComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function StressLevelRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'StressLevel' ---
    for (const thisComponent of StressLevelComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Run 'End Routine' code from stresslevelslider
    stresslevel = stress_slider.getRating();
    function financial(x) {
                  return Number.parseFloat(x).toFixed(2);
                }
    entiretaskloop.addData("stress_level", Math.round(stress_slider.getMarkerPos(), 1));
    psychoJS.experiment.addData('subtract_bonus', subtract_bonus);
    psychoJS.experiment.addData('TOTAL_TASK_BONUS', 6- subtract_bonus);

    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(stresslevel_keypress.corr, level);
    }
    psychoJS.experiment.addData('stresslevel_keypress.keys', stresslevel_keypress.keys);
    if (typeof stresslevel_keypress.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('stresslevel_keypress.rt', stresslevel_keypress.rt);
        routineTimer.reset();
        }
    
    stresslevel_keypress.stop();
    // the Routine "StressLevel" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}
//--- Prepare to start Routine 'End_Screen' ---
var t;
var frameN;
var continueRoutine;
var _end_screen_keys_allKeys;
var End_ScreenComponents;
function End_ScreenRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date

    //--- Prepare to start Routine 'end_Screen' ---
    t = 0;
    end_screenclock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    end_screen_keys.keys = undefined;
    end_screen_keys.rt = undefined;
    _end_screen_keys_allKeys = [];
    // keep track of which components have finished
    End_ScreenComponents = [];
    End_ScreenComponents.push(end_screen);
    End_ScreenComponents.push(end_screen_keys);

    for (const thisComponent of End_ScreenComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function End_ScreenRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'end_screen_Screen' ---
    // get current time
    t = end_screenclock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame

    // *end_screen* updates
    if (t >= 0.0 && end_screen.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      end_screen.tStart = t;  // (not accounting for frame time here)
      end_screen.frameNStart = frameN;  // exact frame index

      end_screen.setAutoDraw(true);
    }


    // *end_screen_keys* updates
    if (t >= 0.0 && end_screen_keys.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      end_screen_keys.tStart = t;  // (not accounting for frame time here)
      end_screen_keys.frameNStart = frameN;  // exact frame index

      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { end_screen_keys.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { end_screen_keys.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { end_screen_keys.clearEvents(); });
    }

    if (end_screen_keys.status === PsychoJS.Status.STARTED) {
      let theseKeys = end_screen_keys.getKeys({keyList: ['space'], waitRelease: false});
      _end_screen_keys_allKeys = _end_screen_keys_allKeys.concat(theseKeys);
      if (_end_screen_keys_allKeys.length > 0) {
        end_screen_keys.keys = _end_screen_keys_allKeys[_end_screen_keys_allKeys.length - 1].name;  // just the last key pressed
        end_screen_keys.rt = _end_screen_keys_allKeys[_end_screen_keys_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }

    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }

    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of End_ScreenComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }

    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function End_ScreenRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'end_Screen' ---
    for (const thisComponent of End_ScreenComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(end_screen_keys.corr, level);
    }
    psychoJS.experiment.addData('end_screen_keys.keys', end_screen_keys.keys);
    if (typeof end_screen_keys.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('end_screen_keys.rt', end_screen_keys.rt);
        routineTimer.reset();
        }

    end_screen_keys.stop();
    // the Routine "end_Screen" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();

    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}





function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}

async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  window.location.replace(weblink);
  return Scheduler.Event.QUIT;
}
