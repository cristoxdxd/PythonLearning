import random

sports = ['Soccer','Basketball','Tennis','Golf','Swimming','Karate']

File = open('Exercise.txt','w')
File.close()

with open('Exercise.txt', mode='r+') as myFile:
    for i in range(500):
        myFile.write(str(random.choice(sports)+'\n'))