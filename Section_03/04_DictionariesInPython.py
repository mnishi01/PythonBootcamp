
# Example 01
prices_lookup = {'apple':2.99 ,'orange':1.99, 'milk':5.80}
print(prices_lookup['apple'])

# Example 2
d = {'k1': 123, 'k2': [0,1,2], 'k3':{'insidekey':100}}
print(d['k2'])
print(d['k2'][2])
print(d['k3'])
print(d['k3']['insidekey'])

# Example 3
d = {'key1': ['a','b','c']}
print(d)

my_list = d['key1']
print(my_list)

letter = my_list[2]
print(letter.upper())

print(d['key1'][2].upper())

# Example 4
d = {'k1': 100, 'k2': 200}
print(d)
d['k3'] = 300
print(d)
d['k1'] = 'NEW VALUE'
print(d)

# Example 5
d = {'k1': 100, 'k2': 200}
print(d)
print(d.keys())
print(d.values())
print(d.items())
