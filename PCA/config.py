import json

settings = json.load(open('SETTINGS.json', 'r'))
# print(settings)

WAV_DIR = settings['WAV_DIR']
MFCC_DIR = settings['MFCC_DIR']
LABEL_DIR = settings['LABEL_DIR']
SUBMISSION_DIR = settings['SUBMISSION_DIR']
OUTPUT_DIR = settings['OUTPUT_DIR']
TRAIN_SET = settings['TRAIN_SET']
TEST_SET = settings['TEST_SET']
VAL_SET = settings['VAL_SET']
