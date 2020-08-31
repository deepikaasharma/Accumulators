# total = 0

# for i in range(10):
#     total += i

# print(total)


# x = []

# for num in range(1, 101):
#     if (num**0.5).is_integer():
#         x.append(num)

# print(x)

# x = [44, 9, 93, 57, 35, 29, -4, 81, 54, 43, 42, 96, 55, 87, 11, 8, 8, 97, -3, 25]
# a = 0
# b = 0

# for num in x:
#     if num < a:
#         a = num
#     elif num > b:
#         b = num

# print(a, b)


# letters = ['p', 'y', 't', 'h', 'o', 'n', ' ', 'i', 's', ' ', 'a', 'w', 'e', 's', 'o', 'm', 'e', '!']

# phrase = ''

# for letter in letters:
#     phrase = phrase + letter

# print(phrase)


"""What will be the value of x after this accumulator code runs?"""

x = 0

num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in num_list:
    x += num**2

print(x)
