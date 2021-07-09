#bmi calculator
(mass) = float(input("Weight(kg) "))
(height)=float(input("Height(m)"))
(height2) =(float(height)*float(height))
(bmi) =float(float(mass)/float(height2))
print(" \n")
print("your BMI is:")
print(bmi)
if bmi < 15:
    print ("you are underweight.")
if bmi > 25:
    print("you are overweight")