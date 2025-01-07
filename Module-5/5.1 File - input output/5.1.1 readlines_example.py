f = open("myfile.txt","r")

data = f.readlines() 

print(data)

for f in data:
    print(f)