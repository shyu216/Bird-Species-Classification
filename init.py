import numpy as np
import os

min = 0
max = 100
is_test = 80
is_val = 90

train = open("train.txt", "w")
test = open("test.txt", "w")
val = open("val.txt", "w")

traindataset = "data/NIPS4B_BIRD_CHALLENGE_TRAIN_TEST_MFCC/train"

# all files name in traindataset
files = os.listdir(traindataset)
# shuffle files
for file in files:
    seed = np.random.randint(min, max)
    if seed < is_test:
        train.write(file + "\n")
    elif seed < is_val:
        test.write(file + "\n")
    else:
        val.write(file + "\n")

train.close()
test.close()
val.close()
