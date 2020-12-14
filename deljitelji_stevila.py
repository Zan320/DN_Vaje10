st = int(input("Vpiši celo število: "))

i = 1
print("\nDelitelji: ")
while i <= st:
    if st % i == 0:
        print(i)
    i += 1