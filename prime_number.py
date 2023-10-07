user_number = int(input("Enter a number "))
counter = 0
checker = 0

if user_number == 1:
        print("There are no prime numbers less than %d" %user_number)
elif user_number > 1:
    for x in range(2,user_number):
        i=2
        while i <= x:
            modulus = x % i
            if (x % i) == 0:
                checker += 1
            i+=1
        if checker <= 1:
            counter += 1
        checker = 0
        
    print("There are %d prime numbers less than %d" %(counter,user_number))
        