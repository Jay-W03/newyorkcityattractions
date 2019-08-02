womenintech = ["Syeda", "Taylor", "Regi", "Sara", "Jayda"]

print(womenintech)
print(len(womenintech))
print("The length is", len(womenintech), "women.")

womenintech.insert(2,"Mia")
print(womenintech)

name = input("What name?")
if name in womenintech:
    print(name in womenintech)
    print ("Yes," ,name, " is in the list")
else:
    print("No," ,name, "is not in the list")
