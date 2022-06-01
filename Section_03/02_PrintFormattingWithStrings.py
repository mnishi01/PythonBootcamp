
# .format() method
print('This is a string {}'.format('INSERTED'))
print('The {2} {1} {0}'.format('fox', 'brown', 'quick'))
print('The {q} {b} {f}'.format(f='fox', b='brown', q='quick'))

# float formatting
result = 100/777
print('The result was {}'.format(result))
print('The result was {r}'.format(r=result))
print('The result was {r:1.3f}'.format(r=result))
print('The result was {r:10.3f}'.format(r=result))
print('The result was {r:10.5f}'.format(r=result))

# f-strings method
name = "Jose"
print('Hello, his name is {}'.format(name))
print(f'Hello, his name is {name}')

name = "Sam"
age = "3"
print(f'{name} is {age} years old.')
