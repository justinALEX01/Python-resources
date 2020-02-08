##EX1
def find():
    start = 1, 100
    for i in range(1,100):
        if i % 2 == 0:
            print(i)

        elif i < 10:
            print(i)


        elif (i >= 10 and i <= 20):
            print("Not Pass")
        else:
            print(i > 20)

find()


##EX2
def fizzbuzz(n):
    result = []
    for x in range(1, n+1):
        if x % 3 == 0 and x % 5 == 0:
            result.append("FizzBuzz")
        elif x % 3 == 0:
            result.append('Fizz')
        elif x % 5 == 0:
            result.append('Buzz')
        else:
            result.append(str(x))
    return result

def main():
    print(', '.join(fizzbuzz(100)))

main()
