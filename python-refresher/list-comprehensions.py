fe_developers = ["Mike", "John", "Anna", "Jake", "Jonny"];
be_developers = ["Mike", "Bob", "John", "Anna", "Bill", "Alex"];

lower_case_names = [fe_name.lower() for fe_name in fe_developers + be_developers]

for name in lower_case_names:
    print(name)

print("-----------------")

names_starts_with_j = [name for name in lower_case_names if name.startswith("j")]
names_starts_with_j_capitalize = [name.capitalize() for name in names_starts_with_j]
for name in names_starts_with_j_capitalize:
    print(name)
