# monthly_income = float(input("Enter your monthly income: "))
# monthly_savings = float(input("Enter your monthly savings: "))

# monthly_saving_rate = (monthly_savings / monthly_income) * 100

# print(f"Your monthly saving rate is: {monthly_saving_rate:.2f}%")

# if monthly_saving_rate > 10:
#     print("You are doing great!")
# else:
#     print("You need to save more!")


# in keyword in python

fe_developers = ["Mike", "John", "Anna"];
be_developers = ["Mike", "John", "Anna", "Bill", "Alex"];

student_name = input("Enter developer's name:")
if student_name in fe_developers and student_name in be_developers:
    print(f"{student_name} is a Full Stack Developer")
elif student_name in fe_developers:
    print(f"{student_name} is a Frontend Developer")
elif student_name in be_developers:
    print(f"{student_name} is a Backend Developer")
else:
    print(f"{student_name} is not a developer")
