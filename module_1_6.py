#2 словарь#
my_dict = {"Маргарита": 1654, "Павел": 1955, "Ирина": 1988}
print(my_dict)
print(my_dict["Маргарита"])
my_dict.update({"Алёна": 1999,
"Даниил": 2001})
print(my_dict)

print(my_dict)
a = my_dict.pop("Маргарита")
print(my_dict)
print(a)

print(my_dict)

#3 множество#
my_set = {1, 3, 4, 5, 1, 2, 4, 5, 3, 1}
print(my_set)

my_set = {1, 3, 4, 5, 1, 2, 4, 5, 3, 1, "Рита", True}
print(my_set)

my_set = {1, 3, 4, 5, 1, 2, 4, 5, 3, 1, "Рита", True}
print(my_set.discard("Рита"))
print(my_set)


