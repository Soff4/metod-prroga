def factorial(x):
    if x == 0:
        return 1

    if x == 1:
        return 1

    return (x * factorial(x-1))


num = 5
print("Факторіал", num, "буде", factorial(num))