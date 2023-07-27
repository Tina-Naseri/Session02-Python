SL1 = float(input("What is your length of side 1? "))
SL2 = float(input("What is your length of side 2? "))
SL3 = float(input("What is your length of side 3? "))
if SL1 < SL2 + SL3 and SL2 < SL1 + SL3 and SL3 < SL1 + SL2:
    print ("You can draw a triangle with these lengths")
else:
    print ("You can't draw a triangle with these lengths")