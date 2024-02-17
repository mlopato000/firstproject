# length = int(input("Введите длину:"))
# # print("*" * length)
# # for i in range(11):
# #     print(i, end=" ")
# for i in range(length):
#     for j in range(i + 1):
#         print("*", end="")
#     print()
# point = 10
# while point < 100:
#     point = (point + 1)
#     print(point)

car = ""
while car != "Exeed":
    car = input("Наш автомобиль :")

if car == "Exeed":
    print("Верно!")
