# Program to show the use of lambda functions

double = lambda x: x * 2

# Output: 10
print(double(5))

my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(filter(lambda x: (x%2 == 0) , my_list))

# Output: [4, 6, 8, 12]
print(new_list)
