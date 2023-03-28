#read user BMI information that is weight and height
weight_in_kg = int(input("Weight of the person in kg: "))
height_in_m = float(input("Height of the person in m: "))

#calculate BMI
BMI = weight_in_kg / (height_in_m * height_in_m)

#check the BMI whether it is above 30, 25, 18.5, or below
#and print the message
print()
if(BMI >= 30):
    print("User is obese")
elif(BMI >= 25):
    print("User is overweight")
elif(BMI >= 18.5):
    print("User is normal")
else:
    print("User is underweight")