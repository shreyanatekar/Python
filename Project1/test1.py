# A first Python script
address = ["abc path", "apt 123", "New York"]
pins = {"Mike":1234, "Jack":2222, "Ann":3333}

pin = int(input("Enter your pin: "))

def find_in_file(f):
    myFile = open("Sample.txt")
    fruits = myFile.read()
    fruits = fruits.splitlines()
    if f in fruits:
        return "That fruit is in the file"
    else:
        return "Fruit not in the file "

if pin in pins.values():
    fruit = input("Enter fruit: ")
    print(find_in_file(fruit))
else:
    print("Incorrect pin.")
    print("Only these can access the file: ")
    for key in pins.keys():
        print(key)

