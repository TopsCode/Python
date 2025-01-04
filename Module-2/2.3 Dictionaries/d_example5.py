#nested dictionary :::

# dictionary inside the dictionary 

quiz = {
    1 : {
        #key  : value
        "que" : "who is most popular cricketer ?",
        "ans" : "ms dhoni"
    },
    2 : {
        "que" : "which programing language is most popular ?",
        "ans" : "python"
    },
    3 : {
        "que" : "who is prime minister of india ?",
        "ans" : "narendra modi"
    }
}
#print(quiz)
"""
print(quiz[2])
print("----------")
print(quiz[2]["que"])
myans = input("ENter your ans : ")

if myans == quiz[2]["ans"]:
    print("right answer")
else:
    print("wrong answer")
"""
for i in range(1,len(quiz)+1):
    print(f"({i}) {quiz[i]['que']}")
    myans = input("Enter your ans : ")
    if myans == quiz[i]["ans"]:
        print("right answer")
    else:
        print("wrong answer")
    print()