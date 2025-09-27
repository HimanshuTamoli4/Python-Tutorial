years = input("Enter your age ")
age = int(years);
if age>=18:
    print("you are an adult")
    print("you can vote")
elif age<18 and age>=12:
    print("You are a teenager you can vote after 18")
else:
    print("you are a kid")    
     
print("Thank you")     