number = int(input("Skriv in en siffra: "))

try:
    while number != 0:
        for i in range(11):
            total = number * i
            print("{} * {} = {}".format(number, i, total))

            if i == 10:
                number = int(input("Skriv in en siffra: "))
except:
    print("Det var ingen siffra")
