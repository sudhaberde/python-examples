number = int(input( "Enter the number: "))

newlist = range(2, (number+1))

print ("New list created")

print (newlist)



print (" list of divisors of %d ", number)


divisors = [ iter for iter in newlist if(number%iter == 0)]

print( divisors)