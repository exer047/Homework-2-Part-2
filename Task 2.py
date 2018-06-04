first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))
third_number = int(input("Enter third number: "))
if first_number == second_number or second_number == third_number or third_number == first_number:
    print(first_number + 5, second_number + 5, third_number + 5)
else:
    print("There are no equal numbers!")