number = int(input("Please enter a number for checking the primality"))
if( number ==1 ):

    print( " its a prime number")
elif( number == 2):
    print ("its agin a prime number")

else:
    for x in range(2, number):
        if(number%x==0):
          print("Its  not a prime number")
          break
        else:
          ("its a prime number")
