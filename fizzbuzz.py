fizzy_buzzy_num = 0

while (fizzy_buzzy_num <100):
    fizzy_buzzy_num +=1
    
    if ((fizzy_buzzy_num % 3 == 0) and (fizzy_buzzy_num % 5 == 0)):
        print("FizzBuzz")
    elif (fizzy_buzzy_num % 3 == 0):
        print("Fizz")
    elif (fizzy_buzzy_num % 5 == 0):
        print("Buzz")
    else:
        print(fizzy_buzzy_num)

