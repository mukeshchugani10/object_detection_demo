import os
import math
import random

f_names = []

for filename in os.listdir('data/images/train/'):
	if filename.endswith('.jpg'):
		f_names.append(filename)

random.seed(42)
random.shuffle(f_names)

test = math.floor(0.1*len(f_names))
val = math.floor(0.2*len(f_names))
train = 0.7*len(f_names)

test_files = f_names[:test]
val_files = f_names[test:test+val]
train_files = f_names[test+val:]

# Make sure /images/test and test both are empty
# test_ground_truth also should be empty

for each in test_files:
	os.rename('data/images/train/'+each,'test/'+each)
	os.rename('data/images/train/'+each[:-3]+'xml','test_ground_truth/'+each[:-3]+'xml')

for each in val_files:
	os.rename('data/images/train/'+each,'data/images/test/'+each)
	os.rename('data/images/train/'+each[:-3]+'xml','data/images/test/'+each[:-3]+'xml')
