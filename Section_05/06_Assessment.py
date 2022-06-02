

# Exercise 01
print('Exercise 01')
st = 'Sam print only the words that start with s in this sentence'

list_st = st.split()
print(list_st)

for word_list in list_st:
    if word_list[0].lower()=='s':
        print(word_list)


# Exercise 02
print('\nExercise 02')
for num in range(0,11,2):
    print(num)


# Exercise 03
print('\nExercise 03')
mylist = [num for num in range(1,51) if num%3==0]
print(mylist)


# Exercise 04
print('\nExercise 04')
st = 'Print every word in this sentence that has an even number of letters'

list_st = st.split()
print(list_st)

for word_list in list_st:
    if len(word_list)%2==0:
        print(word_list + ' is even!')


# Exercise 05
print('\nExercise 05')

for num in range(1,101):
    resp = ""
    if num%3 == 0:
        resp += 'Fizz'
    if num%5 == 0:
        resp += 'Buzz'
    print(f'Number: {num} '+ resp)


# Exercise 06
print('\nExercise 06')
st = 'Create a list of the first letters of every word in this string'
list_st = st.split()
print(list_st)
result = [letra[0] for letra in list_st]
print(result)
