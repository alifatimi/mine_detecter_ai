#imports
import joblib

#load model
model = joblib.load('D:\\Projects\\mine detecter proj\\mine_model.joblib')

#functions
def get_Volts():
    while True:
        try:
            user_input = float(input("Input the voltage the FLC sensor is outputting(range is 0v to 1v): "))
            if 0 <= user_input <= 1:
                return user_input
            else:
                print("The number is not between 0 and 1. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a float between 0 and 1.")
def get_SoilType():
    while True:
        try:
            user_input = int(input("Input the soil type of the area(1:Dry and Sandy,2:Dry and Humus,3:Dry and Limy,4:Humid and Sandy,5:Humid and Humus,6:Humid and Limy):"))
            if 1 <= user_input <= 6:
                return user_input
            else:
                print("The number is not between 1 and 6. Please try again.")
        except ValueError:
            print("Invalid input. Please enter an integer between 1 and 6.")
def get_height():
    while True:
        try:
            user_input = float(input("Input the height of sensor(range is 0m to 1m): "))
            if 0 <= user_input <= 1:
                return user_input
            else:
                print("The number is not between 0 and 1. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a float between 0 and 1.")
def main_program():
    print("Welcome to the Magnetic Anomaly based Mine detector(accuracy is 94%)")
    volts = get_Volts()
    height = get_height()
    soil_type = get_SoilType()

    answer = model.predict([[volts,height,soil_type]])
    if answer == 0:
        print("There is no mine in the area!")
    elif answer == 1:
        print("There is a mine in the area!")
    


#start program
while True:
    main_program()
    ans = input("Press 1 to quit,press Enter to restart")
    if ans == "1":
        break
    else:
        continue
