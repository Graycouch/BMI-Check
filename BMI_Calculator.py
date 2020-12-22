height_Meters = float(input("Enter your height in meters: "))
weight_Kilos = float(input("Enter your weight in kilograms: "))
BMI = weight_Kilos / height_Meters ** 2

if height_Meters <= 0 or weight_Kilos <= 0:
    print('Invalid height or weight value')
else:
    print('Your BMI is {:.2f}'.format(BMI))

    if 0 < BMI < 18.5:
        print('You are Underweight')
    elif 18.5 <= BMI < 25:
        print('You are Normal')
    elif 25 <= BMI < 30:
        print('You are Overweight')
    else:
        print('You are Obese')