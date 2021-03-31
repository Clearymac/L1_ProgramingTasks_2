code = int(input("Please enter a 4 digit code: "))

for hack in range(9999):
    print(hack)
    if hack == code:
        print("The code is {}".format(code))
        break
