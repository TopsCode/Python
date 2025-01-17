# here, phonebook is a dictionary 
phoneBook = {
    "harsh" : 77884455,
    "smith" : 78455465,
    "zeba" : 45457874,
}

print(phoneBook)
print(phoneBook.setdefault("zeba"))

print(phoneBook)

print(phoneBook.setdefault("Anjali",8888888))
print(phoneBook)