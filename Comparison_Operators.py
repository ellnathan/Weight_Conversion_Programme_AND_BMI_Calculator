# Collecting the user's name
while True:
    name = input("What is your name? ")
    if len(name) <= 1:
        print("Name cannot be 1 character long")
    elif len(name) >= 20:
        print("Name cannot be longer than 20 characters")
    else:
        print("Name meets requirements, please continue")
        break

print()  # Creating space

# Collect user's surname
while True:
    last_name = input("What is your surname? ")
    if len(last_name) <= 1:
        print("Surname cannot be 1 character long")
    elif len(last_name) >= 20:
        print("Surname cannot be longer than 20 characters")
    else:
        print("Surname meets requirements, please continue")
        break

print()

# Collecting the user's age
while True:
    age = input("How old are you? ")

    if age.isnumeric():  # Check if the input consists of numerical values
        age = int(age)
        if 18 <= age < 120:  # Assuming a reasonable age range
            break
        elif age < 18:
            while True:
                response = input("You need to be over 18 to complete this form. If you are not over 18, please enter 'no'. If you entered the wrong age, enter 'yes' to try again: ")
                if response.lower() == 'no':
                    print("Thank you for using the form.")
                    exit()  # Exit the code if the user is not over 18
                elif response.lower() == 'yes':
                    break  # Ask for the age input again
                else:
                    print("Invalid response. Please enter 'yes' or 'no'.")
        else:
            print("Please enter an age between 18 and 119 (inclusive).")
    else:
        print("Please enter a numerical age.")


print()

# Collect user's email
while True:
    email = input("What is your email address? ")
    if "@" in email and "." in email:
        break
    else:
        print("Invalid email format. Please enter a valid email address.")

print()

# Show the user all the information they inputted
print(f'Thank you for providing your information:')
print(f'Name: {name} {last_name}')
print(f'Age: {age}')
print(f'Email: {email}')
