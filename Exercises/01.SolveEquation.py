import math
print('\nSolve Equations type: ax²+bx+c = 0\n')
a = int(input('Enter a: '))
b = int(input('Enter b: '))
c = int(input('Enter c: '))
print('\nEquation to solve: (',a,')·x² + (',b,')·x + (',c,') = 0')
x1 = (-b + math.sqrt((b**2)-(4*a*c)))/(2*a)
x2 = (-b - math.sqrt((b**2)-(4*a*c)))/(2*a)
print('\nSolutions\n1:',x1,'\n2:',x2)
