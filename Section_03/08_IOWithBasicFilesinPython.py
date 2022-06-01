

myfile = open('G:/My Drive/Training/Python Bootcamp/Section_03/test.txt')

print(myfile.read())
print(myfile.read())

# Reset the cursor
myfile.seek(0)
print('\n')
print('After reset:')
print(myfile.read())

# Assign to a variable
myfile.seek(0)
contents = myfile.read()
print('\n')
print('Variable:')
print(contents)

# Assign to a list
myfile.seek(0)
print('\n')
print('List:')
print(myfile.readlines())

# Close a file
myfile.close()

# Alternative
with open('G:/My Drive/Training/Python Bootcamp/Section_03/test.txt') as my_new_file:
    contents = my_new_file.read()
print('\n')
print('Alternative:')
print(contents)

# Mode = 'r'
with open('G:/My Drive/Training/Python Bootcamp/Section_03/test.txt', mode = 'r') as myfile:
    contents = myfile.read()
print('\n')
print('Mode = r')
print(contents)

# New File
with open('G:/My Drive/Training/Python Bootcamp/Section_03/newtest.txt', mode = 'r') as f:
    print('\n')
    print('New File')
    print (f.read())

with open('G:/My Drive/Training/Python Bootcamp/Section_03/newtest.txt', mode = 'a') as f:
    f.write('\nFOUR ON FORTH')
with open('G:/My Drive/Training/Python Bootcamp/Section_03/newtest.txt', mode = 'r') as f:
    print('\n')
    print('New File After Append')
    print (f.read())

with open('G:/My Drive/Training/Python Bootcamp/Section_03/xpto.txt', mode = 'w') as f:
    f.write('I CREATED THIS FILE!')
with open('G:/My Drive/Training/Python Bootcamp/Section_03/xpto.txt', mode = 'r') as f:
    print('\n')
    print('New File')
    print (f.read())