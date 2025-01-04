# JAY BHAVANI 

"""
expected output : 

{
    "vadapav" :{
        "qty" : 20,
        "price" : 30
    },
    "dabeli" :{
        "qty" : 40,
        "price" : 20
    },
    ...
}
"""
stock = {} # main dictionary 

status = True 
m_status = True 

menu = """
                        MENU 

                press 1 for product manager 
                press 2 for customer
        """
while status:
    print(menu)
    choice = int(input("Enter your choice : "))
    if choice == 1:
        print("MANAGER ACCOUNT")

        while m_status:
            print("Enter your stocks")
            subdictionary = {}  # blank nested dictionary 

            product_name = input("Enter your product : ")
            product_qty = int(input("Enter product qty : "))
            product_price = int(input("Enter product price : "))

            subdictionary["qty"] = product_qty
            subdictionary['price'] = product_price
            subdictionary["total"] = product_qty * product_price

            print("----> subdictionary ",subdictionary)

            stock[product_name] = subdictionary

            print("----> maindictionary ",stock)

            # display stock 

            for k,v in stock.items():
                #print(v)
                print(f"{k}  Qty. {v["qty"]}  Price : 1 X Rs. {stock[k]["price"]}  Total : Rs. {subdictionary['total']}")

            m_exit = input("do you want to add more stocks press 'y' for yes and press 'n' for no : ").lower() 
            if m_exit == 'n' or m_exit == 'no':
                m_status = False
            

    elif choice == 2:
        print("CUSTOMER ACCOUNT")
    else:
        print("INVALID INPUT !!!")

    exit = input("do you want to continue press 'y' for yes and press 'n' for no : ").lower() 
    if exit == 'n' or exit == 'no':
        status = False
    