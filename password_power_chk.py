
password = input()
digit = False
upp = False
llow = False
if (len(password) >= 8):
    for i in password:
        if i.isdigit():
            digit = True
        elif i.upper():
            upp = True
        elif i.lower():
            llow = True
    if(digit == True) and (upp == True or llow == True):
        print("강함")
    else:
        print("약함")
else:
    print("약함")