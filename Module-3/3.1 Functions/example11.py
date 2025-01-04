# keyword arguments 
def student(name,subject):
    print(f"name = {name}")
    print(f"subject = {subject}")

nameValue = input("Enter your name : ")
subjectValue = input("Enter subject : ")

student(subject=subjectValue,name = nameValue)


