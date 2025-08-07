print("[-----------PYHUB-------2025----------]")
print("----PYHUB BY NATIONAL MINISTRY OF REVENUE------")
name=""
age=0
address=""
dob=0
password=0
def sign_up():
    global name,age,address,dob,password
    print("---------Welcome To PYHUB Services By Indian Government----")
    print("---Best Quality Goods And Services Online Here With Trust---")
    name=input("Enter Your Name : ")
    print("Age 18 Or above are Allowed To Buy In PYHUB--2025---")
    age=int(input("Enter Your Age : "))
    if age>=18 :
        print("Eligible For Services")
        address=input("Town/City You Live : ")
        dob=int(input("Enter Your DOB In DDMMYEAR Format : "))
        print("Look , For Security And End To End Encryption DOB Is The Passkey To You")
        password=int(input("Enter A  Integer Password : "))
        print("DOB And Password Are The Login Credentials To You")
        print("Carefully Enter The Password In Every Stage")
        print("Print Your Profile , Sign Up Succesfully Done")
    else :
        print("You Do Not Met The Age Recommendations yet , Try Again later")
def profile():
    safety1=int(input("Enter Your DOB : "))
    safety2=int(input("Enter Your Password : "))
    if safety1==dob and safety2==password :
        print("Access Granted ")
        if age>=18 :
            print("Age Access Verified ")
            print("[[[[_--PYHUB 2025--__]]]]")
            print("^^^^CUSTOMER PROFILE^^^^ : ")
            print(f"Customer Name : {name}")
            print(f"Customer Age : {age}")
            print(f"Customer City : {address}")
            print(f"Customer DOB : {dob}")
            print(f"___---__--PYHUB 2025--__---___")
        else :
            print("No Profile Generated , Close The Window")
    else :
        print("Access Denied")

customer_choices=[]
customer_nums=[]
bill=0
nums=0
category=""
def booking():
    global customer_choices,customer_nums,bill,nums,category
    safety1=int(input("Enter Your DOB : "))
    safety2=int(input("Enter Your Password : "))
    if safety1==dob and safety2==password :
        print("Access Granted ")
        if age>=18 :
            print("Age Access Granted ")
            print("PYHUB BOOKING INSTRUCTIONS :")
            print("1. There Will Be 3 Categories Groceries,Sports,Electronics")
            print("2.You Have To Select One from Lists And Input Unit To It")
            print("3.The Cost Will Be Calculated As Per Category Wise")
            print("4.Finally You Have To Print That Bill For Further Use")
            print("5.Bill Will Be Generated Once Only , Make Sure You Save It ")
            categories_list=["Electronics","Groceries","Sports"] #all small letters only
            print("For Check Up And Cross Checking")
            print(categories_list)
            category=input("Out Of 3 Which Category ? : ")
            if category.lower()=="groceries" :
                groceries_list= [
    "Rice", "Wheat Flour", "Sugar", "Salt", "Toor Dal", "Urad Dal", "Chana Dal",
    "Cooking Oil", "Ghee", "Milk", "Curd", "Tea Powder", "Coffee Powder",
    "Biscuits", "Bread", "Eggs", "Chicken", "Mutton", "Fish", "Onions",
    "Tomatoes", "Potatoes", "Carrots", "Beans", "Green Peas", "Spinach",
    "Apples", "Bananas", "Oranges", "Mangoes"
]

                groceries_prices= [
    50, 45, 40, 20, 100, 110, 90,
    130, 500, 50, 40, 200, 400,
    30, 25, 6, 180, 600, 250, 30,
    25, 20, 40, 45, 60, 20,
    120, 40, 80, 150
]
                print(groceries_list)
                print("Enter Items As In The Display ")
                pref=input("Enter Item Name : ")
                num=int(input("Enter How Many Units Needed : "))
                deci=input("Will You Buy More ? yes/no : ")
                customer_choices.append(pref)
                customer_nums.append(num)
                while deci.lower()=="yes":
                    pref=input("Enter Item Name : ")
                    num=int(input("Enter How Many Units Needed : "))
                    deci=input("Will You Buy More yes/no ? : ")
                    customer_choices.append(pref)
                    customer_nums.append(num)
                print(customer_choices)
                print("Cross Checking Purpose")
                for x in customer_choices :
                    index=groceries_list.index(x)
                    price=groceries_prices[index]
                    list2=customer_choices.index(x)
                    nums=customer_nums[list2]
                    bill+= price * nums
                print(bill)
            elif category.lower()=="electronics" :
                electronics_list= [
    "Smartphone",
    "Laptop",
    "Bluetooth Speaker",
    "Smart Watch",
    "Wireless Earbuds",
    "Tablet",
    "Power Bank",
    "LED Monitor",
    "Portable Hard Drive",
    "Wireless Mouse"
]
                electronics_prices= [
    30000,   # Smartphone
    60000,   # Laptop
    2999,    # Bluetooth Speaker
    9999,    # Smart Watch
    1999,    # Wireless Earbuds
    55000,   # Tablet
    8500,    # Power Bank
    8499,    # LED Monitor
    4499,    # Portable Hard Drive
    999      # Wireless Mouse
]
                print(electronics_list)
                print("Enter Items As per Display")
                pref=input("Enter Item Name : ")
                num=int(input("Enter How Many Units Needed : "))
                deci=input("Wanna Add ? : ")
                customer_choices.append(pref)
                customer_nums.append(num)
                while deci.lower()=="yes":
                    pref=input("Enter Item Name : ")
                    num=int(input("Enter How Many Units Needed : "))
                    deci=input("Wanna Add ? : ")
                    customer_choices.append(pref)
                    customer_nums.append(num)
                print(customer_choices)
                print("Cross Checking Purpose")
                for x in customer_choices :
                    index=electronics_list.index(x)
                    price=electronics_prices[index]
                    list2=customer_choices.index(x)
                    nums=customer_nums[list2]
                    bill+= price * nums
                print(bill)
            elif category.lower()=="sports" :
                sports_list = [
    "Football",
    "Cricket Bat",
    "Badminton Racket",
    "Tennis Ball Pack",
    "Skipping Rope",
    "Yoga Mat",
    "Basketball",
    "Gym Gloves",
    "Water Bottle (Sports)",
    "Dumbbells (Pair)"
]

                sports_prices = [
    4099,     # Football
    6000,    # Cricket Bat
    8999,     # Badminton Racket
    3499,     # Tennis Ball Pack
    1999,     # Skipping Rope
    999,     # Yoga Mat
    1500,     # Basketball
    500,     # Gym Gloves
    999,     # Water Bottle (Sports)
    2000      # Dumbbells (Pair)
]
                print(sports_list)
                print("Enter Items As Per Display ONLY")
                pref=input("Enter Item Name : ")
                num=int(input("Enter How Many Units Needed : "))
                deci=input("Wanna Add ? : ")
                customer_choices.append(pref)
                customer_nums.append(num)
                while deci.lower()=="yes":
                    pref=input("Enter Item Name : ")
                    num=int(input("Enter How Many Units Needed : "))
                    deci=input("Wanna Add ? : ")
                    customer_choices.append(pref)
                    customer_nums.append(num)
                print(customer_choices)
                print("Cross Checking Purpose")
                for x in customer_choices :
                    index=sports_list.index(x)
                    price=sports_prices[index]
                    list2=customer_choices.index(x)
                    nums=customer_nums[list2]
                    bill+= price * nums
                print(bill)
            else :
                print("No Items Matched Your Search")
                print("Billing Not Possible Cancel Your Billing Request")
        else:
            print("Age Synchronisation Failed")
            print("Do Not Try For Billing Not Possible ")
final_price=0
tax=0.0
def billing():
    global final_price,tax
    safety1=int(input("Enter Your DOB : "))
    safety2=int(input("Enter Your Password : "))
    if safety1==dob and safety2==password :
        print("Access Granted ")
        if age>=18 :
            estimation=bill
            print(f"Estimation = {estimation}")
            #Taxes Section
            if category.lower()=="electronics":
                tax=0.25
            elif category.lower()=="sports":
                tax=0.10
            else :
                print("No Tax for These products")
                tax=0.00
            final_price=bill*tax + bill 
            print(final_price)

            print("---------PYHUB ---INDIA-----2025--------")
            print("[PYHUB[BY -----INDIAN GOVERNMENT------]]")
            print("---------------BILLING SECTION-----------")
            print("-------------------------------------------")
            print(f"---CUSTOMER NAME = {name}")
            print(f"---CITY FOR DELIVERY = {address}")
            print("PYHUB DIRECT AFFILLIATION WITH INDIAN GOVERNMENT")
            print("-------------------------------------------------")
            print(f"--------{customer_choices}-----------------")
            print(f"--------{customer_nums}---------------------")
            print("Correspondance Maintained In Above Billing")
            print(f"-----ESTIMATION COST = {bill}---------------")
            print(f"-----------TAX PERCENTAGE = {tax}-----------")
            print(f"-----FINAL PRICE COSTS AFTER ADDING TAXES DISPLAYED BELOW-----")
            print(f"FINAL PRICE TO BE PAID -------------------")
            print(f"-----------------------{final_price}----------------")
            print("Instructions :")
            print("1. This Is A One Time Generated Bill , Store It Immediately")
            print("2. If This Bill Is Not Restored You Cannot Access It From Online")
            print('3. This Bill Has The Power Inbuilt For Free Road Transportation All Over India')
            print("4. Issues Made And Returning Of The Object Shall Be Done Within A Week")
            print("5. Govt Officers Shall Produce Proofs How This Amount Is Been Purchase Use")
            print("6. For Groceries This Bill Might Not Seem Official")
            print("7. PYHUB Is Generally A Hub Of Electronics And Sports")
            print("8. Make Use Of This And To Certify The Production")
        else:
            print("Pay Fine For Using This Without Age Restriction")
    else:
        print("Authentication failed")
input2=""      
def payment():
    global input2
    safety1=int(input("Enter Your DOB : "))
    safety2=int(input("Enter Your Password : "))
    if safety1==dob and safety2==password :
        print("Access Granted ")
        if age>=18 :
            print("Age Access Verified")
            print("We Are Entering Payment Section")
            print("----Please Be Careful In This Section----")
            print("---Note That You Enter Your Passwords Correct----")
            print("Important Instructions :")
            print("1.Users Shall Read And Abide The Instructions")
            print("2.Higher Amounts Are Not Allowed For Personal Booking")
            print("3.To Book Higher Amounts For Industry Purpose You Need To Enter ")
            print("Company Name To Prove Your Authentication")
            print("4.The Limit For Personal Booking Is 3,00,000 Only")
            print("----------INSTRUCTIONS CLOSED-----------------")
            if final_price <= 300000 :
                print("You Are Eligible For Personal Booking ")
                print(f"Bill To Be Paid = {final_price}")
                print("Enter Your Password To Proceed Payment")
                input1=int(input("Enter Your Password : "))
                if input1==password :
                    print("Authentication Succesfully Verified")
                    print(f"Payment Succesful Of {final_price}Rs/-")
                    print("Thanks For Choosing PYHUB-2025 Services")
                    print("---Hoping You Get Back Soon---")
                else :
                    print("Authentication Failed")
            if final_price > 300000 :
                print("-You Are Eligible For Industry Based Services Only")
                print("-You Need To Enter A Valid Company Name Behalf Whom")
                print("You Are Purchasing Goods")
                company_list=["DMART","VIJAY SALES","BAJAJ ELECTRONICS","RELIANCE DIGITAL","SPORTS HUB","SAMSUNG DIGITAL","APPLE STORE","SONOVISION"]
                print("The Following Companies Are Accepted In The PYHUB-2025 ")
                print(company_list)
                print("Enter Your Company Behalf Your Purchase")
                input2=input("Company Name From The Display : ")
                idx=company_list.index(input2)
                if idx>=0 :
                    print("Company Access Accepted")
                    print(f"You Need To Pay The Bill Of {final_price}Rs/-")
                    print(f"Behalf Of {input2}")
                    print("Enter The Password To Continue With Payment")
                    nums=int(input("Enter Your Password : "))
                    if nums==password :
                        print("Authentication Matched")
                        print(f"Payment Succesfully of {final_price} Done")
                        print("Thanks For Choosing PYHUB-2025")
                        print("Hope You Visit Us Again")
                    else :
                        print("Authentication failed")
                else :
                    print("Enter A Valid Company Name")
        else :
            print("AGE ACCESS FAILED")
    else :
        print("Authentication Failed")
def statement():
    safety1=int(input("Enter Your DOB : "))
    safety2=int(input("Enter Your Password : "))
    if safety1==dob and safety2==password :
        print("Access Granted ")
        if age>=18 :
            print("Age Access Granted")
            print("--------------------PYHUB-2025-----------------")
            print("-------------STATEMENT OF PURCHASE-------------")
            print(f"Customer Name = {name}")
            print("-----------------------------ITEMS PURCHASED----")
            print(f"-------{customer_choices}-----------------")
            print(f"------Net Quantity = {customer_nums}----------")
            print(f"------------CITY OF DELIVERY = {address}-----")
            print(f"-------------------------------------------------")
            print(f"--ESTIMATION PRICE = {bill} Rs/- ----------------")
            print(f"----------TAXES APPLIED PERCENTAGE = {tax}-----")
            print(f"--------------FINAL BILLING SECTION----------------")
            print(f"Final Bill To Be Paid = {final_price}Rs/- ------------")
            print("Complete Product And Management Systems Abide Govt Rules")
            if final_price > 300000 :
                print(f"Company Name Behalf The Purchase = {input2}")
                print(f"The Company {input2} Is Responsible For The Transaction")
            else :
                print("Personal Booking Process ")
                print("Verified Booking Systems And GreenLit The Procedure")
        else :
            print("Age Access Denied")
    else :
        print("Authentication Failed")
def exit():
    print("-------------PYHUB-2025----------------")
    print("Hope You Visit The Store Again")
    print("Wishing You All The Best And Thanking You Once Again")
    print("PROGRAMME TERMINATED")
    print("THE END-------")

sign_up()
profile()
booking()
billing()
payment()
statement()
exit()
    

        

           




        
    



                



    














    








