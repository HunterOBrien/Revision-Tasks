pin = input("Please enter your 4 digit pin number: ")
while len(pin) != 4 or not pin.isnumeric():
    pin = input("Please enter your 4 digit pin number: ")
print(f"Your PIN is {pin}")
