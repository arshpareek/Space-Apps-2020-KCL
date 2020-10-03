import os
import random
os.chdir("SatImageData")
if(os.path.isdir('train/yes')) is False:
    os.makedirs('train/no')
    os.makedirs('train/yes')
    os.makedirs('valid/no')
    os.makedirs('valid/yes')
    os.makedirs('test/no')
    os.makedirs('test/yes')

    yesDir = "yes"
    noDir = "no"

    trainSplit = 0.7 
    validSplit = 0.2
    testSplit = 0.1

    numberOfYesImages = len([image for image in os.listdir(yesDir) if os.path.isfile(image)])
    numberOfNoImages = len([image for image in os.listdir(noDir) if os.path.isfile(image)])
    for x in range(int(numberOfYesImages * trainSplit)) :
        filename = random.choice(os.listdir(yesDir))
        filePath = os.path.join(yesDir, filename)
        shutil.move(filePath, 'train/yes')

    for x in range(int(numberOfNoImages * trainSplit)) :
        filename = random.choice(os.listdir(noDir))
        filePath = os.path.join(noDir, filename)
        shutil.move(filePath, 'train/no')

    for x in range(int(numberOfYesImages * validSplit)) :
        filename = random.choice(os.listdir(yesDir))
        filePath = os.path.join(yesDir, filename)
        shutil.move(filePath, 'valid/yes')

    for x in range(int(numberOfNoImages * validSplit)) :
        filename = random.choice(os.listdir(noDir))
        filePath = os.path.join(noDir, filename)
        shutil.move(filePath, 'valid/no')

    for x in range(int(numberOfYesImages * testSplit)) :
        filename = random.choice(os.listdir(yesDir))
        filePath = os.path.join(yesDir, filename)
        shutil.move(filePath, 'valid/yes')

    for x in range(int(numberOfNoImages * testSplit)) :
        filename = random.choice(os.listdir(noDir))
        filePath = os.path.join(noDir, filename)
        shutil.move(filePath, 'valid/no')

