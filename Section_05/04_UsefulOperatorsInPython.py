from random import shuffle
from random import randint


# Range
mylist = [1, 2, 3]

print('Range standard')
for num in range(10):
    print(num)

print('\nRange interval')
for num in range(3, 10):
    print(num)

print('\nRange steps')
for num in range(0, 10, 2):
    print(num)

print('\n', list(range(0,10,2)))


# Enumarate
index_count = 0
word = 'abcde'

print('\nStandard')
for letter in word:
    print(f'At index {index_count}, the letter is {letter}')
    index_count += 1

print('\nEnumerate Std')
for item in enumerate(word):
    print(item)

print('\nEnumerate Reviewed')
for (index, letter) in enumerate(word):
    print(index)
    print(letter)
    print('\n')


# Zip
mylist1 = [1, 2, 3, 4, 5, 6]
mylist2 = ['a', 'b', 'c']
mylist3 = [100, 200, 300]

print('\nZip')
for item in zip(mylist1, mylist2, mylist3):
    print (item)

print(list(zip(mylist1, mylist2, mylist3)))


# In
print('\nIn - List')
print ('x' in [1, 2, 3])
print ('x' in ['x', 'y', 'z'])

print('\nIn - String')
print ('a' in 'a world')

print('\nIn - Dictionary')
d = {'mykey':345}
print ('mykey' in d)
print (345 in d.values())
print (345 in d.keys())


# Min/Max
print('\nMathematical')
mylist = [10, 20, 30, 40, 100]
print(min(mylist))
print(max(mylist))


# Shuffle
print('\nShuffle')
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(mylist)

shuffle(mylist)
print(mylist)


# Random
print('\nRandom')
mynum = randint(0,100)
print(mynum)


# Input
result = input('Enter a number here: ')
print(result)
print(type(result))
print(float(result))
print(int(result))


