
print("----------Arithmetic Calculator---------- ")   
print("for Addition Press'+'")
print("for Subtraction Press'-'")
print("for Multiplication Press'*'")
print("for Division Press'/'")
      
    
while True:
        choice = input("Enter Your Choice:")
        a = int(input("Enter first number: "))
        b = int(input("Enter first number: "))
        
        if choice =='+':
            print("Sum is",a+b)
        elif choice == '-':
            print("Subtraction is",a-b)
        elif choice =='*':
            print("Multiplication is",a*b)
        elif choice =='/':
            print("Division is",a/b)
            break
        else:
            print("Invalid input")
            

        
