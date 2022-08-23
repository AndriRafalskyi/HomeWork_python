a = int(input("А:"))
b = int(input("Б:"))
c = int(input("В:"))

while a < b:
    print(a)
    a += c
    if a >= b:
        print(a)