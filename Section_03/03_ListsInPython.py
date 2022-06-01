
my_list = ['one', 'two', 'three']
another_list = ['four', 'five']

print('My list: ', len(my_list))
print(my_list+another_list)

new_list = my_list + another_list
print('New List: ', new_list)

# replace 1 element
new_list[0]='ONE ALL CAPS'
print('Changed New List: ', new_list)

# append 1 element (at the end)
new_list.append('six')
print('New List: ', new_list)
new_list.append('seven')
print('New List: ', new_list)

# delete 1 element (at the end)
new_list.pop()
print('New List: ', new_list)

popped_item = new_list.pop()
print('New List: ', new_list)
print('Popped element: ', popped_item)

# delete 1 element (with index)
new_list.pop(0)
print('New List: ', new_list)

# sort
new_list = ['a', 'e', 'x', 'b', 'c']
num_list = [4, 1, 8, 3]

new_list.sort()
print('New List: ', new_list)

num_list.sort()
print('Num List: ', num_list)

# reverse
num_list.reverse()
print('Num List: ', num_list)
