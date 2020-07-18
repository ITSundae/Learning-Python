#K. Davenport
#FOR COLLEGE
#July 17th, 2020
#BMI Calculator: A calculator that calculates BMI and heart rate.

#A function that handles error messages.
def error_message():
    print("Please input a number.")

#This function helps print results professionally for the workout section.
def intensity_results():
    print(f"|\t      {workoutIntensity}% |\t   {maxHeartRate} BPM |")

#This is a check that helps the user with converting feet to inches for use with the program.
#Thanks Bee from TryHackMe for helping me out with the variable.lower() statement with in[""].
print("This is a program that helps you with calculating your BMI and what your max heart rate will be at different workout intervals. \n")
while True:
    inchesAid=input("Before we proceed, do you need assistance with converting feet into inches? ")
    if isinstance(inchesAid, str):
        if inchesAid.lower() in ["y", "yes"]:
            print("All right. I can help you out. \n")
            inchesAid="t"
            break
        elif inchesAid.lower() in ["n", "no"]:
            print("You're more independant than me! I won't help you out! \n")
            inchesAid="f"
            break
        else:
            print("Please select from either yes or no.")
    else:
        print("Please input yes or no.")

#If the user selected that they needed help previously, we will do the math for them.
while inchesAid=="t":
    while True:
        userFeet=input("Please input how many feet tall you stand at. ")
        if userFeet.isdigit():
            userFeet=int(userFeet)
            break
        else: error_message()

    while True:
        userInches=input(f"If you stand at {userFeet} feet, how many inches are spare? ")
        if userInches.isdigit():
            userInches=int(userInches)
            break
        else: error_message()

    userHeight=(userFeet*12 +userInches)
    print(f"Okay. I'll remember that you are {userHeight} inches tall.")
    userHeight=float(userHeight)
    break

#If the user selected that they don't need help, we run this code instead.
if inchesAid=="f":
    while True:
        userHeight=input("How tall are you in inches? ")
        if userHeight.isdigit():
            userHeight=float(userHeight)
            break
        else: error_message()

#We are onto what the main program should be at this point since conversion is no-longer needed.
while True:
    userWeight=input("How much do you weigh in pounds? ")
    if userWeight.isdigit():
        userWeight=float(userWeight)
        break
    else: error_message()

while True:
    userAge=input("How old are you? ")
    if userAge.isdigit():
        userAge=int(userAge)
        break
    else: error_message()

while True:
    heartRate=input("What is your resting heart rate? ")
    if heartRate.isdigit():
        heartRate=int(heartRate)
        break
    else: error_message()

#Formula provided via cdc.gov/healthyweight/assessing/bmi/childrens_bmi/childrens_bmi_formula.html
bmiResults=userWeight*703 / userHeight**2

#We lock the BMi results to 2 digits.
bmiResults=round(bmiResults,2)

#Decision tree that determines what to print to the user.
if bmiResults<=18.5:
    userBMI="underweight"
elif bmiResults<=24.9:
    userBMI="average"
elif bmiResults<=29.9:
    userBMI="overweight"
else: userBMI="obese"

#Here we handle printing results for BMI.
print(f"\n\nHere are your results!")
print(f"You are {userBMI} with a BMI of {bmiResults}.")
print("\n\nYour Workout Intensity Heart Rates:")
print("-"*35)
print("\tINTENSITY:\tHEART RATE:")
print("-"*35)

#This works with printing work out intensity results.
workoutIntensity=50
while workoutIntensity <= 95:
    maxHeartRate=(((220-userAge) -heartRate) *(workoutIntensity/100)) +heartRate
    maxHeartRate=int(maxHeartRate)
    intensity_results()
    workoutIntensity=workoutIntensity+5
print("-"*35)
