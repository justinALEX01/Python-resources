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
