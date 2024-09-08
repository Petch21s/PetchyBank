import os
from datetime import date
import re
import datetime
import time

def timenow():
    data = datetime.datetime.now()
    time = data.time()
    data = f'{data.day}/{data.month}/{data.year}'
    return data

def splash():
    folder1 = "Statement"
    root = "."
    state_ment = f"{root}/{folder1}"
    try :
        os.makedirs(state_ment)
    except:
        pass

    folder2 = "AccountData"
    root = "."
    state_ment = f"{root}/{folder2}"
    try :
        os.makedirs(state_ment)
    except:
        pass

    print("██████╗ ███████╗████████╗ ██████╗██╗  ██╗██╗   ██╗        ██████╗  █████╗ ███╗   ██╗██╗  ██╗")
    print("██╔══██╗██╔════╝╚══██╔══╝██╔════╝██║  ██║╚██╗ ██╔╝        ██╔══██╗██╔══██╗████╗  ██║██║ ██╔╝")
    print("██████╔╝█████╗     ██║   ██║     ███████║ ╚████╔╝         ██████╔╝███████║██╔██╗ ██║█████╔╝ ")
    print("██╔═══╝ ██╔══╝     ██║   ██║     ██╔══██║  ╚██╔╝          ██╔══██╗██╔══██║██║╚██╗██║██╔═██╗ ")
    print("██║     ███████╗   ██║   ╚██████╗██║  ██║   ██║           ██████╔╝██║  ██║██║ ╚████║██║  ██╗")
    print("╚═╝     ╚══════╝   ╚═╝    ╚═════╝╚═╝  ╚═╝   ╚═╝           ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝")
    print("- Make by Phestsuwaphat Thongsuk -".center(92))
    time.sleep(2)
    os.system('cls')

def acces_folder(foldername,textname):
    root = "."
    file = foldername
    path = f'{root}/{file}'
    textflie = textname
    folder = os.path.join(path,textflie)
    return folder

def calculateAge(birthDate):
    days_in_year = 365.2425   
    age = int((date.today() - birthDate).days / days_in_year)
    return age

def validate():   
  
    CRED = '\033[91m'
    CEND = '\033[0m'
    password = input("Enter your password: ") 
    while len(password) < 6 or len(password) > 16 or not re.search("[a-z]",password)\
        or not re.search("[A-Z]",password) or not re.search("[!@#$%^&*.]",password)\
        or re.search("\s",password) or not re.search("[0-9]",password) :
        print()
        if len(password) < 6 :
            print(CRED+"Minimum length 6 characters."+CEND)

        if len(password) > 16 :
            print(CRED+"Maximum length 16 characters."+CEND)

        if not re.search("[a-z]",password):
            print(CRED+"At least 1 letter between [a-z]."+CEND)

        if not re.search("[A-Z]",password):
            print(CRED+"At least 1 letter between [A-Z]."+CEND)

        if not re.search("[!@#$%^&*.]",password):
            print(CRED+"At least 1 character from [!@#$%^&*]."+CEND)

        if re.search("\s",password):
            pass

        if not re.search("[0-9]",password) :
            print(CRED+"At least 1 number between [0-9]."+CEND)

        print()
        password = input("Enter your password: ")
    return password
        
def register(): #Import datetime
    CRED = '\033[91m'
    CEND = '\033[0m'

    file = acces_folder("AccountData","Amount")
    with open(file+".txt","a+") as file_ :
        pass
    with open(file+".txt","r") as file_ :
        list = []
        data = file_.readlines()
        for i in data :
            x = i.split()
            list.append(x[0])
        count_acc = len(list)
    
        ACCOUNT_ID = 1000000001 + count_acc
        ACCOUNT_NUMBER = str(ACCOUNT_ID)
        ACCOUNT_ID = ACCOUNT_NUMBER[0:3]+"-"+ACCOUNT_NUMBER[3:6]+"-"+ACCOUNT_NUMBER[6:10]
        balance    = 0.00

    fname = "?"
    while True :
        template("Register Menu")
        print()
        #fname = "Phestsuwaphat"
        #lname = "Thongsuk"
        fname = "?"
        while True :
            fname = input("Enter your firtname: ").capitalize().strip().replace(" ","")
            if not fname.isalpha():
                print(CRED+"\nSorry, your firtname must be alphabet."+CEND)
                ask = input(">>> Do you want to try again? (Y - Yes / N - No):").lower().strip()
                print()
                if ask == "y" or ask == "yes" :
                    pass

                elif ask == "n" or ask == "no":
                    os.system('cls')
                    return
                    
                else :
                    print(CRED +"Invalid menu, Please try agian later." + CEND)
                    time.sleep(1.5)
                    os.system('cls')
                    return
                
            else :
                break

        lname = "?"
        while True :
            lname = input("Enter your lastname: ").capitalize().strip().replace(" ","")
            if not lname.isalpha():
                print(CRED+"\nSorry, your lastname must be alphabet."+CEND)
                ask = input(">>> Do you want to try again? (Y - Yes / N - No):").lower().strip()
                print()
                if ask == "y" or ask == "yes" :
                    pass

                elif ask == "n" or ask == "no":
                    os.system('cls')
                    return
                    
                else :
                    print(CRED +"Invalid menu, Please try agian later." + CEND)
                    time.sleep(1.5)
                    os.system('cls')
                    return
                
            else :
                break

        name = fname+" "+lname
        print('\nAre you sure too use this name? "'+name+'"')
        ask = input(">>> Confirm or not?? (Y - Yes / N - No):").lower().strip()
        print()
        if ask == "y" or ask == "yes" :
            break
        elif ask == "n" or ask == "no" :
            print("Did you want to try agian ?")
            ask1 = input(">>> Confirm or not?? (Y - Yes / N - No):").lower().strip()
            if ask1 == "y" or ask1 == "yes" :
                pass
                os.system('cls')
            elif ask1 == "n" or ask1 == "no" :
                os.system('cls')
                return
        else :
            #print(CRED + "Error, does not compute!" + CEND)
            print(CRED +"Invalid menu, Please try agian later." + CEND)
            time.sleep(1.5)
            os.system('cls')
            return

    id = "?"
    while True :
        id = input("Enter your ID-Card (13 digits): ")
        #id = "1234567890123"
        file = acces_folder("AccountData","Amount")
        with open(file+".txt","r") as _file :
            data = _file.readlines()
            list = []
            for i in data :
                x = i.split()
                list.append(x[1])

        if id in list :
            print(CRED + "this ID is alredy have"+ CEND)
            time.sleep(1.5)
            os.system('cls')
            return

        elif len(id) != 13 or not id.isnumeric() :
            print(CRED + "\nSorry, ID must have 13 digits"+ CEND)
            print("Did you want to try agian? ")
            ask = input(">>> Confirm or not?? (Y - Yes / N - No):").lower().strip()
            print()
            if ask == "y" or ask == "yes" :
                pass
            elif ask == "n" or ask == "no":
                os.system('cls')
                return
            else :
                print(CRED +"Invalid menu, Please try agian later." + CEND)
                time.sleep(1.5)
                os.system('cls')
                return
        else :
            break 

    day = "?" 
    while True :
        try :
            day = int(input("Enter day of birth: "))
            #day = 26
        except :
            print(CRED+ "\nSorry, please make the correct entry."+ CEND)
            time.sleep(1.5)
            os.system('cls')
            return 
        
        if day > 31 :
            print(CRED + "\nSorry, Please enter your day of birth correctly."+ CEND)
            ask = input(">>> Do you want to try again? (Y - Yes / N - No):").lower().strip()
            print()
            if ask == "y" or ask == "yes":
                pass
            elif ask == "n" or ask == "no":
                os.system('cls')
                return
            else :
                print(CRED +"Invalid menu, Please try agian later." + CEND)
                time.sleep(1.5)
                os.system('cls')
                return
        else :
            break 

    month = "?"
    while True :
        try :
            month = int(input("Enter month of birth: "))
        except :
            print(CRED + "\nSorry, Please enter your date of birth correctly."+ CEND)
            time.sleep(1.5)
            os.system('cls')
            return
        
        if month > 12 :
            print(CRED + "\nSorry, Please enter your month of birth correctly."+ CEND)
            ask = input(">>> Do you want to try again? (Y - Yes / N - No):").lower().strip()
            print()
            if ask == "y" or ask == "yes" :
                pass
    
            elif ask == "n" or ask == "no" :
                os.system('cls')
                return
            else :
                print(CRED +"Invalid menu, Please try agian later." + CEND)
                time.sleep(1.5)
                os.system('cls')
                return
        else :
            break
    
    today = date.today()
    this_year = datetime.date.today().year
    
    year = "?"
    while True :
        try :
            year = int(input("Enter year of birth(AD): "))
            
        except :
            print(CRED + "\nSorry, Please enter your year of birth correctly."+ CEND)
            time.sleep(1.5)
            os.system('cls')
            return
        if year > this_year or year <= 1900 :
            print(CRED + "\nSorry, you need to enter the correct year of birth(AD).\n"+ CEND)
            ask = input(">>> Did you wanna try agian?? (Y - Yes / N - No):").lower().strip()
            print()
            if ask == "y" or ask =="yes" :
                pass

            elif ask == "n" or ask == "no":
                os.system('cls')
                return
            else :
                print(CRED +"Invalid menu, Please try agian later." + CEND)
                time.sleep(1.5)
                os.system('cls')
                return
        else :
            break

    age = "?"
    while True :
        age = calculateAge(date(year,month, day))
        if age < 15 or age > 100 :
            print(CRED+"Sorry,Age under 15 can not use. "+CEND)
            time.sleep(1.5)
            os.system('cls')
            return
        else :
            break

    password = validate()
    encode   = password[0]+"!"+password[-1]+"X"+password[1]+"x"+password[2]+"81"+password[2]+password[-1]+password[3:5]
    #print(encode)
    pincode = 0

    while True :
        pincode  = input("Enter a pin number: ")
        if not pincode.isnumeric() or len(pincode) < 6 or len(pincode) > 6 :
            print(CRED +"\nSorry, The pincode has only 6 digits."+CEND)
            ask = input(">>> Did you wanna try agian?? (Y - Yes / N - No):").lower()
            print()
            if ask == "y" :
                pass
        
            elif ask == "n" :
                os.system('cls')
                return
            else :
                print(CRED +"Invalid menu, Please try agian later." + CEND)
                time.sleep(1.5)
                os.system('cls')
                return
        else :
            break
     
    file = acces_folder("AccountData","Amount")
    with open(file+".txt","a+") as file_ :
        file_.write("%s %s\n"%(ACCOUNT_NUMBER,id))   

    file = acces_folder("AccountData",ACCOUNT_NUMBER)
    with open(file+".txt","a+") as file_ :
        file_.write("%s %s %s %s %s %0.2f"%(ACCOUNT_ID,id,name,encode,pincode,balance))
        
    file = acces_folder("Statement","ST_"+ACCOUNT_NUMBER)
    with open(file+".txt",'a+') as _file :
        _file.write("%-3s %-20s %-20s %-20s %-15s\n"%("","Time","Deposit","Withdraw","Balance"))
        x = "-"*80
        _file.write("%s\n"%(x))
    CRED = '\033[32m'
    CEND = '\033[0m'
    COLOR = '\033[94m'
    COLORS = '\033[0m'
    print('\n\n Your Account ID is:',COLOR+ACCOUNT_ID+COLORS)
    print(CRED + "- Register Success - ".center(41) + CEND)
    print()
    back = input("Enter any key back to menu..")
    os.system('cls')

def template(text):
    print("•• <<────────────≪•◦⚜◦•≫────────────>> ••")
    print(text.center(41))
    print("<<────────────≪•◦⚜◦•≫────────────>>".center(41))
    
def login():
    CRED = '\033[91m'
    CEND = '\033[0m'
    account = "?"
    while True:
        template("Login Menu")
        account = input("Enter account ID: ").strip().replace(" ","").replace("-","")
        file = acces_folder("AccountData",account)
        try:
            with open(file+".txt",'r') as _file :
                break
        except :
            print(CRED +"\nSorry, this account doesn't exist."+CEND)
            ask = input(">>> Did you wanna try agian?? (Y - Yes / N - No): ").strip().lower()
            print()
            if ask == "y" or ask == "yes ":
                
                pass
            elif ask  == "n" or ask == "no" :
                os.system('cls')
                return
            else :
                print(CRED +"Invalid menu, Please try agian later."+CEND)
                time.sleep(1.5)
                os.system('cls')
                return


    with open(file+".txt") as _file :
        data = _file.readline().split()
        password = "?"
        encode = "?"
        while True :
            password = input("Enter a password: ")
            encode   = password[0]+"!"+password[-1]+"X"+password[1]+"x"+password[2]+"81"+password[2]+password[-1]+password[3:5]
            if encode != data[4] :
                print(CRED + "\nIncorrect password, Please try again."+CEND)
                ask = input(">>> Did you wanna try agian?? (Y - Yes / N - No): ").strip().lower()
                print()
                if ask == "y" or ask == "yes ":
                    pass
                    
                elif ask  == "n" or ask == "no" :
                    os.system('cls')
                    return
                else :
                    print(CRED +"Invalid menu, Please try agian later."+CEND)
                    time.sleep(1.5)
                    os.system('cls')
            else :
                break

        pin = "?"
        while True :
            pin = input("Enter a pin: ")
            if pin != data[5] :
                print(CRED +"\nIncorrect pin, Please try again." + CEND)
                ask = input(">>> Did you wanna try agian?? (Y - Yes / N - No): ").strip().lower()
                print()
                if ask == "y" or ask == "yes ":
                    pass
                elif ask  == "n" or ask == "no" :
                    os.system('cls')
                    return
                else :
                    print(CRED +"Invalid menu, Please try agian later."+CEND)
                    time.sleep(1.5)
                    os.system('cls')
            else :
                break
        os.system('cls')
    home(account)

def home(Account_ID):
    
    file = acces_folder("AccountData",Account_ID)

    with open(file+".txt") as _file :
        data = _file.readline().split()
        name = data[2]+" "+data[3]
        name = name.center(41)
        account_id = data[0]
        print("•• <<────────────≪•◦⚜◦•≫────────────>> ••")
        print(name.center(41))
        id_acc = "<<────────≪•"+account_id+"•≫────────>>"
        print(id_acc.center(41))
        #print("Home".center(45))
        print()
        print("Current Balance".center(41))
        print(data[6].center(41))
        print("\n%-5s %-19s %s"%("","1.Deposit","2.Withdraw"))
        print("\n%-5s %-19s %s\n"%("","3.Transfer","4.Statement"))
        print("5.logout".center(41))
        print("")
        print("•─────────────────────────────────•".center(41))
        home = input("    Enter menu: ")
        os.system('cls')
        while home != "5" :
            if home == "1" :
                deposit(Account_ID)       

            elif home == "2" :
                withdraw(Account_ID)


            elif home == "3" :
                transfer(Account_ID)


            elif home == "4": 
                statement(Account_ID)

            else :
                pass
        
            file = acces_folder("AccountData",Account_ID)
            with open(file+".txt") as _file :
                data = _file.readline().split()
                name = data[2]+" "+data[3]
                name = name.center(41)

            account_id = data[0]
            print("•• <<────────────≪•◦⚜◦•≫────────────>> ••")
            print(name.center(41))
            id_acc = "<<────────≪•"+account_id+"•≫────────>>"
            print(id_acc.center(41))
            print()
            print("Current Balance".center(41))
            print(data[6].center(41))  
            print("\n%-5s %-19s %s"%("","1.Deposit","2.Withdraw"))
            print("\n%-5s %-19s %s\n"%("","3.Transfer","4.Statement"))
            print("5.logout".center(41))
            print("")
            print("•─────────────────────────────────•".center(41))
            home = input("    Enter menu: ")
            os.system('cls')
 
def statement(Account_ID):

    file = acces_folder("Statement","ST_"+Account_ID)
    with open(file+".txt","r") as file_ :
        data = file_.read()
        if "    Time                 Deposit              Withdraw             Balance        \n--------------------------------------------------------------------------------\n" == data :
            print("Sorry, Statement record is empty.")
            time.sleep(1.5)
            os.system('cls')
        else :
            print(data)
    back = input("Enter any key to back menu...")
    os.system('cls')
    return

def deposit(Account_ID):
    import time
    CRED = '\033[91m'
    CEND = '\033[0m'
    template("Deposit Menu")
    deposit_amt = "?"
    
    while True:        
        try: 
            deposit_amt = float(input("Enter amount to deposit: ")) 
            bal = str(deposit_amt)
        except:
            print("Invalid You can only deposit money..")
            time.sleep(1.5)
            os.system('cls')
            return
        CRED = '\033[91m'
        CEND = '\033[0m'


        CRED = '\033[32m'
        CEND = '\033[0m'
        if deposit_amt <= 0 :
            print(CRED+"\nSorry, Please deposit a minimum of 20 baht."+CEND)
            time.sleep(1.5)
            os.system('cls')
            return

        if deposit_amt > 1000000000 :
            print(CRED+"\nMaximun deposit is 1 Billion."+CEND)
            time.sleep(1.5)
            os.system('cls')
            return
        CRED = '\033[32m'
        CEND = '\033[0m'
        print()
        print("Deposit",CRED+bal+CEND,"to your account.")
        cm = input("Did you confirm ? ( Y - Yes / N - No ): ").upper().strip()
        if cm == "Y" or cm == "YES" :
            CRED = '\033[32m'
            CEND = '\033[0m'
            cancel_message = CRED+"Deposit, Success!!"+CEND
            print()
            print(cancel_message.center(49))
            time.sleep(1)
            os.system('cls')
            break
        elif cm == "N" or cm == "NO" :
            CRED = '\033[91m'
            CEND = '\033[0m'
            cancel_message = CRED+"Cancel"+CEND
            print()
            print(cancel_message.center(49))
            time.sleep(1)
            os.system('cls')
            return
        else :
            print(CRED + "\nSorry, Invalid menu!" + CEND)
            time.sleep(1)
            os.system('cls')
            return
    
    file = acces_folder("AccountData",Account_ID)
    with open(file+".txt") as _file :
        cache = []
        data = _file.readline().split()
        floatdata = float(data[6])
        
        balance = floatdata + deposit_amt
        
        for i in data :
            cache.append(i)
        amount = float(cache[6])
        cache.pop(6)
        cache.append(balance)
        new_balance = cache[6]
        time = timenow()
        file = acces_folder("AccountData",Account_ID) #Change Balance 
        name = data[2]+" "+data[3]
        name = name[0:22]
        with open(file+".txt","w") as _file :
           _file.write("%s %s %s %s %s %s %0.2f"%(data[0],data[1],data[2],data[3],data[4],data[5],new_balance))

        file = acces_folder("Statement","ST_"+Account_ID)
        with open(file+".txt",'a+') as _file :
            _file.write("%s %-20s %10.2f %41.2f\n"%("",time,deposit_amt,new_balance))
            #_file.write("%s %-20s %10.2f %-20s %20.2f\n"%("",time,deposit_amt,"",new_balance))
    

        os.system('cls')
        return

def timenow():
    data = datetime.datetime.now()
    time = data.time()
    data = f'{data.day}/{data.month}/{data.year}'
    return data

def main():
    splash()
    template("Welcome to PetchyBank")
    print()
    print("%16s\n%19s\n%26s\n%23s\n"%("[1] - Login","[2] - Register","[3] - Forget Password","[4] - Exit Program"))
    print("─────────────────────────────────".center(41))
    menu = input("     Enter a menu: ")
    os.system('cls')

    while menu != "4" :
        if menu == "1" :
            login()

        elif menu == "2" :
            register()

        elif menu == "3" :
            forget()

        else :
            print("Invalid menu")
        
        template("Welcome to PetchyBank")
        print()
        print("%16s\n%19s\n%26s\n%23s\n"%("[1] - Login","[2] - Register","[3] - Forget Password","[4] - Exit Program"))
        print("─────────────────────────────────".center(41))
        
        menu = input("     Enter a menu: ")
        os.system('cls')

def withdraw(Account_ID):
    import time
    CRED = '\033[91m'
    CEND = '\033[0m'
    template("Withdraw Menu")
    withdraw_amt = "?"
    while True :
        try: 
            withdraw_amt = float(input("Enter amount to withdraw: "))
            bal = str(withdraw_amt)
        except:
            print(CRED+"\nInvalid You can only deposit money.."+CEND)
            time.sleep(2)
            os.system('cls')
            return

        if withdraw_amt < 100 :
            print(CRED+"\nMinimum withdraw is 100 Baht."+CEND)
            time.sleep(1.5)
            os.system('cls')
            return

        if withdraw_amt > 1000000000 :
            print(CRED+"\nMaximum withdraw is 1 Billion."+CEND)
            time.sleep(1.5)
            os.system('cls')
            return

        print("\nWithdraw",CRED+bal+CEND,"from your account")
        cm = input("Did you confirm ? ( Y - Yes / N - No ): ").upper().strip()
        if cm == "Y" or cm == "YES" :
            break
        elif cm == "N" or cm == "NO" :
            CRED = '\033[91m'
            CEND = '\033[0m'
            cancel_message = CRED+"Cancel"+CEND
            print()
            print(cancel_message.center(49))
            time.sleep(1)
            os.system('cls')
            return
        else :
            print(CRED + "\nSorry, Invalid menu!" + CEND)
            time.sleep(1)
            os.system('cls')
            return

    file = acces_folder("AccountData",Account_ID)
    with open(file+".txt") as _file :
        cache = []
        data = _file.readline().split()
        floatdata = float(data[6])
        enter_pin = input("Enter a pincode: ")
        if enter_pin != data[5] :
            print(CRED+"\nSorry, wrong pincode."+CEND)
            time.sleep(1)
            os.system('cls')
            return
        
        balance = floatdata - withdraw_amt
        if balance < 0 :
            print(CRED+"\nSorry, the amount is not enough."+CEND)
            time.sleep(1)
            os.system('cls')
            return

        for i in data :
            cache.append(i)
        cache.pop(6)
        cache.append(balance)
        new_balance = cache[6]
        time = timenow()
        file = acces_folder("AccountData",Account_ID) #Change Balance 
        name = data[2]+" "+data[3]
        name = name[0:22]
        with open(file+".txt","w") as _file :
           _file.write("%s %s %s %s %s %s %0.2f"%(data[0],data[1],data[2],data[3],data[4],data[5],new_balance))

        file = acces_folder("Statement","ST_"+Account_ID)
        with open(file+".txt",'a+') as _file :
            _file.write("%s %-20s %31.2f %20.2f\n"%("",time,withdraw_amt,new_balance))
            #_file.write("\n%-15s %-26s %-14s %-15.2f %-15.2f"%(time,name,"Withdraw",withdraw_amt,new_balance))
        CRED = '\033[32m'
        CEND = '\033[0m'
        cancel_message = CRED+"Withdraw, Success!!"+CEND
        print()
        print(cancel_message.center(49))

        import time
        time.sleep(1)
        os.system('cls')    
        return

def transfer(Account_ID):
    import time
    CRED = '\033[91m'
    CEND = '\033[0m'
    template("Transfer Menu")
    user_acc = input("Enter account ID: ").strip().replace(" ","").replace("-","")
    #user_acc = "1000000002"
    file = acces_folder("AccountData",user_acc)
    try :
        with open(file+".txt",'r') as _file :
            data = _file.read().split()
            #user_balance = float(data[6])
            
    except :
        print(CRED+"\nSorry, Invalid Account please try agian later."+CEND)
        time.sleep(1)
        os.system('cls')
        return
    

    transfer_amt = "?"
    while True :
        try :
            transfer_amt = float(input("Enter transfer amount: "))
            bal = str(transfer_amt)
        except :
            print(CRED+"\nSorry, Please enter the correct amount."+CEND)
            time.sleep(1)
            os.system('cls')
            
        if transfer_amt < 100 :
            print(CRED+"\nMinimum transfer is 100 Baht."+CEND)
            time.sleep(1.5)
            os.system('cls')
            return

        if transfer_amt > 1000000000 :
            print(CRED+"\nMaximun transfer is 1 Billion."+CEND)
            time.sleep(1.5)
            os.system('cls')
            return

        COLOR = '\033[94m'
        COLORS = '\033[0m'
        print("Transfer",CRED+bal+CEND,"to",COLOR+data[0]+COLORS,"Account ID")
        cm = input("Did you confirm ? ( Y - Yes / N - No ): ").upper().strip()
        if cm == "Y" or cm == "YES" :
            break
        elif cm == "N" or cm == "NO" :
            CRED = '\033[91m'
            CEND = '\033[0m'
            cancel_message = CRED+"Cancel"+CEND
            print()
            print(cancel_message.center(49))
            time.sleep(1)
            os.system('cls')
            return
        else :
            print(CRED + "\nSorry, Invalid menu!" + CEND)
            time.sleep(1)
            os.system('cls')
            return

    file = acces_folder("AccountData",Account_ID)
    with open(file+'.txt','r') as _file :
        data = _file.read().split()
        balance = float(data[6])
        newbalace = balance - transfer_amt 
        time = timenow()
        name = data[2]+" "+data[3]
        enter_pin = input("Enter a pincode: ")
        if enter_pin != data[5] :
            print(CRED+"\nSorry, wrong pincode."+CEND)
            import time
            time.sleep(1)
            os.system('cls')
            return

        if newbalace < 0 :
            print(CRED+"\nSorry, the amount is not enough."+CEND)
            import time
            time.sleep(1)
            os.system('cls')
            return
        
        #Owner User
        with open(file+".txt",'w') as file_ :
            file_.write("%s %s %s %s %s %s %s"%(data[0],data[1],data[2],data[3],data[4],data[5],newbalace))
        #statement Owner 
        
        #100-000-0002 1234567890124 Kunsre Mana !!4XMxa81a4na 123456 10000000000.00
        file = acces_folder("Statement","ST_"+Account_ID)
        with open(file+".txt",'a+') as _file :
            _file.write("%s %-20s %31.2f %20.2f\n"%("",time,transfer_amt,newbalace))
            #_file.write("\n%-15s %-26s %-14s %-15.2f %-15.2f"%(time,name,"Transfer-OUT",transfer_amt,newbalace))
    
    #Parter account
    file = acces_folder("AccountData",user_acc)
    with open(file+'.txt','r') as _file :
        data = _file.read().split()
        balance = float(data[6])
        newbalace = balance + transfer_amt 
        time = timenow()
        name = data[2]+" "+data[3]

        #Owner User
        with open(file+".txt",'w') as file_ :
            file_.write("%s %s %s %s %s %s %s"%(data[0],data[1],data[2],data[3],data[4],data[5],newbalace))
        #statement Owner 
        
        #100-000-0002 1234567890124 Kunsre Mana !!4XMxa81a4na 123456 10000000000.00
        file = acces_folder("Statement","ST_"+user_acc)
        with open(file+".txt",'a+') as _file :
            _file.write("%s %-20s %10.2f %41.2f\n"%("",time,transfer_amt,newbalace))
            #_file.write("\n%-15s %-26s %-14s %-15.2f %-15.2f"%(time,name,"Transfer-IN",transfer_amt,newbalace))
    CRED = '\033[32m'
    CEND = '\033[0m'
    cancel_message = CRED+"Transfer, Success!!"+CEND
    print()
    print(cancel_message.center(49))
    import time
    time.sleep(1)
    os.system('cls')    
    return

def forget():
    CRED = '\033[91m'
    CEND = '\033[0m'
    template("Password Recovery")
    account = input("Enter account ID: ").strip().replace(" ","").replace("-","")
    file = acces_folder("AccountData",account)
    try :
        with open(file+".txt","r") as file_ :
            pass
    except :
        print("Sorry, This account does not exist")
        time.sleep(1.5)
        os.system('cls')
        return

    with open(file+".txt",'r') as file_:
        data = file_.read().split()
        id = input("Enter your ID-card (13digits): ")
        if id != data[1] :
            print(CRED+"\nSorry, Invalid ID card number."+CEND)
            time.sleep(1)
            os.system('cls')
            return

        pincode = input("Enter a pincode: ")
        if pincode != data[5] :
            print(CRED+"\nSorry, Invalid pincode."+CEND)
            time.sleep(1)
            os.system('cls')
            return
        acc_id = data[0]
        user_id = data[1]
        fname = data[2]
        lname = data[3]
        
        os.system('cls')
        template("New Password")
        password = validate()
        encode   = password[0]+"!"+password[-1]+"X"+password[1]+"x"+password[2]+"81"+password[2]+password[-1]+password[3:5]
        if encode == data[4] :
            print(CRED+"\nThis password already use. Please create new password."+CEND)
            time.sleep(1.5)
            os.system('cls')
            return

        bal = data[6]
        file = acces_folder("AccountData",account)
        with open(file+".txt",'w') as file_ :
            file_.write("%s %s %s %s %s %s %s"%(acc_id,user_id,fname,lname,encode,pincode,bal))
        CRED = '\033[32m'
        CEND = '\033[0m'
        print(CRED + "- Recovery Success - ".center(41) + CEND)
        print()
        time.sleep(1.5)
        os.system('cls')

main()