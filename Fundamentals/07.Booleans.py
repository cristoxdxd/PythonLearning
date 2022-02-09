var1 = True
var2 = False
print(type(var1))
print(var1.bit_length())
print(var2.bit_length())

## Operators

print(var1 or var2)
print(not var2)
# Conjunction
print(var1 and var2)
### print(var1 ^ var2) # Bit-to-bit comparisson [xor]
print(var1 & var2) # get truly(1) or falsy(0)
# Disjunction
print(var1 | var2)
# Denial
print(not var1)


var3 = 2
var4 = 3

print(var3 & var4) # connjunction in bits
print(var3 | var4) # disjunction in bits
print(~var2)       # denial in bits
# Displacement
print(var1 >> var2) # to right
print(var1 << var2) # to left