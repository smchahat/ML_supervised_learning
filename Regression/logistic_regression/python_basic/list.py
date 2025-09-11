lst = [1,6,32,4, 977, 3,2]


lst.append(100) # add at the end

lst.pop(1) # remove element of index 2
lst.pop() # rm last ele

lst.extend([43,56,21]) # add these ele

lst.remove(56) # rm specific num

lst.insert(1, 99) # at index 1 insert 99

del lst[5:] # del all from 5 index

print(lst)

print(sum(lst[2:]))

print(max(lst))

print(min(lst))

lst.sort()

print(lst)