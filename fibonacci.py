def fibonacci(number):




    if number==1:
       numlist = [1]
       return numlist

    elif number==2:
        numlist = [1,1]
        return numlist

    else:
        numlist = [1, 1]

        for iter in range(2,number+1):
            numlist.append(numlist[iter-1]+numlist[iter-2])
        return numlist




number = int(input("Enter a number greater than 0"))

print("Fibonacci series is \n")

numList=fibonacci(number)

print(numList)