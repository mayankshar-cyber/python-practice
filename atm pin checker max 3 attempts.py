# atm pin checker max 3 attempts


max_tries=3
attempts=0
while True:
    pin=int(input("enter your pin:"))
    atm_pin=3434
    attempts=attempts+1
    remaining=max_tries-attempts
    if atm_pin !=pin:
        print("incorrect pin",remaining,"attempt left")
        if remaining==0:
            print("you're account have been locked , please contact your branch.")
            break
    else:
        print("congratualation, you have entered the correct pin.")
        break