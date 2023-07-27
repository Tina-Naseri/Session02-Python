name = input("Please enter you name: ")
family = input("Please enter you family: ")
print ("Hello Dear", name, family)
mark1 = float(input ("What is your mark of lesson 1? "))
mark2 = float(input ("What is your mark of lesson 2? "))
mark3 = float(input ("What is your mark of lesson 3? "))
avg = (mark1 + mark2 + mark3) / 3
if avg >= 17:
    print ("Your Average is: ", avg, "and your Status is: GREATE")
if avg < 17 >= 12:
    print ("Your Average is: ", avg, "and your Status is: NORMAL")
if avg < 12:
    print ("Your Average is: ", avg, "and your Status is: FAIL")