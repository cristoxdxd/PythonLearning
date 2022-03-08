File = open('Exercise.txt')
File.seek(0)
SportsList = File.readlines()

soccerCounter = 0
basketballCounter = 0
tennisCounter = 0
golfCounter = 0
swimmingCounter = 0
karateCounter = 0

for i in range(len(SportsList)):
    if (SportsList[i] == 'Soccer\n'):
        soccerCounter += 1
    elif (SportsList[i] == 'Basketball\n'):
        basketballCounter += 1
    elif (SportsList[i] == 'Tennis\n'):
        tennisCounter += 1
    elif (SportsList[i] == 'Golf\n'):
        golfCounter += 1
    elif (SportsList[i] == 'Swimming\n'):
        swimmingCounter += 1
    elif (SportsList[i] == 'Karate\n'):
        karateCounter += 1
    else:
        pass

sports = ['Soccer','Basketball','Tennis','Golf','Swimming','Karate']
sportsCounters = [soccerCounter, basketballCounter, tennisCounter, golfCounter, swimmingCounter, karateCounter]

File = open('ExerciseSummary.txt','w')
File.close()

with open('ExerciseSummary.txt', mode='w+') as myFile:
    for i in range(len(sports)):
        myFile.write(sports[i]+':'+str(sportsCounters[i])+'\n')
