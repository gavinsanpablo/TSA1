num1 = int(input("Enter the first number: ")) 
num2 = int(input("Enter the second number: ")) 
num3 = int(input("Enter the third number: ")) 
if num1 >= num2: 
    if num2 >= num3: 
        print("Descending order:", num1, num2, num3) 
    else: 
        if num1 >= num3: 
            print("Descending order:", num1, num3, num2) 
        else: 
            print("Descending order:", num3, num1, num2) 
else: 
    if num2 >= num3: 
        if num1 >= num3: 
            print("Descending order:", num2, num1, num3) 
        else: 
            print("Descending order:", num2, num3, num1) 
    else: 
        print("Descending order:", num3, num2, num1) 