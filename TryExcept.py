try: 
    a = int(input("Enter the first  number: "))
    b = int(input("Enter the second number: "))
    print("The sum of two numbers is: ", a+b) #sum(a,b) also can be used

except:
    print("Invalid entry")    

else:
    print("Right Entry")

finally:
    print("Try catch finished")        

    