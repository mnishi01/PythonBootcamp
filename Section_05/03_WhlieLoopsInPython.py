

# Pass
print('PASS')
x = [1, 2, 3]

for item in x:
    pass

print('End of my script!')


# Continue
print('\nCONTINUE')
mystring = 'Sammy'

for letter in mystring:
    if letter == 'a':
        continue
    print(letter)


# Break
print('\nBREAK (FOR)')
for letter in mystring:
    if letter == 'a':
        break
    print(letter)


print('\nBREAK (WHILE)')
x = 0
while x < 5:
    if x == 2:
        break
    print(x)
    x += 1
