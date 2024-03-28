login = input()
user = {"name" : ["John","July","Sam"],
       "password" : [123123,456456,789789],
       "user_role" : ["admin","editor","viewer"]}

if login in user["name"]:
    psw = int(input())
    if psw in user["password"]:
        print("Pass")
        if login == "John" and psw == 123123:
            print("Full Access")
        elif login == "July" and psw == 456456:
            print("Edit Permission")
        elif login == "Sam" and psw == 789789:
            print("View Permission")
    else:
        print("Wrong Password")
else:
    print("Access Denied")