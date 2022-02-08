simple = str('\tStrings\nSimple string')
print(simple)
multipleLines = '''
Hello!
.
.
.
This is a multiple lines string
'''
print(multipleLines)

# Operators
string1 = 'Python'
string2 = ' is a programming language'
float1 = 58.9
print(string1+string2+' & '+str(float1)+' is a number\n')

print('\tFormated strings')
name = 'Cristo'
level = 5 
### Variables based
print(f'1. Hi, I\'m {name} & my level is {level}')
### str class method
print('2. Hi, I\'m {} & my level is {}'.format(name,level))
### str class method with position (repetition is possible)
print('3. Hi, I\'m {1} & my level is {0}'.format(level,name))
### str class method with assignment
print('4. Hi, I\'m {aName} & my level is {newLevel}'.format(aName='Rodrigo', newLevel=level+5))

print('\n\tIndexing')
string3 = 'This is a programming course'
print('The string lenght is:',len(string3))
'''print(string3[0])
print(string3[27])
#print(string3[28]) # Out of range
print(string3[-1])  # with '-' sign the characters starts at the last
print(string3[-28])'''
print(string3[1]+string3[8]+string3[3])
print(string3[0:9]+string3[21:28]) # [includedValue : excludedValue : steps]
print(string3[::3])
print(string3[::-3])
invertedString3 = string3[::-1]
print(invertedString3)
'''
    Strings in Python are immutables
    So, this is imposible:
    string3[0] = 't' -> does not support item assignment    
'''

# Most used Python str methods
print(string3.upper())
print(string3.lower())
print(string3.capitalize())
string4 = 'Three trees throw leaves in other trees'
print(string4.find('trees'))
print(string4.find('treasure'))
print(string4.startswith('Three'))
print(string4.endswith('trees'))
print(string4.startswith('Throw'))
