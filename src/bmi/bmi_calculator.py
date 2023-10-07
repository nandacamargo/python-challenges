'''This program is to calculate BMI (Body Mass Index)'''
import sys

# Do not print traceback to the end user
sys.tracebacklimit = 0 

class BMI():

    def __init__(self, height, weight):
        self.height = height
        self.weight = weight

    def calculate_bmi(self):
        bmi = self.weight / (self.height * self.height)

        weight_ranges = [18.5, 25, 30, 35]

        result = ["underweight", "normal weight", "slightly overweight", 
                "overweight", "clinically obese"]

        for i in range(4):
            if (bmi <  weight_ranges[i]):
                print(f"Your BMI is {bmi}, you are {result[i]}")
                return result[i]

        print(f"Your BMI is {bmi}, you are clinically obese")
        return "clinically obese"


if __name__ == '__main__':

    try:
        height = float(input("What is your height, in meters? "))
        weight = float(input("What is your weight in kilograms? "))
    except: 
        raise ValueError("You provided an invalid height or weight.\n It should be a decimal number!")


    bmi = BMI(height, weight)
    bmi.calculate_bmi()