print('\tPalindromes')
possibleP = str(input('Enter a string: '))

if possibleP == possibleP[::-1] :
    print('It is a palindrome')
elif possibleP.lower() == possibleP[::-1].lower() :
    print('It is a palindrome if all lower')
elif possibleP.replace(' ','') == possibleP[::-1].replace(' ','') :
    print('It is a palindrome if no spaces')
elif possibleP.replace(' ','').lower() == possibleP[::-1].replace(' ','').lower() :
    print('It is a palindrome if all lower and no spaces')
else :
    print('It isn\'t a palindrome')
    print('\''+possibleP+'\' is not equal to \''+possibleP[::-1]+'\'')

