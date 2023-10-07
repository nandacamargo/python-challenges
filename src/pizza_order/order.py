import sys

'''This program calculates the bill for a given pizza order
============================================================
Rules:
Small Pizza: $15
Medium Pizza: $20
Large Pizza: $25

Add pepperoni for small pizza: + $2
Add pepperoni for medium or large pizza: + $3
Add extra cheese for any size of pizza: $1
============================================================
'''

# Do not print traceback to the end user
sys.tracebacklimit = 0 

valid_sizes = ["S", "M", "L"]
valid_answers = ["Y", "N"]

class Order():

    def __init__(self, size, pepperoni, extra_cheese):
        self.size = size
        self.pepperoni = pepperoni
        self.extra_cheese = extra_cheese

    def usage(self):
        print("Provide a file with the following format: \n")
        print("First line - 1 letter with the pizza size: small (S), medium (M) or large (L)")
        print("Second line - add pepperoni (Y) or not (N)")
        print("Third line - add extra cheese (Y) or not (N)")

    def calculate_bill(self):

        bill = 0

        match self.size:
            case "S":
                bill += 15
            case "M":
                bill += 20
            case "L":
                bill += 25

        if (self.pepperoni == "Y" and self.size == "S"):
            bill += 2
        elif (self.pepperoni == "Y" and (self.size == "M" or self.size == "L")):
            bill += 3

        if (self.extra_cheese == "Y"):
            bill += 1

        print(f"Thank you for buying our pizza. The bill is: ${bill}")
        return bill


if __name__ == '__main__':

    with open("current_order.txt", "r") as f:

        try:
            size = f.readline().strip()
            pepperoni = f.readline().strip()
            extra_cheese = f.readline().strip()

            if (size not in valid_sizes or pepperoni not in valid_answers 
                or extra_cheese not in valid_answers):
                usage()
                sys.exit(2)
        except:
            raise ValueError("Provided values do not conform with expected ones")

    order = Order(size, pepperoni, extra_cheese)
    order.calculate_bill()