with open('Example.txt', 'r+') as myFile:
    
    print(myFile.read())
    
    myFile.write('\nText that was written by the script \'02.File.py\'')
    myFile.seek(0)
    print(myFile.read())