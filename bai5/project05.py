for item in range(30, 300):
    if item % 7 == 0:
        if item % 13 == 0:
            print ("a-z")
        else:
            print ("abc")
    elif item % 13 == 0:
        print ("xyz")
    else:
        print (item)
