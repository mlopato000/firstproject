length = int(input("Введите длину:"))
# print("*" * length)
# for i in range(11):
#     print(i, end=" ")
for i in range(length):
    for j in range(i+1):
        print("*", end="")
    print()


