

# Strings
print('STRINGS')

s = 'hello'

print(s[1])
print(s[::-1])
print(s[4])
print(s[-1])


# Lists
print('\nLISTS')

list_a = [0]*3
print(list_a)
list_b = [0, 0, 0]
print(list_b)

list_c = [1, 2, [3, 4, 'hello']]
print(list_c)
list_c[2][2] = 'goodbye'
print(list_c)

list_d = [5, 3, 4, 6, 1]
print(list_d)
list_d.sort()
print(list_d)
list_d = [5, 3, 4, 6, 1]
print(list_d)
print(sorted(list_d))


# Dictionaries
print('\nDICTIONARIES')

d = {'simple_key':'hello'}
print(d['simple_key'])

d = {'k1':{'k2':'hello'}}
print(d['k1']['k2'])

d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d['k1'][0]['nest_key'][1][0])

d = {'k1':[1, 2, {'k2':['this is tricky', {'tough':[1, 2, ['hello']]}]}]}
print(d['k1'][2]['k2'][1]['tough'][2][0])




