if __name__ == "__main__":
    riders = 0
    heightdataharvest = []
    while riders != 8:
        try:  # runs code if all inputs can be interpreted
            height = input("\nheight: ")
            heightdataharvest.append(height)
            if int(height) < 120:
                print("you are not allowed to ride.")
            elif int(height) < 140:
                while True:
                    adultStatus = input("are you riding with an adult? y/n: ")
                    if adultStatus.lower() == "n":
                        print("you are not allowed to ride.")
                        break
                    elif adultStatus.lower() == "y":
                        print("you are allowed to ride.")
                        if riders < 7:
                            riders += 2
                            print("your child/adult ticket costs £25.")
                        else:
                            print("however, we are full.")
                        print("riders: " + str(riders))
                        break
                    else:
                        print("error: bad input")
            elif int(height) > 269:
                print("error: bad input")
                # if they are an impossible height it don't let them in fr
            elif height == "your mum":
                print("you're always allowed to ride bbg")
            else:
                print("you are allowed to ride")
                print("your adult ticket costs £18")
                riders += 1
                print("riders: " + str(riders))
        except ValueError:  # if the type is wrong then the program breaks and repeats
            print("error: bad input")
    print("ride is full")

# all of this is pretty self explanatory innit
