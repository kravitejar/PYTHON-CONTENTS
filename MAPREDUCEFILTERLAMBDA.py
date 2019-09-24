# Program to show the use of lambda functions

double = lambda x: x * 2

# Output: 10
print(double(5))


# Program to filter out only the even items from a list

my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(filter(lambda x: (x%5 != 0) , my_list))

# Output: [4, 6, 8, 12]
print(new_list)



# Program to double each item in a list using map()

my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(map(lambda x: x * 2 , my_list))

# Output: [2, 10, 8, 12, 16, 22, 6, 24]
print(new_list)




# Python code to illustrate  
# reduce() with lambda() 
# to get sum of a list 
from functools import reduce
li = [5, 8, 10, 20, 50, 100] 
sum = reduce((lambda x, y: x + y), li) 
print (sum) 
