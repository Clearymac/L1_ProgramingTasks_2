#making the code input a var
code = int(input("Please enter a 4 digit code: "))

for hack in range(9999):
    if hack < 1000 and hack > 99:
        print("0" + hack)
    if hack < 100  and hack > 9:
        print("00" + hack)
    if hack < 10:
        print("000" + hack)
    if hack > 999:
        print(hack)
    if hack == code:
        print("The code is {}".format(code))
        break
