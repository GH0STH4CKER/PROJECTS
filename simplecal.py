print("Press 1 for addition +")
print("Press 2 for substraction -")
print("Press 3 for multiplication *")
print("Press 4 for divition /")

fno = int(input("\nEnter function number :"))

if fno == 1:
    print("\nADDITION +")
    num1 = int(input("\nEnter first number : "))
    num2 = int(input("Enter second number : "))
    ans = num1 + num2
    print("\nAnswer is",ans)
elif fno == 2:
     print("\nSUBSTRAACTION -")
     num1 = int(input("\nEnter first number : "))
     num2 = int(input("Enter second number : "))
     ans = num1 - num2
     print("\nAnswer is",ans)
elif fno == 3:
     print("\nMULTIPLICATION *")
     num1 = int(input("\nEnter first number : "))
     num2 = int(input("Enter second number : "))
     ans = num1 * num2
     print("\nAnswer is",ans)
elif fno == 4:
     print("\nDIVITION /")
     num1 = int(input("\nEnter first number : "))
     num2 = int(input("Enter second number : "))
     ans = num1 / num2
     print("\nAnswer is",ans)
else:
     print("Invalid function")

input("\nPress enter to exit")     

    
