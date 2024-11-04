number = 32
if number >= 20:
    print("Number is greater than 20.")


number = 12
if number >= 20:
    print("Number is greater than 20.")
else:
    print("Number is less than 20.")


marks = 75
if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
else:
    print("Grade: D")

number = 10
if number > 15:
    print(number, "greater than 15")
elif number > 5:
    print(number, "greater than 5 but less than or equal to 15")
elif number == 10:
    print(number, "is exactly 10")


number = 10
number_2 = 20
if number > 5:
    if number_2 > 15:
        print(number, "greater than 5 and ", number_2, "is greater than 15")
    else:
        print(number, "greater than 5 but ", number_2, "is not greater than 15")
else:
    print(number, "is 5 or less")


number_1 = 15
number_2 = 25
if number_1 > 9 and number_2 > 18:
    print(number_1, "is greater than 9 and ", number_2, "is greater than 18")

number_1 = 15
number_2 = 12
if number_1 > 9 or number_2 > 18:
    print(number_1, "is greater than 9 and ", number_2, "is less than 18")

