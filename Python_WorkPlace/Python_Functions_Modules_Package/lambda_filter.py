#Lambda
# Program to filter out only the even items from a list

my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(filter(lambda x: (x * 2) , my_list))

# Output: [4, 6, 8, 12]
print(new_list)
