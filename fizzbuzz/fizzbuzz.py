# For numbers 1 through 100, print `fizz` if the number is divisible by 3,
# `buzz` if the number is divisible by 5 and `fizzbuzz` if the number if the number
#  is divisible by both 3 and 5. If the number isn't divisible by 3 or 5, just output the number itself.


for i in range(1,101):

    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
    elif i % 5 == 0:
        print("buzz")
    elif i % 3 == 0:
        print("fizz")
    else:
        print(i)


