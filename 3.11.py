def collatz(number):
    if number % 2 == 0:
        print(str(number // 2))
        return number // 2
    else:
        print(str(3 * number + 1))
        return 3 * number + 1

print("input a number: ")
try:
    number = int(input())

    while number != 1:
        number = collatz(number)

except ValueError:
    print('You must input a number!')

