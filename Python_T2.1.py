x = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]
print(sum(x))

print('ceva') if x != 0 else print('altceva')
sm = sum(x[0:len(x)])
print(sm)

even_count, odd_count = 0, 0

for num in x:

    # checking condition
    if num % 2 == 0:
        even_count += 1

    else:
        odd_count += 1

print("Even numbers in the list: ", even_count)
print("Odd numbers in the list: ", odd_count)


def EvenOddSum(a, n):
    even = 0
    odd = 0
    for i in range(n):

        # Loop to find evem, odd Sum
        if i % 2 == 0:
            even += a[i]
        else:
            odd += a[i]

    print("Even index positions sum ", even)
    print("nOdd index positions sum ", odd)

x = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]

n = len(x)

EvenOddSum(x, n)

#check if the number is polynomial

# initializing number
x = 1234554321

# printing the original number
print("The original number is : " + str(x))

# using str() + string slicing
# for checking a number is palindrome
res = str(x) == str(x)[::-1]

# printing result
print("Is the number palindrome ? : " + str(res))
