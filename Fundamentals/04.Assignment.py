variable1 = None
print('The variable initialized with',variable1,'is:',type(variable1))

y = 10
print(y)    #10
y = y * 2   #20
print(y*2)  #40
print(y)    #20

a, b, c, greet = 2, 3, 5, 'Hi!'
print(a+b+c)
print(greet)

'''
An error could be generated by:
x, y = 10, 11
z, y = x, z+2 # in this line the z assignment is tried to be used and initialized at the same time
'''