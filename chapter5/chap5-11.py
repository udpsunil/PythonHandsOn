
numbers = range(1, 10)

for number in numbers:
    if number not in [1, 2, 3]:
        print(str(number)+'th', end=" ")
    else:
        if number == 1:
            print(str(number)+'st', end=" ")
        elif number == 2:
            print(str(number)+'nd', end=" ")
        else:
            print(str(number)+'rd', end=" ")