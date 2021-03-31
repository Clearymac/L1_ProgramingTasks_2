#making the code input a var and makes sure retard enters a 4 digit code
code = int(input("Please enter a 4 digit code: "))

while code < 0 or code > 9999:
    code = int(input("Please enter a 4 digit code: "))
if code < 0 or code > 9999:
        print("Your mum suck me good and hard through my jorts")

print(code)

for hack in range(10000):
    if hack < 1000 and hack > 99:
        print("0{}".format(hack))
    if hack < 100  and hack > 9:
        print("00{}".format(hack))
    if hack < 10:
        print("000{}".format(hack))
    if hack > 999:
        print(hack)
        if code == hack and (code < 1000 and code > 99):
            print("0{}".format(code))
        if code == hack and (code < 100  and code > 9):
            print("00{}".format(code))
        if code == hack and code < 10:
            print("000{}".format(code))
        if code == hack and code > 999:
            print(code)
