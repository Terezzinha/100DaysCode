##import range

for number in range(2,16):
   
    if (number % 3 == 0) and (number % 5 == 0):
        print(str(number) + " Buzz Fizz") 
    elif (number % 3 == 0):
        print(str(number) + " Buzz") 
    elif (number % 5 == 0):
        print(str(number) + " Fizz") 
    else:
        print("oi " + str(number))
    
