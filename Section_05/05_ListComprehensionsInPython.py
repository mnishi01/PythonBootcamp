

mystring = 'Hello'
mylist = []

print('Standard for')
for letter in mystring:
    mylist.append(letter)
print(mylist)


print('\nOther approach')
mylist = [letter for letter in mystring]
print(mylist)

mylist = [letter for letter in 'word']
print(mylist)

print('\nOther approach - Numbers')
mylist = [num for num in range(0,11)]
print(mylist)

mylist = [num**2 for num in range(0,11)]
print(mylist)

print('\nOther approach - If')
mylist = [num for num in range(0,11) if num%2==0]
print(mylist)

mylist = [num**2 for num in range(0,11) if num%2==0]
print(mylist)

print('\nOther approach - Formula and List')
celcius = [0, 10, 20, 34.5]
fahrenheit = [( (9/5)*temp + 32) for temp in celcius]
print(celcius)
print(fahrenheit)

print('\nOther approach - If and Else')
results = [ x if x%2==0 else 'ODD' for x in range(0,11)]
print(results)

print('\nNested')
mylist = []
for x in [2, 4, 6]:
    for y in [1, 10, 1000]:
        mylist.append(x*y)
print(mylist)

print('\nNested - Other approach')
mylist = [x*y for x in [2, 4, 6] for y in [1, 10, 1000]]
print(mylist)
