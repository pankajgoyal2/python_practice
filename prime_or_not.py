num = int(input("Please enter the number. "))

factors = 0

for i in range(1, num + 1):
    if num % i == 0:
        factors += 1

prime = True

if factors > 2:
    prime = False

if not prime:
    print(num, "is composite")

else :
    print(num, "is prime")
