def febonacchiSeries(num):
    a = 0
    b = 1
    if num == 1:
        print(0)
    elif num == 0:
        print("Enter the num ber greter than zero")
    else:
        print(a)
        print(b)
        for i in range(2, num):
            c = a + b

            a = b
            b = c
            print(c)


num = int(input("Enter the number"))
febonacchiSeries(num)
