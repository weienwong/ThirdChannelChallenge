

def fizz_buzz(num):
    if num % 3 is 0 and num % 5 is 0:
        return "FizzBuzz"
    elif num % 3 is 0 or str(num).find("3") is not -1:
        return "Fizz"
    elif num % 5 is 0 or str(num).find("5") is not -1:
        return "Buzz"
    else:
        return num


def main():
    for n in range(1,100):
        print(fizz_buzz(n))

if __name__ == "__main__":
    main()