import sys
encrypted = sys.argv[1]
everything = False

try:
    shift = int(sys.argv[2])
except IndexError as err:
    everything = True


la = "abcdefghijklmnopqrstuvwxyz"  # lower case alphabet
ua = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # upper case alphabet


def rotate(shift):
    flag = ""
    for x in encrypted:
        if x.isalpha():
            if x.islower():
                index = la.find(x)
                index = (index + shift) % 26
                flag += la[index]
            else:
                index = ua.find(x)
                index = (index + shift) % 26
                flag += ua[index]
        else:
            flag += x
    return flag


if everything:
    for i in range(26):
        print(f"ROT {i:2}\t", rotate(i))
else:
    print(rotate(shift))

