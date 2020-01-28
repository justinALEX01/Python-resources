x = [5, 4, 3, 2, 0, 2]
print(max(x))

sum_ = 0
for item in x:
    if item % 2 != 0:
        sum_ += item
print(sum_)

def getMaxLength(arr, n):
    count = 0
    result = 0

    for i in range(0, n):
        if (arr[i] == 0):
            count = 0
        else:
            count += 1
            result = max(result, count)

    return result
num = [5,4,1,2,3,0]

for i in range(len(num)-1):
    if num[i] + 1 == num[i + 1]:
        if i == 0 or (i - 1 >= 0 and num[i - 1] != num[i] - 1):
            print('Consecutive', num[i])
        print('Consecutive', num[i + 1])
