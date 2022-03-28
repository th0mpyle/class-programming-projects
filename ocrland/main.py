riders = 0
while riders != 8:
    try:
        height = input("height: ")
        if int(height) < 120:
            print("you are not allowed to ride.")
        elif int(height) < 140:
            while true:
                adultStatus = input("are you riding with an adult? y/n: ")
                if adultStatus.lower() == "n":
                    print("you are not allowed to ride.")
                    break
                elif adultStatus.lower() == "y":
                    print("you are allowed to ride.")
                    riders += 1
                    print("riders: " + str(riders))
                    break
                else:
                    print("error: bad input")

        elif int(height) > 269:
            print("error: bad input")
        else:
            print("you are allowed to ride")
            riders += 1
            print("riders: " + str(riders))

    except ValueError:
        print("error: bad input")
