while True:
    print()

    print('Hello, you can use this calculator to compare your weight in Kilos (kg) or Pounds (lbs)')
    print('Please enter your weight below in either kg or lbs and follow the instructions')

    print()

    weight = float(input('Weight: '))
    unit = input('(K)g or (L)bs: ')

    if unit.upper() == "L":
        weight_kg = weight * 0.45
        weight_kg = round(weight_kg, 2)
        print(f'You are {weight_kg} kilograms (kg)')

    elif unit.upper() == "K":
        weight_pounds = weight // 0.45
        weight_pounds = round(weight_pounds, 2)
        print(f'You are {weight_pounds} pounds (lbs)')

    print()

    while True:
        calculate_bmi = input('Would you like to calculate your BMI (yes/no)? ')

        if calculate_bmi.lower() == 'yes' and unit.upper() == 'L':
            print('To find out your BMI, please enter your height in meters (m):')
            height_m = float(input('What is your height (m): '))
            # Calculate BMI using the formula (weight_kg / height_m / height_m) * 10000
            bmi = (weight_kg / (height_m ** 2)) * 10000
            print(f'Your BMI is: {bmi:.2f}')

            # bmi_classification
            if calculate_bmi.lower() == 'yes':
                if bmi < 18.5:
                    print('You are Underweight')
                elif 18.5 <= bmi < 25:
                    print('You are in the Healthy Weight range')
                elif 25 <= bmi < 30:
                    print('You are Overweight')
                else:
                    print('You are Obese')

        elif calculate_bmi.lower() == 'yes' and unit.upper() == 'K':
            print('To find out your BMI, please enter your height in meters (m):')
            height_m = float(input('What is your height (m): '))
            # Calculate BMI using the formula (weight_kg / height_m / height_m) * 10000
            bmi = (weight_pounds / 2.205) / (height_m ** 2) * 10000

            # bmi_classification
            if calculate_bmi.lower() == 'yes':
                if bmi < 18.5:
                    print('You are Underweight')
                elif 18.5 <= bmi < 25:
                    print('You are in the Healthy Weight range')
                elif 25 <= bmi < 30:
                    print('You are Overweight')
                else:
                    print('You are Obese')

        elif calculate_bmi.lower() == 'no':
            print('Thank you for using the tool')
            break

        else:
            print('Please answer yes or no to use the weight conversion and BMI calculator')

    continue_to_next = input('Would you like to calculate again with a different weight (yes/no)? ')
    if continue_to_next.lower() != 'yes':
        break
