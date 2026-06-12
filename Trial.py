def factorial_generator(max_value):
    factorial = 1
    for i in range(max_value + 1):
        if i == 0:
            yield 1
        else:
            factorial *= i
            yield factorial

user_input = int(input("Enter a number: "))
for num in factorial_generator(user_input):
    print(num,end=" ")