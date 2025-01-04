# product 

# here, products is a main dictionary 
products = {
    # here, mobile is a nested dictionary 
    "mobile" : {
        "motorola" : {
            "ram" : 8,
            "camera"  : "50MP",
            "price" : 17999
        },
        "samsung galaxy s23" : {
            "ram" : 16,
            "camera" : "50MP",
            "price" : 47999
        }
    },
    "laptop" : {
        "lenovo ideapad" : {
            "specification" : "8GB RAM 128GB SSD",
            "price" : 31990
        },
        "DELL Inspiron 3520" : {
            "specification" : "8GB RAM 256GB SSD",
            "price" : 34690
        }
    }
}

# accessing nested dictionary 
#print(products["mobile"])
#print(products["mobile"]["motorola"]["camera"])

choice = int(input("Enter your choice for mobile type 1 and for laptop press 2 : "))
if choice == 1:
    #print(products["mobile"])
    for k in products["mobile"].keys():
        print(f"Product details of {k} ")
        print(f"ram : {products['mobile'][k]["ram"]}")   
        print(f"camera : {products['mobile'][k]["camera"]}")
        print(f"price : {products['mobile'][k]["price"]}")  
        print()        

        # same output like flipkart products (only designing missing)
else:
    print(products["laptop"])

# Task perform same for laptop details 

