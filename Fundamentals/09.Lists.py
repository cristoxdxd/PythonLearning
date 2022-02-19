list1 = [1,2,3,4,5,6,7,8,9,10]
print(type(list1))

list2 = ['a','b','c',85,74,True,35.68]
print(list2)

print(len(list2))
print(list2[0])

list2[5] = False
print(list2)

list2.append('Hi!')

list2.insert(1,False)

list2.extend(['Juan','Pablo'])

list2.pop(3)

list2.remove(False)

print('Juan' in list2)

list3 = list2.copy()

list3.reverse()

print(list3.index('Pablo'))

list4 = [87,45,69,78,31,2]

list4.sort()
print(list4)
list4.sort(reverse = True)
print(list4)

string1 = 'Hi, how are you?'
string2 = 'I\'m fine'
list5 = string1.split(' ')

print(list5.count())
print(string1.join(string2))

list6 =list5.copy()
list6.clear()
print(list6)

