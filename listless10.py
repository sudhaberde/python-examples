
print ("List comprehension program")

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

newList = [ iter for iter in a if iter < 6]

print(newList)