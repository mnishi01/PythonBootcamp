

# List
print('List')

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in mylist:
    print(num)

print('\nEven numbers')
for num in mylist:
    if num % 2 == 0:
        print(num)
    else:
        print(f'Odd Number: {num}')

print('\nSum')
list_sum = 0
for num in mylist:
    list_sum = list_sum + num
print('Total = ', list_sum)


# String
print('\nString')
mystring = 'Hello World'
for letter in mystring:
    print(letter)


# Tupple
print('\nTuple')
tup = (1, 2, 3)
for item in tup:
    print(item)

print('\nList of Tuples')
mylist = [(1, 2), (3, 4), (5, 6), (7, 8)]
print('Length = ', len(mylist))
for item in mylist:
    print(item)

for (a, b) in mylist:
    print(a)
    print(b)


# Dictionary
print('\nDictionary')
d = {'k1':1, 'k2':2, 'k3':3}
for item in d:
    print(item)
for item in d.items():
    print(item)
for (key, value) in d.items():
    print(value)
for value in d.values():
    print(value)
