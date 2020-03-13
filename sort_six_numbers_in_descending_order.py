# Write a program that accepts six (6) numbers and 
# sorts them in descending order.

# Get numbers from user using list comprehension.
print('Enter six numbers seperated by commas (,)')
number_list = list(int(x) for x in input('').split(','))

if len(number_list) > 6:
    print('You have entered more than six numbers.')
elif len(number_list) < 6:
    print('You have entered less than size numbers.')
elif len(number_list) == 6:
    number_list.sort(reverse=True)

print(number_list)
