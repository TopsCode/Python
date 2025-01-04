d = {
    "name" : "AAA",
    "subject" : "Python",
    "framework" : ["django","flask"],
    "score" : 78
}

# accessing dictionary elements 
# print(d["name"])
# print(d.get("name"))
# print(d["framework"])

# for item in d["framework"]:
#     print(item)

# for keys only   using of keys() method 
# for k in d.keys():
#     print(k)

# for values only   using of values() method 
# for v in d.values():
#     print(v)


# fetch both keys and values  using of items() method 
for k,v in d.items():
    print(f"key = {k}  value = {v}")


