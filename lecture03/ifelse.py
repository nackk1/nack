inchar = input("input one character:")
if inchar >= 'A' and inchar <= 'Z' :
    print("You in put Upper Case tetter ", inchar)
elif inchar >= 'a' and inchar <= 'z' :
    print("You in put lower Case tetter ", inchar)
elif inchar >= '0' and inchar <= '9' :
     print("You in put number ", inchar)
else :
     print("it's not a letter or number ", inchar)