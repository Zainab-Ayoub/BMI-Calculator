height = float(input("Enter you height in m: "))
weight = float(input("Enter you weight in kg: "))
BMI = round(weight/height ** 2) 

print(BMI)

if BMI < 18.5:
    print("You are underweight.")
elif BMI < 25:
    print("You have normal weight.") 
elif BMI < 30:
    print("You are overweight.")        
elif BMI < 35:
    print("You are obese.")
else:
    print("You are clinically obese.")            
