import math #as math

number = input('Enter a number: ')
print(type(number))
number = int(number)
print(type(number),'\n')
# number = int(input('Enter a number: '))
a, b = 5, 3
c = a**2

print('\tOperators')
print('Sum:',a+b) # Sum
print('Substract:',a-b) # Substract
print('Multiplication:',a*b) # Multiplication
print('Division:',a/b) # Division
print('Integer Division:',a//b) # Integer Division
print('Power:',a**3) # Power
print('Roots with power operator:',c**(1/2)) # Roots with power operator
print('Module:',a%b) # Module/Residue
if(int(math.sqrt(c))): print(True,'\n') # Square root

#floatnumber = float(input('Enter a float number: '))
print(float(input('Enter a float number: ')))