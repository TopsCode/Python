url1 = "https://www.gmail.com"

url2 = "java.com"

url3 = "www.python"

if url1.startswith("https://") and url1.endswith(".com") or url1.endswith(".in"):
    print("secure url")
else:
    print("not secure url")

if url2.startswith("https://"):
    print("valid url")
else:
    print("invalid url")

