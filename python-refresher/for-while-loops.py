fe_developers = ["Mike", "John", "Anna"];
be_developers = ["Mike", "John", "Anna", "Bill", "Alex"];

# create list of full stack be_developers
full_stack_develpers = [dev for dev in fe_developers if dev in be_developers]

i = 0
while i < len(full_stack_develpers):
    print(full_stack_develpers[i])
    i = i + 1

print("----------------------")

for dev in full_stack_develpers:
    print(dev)
