#1.Linked List
#2.Linear Search
#3.Binary Search
#4.Bubble Sort
#5.Selection Sort
#6.Recursion
#7.Slight Time Complexity Representation
#8.SQL Database
#9.Filing

class Node:
    def __init__(self,Account,Name,PNum,CNum,pin,deposit,ANum):
        self.Account=Account
        self.Name=Name
        self.PNum=PNum
        self.CNum=CNum
        self.pin=pin
        self.deposit=deposit
        self.ANum=ANum
        self.Next=None
        self.Prev=None
        
class Current_AccountLL:
    def __init__(self):
        self.Start=None

    def Insert(self,Account,Name,PNum,CNum,pin,deposit,ANum):
        New=Node(Account,Name,PNum,CNum,pin,deposit,ANum)
        if(self.Start is None):
            self.Start=New
        else:
            ptr=self.Start
            while(ptr.Next is not None):
                ptr=ptr.Next
            ptr.Next=New
            New.Prev=ptr
    
    def Insert_INTO_SQL(self):
        if(self.Start is None):
            print("No Account Information")
        else:
            ptr=self.Start
            while(ptr is not None):
                import pyodbc
                conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=NOMIR-PC\SQLEXPRESS;'
                      'Database=Project;'
                      'Trusted_Connection=yes;')
                cursor=conn.cursor()
                cursor.execute("INSERT INTO Current_Account(Account,Name,PNum,CNIC,PIN,Deposit,ANum) VALUES (?,?,?,?,?,?,?)",(ptr.Account,ptr.Name,ptr.PNum,ptr.CNum,ptr.pin,ptr.deposit,ptr.ANum))
                cursor.execute("INSERT INTO All_Accounts(Account,Name,PNum,CNIC,PIN,Deposit,ANum) VALUES (?,?,?,?,?,?,?)",(ptr.Account,ptr.Name,ptr.PNum,ptr.CNum,ptr.pin,ptr.deposit,ptr.ANum))
                conn.commit()
                conn.close()
                ptr=ptr.Next

    def Print(self):
        if(self.Start is None):
            print("No Account Information")
        else:
            ptr=self.Start
            while(ptr is not None):
                print("\n\t\t\t\t\t=====================================")
                print(f"\t\t\t\t\t\t     Information\n\n\t\t\t\t\tAccount : {(ptr.Account)}\n\t\t\t\t\tName : {(ptr.Name)}\n\t\t\t\t\tPhone Number : {(ptr.PNum)}\n\t\t\t\t\tCNIC : {(ptr.CNum)}\n\t\t\t\t\tPIN : {(ptr.pin)}\n\t\t\t\t\tDeposit : {(ptr.deposit)}\n\t\t\t\t\tAcount Number : {(ptr.ANum)}")
                print("\t\t\t\t\t=====================================")
                ptr=ptr.Next

class Savings_AccountLL:
    def __init__(self):
        self.Start=None

    def Insert(self,Account,Name,PNum,CNum,pin,deposit,ANum):
        New=Node(Account,Name,PNum,CNum,pin,deposit,ANum)
        if(self.Start is None):
            self.Start=New
        else:
            ptr=self.Start
            while(ptr.Next is not None):
                ptr=ptr.Next
            ptr.Next=New
            New.Prev=ptr
    
    def Insert_INTO_SQL(self):
        if(self.Start is None):
            print("No Account Information")
        else:
            ptr=self.Start
            while(ptr is not None):
                import pyodbc
                conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=NOMIR-PC\SQLEXPRESS;'
                      'Database=Project;'
                      'Trusted_Connection=yes;')
                cursor=conn.cursor()
                cursor.execute("INSERT INTO Savings_Account(Account,Name,PNum,CNIC,PIN,Deposit,ANum) VALUES (?,?,?,?,?,?,?)",(ptr.Account,ptr.Name,ptr.PNum,ptr.CNum,ptr.pin,ptr.deposit,ptr.ANum))
                cursor.execute("INSERT INTO All_Accounts(Account,Name,PNum,CNIC,PIN,Deposit,ANum) VALUES (?,?,?,?,?,?,?)",(ptr.Account,ptr.Name,ptr.PNum,ptr.CNum,ptr.pin,ptr.deposit,ptr.ANum))
                conn.commit()
                conn.close()
                ptr=ptr.Next

    def Print(self):
        if(self.Start is None):
            print("No Account Information")
        else:
            ptr=self.Start
            while(ptr is not None):
                print("\n\t\t\t\t\t=====================================")
                print(f"\t\t\t\t\t\t     Information\n\n\t\t\t\t\tAccount : {(ptr.Account)}\n\t\t\t\t\tName : {(ptr.Name)}\n\t\t\t\t\tPhone Number : {(ptr.PNum)}\n\t\t\t\t\tCNIC : {(ptr.CNum)}\n\t\t\t\t\tPIN : {(ptr.pin)}\n\t\t\t\t\tDeposit : {(ptr.deposit)}\n\t\t\t\t\tAcount Number : {(ptr.ANum)}")
                print("\t\t\t\t\t=====================================")
                ptr=ptr.Next

def Home():
    print("\t\t\t\t\t=====================================")
    print("\t\t\t\t\t|\tBank Managemnet System \t    |")
    print("\t\t\t\t\t=====================================")
    print("\n\t\t\t\t   1.Create Account\t\t2.Log In To Account\n\n\t\t\t\t   3.ATM\t\t\t4.Utility Bills\n\n\t\t\t\t   5.Consultancy\t\t6.Exit")
    choice=int(input("Enter Your Choice : "))
    if(choice==1):
        CreateAccount()
    elif(choice==2):
        LoginAccount()
    elif(choice==3):
        ATM()      
    elif(choice==4):
        UtilityBills2()
    elif(choice==5):
        Consultancy()      
    elif(choice==6):
        exit()
    elif(choice==69420):
        R_Facts()
    elif(choice==666):
        FullAccountInfo()
    else:
        print("Invalid Input")
        Home()

def CreateAccount():    
    print("\t\t\t\t\t=====================================")
    print("\t\t\t\t\t|\t    Create Account \t    |")
    print("\t\t\t\t\t=====================================")
    print("\t\t\t\t\t=====================================")
    print("\t\t\t\t\t|\tBank Managemnet System \t    |")
    print("\t\t\t\t\t=====================================")
    print("\n\t\t\t\t   1.Current Account\t\t2.Savings Account")
    print("\nThere Are Two Types Of Account You Can Choose From\nOR Press 3 To Go Back To Main Menu")
    choice=int(input("\nEnter Your Choice : "))
    if(choice==1):
        CurrentAccount()
    elif(choice==2):
        SavingsAccount()     
    elif(choice==3):
        Home()     
    else:
        print("Invalid Input")
        CreateAccount()

def CurrentAccount():
    import random
    Account="Current"
    Name=input("\nEnter Your Name : ")  
    Phone_Number=input("Enter Your Phone Number : ")
    while(len(Phone_Number)!=11):
        print("\nInvalid Phone Number Try Again : ")
        Phone_Number=input("Enter Your Phone Number : ")
    CNIC=input("Enter Your CNIC Number : ")
    while(len(CNIC)!=13):
        print("\nInvalid CNIC Number Try Again : ")
        CNIC=input("Enter Your CNIC Number : ")
    PIN=input("Enter Your 4 Digit Number For ATM : ")
    while(len(PIN)!=4):
        print("Invalid Number For PIN Try Again : ")
        PIN=input("\nEnter Your 4 Digit Number For ATM : ")
    I_Deposit=input("Enter Your Deposit Value : ")
    Account_Number=random.randint(10000,99999)
    print(f"\nThis Is Your Account Number : ",Account_Number)
    CA_LL=Current_AccountLL()
    CA_LL.Insert(Account,Name,Phone_Number,CNIC,PIN,I_Deposit,Account_Number)
    CA_LL.Insert_INTO_SQL()
    CA_LL.Print()
    choice=int(input("\nYour Current Account Is Created \nPress 3 To Go Back To Menu : "))
    if(choice==3):
        Home()
    else:
        print("Invalid Input")
        Home()

def SavingsAccount():
    import random
    Account="Savings"
    Name=input("\nEnter Your Name : ")  
    Phone_Number=input("Enter Your Phone Number : ")
    while(len(Phone_Number)!=11):
        print("\nInvalid Phone Number Try Again : ")
        Phone_Number=input("Enter Your Phone Number : ")
    CNIC=input("Enter Your CNIC Number : ")
    while(len(CNIC)!=13):
        print("\nInvalid CNIC Number Try Again : ")
        CNIC=input("Enter Your CNIC Number : ")
    PIN=input("Enter Your 4 Digit Number For ATM : ")
    while(len(PIN)!=4 ):
        print("Invalid Number For PIN Try Again : ")
        PIN=input("\nEnter Your 4 Digit Number For ATM : ")
    I_Deposit=input("Enter Your Deposit Value: ")
    Account_Number=random.randint(10000,99999)
    print(f"\nThis Is Your Account Number : ",Account_Number)   
    SA_LL=Savings_AccountLL()
    SA_LL.Insert(Account,Name,Phone_Number,CNIC,PIN,I_Deposit,Account_Number)
    SA_LL.Insert_INTO_SQL()
    SA_LL.Print()
    choice=int(input("\nYour Savings Account Is Created \nPress 3 To Go Back To Menu : "))   
    if(choice==3):
        Home()
    else:
        print("Invalid Input")
        Home()

def LoginAccount():
    print("\t\t\t\t\t=====================================")
    print("\t\t\t\t\t|\t\tLog In \t\t    |")
    print("\t\t\t\t\t=====================================")
    import pyodbc
    conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=NOMIR-PC\SQLEXPRESS;'
                      'Database=Project;'
                      'Trusted_Connection=yes;')
    N=input("\nEnter Your Name : ")
    AN=input("Enter Your Account Number : ")
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT Account,Name,CNIC,ANum FROM All_Accounts where Anum=(?)",AN)
        for row in cursor:
            print(f"\nIt Is A {row[0]} Account")
            print(f"Name : "+row[1])
            print(f"CNIC Is : "+row[2])
            print(f"Account Number Is : "+row[3])
            print()
        Acc_T=row[0]
        Acc=int(row[3])
    except:
        print("\nWrong Information\nGoing Back To Menu\n")
        Home()
    print("\t\t\t\t\t=====================================")
    print("\t\t\t\t\t|\tBank Managemnet System \t    |")
    print("\t\t\t\t\t=====================================")
    print("\n\t\t\t\t   1.Deposit Money\t\t2.Withdraw Money\n\n\t\t\t\t   3.ATM\t\t\t4.Utility Bills\n\n\t\t\t\t   5.Loans\t\t\t6.FAQS\n\n\t\t\t\t   7.Consultancy\t\t8.Currency Exchange\n\n\t\t\t\t   9.Back\t\t\t10.Exit")
    choice=int(input("\nEnter Your Choice : "))
    if(choice==1):
        DepositMoney(Acc_T,Acc)
    elif(choice==2):
        WithdrawMoney(Acc_T,Acc)
    elif(choice==3):
        ATM_Bank()      
    elif(choice==4):
        UtilityBills()
    elif(choice==5):
        Loans()      
    elif(choice==6):
        FAQ()  
    elif(choice==7):
        ConsultancyB()
    elif(choice==8):
        CurrencyExchange()      
    elif(choice==9):
        Home()      
    elif(choice==10):
        exit()
    else:
        print("Invalid Input")
        LoginAccount()

def DepositMoney(Account,AccountNumber):
    import pyodbc
    conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=NOMIR-PC\SQLEXPRESS;'
                      'Database=Project;'
                      'Trusted_Connection=yes;')
    cursor = conn.cursor()
    cursor.execute("SELECT Deposit FROM All_Accounts where Anum=(?)",AccountNumber)
    for row in cursor:
        print(f"Current Money In Account : "+row[0])
    CD=int(row[0])
    ND=int(input("\nEnter The Amount You Want To Deposit : "))
    D=CD+ND
    if(Account=="Current"):
        cursor = conn.cursor()
        cursor.execute("UPDATE Current_Account SET Deposit=(?) Where ANum=(?)",(D,AccountNumber))
        cursor.execute("UPDATE All_Accounts SET Deposit=(?) Where ANum=(?)",(D,AccountNumber))
        conn.commit()
        print("Ammount Deposited Succesfully")
        LoginAccount()
    elif(Account=="Savings"):
        cursor = conn.cursor()
        cursor.execute("UPDATE Savings_Account SET Deposit=(?) Where ANum=(?)",(D,AccountNumber))
        cursor.execute("UPDATE All_Accounts SET Deposit=(?) Where ANum=(?)",(D,AccountNumber))
        conn.commit()
        print("Ammount Deposited Succesfully")
        LoginAccount()
    conn.close()

def WithdrawMoney(Account,AccountNumber):
    import pyodbc
    conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=NOMIR-PC\SQLEXPRESS;'
                      'Database=Project;'
                      'Trusted_Connection=yes;')
    cursor = conn.cursor()
    cursor.execute("SELECT Deposit FROM All_Accounts where Anum=(?)",AccountNumber)
    for row in cursor:
        print(f"Current Money In Account : "+row[0])
    CD=int(row[0])
    if(CD<=1000):
        print("\nNot Enough Amount In The Account To Withdraw\nPlease Deposit Some Amount First")
        LoginAccount()
    elif(CD>1000):
        NWD=int(input("\nEnter The Amount You Want To Withdraw : "))
        if(CD<NWD):
            print("Insufficent Funds\nTry A New Amount")
            WithdrawMoney()
        elif(CD>=NWD):
            WD=CD-NWD
            if(Account=="Current"):
                cursor = conn.cursor()
                cursor.execute("UPDATE Current_Account SET Deposit=(?) Where ANum=(?)",(WD,AccountNumber))
                cursor.execute("UPDATE All_Accounts SET Deposit=(?) Where ANum=(?)",(WD,AccountNumber))
                conn.commit()
                print("Ammount Withdraw Succesfully")
                LoginAccount()
            elif(Account=="Savings"):
                cursor = conn.cursor()
                cursor.execute("UPDATE Savings_Account SET Deposit=(?) Where ANum=(?)",(WD,AccountNumber))
                cursor.execute("UPDATE All_Accounts SET Deposit=(?) Where ANum=(?)",(WD,AccountNumber))
                conn.commit()
                print("Ammount Withdraw Succesfully")
                LoginAccount()
        
def ATM():
    print("\t\t\t\t\t=====================================")
    print("\t\t\t\t\t|\t\tATM \t\t    |")
    print("\t\t\t\t\t=====================================")
    import pyodbc
    conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=NOMIR-PC\SQLEXPRESS;'
                      'Database=Project;'
                      'Trusted_Connection=yes;')
    ATM_PIN=str(input("\nEnter Your 4 Digit PIN : "))
    T_PIN=0
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT PIN FROM All_Accounts where PIN=(?)",ATM_PIN)
        for row in cursor:
            print(f"\nPIN : "+row[0])
        T_PIN=row[0]
    except:
        print("\nWrong PIN Number\nGoing Back To Menu\n")
        Home()
    if(T_PIN==ATM_PIN):
        cursor = conn.cursor()
        cursor.execute("SELECT Account,Deposit,ANum FROM All_Accounts where PIN=(?)",ATM_PIN)
        for row in cursor:
            print(f"It Is A {row[0]} Account")
            print(f"Money In Account Is : "+row[1])
            print(f"Account Number : "+row[2])
        D_check=int(row[1])
        print("\t\t\t\t\t=====================================")
        print("\t\t\t\t\t|\tBank Managemnet System \t    |")
        print("\t\t\t\t\t=====================================")
        print("\n\t\t\t\t   1.500\t\t\t\t2.1000\n\n\t\t\t\t   3.2000\t\t\t\t4.5000\n\n\t\t\t\t   5.10000\t\t\t\t6.Back")
        choice=int(input("Enter Your Choice : "))
        if(choice==1):
            if(D_check>=500):
                if(row[0]=="Current"):
                    D_check=D_check-500
                    cursor = conn.cursor()
                    cursor.execute("UPDATE Current_Account SET Deposit=(?) Where ANum=(?)",(D_check,row[2]))
                    cursor.execute("UPDATE All_Accounts SET Deposit=(?) Where ANum=(?)",(D_check,row[2]))
                    conn.commit()
                    print("\nRs.500 Were Withdraw From Your Current Account,\nPlease Collect It")
                    choice1=int(input("\nPress 3 To Go Back To Menu\nPress 6 To Exit\n"))
                    if(choice1==3):
                        Home()
                    elif(choice1==6):
                        exit()
                elif(row[0]=="Savings"):
                    D_check=D_check-500
                    cursor = conn.cursor()
                    cursor.execute("UPDATE Savings_Account SET Deposit=(?) Where ANum=(?)",(D_check,row[2]))
                    cursor.execute("UPDATE All_Accounts SET Deposit=(?) Where ANum=(?)",(D_check,row[2]))
                    conn.commit()
                    print("\nRs.500 Were Withdraw From Your Savings Account,\nPlease Collect It")
                    choice1=int(input("\nPress 3 To Go Back To Menu\nPress 6 To Exit\n"))
                    if(choice1==3):
                        Home()
                    elif(choice1==6):
                        exit()
            elif(D_check<500):
                print("Insufficent Funds\nEnter Your PIN Again")
                ATM()
        elif(choice==2):
            if(D_check>=1000):
                if(row[0]=="Current"):
                    D_check=D_check-1000
                    cursor = conn.cursor()
                    cursor.execute("UPDATE Current_Account SET Deposit=(?) Where ANum=(?)",(D_check,row[2]))
                    cursor.execute("UPDATE All_Accounts SET Deposit=(?) Where ANum=(?)",(D_check,row[2]))
                    conn.commit()
                    print("\nRs.1000 Were Withdraw From Your Current Account,\nPlease Collect It")
                    choice1=int(input("\nPress 3 To Go Back To Menu\nPress 6 To Exit\n"))
                    if(choice1==3):
                        Home()
                    elif(choice1==6):
                        exit()
                elif(row[0]=="Savings"):
                    D_check=D_check-1000
                    cursor = conn.cursor()
                    cursor.execute("UPDATE Savings_Account SET Deposit=(?) Where ANum=(?)",(D_check,row[2]))
                    cursor.execute("UPDATE All_Accounts SET Deposit=(?) Where ANum=(?)",(D_check,row[2]))
                    conn.commit()
                    print("\nRs.1000 Were Withdraw From Your Savings Account,\nPlease Collect It")
                    choice1=int(input("\nPress 3 To Go Back To Menu\nPress 6 To Exit\n"))
                    if(choice1==3):
                        Home()
                    elif(choice1==6):
                        exit()
            elif(D_check<1000):
                print("Insufficent Funds\nEnter Your PIN Again")
                ATM()
        elif(choice==3):
            if(D_check>=2000):
                if(row[0]=="Current"):
                    D_check=D_check-2000
                    cursor = conn.cursor()
                    cursor.execute("UPDATE Current_Account SET Deposit=(?) Where ANum=(?)",(D_check,row[2]))
                    cursor.execute("UPDATE All_Accounts SET Deposit=(?) Where ANum=(?)",(D_check,row[2]))
                    conn.commit()
                    print("\nRs.2000 Were Withdraw From Your Current Account,\nPlease Collect It")
                    choice1=int(input("\nPress 3 To Go Back To Menu\nPress 6 To Exit\n"))
                    if(choice1==3):
                        Home()
                    elif(choice1==6):
                        exit()
                elif(row[0]=="Savings"):
                    D_check=D_check-2000
                    cursor = conn.cursor()
                    cursor.execute("UPDATE Savings_Account SET Deposit=(?) Where ANum=(?)",(D_check,row[2]))
                    cursor.execute("UPDATE All_Accounts SET Deposit=(?) Where ANum=(?)",(D_check,row[2]))
                    conn.commit()
                    print("\nRs.2000 Were Withdraw From Your Savings Account,\nPlease Collect It")
                    choice1=int(input("\nPress 3 To Go Back To Menu\nPress 6 To Exit\n"))
                    if(choice1==3):
                        Home()
                    elif(choice1==6):
                        exit()
            elif(D_check<2000):
                print("Insufficent Funds\nEnter Your PIN Again")
                ATM()
        elif(choice==4):    
            if(D_check>=5000):
                if(row[0]=="Current"):
                    D_check=D_check-5000
                    cursor = conn.cursor()
                    cursor.execute("UPDATE Current_Account SET Deposit=(?) Where ANum=(?)",(D_check,row[2]))
                    cursor.execute("UPDATE All_Accounts SET Deposit=(?) Where ANum=(?)",(D_check,row[2]))
                    conn.commit()
                    print("\nRs.5000 Were Withdraw From Your Current Account,\nPlease Collect It")
                    choice1=int(input("\nPress 3 To Go Back To Menu\nPress 6 To Exit\n"))
                    if(choice1==3):
                        Home()
                    elif(choice1==6):
                        exit()
                elif(row[0]=="Savings"):
                    D_check=D_check-5000
                    cursor = conn.cursor()
                    cursor.execute("UPDATE Savings_Account SET Deposit=(?) Where ANum=(?)",(D_check,row[2]))
                    cursor.execute("UPDATE All_Accounts SET Deposit=(?) Where ANum=(?)",(D_check,row[2]))
                    conn.commit()
                    print("\nRs.5000 Were Withdraw From Your Savings Account,\nPlease Collect It")
                    choice1=int(input("\nPress 3 To Go Back To Menu\nPress 6 To Exit\n"))
                    if(choice1==3):
                        Home()
                    elif(choice1==6):
                        exit()
            elif(D_check<5000):
                print("Insufficent Funds\nEnter Your PIN Again")
                ATM()
        elif(choice==5):           
            if(D_check>=10000):
                if(row[0]=="Current"):
                    D_check=D_check-10000
                    cursor = conn.cursor()
                    cursor.execute("UPDATE Current_Account SET Deposit=(?) Where ANum=(?)",(D_check,row[2]))
                    cursor.execute("UPDATE All_Accounts SET Deposit=(?) Where ANum=(?)",(D_check,row[2]))
                    conn.commit()
                    print("\nRs.10000 Were Withdraw From Your Current Account,\nPlease Collect It")
                    choice1=int(input("\nPress 3 To Go Back To Menu\nPress 6 To Exit\n"))
                    if(choice1==3):
                        Home()
                    elif(choice1==6):
                        exit()
                elif(row[0]=="Savings"):
                    D_check=D_check-10000
                    cursor = conn.cursor()
                    cursor.execute("UPDATE Savings_Account SET Deposit=(?) Where ANum=(?)",(D_check,row[2]))
                    cursor.execute("UPDATE All_Accounts SET Deposit=(?) Where ANum=(?)",(D_check,row[2]))
                    conn.commit()
                    print("\nRs.10000 Were Withdraw From Your Savings Account,\nPlease Collect It")
                    choice1=int(input("\nPress 3 To Go Back To Menu\nPress 6 To Exit\n"))
                    if(choice1==3):
                        Home()
                    elif(choice1==6):
                        exit()
            elif(D_check<10000):
                print("Insufficent Funds\nEnter Your PIN Again")
                ATM()   
        elif(choice==6):
            Home()
        else:
            print("Invalid Input\nEnter Your PIN Again")
            ATM() 
    else:
        print("Wrong PIN Number\nGoing Back To Menu\n")
        Home()
    conn.close()

def ATM_Bank():
    print("\t\t\t\t\t=====================================")
    print("\t\t\t\t\t|\t\tATM \t\t    |")
    print("\t\t\t\t\t=====================================")
    import pyodbc
    conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=NOMIR-PC\SQLEXPRESS;'
                      'Database=Project;'
                      'Trusted_Connection=yes;')
    ATM_PIN=str(input("\nEnter Your 4 Digit PIN : "))
    T_PIN=0
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT PIN FROM All_Accounts where PIN=(?)",ATM_PIN)
        for row in cursor:
            print(f"\nPIN : "+row[0])
        T_PIN=row[0]
    except:
        print("\nWrong PIN Number\nGoing Back To Previous Window\n")
        LoginAccount()
    if(T_PIN==ATM_PIN):
        cursor = conn.cursor()
        cursor.execute("SELECT Account,Deposit,ANum FROM All_Accounts where PIN=(?)",ATM_PIN)
        for row in cursor:
            print(f"Money In Account Is : "+row[1])
        D_check=int(row[1])
        print("\t\t\t\t\t=====================================")
        print("\t\t\t\t\t|\tBank Managemnet System \t    |")
        print("\t\t\t\t\t=====================================")
        print("\n\t\t\t\t   1.500\t\t\t\t2.1000\n\n\t\t\t\t   3.2000\t\t\t\t4.5000\n\n\t\t\t\t   5.10000\t\t\t\t6.Back")
        choice=int(input("Enter Your Choice : "))
        if(choice==1):
            if(D_check>=500):
                if(row[0]=="Current"):
                    D_check=D_check-500
                    cursor = conn.cursor()
                    cursor.execute("UPDATE Current_Account SET Deposit=(?) Where ANum=(?)",(D_check,row[2]))
                    cursor.execute("UPDATE All_Accounts SET Deposit=(?) Where ANum=(?)",(D_check,row[2]))
                    conn.commit()
                    print("\nRs.500 Were Withdraw From Your Current Account,\nPlease Collect It")
                    print("\nGoing Back To Previous Window\n")
                    LoginAccount()
                elif(row[0]=="Savings"):
                    D_check=D_check-500
                    cursor = conn.cursor()
                    cursor.execute("UPDATE Savings_Account SET Deposit=(?) Where ANum=(?)",(D_check,row[2]))
                    cursor.execute("UPDATE All_Accounts SET Deposit=(?) Where ANum=(?)",(D_check,row[2]))
                    conn.commit()
                    print("\nRs.500 Were Withdraw From Your Savings Account,\nPlease Collect It")
                    print("\nGoing Back To Previous Window\n")
                    LoginAccount()
            elif(D_check<500):
                print("Insufficent Funds\nEnter Your PIN Again")
                ATM_Bank() 
        elif(choice==2):
            if(D_check>=1000):
                if(row[0]=="Current"):
                    D_check=D_check-1000
                    cursor = conn.cursor()
                    cursor.execute("UPDATE Current_Account SET Deposit=(?) Where ANum=(?)",(D_check,row[2]))
                    cursor.execute("UPDATE All_Accounts SET Deposit=(?) Where ANum=(?)",(D_check,row[2]))
                    conn.commit()
                    print("\nRs.1000 Were Withdraw From Your Current Account,\nPlease Collect It")
                    print("\nGoing Back To Previous Window\n")
                    LoginAccount()
                elif(row[0]=="Savings"):
                    D_check=D_check-1000
                    cursor = conn.cursor()
                    cursor.execute("UPDATE Savings_Account SET Deposit=(?) Where ANum=(?)",(D_check,row[2]))
                    cursor.execute("UPDATE All_Accounts SET Deposit=(?) Where ANum=(?)",(D_check,row[2]))
                    conn.commit()
                    print("\nRs.1000 Were Withdraw From Your Savings Account,\nPlease Collect It")
                    print("\nGoing Back To Previous Window\n")
                    LoginAccount()
            elif(D_check<1000):
                print("Insufficent Funds\nEnter Your PIN Again")
                ATM_Bank() 
        elif(choice==3):
            if(D_check>=2000):
                if(row[0]=="Current"):
                    D_check=D_check-2000
                    cursor = conn.cursor()
                    cursor.execute("UPDATE Current_Account SET Deposit=(?) Where ANum=(?)",(D_check,row[2]))
                    cursor.execute("UPDATE All_Accounts SET Deposit=(?) Where ANum=(?)",(D_check,row[2]))
                    conn.commit()
                    print("\nRs.2000 Were Withdraw From Your Current Account,\nPlease Collect It")
                    print("\nGoing Back To Previous Window\n")
                    LoginAccount()
                elif(row[0]=="Savings"):
                    D_check=D_check-2000
                    cursor = conn.cursor()
                    cursor.execute("UPDATE Savings_Account SET Deposit=(?) Where ANum=(?)",(D_check,row[2]))
                    cursor.execute("UPDATE All_Accounts SET Deposit=(?) Where ANum=(?)",(D_check,row[2]))
                    conn.commit()
                    print("\nRs.2000 Were Withdraw From Your Savings Account,\nPlease Collect It")
                    print("\nGoing Back To Previous Window\n")
                    LoginAccount()
            elif(D_check<2000):
                print("Insufficent Funds\nEnter Your PIN Again")
                ATM_Bank() 
        elif(choice==4):    
            if(D_check>=5000):
                if(row[0]=="Current"):
                    D_check=D_check-5000
                    cursor = conn.cursor()
                    cursor.execute("UPDATE Current_Account SET Deposit=(?) Where ANum=(?)",(D_check,row[2]))
                    cursor.execute("UPDATE All_Accounts SET Deposit=(?) Where ANum=(?)",(D_check,row[2]))
                    conn.commit()
                    print("\nRs.5000 Were Withdraw From Your Current Account,\nPlease Collect It")
                    choice1=int(input("\nPress 3 To Go Back To Menu\nPress 6 To Exit\n"))
                    print("\nGoing Back To Previous Window\n")
                    LoginAccount()
                elif(row[0]=="Savings"):
                    D_check=D_check-5000
                    cursor = conn.cursor()
                    cursor.execute("UPDATE Savings_Account SET Deposit=(?) Where ANum=(?)",(D_check,row[2]))
                    cursor.execute("UPDATE All_Accounts SET Deposit=(?) Where ANum=(?)",(D_check,row[2]))
                    conn.commit()
                    print("\nRs.5000 Were Withdraw From Your Savings Account,\nPlease Collect It")
                    print("\nGoing Back To Previous Window\n")
                    LoginAccount()
            elif(D_check<5000):
                print("Insufficent Funds\nEnter Your PIN Again")
                ATM_Bank() 
        elif(choice==5):           
            if(D_check>=10000):
                if(row[0]=="Current"):
                    D_check=D_check-10000
                    cursor = conn.cursor()
                    cursor.execute("UPDATE Current_Account SET Deposit=(?) Where ANum=(?)",(D_check,row[2]))
                    cursor.execute("UPDATE All_Accounts SET Deposit=(?) Where ANum=(?)",(D_check,row[2]))
                    conn.commit()
                    print("\nRs.10000 Were Withdraw From Your Current Account,\nPlease Collect It")
                    print("\nGoing Back To Previous Window\n")
                    LoginAccount()
                elif(row[0]=="Savings"):
                    D_check=D_check-10000
                    cursor = conn.cursor()
                    cursor.execute("UPDATE Savings_Account SET Deposit=(?) Where ANum=(?)",(D_check,row[2]))
                    cursor.execute("UPDATE All_Accounts SET Deposit=(?) Where ANum=(?)",(D_check,row[2]))
                    conn.commit()
                    print("\nRs.10000 Were Withdraw From Your Savings Account,\nPlease Collect It")
                    print("\nGoing Back To Previous Window\n")
                    LoginAccount()
            elif(D_check<10000):
                print("Insufficent Funds\nEnter Your PIN Again")
                ATM_Bank()   
        elif(choice==6):
            LoginAccount()
        else:
            print("Invalid Input\nEnter Your PIN Again")
            ATM_Bank() 
    else:
        print("Wrong PIN Number\nGoing Back To Previous Window\n")
        LoginAccount()
    conn.close()

def Loans():
    print("\t\t\t\t\t=====================================")
    print("\t\t\t\t\t|\t\tLoans \t\t    |")
    print("\t\t\t\t\t=====================================")   
    print("\n\t\t\t\t   1.Home Loans\t\t\t2.Car Loans\n\t\t\t\t   3.General Loans\t\t4.Property Loans")
    choice=int(input("\nChoose The Loan You Want(OR Press 5 To Go Back) : "))
    if(choice==1):
        HomeLoan()
    elif(choice==2):
        CarLoan()
    elif(choice==3):
        GeneralLoan()
    elif(choice==4):
        PropertyLoan()
    elif(choice==5):
        LoginAccount()
    else:
        print("Invalid Input\nGoing To Previous Window")
        LoginAccount()

def HomeLoan():
    #In Home Loans The Time Complexity Of Linear Search Will Differ From The General Loans As In General Loans The Array Is Sorted And In Home Loans Array Is Unsorted
    from numpy import array
    import pyodbc
    conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=NOMIR-PC\SQLEXPRESS;'
                      'Database=Project;'
                      'Trusted_Connection=yes;')
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM Employee_ID")
    Emp_ID=array([0 for i in range(10)])
    i=0
    for row in cursor:
        Emp_ID[i]=row[0]
        i=i+1
    LO=int(input("\nThere Are Two Types Of Home Loans We Offer :\n1.Long Term\n2.Short Term\n\nEnter Your Choice : "))
    if(LO==1):
        Sal=int(input("\nEnter Your Monthly Income : "))
        if(Sal>=150000):
            print("\nYou Are Eligible To Apply For This Loan")
            LO1=int(input("\nThere Are 3 Types Of Long Term Loans : \n1.2 Years (2.5% Interest)\n2.5 Years (4% Interest)\n3.7 Years (4.5% Interest)\n\nEnter Your Choice : "))
            if(LO1==1):
                Q1=input("\nAre You A Employee Of The Company(Y/N) : ")
                if(Q1=="Y" or Q1=="y"):
                    Q2=int(input("Enter Your Employee ID : "))
                    for i in range(len(Emp_ID)):
                        if(Emp_ID[i]==Q2):#Searching Unsorted Array 
                            a=input(f"\nIs This The ID You Entered {Emp_ID[i]}(Y/N) :  ")
                            if(a=="Y" or a=="y"):
                                print(f"\nEmployee Of The Company Confirmed Employee ID Is : {Q2}")
                                print("You Will Only Have To Pay 2% Interest")
                                N=input("\nEnter Your Name : ")
                                Cnic=input("Enter Your CNIC Number : ")
                                pn=input("Enter Your Phone Number : ")
                                amount=input("Enter The Amount You Want For Loan : ")
                                print("\n\t\t\t\t\t=====================================")
                                print(f"\t\t\t\t\tName : {N}\n\t\t\t\t\tCNIC : {Cnic}\n\t\t\t\t\tPhone Number : {pn}\n\t\t\t\t\tLoan Type : Long Term (2 Years)\n\t\t\t\t\tEmployee Of The Company : Yes\n\t\t\t\t\tInterest To Pay : 2% Only\n\n\t\t\t\t\tLoan Request Is Sent,\n\t\t\t\t\tYou Will Get A Call Soon.")
                                print("\t\t\t\t\t=====================================")
                                Loans()
                            elif(a=="N" or a=="n"):
                                print("Wrong Employee ID")
                                Loans()
                    print("\nEmployee ID Not Found, Going Back To Previous Window")
                    Loans()
                elif(Q1=="N" or Q1=="n"):
                    Na=input("\nEnter Your Name : ")
                    Cnic=input("Enter Your CNIC Number : ")
                    pn=input("Enter Your Phone Number : ")
                    amount=input("Enter The Amount You Want For Loan : ")
                    print("\n\t\t\t\t\t=====================================")
                    print(f"\t\t\t\t\tName : {Na}\n\t\t\t\t\tCNIC : {Cnic}\n\t\t\t\t\tPhone Number : {pn}\n\t\t\t\t\tLoan Type : Long Term (2 Years)\n\t\t\t\t\tEmployee Of The Company : No\n\t\t\t\t\tInterest To Pay : 2.5% Only\n\n\t\t\t\t\tLoan Request Is Sent,\n\t\t\t\t\tYou Will Get A Call Soon.")
                    print("\t\t\t\t\t=====================================")
                    Loans()
            elif(LO1==2):
                Q1=input("\nAre You A Employee Of The Company(Y/N) : ")
                if(Q1=="Y" or Q1=="y"):
                    Q2=int(input("Enter Your Employee ID : "))
                    for i in range(len(Emp_ID)):
                        if(Emp_ID[i]==Q2):#Searching Unsorted Array 
                            a=input(f"\nIs This The ID You Entered {Emp_ID[i]}(Y/N) :  ")
                            if(a=="Y" or a=="y"):
                                print(f"\nEmployee Of The Company Confirmed Employee ID Is : {Q2}")
                                print("You Will Only Have To Pay 3% Interest")
                                N=input("\nEnter Your Name : ")
                                Cnic=input("Enter Your CNIC Number : ")
                                pn=input("Enter Your Phone Number : ")
                                amount=input("Enter The Amount You Want For Loan : ")
                                print("\n\t\t\t\t\t=====================================")
                                print(f"\t\t\t\t\tName : {N}\n\t\t\t\t\tCNIC : {Cnic}\n\t\t\t\t\tPhone Number : {pn}\n\t\t\t\t\tLoan Type : Long Term (5 Years)\n\t\t\t\t\tEmployee Of The Company : Yes\n\t\t\t\t\tInterest To Pay : 3% Only\n\n\t\t\t\t\tLoan Request Is Sent,\n\t\t\t\t\tYou Will Get A Call Soon.")
                                print("\t\t\t\t\t=====================================")
                                Loans()
                            elif(a=="N" or a=="n"):
                                print("Wrong Employee ID")
                                Loans()
                    print("\nEmployee ID Not Found, Going Back To Previous Window")
                    Loans()
                elif(Q1=="N" or Q1=="n"):
                    Na=input("\nEnter Your Name : ")
                    Cnic=input("Enter Your CNIC Number : ")
                    pn=input("Enter Your Phone Number : ")
                    amount=input("Enter The Amount You Want For Loan : ")
                    print("\n\t\t\t\t\t=====================================")
                    print(f"\t\t\t\t\tName : {Na}\n\t\t\t\t\tCNIC : {Cnic}\n\t\t\t\t\tPhone Number : {pn}\n\t\t\t\t\tLoan Type : Long Term (5 Years)\n\t\t\t\t\tEmployee Of The Company : No\n\t\t\t\t\tInterest To Pay : 4% Only\n\n\t\t\t\t\tLoan Request Is Sent,\n\t\t\t\t\tYou Will Get A Call Soon.")
                    print("\t\t\t\t\t=====================================")
                    Loans()
            elif(LO1==3):
                Q1=input("\nAre You A Employee Of The Company(Y/N) : ")
                if(Q1=="Y" or Q1=="y"):
                    Q2=int(input("Enter Your Employee ID : "))
                    for i in range(len(Emp_ID)):
                        if(Emp_ID[i]==Q2):#Searching Unsorted Array 
                            a=input(f"\nIs This The ID You Entered {Emp_ID[i]}(Y/N) :  ")
                            if(a=="Y" or a=="y"):
                                print(f"\nEmployee Of The Company Confirmed Employee ID Is : {Q2}")
                                print("You Will Only Have To Pay 4% Interest")
                                N=input("\nEnter Your Name : ")
                                Cnic=input("Enter Your CNIC Number : ")
                                pn=input("Enter Your Phone Number : ")
                                amount=input("Enter The Amount You Want For Loan : ")
                                print("\n\t\t\t\t\t=====================================")
                                print(f"\t\t\t\t\tName : {N}\n\t\t\t\t\tCNIC : {Cnic}\n\t\t\t\t\tPhone Number : {pn}\n\t\t\t\t\tLoan Type : Long Term (7 Years)\n\t\t\t\t\tEmployee Of The Company : Yes\n\t\t\t\t\tInterest To Pay : 4% Only\n\n\t\t\t\t\tLoan Request Is Sent,\n\t\t\t\t\tYou Will Get A Call Soon.")
                                print("\t\t\t\t\t=====================================")
                                Loans()
                            elif(a=="N" or a=="n"):
                                print("Wrong Employee ID")
                                Loans()
                    print("\nEmployee ID Not Found, Going Back To Previous Window")
                    Loans()
                elif(Q1=="N" or Q1=="n"):
                    Na=input("\nEnter Your Name : ")
                    Cnic=input("Enter Your CNIC Number : ")
                    pn=input("Enter Your Phone Number : ")
                    amount=input("Enter The Amount You Want For Loan : ")
                    print("\n\t\t\t\t\t=====================================")
                    print(f"\t\t\t\t\tName : {Na}\n\t\t\t\t\tCNIC : {Cnic}\n\t\t\t\t\tPhone Number : {pn}\n\t\t\t\t\tLoan Type : Long Term (7 Years)\n\t\t\t\t\tEmployee Of The Company : No\n\t\t\t\t\tInterest To Pay : 4.5% Only\n\n\t\t\t\t\tLoan Request Is Sent,\n\t\t\t\t\tYou Will Get A Call Soon.")
                    print("\t\t\t\t\t=====================================")
                    Loans()
            else:
                print("\nInvalid Input,Going Back To Loan Screen")
                Loans()
        elif(Sal<150000):
            print("\nYou Are Not Eligible To Apply For This Loan")
            Loans()
    elif(LO==2):
        Sal=int(input("\nEnter Your Monthly Income : "))
        if(Sal>=100000):
            print("\nYou Are Eligible To Apply For This Loan")
            LO1=int(input("\nThere Are 3 Types Of Long Term Loans : \n1.2 Months (2.5% Interest)\n2.5 Months (4% Interest)\n3.1 Year (4.5% Interest)\n\nEnter Your Choice : "))
            if(LO1==1):
                Q1=input("\nAre You A Employee Of The Company(Y/N) : ")
                if(Q1=="Y" or Q1=="y"):
                    Q2=int(input("Enter Your Employee ID : "))
                    for i in range(len(Emp_ID)):
                        if(Emp_ID[i]==Q2):#Searching Unsorted Array 
                            a=input(f"\nIs This The ID You Entered {Emp_ID[i]}(Y/N) :  ")
                            if(a=="Y" or a=="y"):
                                print(f"\nEmployee Of The Company Confirmed Employee ID Is : {Q2}")
                                print("You Will Only Have To Pay 2% Interest")
                                N=input("\nEnter Your Name : ")
                                Cnic=input("Enter Your CNIC Number : ")
                                pn=input("Enter Your Phone Number : ")
                                amount=input("Enter The Amount You Want For Loan : ")
                                print("\n\t\t\t\t\t=====================================")
                                print(f"\t\t\t\t\tName : {N}\n\t\t\t\t\tCNIC : {Cnic}\n\t\t\t\t\tPhone Number : {pn}\n\t\t\t\t\tLoan Type : Short Term (2 Months)\n\t\t\t\t\tEmployee Of The Company : Yes\n\t\t\t\t\tInterest To Pay : 2% Only\n\n\t\t\t\t\tLoan Request Is Sent,\n\t\t\t\t\tYou Will Get A Call Soon.")
                                print("\t\t\t\t\t=====================================")
                                Loans()
                            elif(a=="N" or a=="n"):
                                print("Wrong Employee ID")
                                Loans()
                    print("\nEmployee ID Not Found, Going Back To Previous Window")
                    Loans()
                elif(Q1=="N" or Q1=="n"):
                    Na=input("\nEnter Your Name : ")
                    Cnic=input("Enter Your CNIC Number : ")
                    pn=input("Enter Your Phone Number : ")
                    amount=input("Enter The Amount You Want For Loan : ")
                    print("\n\t\t\t\t\t=====================================")
                    print(f"\t\t\t\t\tName : {Na}\n\t\t\t\t\tCNIC : {Cnic}\n\t\t\t\t\tPhone Number : {pn}\n\t\t\t\t\tLoan Type : Short Term (2 Months)\n\t\t\t\t\tEmployee Of The Company : No\n\t\t\t\t\tInterest To Pay : 2.5% Only\n\n\t\t\t\t\tLoan Request Is Sent,\n\t\t\t\t\tYou Will Get A Call Soon.")
                    print("\t\t\t\t\t=====================================")
                    Loans()
            elif(LO1==2):
                Q1=input("\nAre You A Employee Of The Company(Y/N) : ")
                if(Q1=="Y" or Q1=="y"):
                    Q2=int(input("Enter Your Employee ID : "))
                    for i in range(len(Emp_ID)):
                        if(Emp_ID[i]==Q2):#Searching Unsorted Array 
                            a=input(f"\nIs This The ID You Entered {Emp_ID[i]}(Y/N) :  ")
                            if(a=="Y" or a=="y"):
                                print(f"\nEmployee Of The Company Confirmed Employee ID Is : {Q2}")
                                print("You Will Only Have To Pay 3% Interest")
                                N=input("\nEnter Your Name : ")
                                Cnic=input("Enter Your CNIC Number : ")
                                pn=input("Enter Your Phone Number : ")
                                amount=input("Enter The Amount You Want For Loan : ")
                                print("\n\t\t\t\t\t=====================================")
                                print(f"\t\t\t\t\tName : {N}\n\t\t\t\t\tCNIC : {Cnic}\n\t\t\t\t\tPhone Number : {pn}\n\t\t\t\t\tLoan Type : Short Term (5 Months)\n\t\t\t\t\tEmployee Of The Company : Yes\n\t\t\t\t\tInterest To Pay : 3% Only\n\n\t\t\t\t\tLoan Request Is Sent,\n\t\t\t\t\tYou Will Get A Call Soon.")
                                print("\t\t\t\t\t=====================================")
                                Loans()
                            elif(a=="N" or a=="n"):
                                print("Wrong Employee ID")
                                Loans()
                    print("\nEmployee ID Not Found, Going Back To Previous Window")
                    Loans()
                elif(Q1=="N" or Q1=="n"):
                    Na=input("\nEnter Your Name : ")
                    Cnic=input("Enter Your CNIC Number : ")
                    pn=input("Enter Your Phone Number : ")
                    amount=input("Enter The Amount You Want For Loan : ")
                    print("\n\t\t\t\t\t=====================================")
                    print(f"\t\t\t\t\tName : {Na}\n\t\t\t\t\tCNIC : {Cnic}\n\t\t\t\t\tPhone Number : {pn}\n\t\t\t\t\tLoan Type : Short Term (5 Months)\n\t\t\t\t\tEmployee Of The Company : No\n\t\t\t\t\tInterest To Pay : 4% Only\n\n\t\t\t\t\tLoan Request Is Sent,\n\t\t\t\t\tYou Will Get A Call Soon.")
                    print("\t\t\t\t\t=====================================")
                    Loans()
            elif(LO1==3):
                Q1=input("\nAre You A Employee Of The Company(Y/N) : ")
                if(Q1=="Y" or Q1=="y"):
                    Q2=int(input("Enter Your Employee ID : "))
                    for i in range(len(Emp_ID)):
                        if(Emp_ID[i]==Q2):#Searching Unsorted Array 
                            a=input(f"\nIs This The ID You Entered {Emp_ID[i]}(Y/N) :  ")
                            if(a=="Y" or a=="y"):
                                print(f"\nEmployee Of The Company Confirmed Employee ID Is : {Q2}")
                                print("You Will Only Have To Pay 4% Interest")
                                N=input("\nEnter Your Name : ")
                                Cnic=input("Enter Your CNIC Number : ")
                                pn=input("Enter Your Phone Number : ")
                                amount=input("Enter The Amount You Want For Loan : ")
                                print("\n\t\t\t\t\t=====================================")
                                print(f"\t\t\t\t\tName : {N}\n\t\t\t\t\tCNIC : {Cnic}\n\t\t\t\t\tPhone Number : {pn}\n\t\t\t\t\tLoan Type : Short Term (1 Year)\n\t\t\t\t\tEmployee Of The Company : Yes\n\t\t\t\t\tInterest To Pay : 4% Only\n\n\t\t\t\t\tLoan Request Is Sent,\n\t\t\t\t\tYou Will Get A Call Soon.")
                                print("\t\t\t\t\t=====================================")
                                Loans()
                            elif(a=="N" or a=="n"):
                                print("Wrong Employee ID")
                                Loans()
                    print("\nEmployee ID Not Found, Going Back To Previous Window")
                    Loans()
                elif(Q1=="N" or Q1=="n"):
                    Na=input("\nEnter Your Name : ")
                    Cnic=input("Enter Your CNIC Number : ")
                    pn=input("Enter Your Phone Number : ")
                    amount=input("Enter The Amount You Want For Loan : ")
                    print("\n\t\t\t\t\t=====================================")
                    print(f"\t\t\t\t\tName : {Na}\n\t\t\t\t\tCNIC : {Cnic}\n\t\t\t\t\tPhone Number : {pn}\n\t\t\t\t\tLoan Type : Short Term (1 Year)\n\t\t\t\t\tEmployee Of The Company : No\n\t\t\t\t\tInterest To Pay : 4.5% Only\n\n\t\t\t\t\tLoan Request Is Sent,\n\t\t\t\t\tYou Will Get A Call Soon.")
                    print("\t\t\t\t\t=====================================")
                    Loans()
            else:
                print("\nInvalid Input,Going Back To Loan Screen")
                Loans()
        elif(Sal<100000):
            print("\nYou Are Not Eligible To Apply For This Loan")
            Loans()
    else:
        print("\nInvalid Input,Going Back To Previous Screen")
        Loans()

def CarLoan():
    from numpy import array
    import pyodbc
    conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=NOMIR-PC\SQLEXPRESS;'
                      'Database=Project;'
                      'Trusted_Connection=yes;')
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM Employee_ID")
    Emp_ID=array([0 for i in range(10)])
    i=0
    for row in cursor:
        Emp_ID[i]=row[0]
        i=i+1
    RecursiveBubbleSort(Emp_ID)
    print(Emp_ID)
    LO=int(input("\nThere Are Two Types Of Car Loans We Offer :\n1.Long Term\n2.Short Term\n\nEnter Your Choice : "))
    if(LO==1):
        Sal=int(input("\nEnter Your Monthly Income : "))
        if(Sal>=150000):
            print("\nYou Are Eligible To Apply For This Loan")
            LO1=int(input("\nThere Are 3 Types Of Long Term Loans : \n1.2 Years (2.5% Interest)\n2.5 Years (4% Interest)\n3.7 Years (4.5% Interest)\n\nEnter Your Choice : "))
            if(LO1==1):
                Q1=input("\nAre You A Employee Of The Company(Y/N) : ")
                if(Q1=="Y" or Q1=="y"):
                    Q2=int(input("Enter Your Employee ID : "))
                    low=0
                    high=len(Emp_ID)-1
                    mid=0
                    while(low<=high):#Searching Sorted Array
                        mid=(high+low)//2
                        if(Emp_ID[mid]<Q2):
                            low=mid+1
                        elif(Emp_ID[mid]>Q2):
                            high=mid-1
                        else:
                            a=input(f"\nIs This The ID You Entered {Emp_ID[mid]}(Y/N) :  ")
                            if(a=="Y" or a=="y"):
                                print(f"\nEmployee Of The Company Confirmed Employee ID Is : {Q2}")
                                print("You Will Only Have To Pay 2% Interest")
                                N=input("\nEnter Your Name : ")
                                Cnic=input("Enter Your CNIC Number : ")
                                pn=input("Enter Your Phone Number : ")
                                amount=input("Enter The Amount You Want For Loan : ")
                                print("\n\t\t\t\t\t=====================================")
                                print(f"\t\t\t\t\tName : {N}\n\t\t\t\t\tCNIC : {Cnic}\n\t\t\t\t\tPhone Number : {pn}\n\t\t\t\t\tLoan Type : Long Term (2 Years)\n\t\t\t\t\tEmployee Of The Company : Yes\n\t\t\t\t\tInterest To Pay : 2% Only\n\n\t\t\t\t\tLoan Request Is Sent,\n\t\t\t\t\tYou Will Get A Call Soon.")
                                print("\t\t\t\t\t=====================================")
                                Loans()
                            elif(a=="N" or a=="n"):
                                print("Wrong Employee ID")
                                Loans()
                    print("\nEmployee ID Not Found, Going Back To Previous Window")
                    Loans()
                elif(Q1=="N" or Q1=="n"):
                    Na=input("\nEnter Your Name : ")
                    Cnic=input("Enter Your CNIC Number : ")
                    pn=input("Enter Your Phone Number : ")
                    amount=input("Enter The Amount You Want For Loan : ")
                    print("\n\t\t\t\t\t=====================================")
                    print(f"\t\t\t\t\tName : {Na}\n\t\t\t\t\tCNIC : {Cnic}\n\t\t\t\t\tPhone Number : {pn}\n\t\t\t\t\tLoan Type : Long Term (2 Years)\n\t\t\t\t\tEmployee Of The Company : No\n\t\t\t\t\tInterest To Pay : 2.5% Only\n\n\t\t\t\t\tLoan Request Is Sent,\n\t\t\t\t\tYou Will Get A Call Soon.")
                    print("\t\t\t\t\t=====================================")
                    Loans()
            elif(LO1==2):
                Q1=input("\nAre You A Employee Of The Company(Y/N) : ")
                if(Q1=="Y" or Q1=="y"):
                    Q2=int(input("Enter Your Employee ID : "))
                    low=0
                    high=len(Emp_ID)-1
                    mid=0
                    while(low<=high):#Searching Sorted Array
                        mid=(high+low)//2
                        if(Emp_ID[mid]<Q2):
                            low=mid+1
                        elif(Emp_ID[mid]>Q2):
                            high=mid-1
                        else:
                            a=input(f"\nIs This The ID You Entered {Emp_ID[mid]}(Y/N) :  ")
                            if(a=="Y" or a=="y"):
                                print(f"\nEmployee Of The Company Confirmed Employee ID Is : {Q2}")
                                print("You Will Only Have To Pay 3% Interest")
                                N=input("\nEnter Your Name : ")
                                Cnic=input("Enter Your CNIC Number : ")
                                pn=input("Enter Your Phone Number : ")
                                amount=input("Enter The Amount You Want For Loan : ")
                                print("\n\t\t\t\t\t=====================================")
                                print(f"\t\t\t\t\tName : {N}\n\t\t\t\t\tCNIC : {Cnic}\n\t\t\t\t\tPhone Number : {pn}\n\t\t\t\t\tLoan Type : Long Term (5 Years)\n\t\t\t\t\tEmployee Of The Company : Yes\n\t\t\t\t\tInterest To Pay : 3% Only\n\n\t\t\t\t\tLoan Request Is Sent,\n\t\t\t\t\tYou Will Get A Call Soon.")
                                print("\t\t\t\t\t=====================================")
                                Loans()
                            elif(a=="N" or a=="n"):
                                print("Wrong Employee ID")
                                Loans()
                    print("\nEmployee ID Not Found, Going Back To Previous Window")
                    Loans()
                elif(Q1=="N" or Q1=="n"):
                    Na=input("\nEnter Your Name : ")
                    Cnic=input("Enter Your CNIC Number : ")
                    pn=input("Enter Your Phone Number : ")
                    amount=input("Enter The Amount You Want For Loan : ")
                    print("\n\t\t\t\t\t=====================================")
                    print(f"\t\t\t\t\tName : {Na}\n\t\t\t\t\tCNIC : {Cnic}\n\t\t\t\t\tPhone Number : {pn}\n\t\t\t\t\tLoan Type : Long Term (5 Years)\n\t\t\t\t\tEmployee Of The Company : No\n\t\t\t\t\tInterest To Pay : 4% Only\n\n\t\t\t\t\tLoan Request Is Sent,\n\t\t\t\t\tYou Will Get A Call Soon.")
                    print("\t\t\t\t\t=====================================")
                    Loans()
            elif(LO1==3):
                Q1=input("\nAre You A Employee Of The Company(Y/N) : ")
                if(Q1=="Y" or Q1=="y"):
                    Q2=int(input("Enter Your Employee ID : "))
                    low=0
                    high=len(Emp_ID)-1
                    mid=0
                    while(low<=high):#Searching Sorted Array
                        mid=(high+low)//2
                        if(Emp_ID[mid]<Q2):
                            low=mid+1
                        elif(Emp_ID[mid]>Q2):
                            high=mid-1
                        else:
                            a=input(f"\nIs This The ID You Entered {Emp_ID[mid]}(Y/N) :  ")
                            if(a=="Y" or a=="y"):
                                print(f"\nEmployee Of The Company Confirmed Employee ID Is : {Q2}")
                                print("You Will Only Have To Pay 4% Interest")
                                N=input("\nEnter Your Name : ")
                                Cnic=input("Enter Your CNIC Number : ")
                                pn=input("Enter Your Phone Number : ")
                                amount=input("Enter The Amount You Want For Loan : ")
                                print("\n\t\t\t\t\t=====================================")
                                print(f"\t\t\t\t\tName : {N}\n\t\t\t\t\tCNIC : {Cnic}\n\t\t\t\t\tPhone Number : {pn}\n\t\t\t\t\tLoan Type : Long Term (7 Years)\n\t\t\t\t\tEmployee Of The Company : Yes\n\t\t\t\t\tInterest To Pay : 4% Only\n\n\t\t\t\t\tLoan Request Is Sent,\n\t\t\t\t\tYou Will Get A Call Soon.")
                                print("\t\t\t\t\t=====================================")
                                Loans()
                            elif(a=="N" or a=="n"):
                                print("Wrong Employee ID")
                                Loans()
                    print("\nEmployee ID Not Found, Going Back To Previous Window")
                    Loans()
                elif(Q1=="N" or Q1=="n"):
                    Na=input("\nEnter Your Name : ")
                    Cnic=input("Enter Your CNIC Number : ")
                    pn=input("Enter Your Phone Number : ")
                    amount=input("Enter The Amount You Want For Loan : ")
                    print("\n\t\t\t\t\t=====================================")
                    print(f"\t\t\t\t\tName : {Na}\n\t\t\t\t\tCNIC : {Cnic}\n\t\t\t\t\tPhone Number : {pn}\n\t\t\t\t\tLoan Type : Long Term (7 Years)\n\t\t\t\t\tEmployee Of The Company : No\n\t\t\t\t\tInterest To Pay : 4.5% Only\n\n\t\t\t\t\tLoan Request Is Sent,\n\t\t\t\t\tYou Will Get A Call Soon.")
                    print("\t\t\t\t\t=====================================")
                    Loans()
            else:
                print("\nInvalid Input,Going Back To Loan Screen")
                Loans()
        elif(Sal<150000):
            print("\nYou Are Not Eligible To Apply For This Loan")
            Loans()
    elif(LO==2):
        Sal=int(input("\nEnter Your Monthly Income : "))
        if(Sal>=100000):
            print("\nYou Are Eligible To Apply For This Loan")
            LO1=int(input("\nThere Are 3 Types Of Long Term Loans : \n1.2 Months (2.5% Interest)\n2.5 Months (4% Interest)\n3.1 Year (4.5% Interest)\n\nEnter Your Choice : "))
            if(LO1==1):
                Q1=input("\nAre You A Employee Of The Company(Y/N) : ")
                if(Q1=="Y" or Q1=="y"):
                    Q2=int(input("Enter Your Employee ID : "))
                    low=0
                    high=len(Emp_ID)-1
                    mid=0
                    while(low<=high):#Searching Sorted Array
                        mid=(high+low)//2
                        if(Emp_ID[mid]<Q2):
                            low=mid+1
                        elif(Emp_ID[mid]>Q2):
                            high=mid-1
                        else:
                            a=input(f"\nIs This The ID You Entered {Emp_ID[mid]}(Y/N) :  ")
                            if(a=="Y" or a=="y"):
                                print(f"\nEmployee Of The Company Confirmed Employee ID Is : {Q2}")
                                print("You Will Only Have To Pay 2% Interest")
                                N=input("\nEnter Your Name : ")
                                Cnic=input("Enter Your CNIC Number : ")
                                pn=input("Enter Your Phone Number : ")
                                amount=input("Enter The Amount You Want For Loan : ")
                                print("\n\t\t\t\t\t=====================================")
                                print(f"\t\t\t\t\tName : {N}\n\t\t\t\t\tCNIC : {Cnic}\n\t\t\t\t\tPhone Number : {pn}\n\t\t\t\t\tLoan Type : Short Term (2 Months)\n\t\t\t\t\tEmployee Of The Company : Yes\n\t\t\t\t\tInterest To Pay : 2% Only\n\n\t\t\t\t\tLoan Request Is Sent,\n\t\t\t\t\tYou Will Get A Call Soon.")
                                print("\t\t\t\t\t=====================================")
                                Loans()
                            elif(a=="N" or a=="n"):
                                print("Wrong Employee ID")
                                Loans()
                    print("\nEmployee ID Not Found, Going Back To Previous Window")
                    Loans()
                elif(Q1=="N" or Q1=="n"):
                    Na=input("\nEnter Your Name : ")
                    Cnic=input("Enter Your CNIC Number : ")
                    pn=input("Enter Your Phone Number : ")
                    amount=input("Enter The Amount You Want For Loan : ")
                    print("\n\t\t\t\t\t=====================================")
                    print(f"\t\t\t\t\tName : {Na}\n\t\t\t\t\tCNIC : {Cnic}\n\t\t\t\t\tPhone Number : {pn}\n\t\t\t\t\tLoan Type : Short Term (2 Months)\n\t\t\t\t\tEmployee Of The Company : No\n\t\t\t\t\tInterest To Pay : 2.5% Only\n\n\t\t\t\t\tLoan Request Is Sent,\n\t\t\t\t\tYou Will Get A Call Soon.")
                    print("\t\t\t\t\t=====================================")
                    Loans()
            elif(LO1==2):
                Q1=input("\nAre You A Employee Of The Company(Y/N) : ")
                if(Q1=="Y" or Q1=="y"):
                    Q2=int(input("Enter Your Employee ID : "))
                    low=0
                    high=len(Emp_ID)-1
                    mid=0
                    while(low<=high):#Searching Sorted Array
                        mid=(high+low)//2
                        if(Emp_ID[mid]<Q2):
                            low=mid+1
                        elif(Emp_ID[mid]>Q2):
                            high=mid-1
                        else:
                            a=input(f"\nIs This The ID You Entered {Emp_ID[mid]}(Y/N) :  ")
                            if(a=="Y" or a=="y"):
                                print(f"\nEmployee Of The Company Confirmed Employee ID Is : {Q2}")
                                print("You Will Only Have To Pay 3% Interest")
                                N=input("\nEnter Your Name : ")
                                Cnic=input("Enter Your CNIC Number : ")
                                pn=input("Enter Your Phone Number : ")
                                amount=input("Enter The Amount You Want For Loan : ")
                                print("\n\t\t\t\t\t=====================================")
                                print(f"\t\t\t\t\tName : {N}\n\t\t\t\t\tCNIC : {Cnic}\n\t\t\t\t\tPhone Number : {pn}\n\t\t\t\t\tLoan Type : Short Term (5 Months)\n\t\t\t\t\tEmployee Of The Company : Yes\n\t\t\t\t\tInterest To Pay : 3% Only\n\n\t\t\t\t\tLoan Request Is Sent,\n\t\t\t\t\tYou Will Get A Call Soon.")
                                print("\t\t\t\t\t=====================================")
                                Loans()
                            elif(a=="N" or a=="n"):
                                print("Wrong Employee ID")
                                Loans()
                    print("\nEmployee ID Not Found, Going Back To Previous Window")
                    Loans()
                elif(Q1=="N" or Q1=="n"):
                    Na=input("\nEnter Your Name : ")
                    Cnic=input("Enter Your CNIC Number : ")
                    pn=input("Enter Your Phone Number : ")
                    amount=input("Enter The Amount You Want For Loan : ")
                    print("\n\t\t\t\t\t=====================================")
                    print(f"\t\t\t\t\tName : {Na}\n\t\t\t\t\tCNIC : {Cnic}\n\t\t\t\t\tPhone Number : {pn}\n\t\t\t\t\tLoan Type : Short Term (5 Months)\n\t\t\t\t\tEmployee Of The Company : No\n\t\t\t\t\tInterest To Pay : 4% Only\n\n\t\t\t\t\tLoan Request Is Sent,\n\t\t\t\t\tYou Will Get A Call Soon.")
                    print("\t\t\t\t\t=====================================")
                    Loans()
            elif(LO1==3):
                Q1=input("\nAre You A Employee Of The Company(Y/N) : ")
                if(Q1=="Y" or Q1=="y"):
                    Q2=int(input("Enter Your Employee ID : "))
                    low=0
                    high=len(Emp_ID)-1
                    mid=0
                    while(low<=high):#Searching Sorted Array
                        mid=(high+low)//2
                        if(Emp_ID[mid]<Q2):
                            low=mid+1
                        elif(Emp_ID[mid]>Q2):
                            high=mid-1
                        else:
                            a=input(f"\nIs This The ID You Entered {Emp_ID[mid]}(Y/N) :  ")
                            if(a=="Y" or a=="y"):
                                print(f"\nEmployee Of The Company Confirmed Employee ID Is : {Q2}")
                                print("You Will Only Have To Pay 4% Interest")
                                N=input("\nEnter Your Name : ")
                                Cnic=input("Enter Your CNIC Number : ")
                                pn=input("Enter Your Phone Number : ")
                                amount=input("Enter The Amount You Want For Loan : ")
                                print("\n\t\t\t\t\t=====================================")
                                print(f"\t\t\t\t\tName : {N}\n\t\t\t\t\tCNIC : {Cnic}\n\t\t\t\t\tPhone Number : {pn}\n\t\t\t\t\tLoan Type : Short Term (1 Year)\n\t\t\t\t\tEmployee Of The Company : Yes\n\t\t\t\t\tInterest To Pay : 4% Only\n\n\t\t\t\t\tLoan Request Is Sent,\n\t\t\t\t\tYou Will Get A Call Soon.")
                                print("\t\t\t\t\t=====================================")
                                Loans()
                            elif(a=="N" or a=="n"):
                                print("Wrong Employee ID")
                                Loans()
                    print("\nEmployee ID Not Found, Going Back To Previous Window")
                    Loans()
                elif(Q1=="N" or Q1=="n"):
                    Na=input("\nEnter Your Name : ")
                    Cnic=input("Enter Your CNIC Number : ")
                    pn=input("Enter Your Phone Number : ")
                    amount=input("Enter The Amount You Want For Loan : ")
                    print("\n\t\t\t\t\t=====================================")
                    print(f"\t\t\t\t\tName : {Na}\n\t\t\t\t\tCNIC : {Cnic}\n\t\t\t\t\tPhone Number : {pn}\n\t\t\t\t\tLoan Type : Short Term (1 Year)\n\t\t\t\t\tEmployee Of The Company : No\n\t\t\t\t\tInterest To Pay : 4.5% Only\n\n\t\t\t\t\tLoan Request Is Sent,\n\t\t\t\t\tYou Will Get A Call Soon.")
                    print("\t\t\t\t\t=====================================")
                    Loans()
            else:
                print("\nInvalid Input,Going Back To Loan Screen")
                Loans()
        elif(Sal<100000):
            print("\nYou Are Not Eligible To Apply For This Loan")
            Loans()
    else:
        print("\nInvalid Input,Going Back To Previous Screen")
        Loans()
            
def RecursiveBubbleSort(Array):
    c=0
    for i in range(len(Array)-1):
        if(Array[i]>Array[i+1]):
            Array[i],Array[i+1]=Array[i+1],Array[i]
            c=c+1
    if(c==0):
        return Array
    else:
        return RecursiveBubbleSort(Array)

def GeneralLoan():
    #In Geenal Loan The Time Complexity Of Linear Search Will Differ From The Home Loans As In General Loans The Array Is Sorted And In Home Loans Array Is Unsorted
    from numpy import array
    import pyodbc
    conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=NOMIR-PC\SQLEXPRESS;'
                      'Database=Project;'
                      'Trusted_Connection=yes;')
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM Employee_ID")
    Emp_ID=array([0 for i in range(10)])
    i=0
    for row in cursor:
        Emp_ID[i]=row[0]
        i=i+1
    for i in range(len(Emp_ID)):
        T_index=i
        for j in range(i+1,len(Emp_ID)):
            if(Emp_ID[T_index]>Emp_ID[j]):
                T_index=j     
        Emp_ID[i],Emp_ID[T_index]=Emp_ID[T_index],Emp_ID[i]
    LO=int(input("\nThere Are Two Types Of General Loans We Offer :\n1.Long Term\n2.Short Term\n\nEnter Your Choice : "))
    if(LO==1):
        Sal=int(input("\nEnter Your Monthly Income : "))
        if(Sal>=150000):
            print("\nYou Are Eligible To Apply For This Loan")
            LO1=int(input("\nThere Are 3 Types Of Long Term Loans : \n1.2 Years (2.5% Interest)\n2.5 Years (4% Interest)\n3.7 Years (4.5% Interest)\n\nEnter Your Choice : "))
            if(LO1==1):
                Q1=input("\nAre You A Employee Of The Company(Y/N) : ")
                if(Q1=="Y" or Q1=="y"):
                    Q2=int(input("Enter Your Employee ID : "))
                    for i in range(len(Emp_ID)):
                        if(Emp_ID[i]==Q2):#Searching Sorted Array
                            a=input(f"\nIs This The ID You Entered {Emp_ID[i]}(Y/N) :  ")
                            if(a=="Y" or a=="y"):
                                print(f"\nEmployee Of The Company Confirmed Employee ID Is : {Q2}")
                                print("You Will Only Have To Pay 2% Interest")
                                N=input("\nEnter Your Name : ")
                                Cnic=input("Enter Your CNIC Number : ")
                                pn=input("Enter Your Phone Number : ")
                                amount=input("Enter The Amount You Want For Loan : ")
                                print("\n\t\t\t\t\t=====================================")
                                print(f"\t\t\t\t\tName : {N}\n\t\t\t\t\tCNIC : {Cnic}\n\t\t\t\t\tPhone Number : {pn}\n\t\t\t\t\tLoan Type : Long Term (2 Years)\n\t\t\t\t\tEmployee Of The Company : Yes\n\t\t\t\t\tInterest To Pay : 2% Only\n\n\t\t\t\t\tLoan Request Is Sent,\n\t\t\t\t\tYou Will Get A Call Soon.")
                                print("\t\t\t\t\t=====================================")
                                Loans()
                            elif(a=="N" or a=="n"):
                                print("Wrong Employee ID")
                                Loans()
                    print("\nEmployee ID Not Found, Going Back To Previous Window")
                    Loans()
                elif(Q1=="N" or Q1=="n"):
                    Na=input("\nEnter Your Name : ")
                    Cnic=input("Enter Your CNIC Number : ")
                    pn=input("Enter Your Phone Number : ")
                    amount=input("Enter The Amount You Want For Loan : ")
                    print("\n\t\t\t\t\t=====================================")
                    print(f"\t\t\t\t\tName : {Na}\n\t\t\t\t\tCNIC : {Cnic}\n\t\t\t\t\tPhone Number : {pn}\n\t\t\t\t\tLoan Type : Long Term (2 Years)\n\t\t\t\t\tEmployee Of The Company : No\n\t\t\t\t\tInterest To Pay : 2.5% Only\n\n\t\t\t\t\tLoan Request Is Sent,\n\t\t\t\t\tYou Will Get A Call Soon.")
                    print("\t\t\t\t\t=====================================")
                    Loans()
            elif(LO1==2):
                Q1=input("\nAre You A Employee Of The Company(Y/N) : ")
                if(Q1=="Y" or Q1=="y"):
                    Q2=int(input("Enter Your Employee ID : "))
                    for i in range(len(Emp_ID)):
                        if(Emp_ID[i]==Q2):#Searching Sorted Array
                            a=input(f"\nIs This The ID You Entered {Emp_ID[i]}(Y/N) :  ")
                            if(a=="Y" or a=="y"):
                                print(f"\nEmployee Of The Company Confirmed Employee ID Is : {Q2}")
                                print("You Will Only Have To Pay 3% Interest")
                                N=input("\nEnter Your Name : ")
                                Cnic=input("Enter Your CNIC Number : ")
                                pn=input("Enter Your Phone Number : ")
                                amount=input("Enter The Amount You Want For Loan : ")
                                print("\n\t\t\t\t\t=====================================")
                                print(f"\t\t\t\t\tName : {N}\n\t\t\t\t\tCNIC : {Cnic}\n\t\t\t\t\tPhone Number : {pn}\n\t\t\t\t\tLoan Type : Long Term (5 Years)\n\t\t\t\t\tEmployee Of The Company : Yes\n\t\t\t\t\tInterest To Pay : 3% Only\n\n\t\t\t\t\tLoan Request Is Sent,\n\t\t\t\t\tYou Will Get A Call Soon.")
                                print("\t\t\t\t\t=====================================")
                                Loans()
                            elif(a=="N" or a=="n"):
                                print("Wrong Employee ID")
                                Loans()
                    print("\nEmployee ID Not Found, Going Back To Previous Window")
                    Loans()
                elif(Q1=="N" or Q1=="n"):
                    Na=input("\nEnter Your Name : ")
                    Cnic=input("Enter Your CNIC Number : ")
                    pn=input("Enter Your Phone Number : ")
                    amount=input("Enter The Amount You Want For Loan : ")
                    print("\n\t\t\t\t\t=====================================")
                    print(f"\t\t\t\t\tName : {Na}\n\t\t\t\t\tCNIC : {Cnic}\n\t\t\t\t\tPhone Number : {pn}\n\t\t\t\t\tLoan Type : Long Term (5 Years)\n\t\t\t\t\tEmployee Of The Company : No\n\t\t\t\t\tInterest To Pay : 4% Only\n\n\t\t\t\t\tLoan Request Is Sent,\n\t\t\t\t\tYou Will Get A Call Soon.")
                    print("\t\t\t\t\t=====================================")
                    Loans()
            elif(LO1==3):
                Q1=input("\nAre You A Employee Of The Company(Y/N) : ")
                if(Q1=="Y" or Q1=="y"):
                    Q2=int(input("Enter Your Employee ID : "))
                    for i in range(len(Emp_ID)):
                        if(Emp_ID[i]==Q2):#Searching Sorted Array
                            a=input(f"\nIs This The ID You Entered {Emp_ID[i]}(Y/N) :  ")
                            if(a=="Y" or a=="y"):
                                print(f"\nEmployee Of The Company Confirmed Employee ID Is : {Q2}")
                                print("You Will Only Have To Pay 4% Interest")
                                N=input("\nEnter Your Name : ")
                                Cnic=input("Enter Your CNIC Number : ")
                                pn=input("Enter Your Phone Number : ")
                                amount=input("Enter The Amount You Want For Loan : ")
                                print("\n\t\t\t\t\t=====================================")
                                print(f"\t\t\t\t\tName : {N}\n\t\t\t\t\tCNIC : {Cnic}\n\t\t\t\t\tPhone Number : {pn}\n\t\t\t\t\tLoan Type : Long Term (7 Years)\n\t\t\t\t\tEmployee Of The Company : Yes\n\t\t\t\t\tInterest To Pay : 4% Only\n\n\t\t\t\t\tLoan Request Is Sent,\n\t\t\t\t\tYou Will Get A Call Soon.")
                                print("\t\t\t\t\t=====================================")
                                Loans()
                            elif(a=="N" or a=="n"):
                                print("Wrong Employee ID")
                                Loans()
                    print("\nEmployee ID Not Found, Going Back To Previous Window")
                    Loans()
                elif(Q1=="N" or Q1=="n"):
                    Na=input("\nEnter Your Name : ")
                    Cnic=input("Enter Your CNIC Number : ")
                    pn=input("Enter Your Phone Number : ")
                    amount=input("Enter The Amount You Want For Loan : ")
                    print("\n\t\t\t\t\t=====================================")
                    print(f"\t\t\t\t\tName : {Na}\n\t\t\t\t\tCNIC : {Cnic}\n\t\t\t\t\tPhone Number : {pn}\n\t\t\t\t\tLoan Type : Long Term (7 Years)\n\t\t\t\t\tEmployee Of The Company : No\n\t\t\t\t\tInterest To Pay : 4.5% Only\n\n\t\t\t\t\tLoan Request Is Sent,\n\t\t\t\t\tYou Will Get A Call Soon.")
                    print("\t\t\t\t\t=====================================")
                    Loans()
            else:
                print("\nInvalid Input,Going Back To Loan Screen")
                Loans()
        elif(Sal<150000):
            print("\nYou Are Not Eligible To Apply For This Loan")
            Loans()
    elif(LO==2):
        Sal=int(input("\nEnter Your Monthly Income : "))
        if(Sal>=100000):
            print("\nYou Are Eligible To Apply For This Loan")
            LO1=int(input("\nThere Are 3 Types Of Long Term Loans : \n1.2 Months (2.5% Interest)\n2.5 Months (4% Interest)\n3.1 Year (4.5% Interest)\n\nEnter Your Choice : "))
            if(LO1==1):
                Q1=input("\nAre You A Employee Of The Company(Y/N) : ")
                if(Q1=="Y" or Q1=="y"):
                    Q2=int(input("Enter Your Employee ID : "))
                    for i in range(len(Emp_ID)):
                        if(Emp_ID[i]==Q2):#Searching Sorted Array
                            a=input(f"\nIs This The ID You Entered {Emp_ID[i]}(Y/N) :  ")
                            if(a=="Y" or a=="y"):
                                print(f"\nEmployee Of The Company Confirmed Employee ID Is : {Q2}")
                                print("You Will Only Have To Pay 2% Interest")
                                N=input("\nEnter Your Name : ")
                                Cnic=input("Enter Your CNIC Number : ")
                                pn=input("Enter Your Phone Number : ")
                                amount=input("Enter The Amount You Want For Loan : ")
                                print("\n\t\t\t\t\t=====================================")
                                print(f"\t\t\t\t\tName : {N}\n\t\t\t\t\tCNIC : {Cnic}\n\t\t\t\t\tPhone Number : {pn}\n\t\t\t\t\tLoan Type : Short Term (2 Months)\n\t\t\t\t\tEmployee Of The Company : Yes\n\t\t\t\t\tInterest To Pay : 2% Only\n\n\t\t\t\t\tLoan Request Is Sent,\n\t\t\t\t\tYou Will Get A Call Soon.")
                                print("\t\t\t\t\t=====================================")
                                Loans()
                            elif(a=="N" or a=="n"):
                                print("Wrong Employee ID")
                                Loans()
                    print("\nEmployee ID Not Found, Going Back To Previous Window")
                    Loans()
                elif(Q1=="N" or Q1=="n"):
                    Na=input("\nEnter Your Name : ")
                    Cnic=input("Enter Your CNIC Number : ")
                    pn=input("Enter Your Phone Number : ")
                    amount=input("Enter The Amount You Want For Loan : ")
                    print("\n\t\t\t\t\t=====================================")
                    print(f"\t\t\t\t\tName : {Na}\n\t\t\t\t\tCNIC : {Cnic}\n\t\t\t\t\tPhone Number : {pn}\n\t\t\t\t\tLoan Type : Short Term (2 Months)\n\t\t\t\t\tEmployee Of The Company : No\n\t\t\t\t\tInterest To Pay : 2.5% Only\n\n\t\t\t\t\tLoan Request Is Sent,\n\t\t\t\t\tYou Will Get A Call Soon.")
                    print("\t\t\t\t\t=====================================")
                    Loans()
            elif(LO1==2):
                Q1=input("\nAre You A Employee Of The Company(Y/N) : ")
                if(Q1=="Y" or Q1=="y"):
                    Q2=int(input("Enter Your Employee ID : "))
                    for i in range(len(Emp_ID)):
                        if(Emp_ID[i]==Q2):#Searching Sorted Array
                            a=input(f"\nIs This The ID You Entered {Emp_ID[i]}(Y/N) :  ")
                            if(a=="Y" or a=="y"):
                                print(f"\nEmployee Of The Company Confirmed Employee ID Is : {Q2}")
                                print("You Will Only Have To Pay 3% Interest")
                                N=input("\nEnter Your Name : ")
                                Cnic=input("Enter Your CNIC Number : ")
                                pn=input("Enter Your Phone Number : ")
                                amount=input("Enter The Amount You Want For Loan : ")
                                print("\n\t\t\t\t\t=====================================")
                                print(f"\t\t\t\t\tName : {N}\n\t\t\t\t\tCNIC : {Cnic}\n\t\t\t\t\tPhone Number : {pn}\n\t\t\t\t\tLoan Type : Short Term (5 Months)\n\t\t\t\t\tEmployee Of The Company : Yes\n\t\t\t\t\tInterest To Pay : 3% Only\n\n\t\t\t\t\tLoan Request Is Sent,\n\t\t\t\t\tYou Will Get A Call Soon.")
                                print("\t\t\t\t\t=====================================")
                                Loans()
                            elif(a=="N" or a=="n"):
                                print("Wrong Employee ID")
                                Loans()
                    print("\nEmployee ID Not Found, Going Back To Previous Window")
                    Loans()
                elif(Q1=="N" or Q1=="n"):
                    Na=input("\nEnter Your Name : ")
                    Cnic=input("Enter Your CNIC Number : ")
                    pn=input("Enter Your Phone Number : ")
                    amount=input("Enter The Amount You Want For Loan : ")
                    print("\n\t\t\t\t\t=====================================")
                    print(f"\t\t\t\t\tName : {Na}\n\t\t\t\t\tCNIC : {Cnic}\n\t\t\t\t\tPhone Number : {pn}\n\t\t\t\t\tLoan Type : Short Term (5 Months)\n\t\t\t\t\tEmployee Of The Company : No\n\t\t\t\t\tInterest To Pay : 4% Only\n\n\t\t\t\t\tLoan Request Is Sent,\n\t\t\t\t\tYou Will Get A Call Soon.")
                    print("\t\t\t\t\t=====================================")
                    Loans()
            elif(LO1==3):
                Q1=input("\nAre You A Employee Of The Company(Y/N) : ")
                if(Q1=="Y" or Q1=="y"):
                    Q2=int(input("Enter Your Employee ID : "))
                    for i in range(len(Emp_ID)):
                        if(Emp_ID[i]==Q2):#Searching Sorted Array
                            a=input(f"\nIs This The ID You Entered {Emp_ID[i]}(Y/N) :  ")
                            if(a=="Y" or a=="y"):
                                print(f"\nEmployee Of The Company Confirmed Employee ID Is : {Q2}")
                                print("You Will Only Have To Pay 4% Interest")
                                N=input("\nEnter Your Name : ")
                                Cnic=input("Enter Your CNIC Number : ")
                                pn=input("Enter Your Phone Number : ")
                                amount=input("Enter The Amount You Want For Loan : ")
                                print("\n\t\t\t\t\t=====================================")
                                print(f"\t\t\t\t\tName : {N}\n\t\t\t\t\tCNIC : {Cnic}\n\t\t\t\t\tPhone Number : {pn}\n\t\t\t\t\tLoan Type : Short Term (1 Year)\n\t\t\t\t\tEmployee Of The Company : Yes\n\t\t\t\t\tInterest To Pay : 4% Only\n\n\t\t\t\t\tLoan Request Is Sent,\n\t\t\t\t\tYou Will Get A Call Soon.")
                                print("\t\t\t\t\t=====================================")
                                Loans()
                            elif(a=="N" or a=="n"):
                                print("Wrong Employee ID")
                                Loans()
                    print("\nEmployee ID Not Found, Going Back To Previous Window")
                    Loans()
                elif(Q1=="N" or Q1=="n"):
                    Na=input("\nEnter Your Name : ")
                    Cnic=input("Enter Your CNIC Number : ")
                    pn=input("Enter Your Phone Number : ")
                    amount=input("Enter The Amount You Want For Loan : ")
                    print("\n\t\t\t\t\t=====================================")
                    print(f"\t\t\t\t\tName : {Na}\n\t\t\t\t\tCNIC : {Cnic}\n\t\t\t\t\tPhone Number : {pn}\n\t\t\t\t\tLoan Type : Short Term (1 Year)\n\t\t\t\t\tEmployee Of The Company : No\n\t\t\t\t\tInterest To Pay : 4.5% Only\n\n\t\t\t\t\tLoan Request Is Sent,\n\t\t\t\t\tYou Will Get A Call Soon.")
                    print("\t\t\t\t\t=====================================")
                    Loans()
            else:
                print("\nInvalid Input,Going Back To Loan Screen")
                Loans()
        elif(Sal<100000):
            print("\nYou Are Not Eligible To Apply For This Loan")
            Loans()
    else:
        print("\nInvalid Input,Going Back To Previous Screen")
        Loans()

def PropertyLoan():
    from numpy import array
    import pyodbc
    conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=NOMIR-PC\SQLEXPRESS;'
                      'Database=Project;'
                      'Trusted_Connection=yes;')
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM Employee_ID")
    Emp_ID=array([0 for i in range(10)])
    i=0
    for row in cursor:
        Emp_ID[i]=row[0]
        i=i+1
    for i in range(1,len(Emp_ID)):
        T_Value=Emp_ID[i]
        j=i-1
        while(j >= 0 and T_Value<Emp_ID[j]):
                Emp_ID[j + 1]=Emp_ID[j]
                j=j-1
        Emp_ID[j+1]=T_Value
    LO=int(input("\nThere Are Two Types Of Property Loans We Offer :\n1.Long Term\n2.Short Term\n\nEnter Your Choice : "))
    if(LO==1):
        Sal=int(input("\nEnter Your Monthly Income : "))
        if(Sal>=150000):
            print("\nYou Are Eligible To Apply For This Loan")
            LO1=int(input("\nThere Are 3 Types Of Long Term Loans : \n1.2 Years (2.5% Interest)\n2.5 Years (4% Interest)\n3.7 Years (4.5% Interest)\n\nEnter Your Choice : "))
            if(LO1==1):
                Q1=input("\nAre You A Employee Of The Company(Y/N) : ")
                if(Q1=="Y" or Q1=="y"):
                    Q2=int(input("Enter Your Employee ID : "))
                    low=0
                    high=len(Emp_ID)-1
                    mid=0
                    while(low<=high):
                        mid=(high+low)//2
                        if(Emp_ID[mid]<Q2):
                            low=mid+1
                        elif(Emp_ID[mid]>Q2):
                            high=mid-1
                        else:
                            a=input(f"\nIs This The ID You Entered {Emp_ID[mid]}(Y/N) :  ")
                            if(a=="Y" or a=="y"):
                                print(f"\nEmployee Of The Company Confirmed Employee ID Is : {Q2}")
                                print("You Will Only Have To Pay 2% Interest")
                                N=input("\nEnter Your Name : ")
                                Cnic=input("Enter Your CNIC Number : ")
                                pn=input("Enter Your Phone Number : ")
                                amount=input("Enter The Amount You Want For Loan : ")
                                print("\n\t\t\t\t\t=====================================")
                                print(f"\t\t\t\t\tName : {N}\n\t\t\t\t\tCNIC : {Cnic}\n\t\t\t\t\tPhone Number : {pn}\n\t\t\t\t\tLoan Type : Long Term (2 Years)\n\t\t\t\t\tEmployee Of The Company : Yes\n\t\t\t\t\tInterest To Pay : 2% Only\n\n\t\t\t\t\tLoan Request Is Sent,\n\t\t\t\t\tYou Will Get A Call Soon.")
                                print("\t\t\t\t\t=====================================")
                                Loans()
                            elif(a=="N" or a=="n"):
                                print("Wrong Employee ID")
                                Loans()
                    print("\nEmployee ID Not Found, Going Back To Previous Window")
                    Loans()
                elif(Q1=="N" or Q1=="n"):
                    Na=input("\nEnter Your Name : ")
                    Cnic=input("Enter Your CNIC Number : ")
                    pn=input("Enter Your Phone Number : ")
                    amount=input("Enter The Amount You Want For Loan : ")
                    print("\n\t\t\t\t\t=====================================")
                    print(f"\t\t\t\t\tName : {Na}\n\t\t\t\t\tCNIC : {Cnic}\n\t\t\t\t\tPhone Number : {pn}\n\t\t\t\t\tLoan Type : Long Term (2 Years)\n\t\t\t\t\tEmployee Of The Company : No\n\t\t\t\t\tInterest To Pay : 2.5% Only\n\n\t\t\t\t\tLoan Request Is Sent,\n\t\t\t\t\tYou Will Get A Call Soon.")
                    print("\t\t\t\t\t=====================================")
                    Loans()
            elif(LO1==2):
                Q1=input("\nAre You A Employee Of The Company(Y/N) : ")
                if(Q1=="Y" or Q1=="y"):
                    Q2=int(input("Enter Your Employee ID : "))
                    low=0
                    high=len(Emp_ID)-1
                    mid=0
                    while(low<=high):
                        mid=(high+low)//2
                        if(Emp_ID[mid]<Q2):
                            low=mid+1
                        elif(Emp_ID[mid]>Q2):
                            high=mid-1
                        else:
                            a=input(f"\nIs This The ID You Entered {Emp_ID[mid]}(Y/N) :  ")
                            if(a=="Y" or a=="y"):
                                print(f"\nEmployee Of The Company Confirmed Employee ID Is : {Q2}")
                                print("You Will Only Have To Pay 3% Interest")
                                N=input("\nEnter Your Name : ")
                                Cnic=input("Enter Your CNIC Number : ")
                                pn=input("Enter Your Phone Number : ")
                                amount=input("Enter The Amount You Want For Loan : ")
                                print("\n\t\t\t\t\t=====================================")
                                print(f"\t\t\t\t\tName : {N}\n\t\t\t\t\tCNIC : {Cnic}\n\t\t\t\t\tPhone Number : {pn}\n\t\t\t\t\tLoan Type : Long Term (5 Years)\n\t\t\t\t\tEmployee Of The Company : Yes\n\t\t\t\t\tInterest To Pay : 3% Only\n\n\t\t\t\t\tLoan Request Is Sent,\n\t\t\t\t\tYou Will Get A Call Soon.")
                                print("\t\t\t\t\t=====================================")
                                Loans()
                            elif(a=="N" or a=="n"):
                                print("Wrong Employee ID")
                                Loans()
                    print("\nEmployee ID Not Found, Going Back To Previous Window")
                    Loans()
                elif(Q1=="N" or Q1=="n"):
                    Na=input("\nEnter Your Name : ")
                    Cnic=input("Enter Your CNIC Number : ")
                    pn=input("Enter Your Phone Number : ")
                    amount=input("Enter The Amount You Want For Loan : ")
                    print("\n\t\t\t\t\t=====================================")
                    print(f"\t\t\t\t\tName : {Na}\n\t\t\t\t\tCNIC : {Cnic}\n\t\t\t\t\tPhone Number : {pn}\n\t\t\t\t\tLoan Type : Long Term (5 Years)\n\t\t\t\t\tEmployee Of The Company : No\n\t\t\t\t\tInterest To Pay : 4% Only\n\n\t\t\t\t\tLoan Request Is Sent,\n\t\t\t\t\tYou Will Get A Call Soon.")
                    print("\t\t\t\t\t=====================================")
                    Loans()
            elif(LO1==3):
                Q1=input("\nAre You A Employee Of The Company(Y/N) : ")
                if(Q1=="Y" or Q1=="y"):
                    Q2=int(input("Enter Your Employee ID : "))
                    low=0
                    high=len(Emp_ID)-1
                    mid=0
                    while(low<=high):
                        mid=(high+low)//2
                        if(Emp_ID[mid]<Q2):
                            low=mid+1
                        elif(Emp_ID[mid]>Q2):
                            high=mid-1
                        else:
                            a=input(f"\nIs This The ID You Entered {Emp_ID[mid]}(Y/N) :  ")
                            if(a=="Y" or a=="y"):
                                print(f"\nEmployee Of The Company Confirmed Employee ID Is : {Q2}")
                                print("You Will Only Have To Pay 4% Interest")
                                N=input("\nEnter Your Name : ")
                                Cnic=input("Enter Your CNIC Number : ")
                                pn=input("Enter Your Phone Number : ")
                                amount=input("Enter The Amount You Want For Loan : ")
                                print("\n\t\t\t\t\t=====================================")
                                print(f"\t\t\t\t\tName : {N}\n\t\t\t\t\tCNIC : {Cnic}\n\t\t\t\t\tPhone Number : {pn}\n\t\t\t\t\tLoan Type : Long Term (7 Years)\n\t\t\t\t\tEmployee Of The Company : Yes\n\t\t\t\t\tInterest To Pay : 4% Only\n\n\t\t\t\t\tLoan Request Is Sent,\n\t\t\t\t\tYou Will Get A Call Soon.")
                                print("\t\t\t\t\t=====================================")
                                Loans()
                            elif(a=="N" or a=="n"):
                                print("Wrong Employee ID")
                                Loans()
                    print("\nEmployee ID Not Found, Going Back To Previous Window")
                    Loans()
                elif(Q1=="N" or Q1=="n"):
                    Na=input("\nEnter Your Name : ")
                    Cnic=input("Enter Your CNIC Number : ")
                    pn=input("Enter Your Phone Number : ")
                    amount=input("Enter The Amount You Want For Loan : ")
                    print("\n\t\t\t\t\t=====================================")
                    print(f"\t\t\t\t\tName : {Na}\n\t\t\t\t\tCNIC : {Cnic}\n\t\t\t\t\tPhone Number : {pn}\n\t\t\t\t\tLoan Type : Long Term (7 Years)\n\t\t\t\t\tEmployee Of The Company : No\n\t\t\t\t\tInterest To Pay : 4.5% Only\n\n\t\t\t\t\tLoan Request Is Sent,\n\t\t\t\t\tYou Will Get A Call Soon.")
                    print("\t\t\t\t\t=====================================")
                    Loans()
            else:
                print("\nInvalid Input,Going Back To Loan Screen")
                Loans()
        elif(Sal<150000):
            print("\nYou Are Not Eligible To Apply For This Loan")
            Loans()
    elif(LO==2):
        Sal=int(input("\nEnter Your Monthly Income : "))
        if(Sal>=100000):
            print("\nYou Are Eligible To Apply For This Loan")
            LO1=int(input("\nThere Are 3 Types Of Long Term Loans : \n1.2 Months (2.5% Interest)\n2.5 Months (4% Interest)\n3.1 Year (4.5% Interest)\n\nEnter Your Choice : "))
            if(LO1==1):
                Q1=input("\nAre You A Employee Of The Company(Y/N) : ")
                if(Q1=="Y" or Q1=="y"):
                    Q2=int(input("Enter Your Employee ID : "))
                    low=0
                    high=len(Emp_ID)-1
                    mid=0
                    while(low<=high):
                        mid=(high+low)//2
                        if(Emp_ID[mid]<Q2):
                            low=mid+1
                        elif(Emp_ID[mid]>Q2):
                            high=mid-1
                        else:
                            a=input(f"\nIs This The ID You Entered {Emp_ID[mid]}(Y/N) :  ")
                            if(a=="Y" or a=="y"):
                                print(f"\nEmployee Of The Company Confirmed Employee ID Is : {Q2}")
                                print("You Will Only Have To Pay 2% Interest")
                                N=input("\nEnter Your Name : ")
                                Cnic=input("Enter Your CNIC Number : ")
                                pn=input("Enter Your Phone Number : ")
                                amount=input("Enter The Amount You Want For Loan : ")
                                print("\n\t\t\t\t\t=====================================")
                                print(f"\t\t\t\t\tName : {N}\n\t\t\t\t\tCNIC : {Cnic}\n\t\t\t\t\tPhone Number : {pn}\n\t\t\t\t\tLoan Type : Short Term (2 Months)\n\t\t\t\t\tEmployee Of The Company : Yes\n\t\t\t\t\tInterest To Pay : 2% Only\n\n\t\t\t\t\tLoan Request Is Sent,\n\t\t\t\t\tYou Will Get A Call Soon.")
                                print("\t\t\t\t\t=====================================")
                                Loans()
                            elif(a=="N" or a=="n"):
                                print("Wrong Employee ID")
                                Loans()
                    print("\nEmployee ID Not Found, Going Back To Previous Window")
                    Loans()
                elif(Q1=="N" or Q1=="n"):
                    Na=input("\nEnter Your Name : ")
                    Cnic=input("Enter Your CNIC Number : ")
                    pn=input("Enter Your Phone Number : ")
                    amount=input("Enter The Amount You Want For Loan : ")
                    print("\n\t\t\t\t\t=====================================")
                    print(f"\t\t\t\t\tName : {Na}\n\t\t\t\t\tCNIC : {Cnic}\n\t\t\t\t\tPhone Number : {pn}\n\t\t\t\t\tLoan Type : Short Term (2 Months)\n\t\t\t\t\tEmployee Of The Company : No\n\t\t\t\t\tInterest To Pay : 2.5% Only\n\n\t\t\t\t\tLoan Request Is Sent,\n\t\t\t\t\tYou Will Get A Call Soon.")
                    print("\t\t\t\t\t=====================================")
                    Loans()
            elif(LO1==2):
                Q1=input("\nAre You A Employee Of The Company(Y/N) : ")
                if(Q1=="Y" or Q1=="y"):
                    Q2=int(input("Enter Your Employee ID : "))
                    low=0
                    high=len(Emp_ID)-1
                    mid=0
                    while(low<=high):
                        mid=(high+low)//2
                        if(Emp_ID[mid]<Q2):
                            low=mid+1
                        elif(Emp_ID[mid]>Q2):
                            high=mid-1
                        else:
                            a=input(f"\nIs This The ID You Entered {Emp_ID[mid]}(Y/N) :  ")
                            if(a=="Y" or a=="y"):
                                print(f"\nEmployee Of The Company Confirmed Employee ID Is : {Q2}")
                                print("You Will Only Have To Pay 3% Interest")
                                N=input("\nEnter Your Name : ")
                                Cnic=input("Enter Your CNIC Number : ")
                                pn=input("Enter Your Phone Number : ")
                                amount=input("Enter The Amount You Want For Loan : ")
                                print("\n\t\t\t\t\t=====================================")
                                print(f"\t\t\t\t\tName : {N}\n\t\t\t\t\tCNIC : {Cnic}\n\t\t\t\t\tPhone Number : {pn}\n\t\t\t\t\tLoan Type : Short Term (5 Months)\n\t\t\t\t\tEmployee Of The Company : Yes\n\t\t\t\t\tInterest To Pay : 3% Only\n\n\t\t\t\t\tLoan Request Is Sent,\n\t\t\t\t\tYou Will Get A Call Soon.")
                                print("\t\t\t\t\t=====================================")
                                Loans()
                            elif(a=="N" or a=="n"):
                                print("Wrong Employee ID")
                                Loans()
                    print("\nEmployee ID Not Found, Going Back To Previous Window")
                    Loans()
                elif(Q1=="N" or Q1=="n"):
                    Na=input("\nEnter Your Name : ")
                    Cnic=input("Enter Your CNIC Number : ")
                    pn=input("Enter Your Phone Number : ")
                    amount=input("Enter The Amount You Want For Loan : ")
                    print("\n\t\t\t\t\t=====================================")
                    print(f"\t\t\t\t\tName : {Na}\n\t\t\t\t\tCNIC : {Cnic}\n\t\t\t\t\tPhone Number : {pn}\n\t\t\t\t\tLoan Type : Short Term (5 Months)\n\t\t\t\t\tEmployee Of The Company : No\n\t\t\t\t\tInterest To Pay : 4% Only\n\n\t\t\t\t\tLoan Request Is Sent,\n\t\t\t\t\tYou Will Get A Call Soon.")
                    print("\t\t\t\t\t=====================================")
                    Loans()
            elif(LO1==3):
                Q1=input("\nAre You A Employee Of The Company(Y/N) : ")
                if(Q1=="Y" or Q1=="y"):
                    Q2=int(input("Enter Your Employee ID : "))
                    low=0
                    high=len(Emp_ID)-1
                    mid=0
                    while(low<=high):
                        mid=(high+low)//2
                        if(Emp_ID[mid]<Q2):
                            low=mid+1
                        elif(Emp_ID[mid]>Q2):
                            high=mid-1
                        else:
                            a=input(f"\nIs This The ID You Entered {Emp_ID[mid]}(Y/N) :  ")
                            if(a=="Y" or a=="y"):
                                print(f"\nEmployee Of The Company Confirmed Employee ID Is : {Q2}")
                                print("You Will Only Have To Pay 4% Interest")
                                N=input("\nEnter Your Name : ")
                                Cnic=input("Enter Your CNIC Number : ")
                                pn=input("Enter Your Phone Number : ")
                                amount=input("Enter The Amount You Want For Loan : ")
                                print("\n\t\t\t\t\t=====================================")
                                print(f"\t\t\t\t\tName : {N}\n\t\t\t\t\tCNIC : {Cnic}\n\t\t\t\t\tPhone Number : {pn}\n\t\t\t\t\tLoan Type : Short Term (1 Year)\n\t\t\t\t\tEmployee Of The Company : Yes\n\t\t\t\t\tInterest To Pay : 4% Only\n\n\t\t\t\t\tLoan Request Is Sent,\n\t\t\t\t\tYou Will Get A Call Soon.")
                                print("\t\t\t\t\t=====================================")
                                Loans()
                            elif(a=="N" or a=="n"):
                                print("Wrong Employee ID")
                                Loans()
                    print("\nEmployee ID Not Found, Going Back To Previous Window")
                    Loans()
                elif(Q1=="N" or Q1=="n"):
                    Na=input("\nEnter Your Name : ")
                    Cnic=input("Enter Your CNIC Number : ")
                    pn=input("Enter Your Phone Number : ")
                    amount=input("Enter The Amount You Want For Loan : ")
                    print("\n\t\t\t\t\t=====================================")
                    print(f"\t\t\t\t\tName : {Na}\n\t\t\t\t\tCNIC : {Cnic}\n\t\t\t\t\tPhone Number : {pn}\n\t\t\t\t\tLoan Type : Short Term (1 Year)\n\t\t\t\t\tEmployee Of The Company : No\n\t\t\t\t\tInterest To Pay : 4.5% Only\n\n\t\t\t\t\tLoan Request Is Sent,\n\t\t\t\t\tYou Will Get A Call Soon.")
                    print("\t\t\t\t\t=====================================")
                    Loans()
            else:
                print("\nInvalid Input,Going Back To Loan Screen")
                Loans()
        elif(Sal<100000):
            print("\nYou Are Not Eligible To Apply For This Loan")
            Loans()
    else:
        print("\nInvalid Input,Going Back To Previous Screen")
        Loans()

def UtilityBills():
    print("\t\t\t\t\t=====================================")
    print("\t\t\t\t\t|\t    Utility Bills\t    |")
    print("\t\t\t\t\t=====================================")
    print("\n\t\t\t\t\t1.Electricity\t\t\t2.Gas\n\n\t\t\t\t\t3.Water\t\t\t\t4.Back")
    print("\nUtility Bills Can Only Be Paid In Cash")
    choice=int(input("\nEnter Your Choice : "))
    if(choice==1):
        ElectricityB()
    elif(choice==2):
        GasB()
    elif(choice==3):
        WaterB()
    elif(choice==4):
        LoginAccount()

def ElectricityB():
    D1=int(input("\nEnter Current Date Of The Month : "))
    D2=int(input("Enter The Bill Due Date Of The Month : "))
    BA=int(input("\nEnter The Amount Of Your Bill : "))
    if(D1<=D2):
        print(f"\nPlease Pay Bill Amount {BA}")
        LoginAccount()
    elif(D1>D2):
        BA2=int(input("Enter The Due Amount Of Your Bill : "))
        BA2=BA+BA2
        print(f"\nPlease Pay Bill Amount {BA2}")
        LoginAccount()

def GasB():
    D1=int(input("\nEnter Current Date Of The Month : "))
    D2=int(input("Enter The Bill Due Date Of The Month : "))
    BA=int(input("\nEnter The Amount Of Your Bill : "))
    if(D1<=D2):
        print(f"\nPlease Pay Bill Amount {BA}")
        LoginAccount()
    elif(D1>D2):
        BA2=int(input("Enter The Due Amount Of Your Bill : "))
        BA2=BA+BA2
        print(f"\nPlease Pay Bill Amount {BA2}")
        LoginAccount()

def WaterB():
    D1=int(input("\nEnter Current Date Of The Month : "))
    D2=int(input("Enter The Bill Due Date Of The Month : "))
    BA=int(input("\nEnter The Amount Of Your Bill : "))
    if(D1<=D2):
        print(f"\nPlease Pay Bill Amount {BA}")
        LoginAccount()
    elif(D1>D2):
        BA2=int(input("Enter The Due Amount Of Your Bill : "))
        BA2=BA+BA2
        print(f"\nPlease Pay Bill Amount {BA2}")
        LoginAccount()

def UtilityBills2():
    print("\t\t\t\t\t=====================================")
    print("\t\t\t\t\t|\t    Utility Bills\t    |")
    print("\t\t\t\t\t=====================================")
    print("\n\t\t\t\t\t1.Electricity\t\t\t2.Gas\n\n\t\t\t\t\t3.Water\t\t\t\t4.Back")
    print("\nUtility Bills Can Only Be Paid In Cash")
    choice=int(input("\nEnter Your Choice : "))
    if(choice==1):
        ElectricityB2()
    elif(choice==2):
        GasB2()
    elif(choice==3):
        WaterB2()
    elif(choice==4):
        Home()

def ElectricityB2():
    D1=int(input("\nEnter Current Date Of The Month : "))
    D2=int(input("Enter The Bill Due Date Of The Month : "))
    BA=int(input("\nEnter The Amount Of Your Bill : "))
    if(D1<=D2):
        print(f"\nPlease Pay Bill Amount {BA}")
        Home()
    elif(D1>D2):
        BA2=int(input("Enter The Due Amount Of Your Bill : "))
        BA2=BA+BA2
        print(f"\nPlease Pay Bill Amount {BA2}")
        Home()

def GasB2():
    D1=int(input("\nEnter Current Date Of The Month : "))
    D2=int(input("Enter The Bill Due Date Of The Month : "))
    BA=int(input("\nEnter The Amount Of Your Bill : "))
    if(D1<=D2):
        print(f"\nPlease Pay Bill Amount {BA}")
        Home()
    elif(D1>D2):
        BA2=int(input("Enter The Due Amount Of Your Bill : "))
        BA2=BA+BA2
        print(f"\nPlease Pay Bill Amount {BA2}")
        Home()

def WaterB2():
    D1=int(input("\nEnter Current Date Of The Month : "))
    D2=int(input("Enter The Bill Due Date Of The Month : "))
    BA=int(input("\nEnter The Amount Of Your Bill : "))
    if(D1<=D2):
        print(f"\nPlease Pay Bill Amount {BA}")
        Home()
    elif(D1>D2):
        BA2=int(input("Enter The Due Amount Of Your Bill : "))
        BA2=BA+BA2
        print(f"\nPlease Pay Bill Amount {BA2}")
        Home()

def CurrencyExchange():
    print("\t\t\t\t\t=====================================")
    print("\t\t\t\t\t|\t   Currency Exchange\t    |")
    print("\t\t\t\t\t=====================================")
    print("\n\t\t\t\t1.US Dollar(USD)\t\t2.European Euro(EUR) \n\n\t\t\t\t3.Japanese Yen(JPY)\t\t4.Sterling Pound(GBP)\n\n\t\t\t\t5.Swiss Franc(CHF)\t\t6.Canadian Dollar(CAD)\n\n\t\t\t\t7.South African Rand(ZAR)\t8.Chinese Renminbi(CNH)")
    print("\nOur Primary Currency Is Pakistani Rupee(PKR)\nSo All Of These Currencies Can Either Be Converted Into Pakistani Rupee Or Vice Versa\nWe Only Deal In Cash")
    choice=int(input("\nEnter Your Choice(OR Press 9 To Go Back) : "))
    if(choice==1):
        USD_TO_PKR()
    elif(choice==2):
        EUR_TO_PKR()
    elif(choice==3):
        JPY_TO_PKR()
    elif(choice==4):
        GBP_TO_PKR()
    elif(choice==5):
        CHF_TO_PKR()
    elif(choice==6):
        CAD_TO_PKR()
    elif(choice==7):
        ZAR_TO_PKR()
    elif(choice==8):
        CNH_TO_PKR()
    elif(choice==9):
        LoginAccount()

def USD_TO_PKR():
    print("\n1.Convert From USD To PKR\n2.Convert From PKR To USD")
    Q1=int(input("\nEnter Your Choice : "))
    if(Q1==1):
        A1=int(input("\nEnter Your Amount In Dollars : "))
        A2=float(A1*153.55)
        A3=round(A2,3)
        print(f"\nThis Is Your Converted Amount : {A3} PKR\nPlease Collect It\n")
        LoginAccount()
    elif(Q1==2):
        A1=int(input("\nEnter Your Amount In Pakistani Rupees : "))
        A2=float(A1/153.55)
        A3=round(A2,3)
        print(f"\nThis Is Your Converted Amount {A3} USD\nPlease Collect It\n")
        LoginAccount()

def EUR_TO_PKR():
    print("\n1.Convert From EUR To PKR\n2.Convert From PKR To EUR")
    Q1=int(input("\nEnter Your Choice : "))
    if(Q1==1):
        A1=int(input("\nEnter Your Amount In European Euro : "))
        A2=float(A1*180.60)
        A3=round(A2,3)
        print(f"\nThis Is Your Converted Amount : {A3} PKR\nPlease Collect It\n")
        LoginAccount()
    elif(Q1==2):
        A1=int(input("\nEnter Your Amount In Pakistani Rupees : "))
        A2=float(A1/180.60)
        A3=round(A2,3)
        print(f"\nThis Is Your Converted Amount {A3} USD\nPlease Collect It\n")
        LoginAccount()

def JPY_TO_PKR():
    print("\n1.Convert From JPY To PKR\n2.Convert From PKR To JPY")
    Q1=int(input("\nEnter Your Choice : "))
    if(Q1==1):
        A1=int(input("\nEnter Your Amount In Japanese Yen : "))
        A2=float(A1*1.39)
        A3=round(A2,3)
        print(f"\nThis Is Your Converted Amount : {A3} PKR\nPlease Collect It\n")
        LoginAccount()
    elif(Q1==2):
        A1=int(input("\nEnter Your Amount In Pakistani Rupees : "))
        A2=float(A1/1.39)
        A3=round(A2,3)
        print(f"\nThis Is Your Converted Amount {A3} USD\nPlease Collect It\n")
        LoginAccount()

def GBP_TO_PKR():
    print("\n1.Convert From GBP To PKR\n2.Convert From PKR To GBP")
    Q1=int(input("\nEnter Your Choice : "))
    if(Q1==1):
        A1=int(input("\nEnter Your Amount In Sterling Pound : "))
        A2=float(A1*212.33)
        A3=round(A2,3)
        print(f"\nThis Is Your Converted Amount : {A3} PKR\nPlease Collect It\n")
        LoginAccount()
    elif(Q1==2):
        A1=int(input("\nEnter Your Amount In Pakistani Rupees : "))
        A2=float(A1/212.33)
        A3=round(A2,3)
        print(f"\nThis Is Your Converted Amount {A3} USD\nPlease Collect It\n")
        LoginAccount()

def CHF_TO_PKR():
    print("\n1.Convert From CHF To PKR\n2.Convert From PKR To CHF")
    Q1=int(input("\nEnter Your Choice : "))
    if(Q1==1):
        A1=int(input("\nEnter Your Amount In Swiss Franc : "))
        A2=float(A1*162.82)
        A3=round(A2,3)
        print(f"\nThis Is Your Converted Amount : {A3} PKR\nPlease Collect It\n")
        LoginAccount()
    elif(Q1==2):
        A1=int(input("\nEnter Your Amount In Pakistani Rupees : "))
        A2=float(A1/162.82)
        A3=round(A2,3)
        print(f"\nThis Is Your Converted Amount {A3} USD\nPlease Collect It\n")
        LoginAccount()

def CAD_TO_PKR():
    print("\n1.Convert From CAD To PKR\n2.Convert From PKR To CAD")
    Q1=int(input("\nEnter Your Choice : "))
    if(Q1==1):
        A1=int(input("\nEnter Your Amount In Canadian Dollar : "))
        A2=float(A1*122.09)
        A3=round(A2,3)
        print(f"\nThis Is Your Converted Amount : {A3} PKR\nPlease Collect It\n")
        LoginAccount()
    elif(Q1==2):
        A1=int(input("\nEnter Your Amount In Pakistani Rupees : "))
        A2=float(A1/122.09)
        A3=round(A2,3)
        print(f"\nThis Is Your Converted Amount {A3} USD\nPlease Collect It\n")
        LoginAccount()

def ZAR_TO_PKR():
    print("\n1.Convert From ZAR To PKR\n2.Convert From PKR To ZAR")
    Q1=int(input("\nEnter Your Choice : "))
    if(Q1==1):
        A1=int(input("\nEnter Your Amount In South African Rand : "))
        A2=float(A1*10.47)
        A3=round(A2,3)
        print(f"\nThis Is Your Converted Amount : {A3} PKR\nPlease Collect It\n")
        LoginAccount()
    elif(Q1==2):
        A1=int(input("\nEnter Your Amount In Pakistani Rupees : "))
        A2=float(A1/10.47)
        A3=round(A2,3)
        print(f"\nThis Is Your Converted Amount {A3} USD\nPlease Collect It\n")
        LoginAccount()

def CNH_TO_PKR():
    print("\n1.Convert From CNH To PKR\n2.Convert From PKR To CNH")
    Q1=int(input("\nEnter Your Choice : "))
    if(Q1==1):
        A1=int(input("\nEnter Your Amount In Chinese Renminbi : "))
        A2=float(A1*23.38)
        A3=round(A2,3)
        print(f"\nThis Is Your Converted Amount : {A3} PKR\nPlease Collect It\n")
        LoginAccount()
    elif(Q1==2):
        A1=int(input("\nEnter Your Amount In Pakistani Rupees : "))
        A2=float(A1/23.38)
        A3=round(A2,3)
        print(f"\nThis Is Your Converted Amount {A3} USD\nPlease Collect It\n")
        LoginAccount()

def Consultancy():
    print("\t\t\t\t\t=====================================")
    print("\t\t\t\t\t|\t      Consultancy\t    |")
    print("\t\t\t\t\t=====================================")
    print("\n\t\t\t\t1.How To Open Account\t\t2.How To Log In To Account\n\n\t\t\t\t3.How To Deposit Money\t\t4.How To Withdraw Money\n\n\t\t\t\t5.How To Exchange Currency\t6.How To Pay Utility Bill\n\n\t\t\t\t7.How To Use ATM\t\t8.How To Apply For Loan")
    choice=int(input("\nEnter Your Choice(OR Press 9 To Go Back) : "))
    if(choice==1):
        Consultancy_Q1()
    elif(choice==2):
        Consultancy_Q2()
    elif(choice==3):
        Consultancy_Q3()
    elif(choice==4):
        Consultancy_Q4()
    elif(choice==5):
        Consultancy_Q5()
    elif(choice==6):
        Consultancy_Q6()
    elif(choice==7):
        Consultancy_Q7()
    elif(choice==8):
        Consultancy_Q8()
    elif(choice==9):
        Home()
    else:
        print("Invalid Input")
        Home()

def Consultancy_Q1():
    print("\nStep 1 : Go To Home Screen")
    print("Step 2 : Select Choice Number 1")
    print("Step 3 : Select Which Account You Want To Create\n\t Select Choice Number 1 For A Current Account OR Select Choice Number 2 For A Savings Account")
    print("Step 4 : Enter All The Required Details")
    print("Step 5 : Wait For It To Process Until You See Your Information On Screen")
    print("\nIf You Follow These Steps Correctly, Your Account Will Be Created")
    Q1=int(input("\nPress 1 If You Want To Ask More Quetions OR Press 2 To Go To Previous Screen : "))
    if(Q1==1):
        print()
        Consultancy()
    elif(Q1==2):
        print()
        Home()
    else:
        print("Invalid Input")
        print()
        Home()

def Consultancy_Q2():
    print("\nStep 1 : Go To Home Screen")
    print("Step 2 : Select Choice Number 2")
    print("Step 3 : First Enter Your Name And Then Enter Your Account Number")
    print("Step 4 : Wait For It To Process Until You See Your Information On Screen And The Logged In Menu")
    print("\nIf You Follow These Steps Correctly, Choosen Operation Will Be Successful")
    Q1=int(input("\nPress 1 If You Want To Ask More Quetions OR Press 2 To Go To Previous Screen : "))
    if(Q1==1):
        print()
        Consultancy()
    elif(Q1==2):
        print()
        Home()
    else:
        print("Invalid Input")
        print()
        Home()

def Consultancy_Q3():
    print("\nThis Can Only Be Done If You Are Logged In Into Your Account")
    print("\nStep 1 : Log In Into Your Account")
    print("Step 2 : Select Choice Number 1")
    print("Step 3 : Enter The Amount You Want To Deposit")
    print("Step 4 : Wait For It To Process Until You A Get Message")
    print("\nIf You Follow These Steps Correctly, Your Choosen Operation Will Be Successful")
    Q1=int(input("\nPress 1 If You Want To Ask More Quetions OR Press 2 To Go To Previous Screen : "))
    if(Q1==1):
        print()
        Consultancy()
    elif(Q1==2):
        print()
        Home()
    else:
        print("Invalid Input")
        print()
        Home()

def Consultancy_Q4():
    print("\nThis Can Only Be Done If You Are Logged In Into Your Account")
    print("\nStep 1 : Log In Into Your Account")
    print("Step 2 : Select Choice Number 2")
    print("Step 3 : Enter The Amount You Want To Withdraw")
    print("Step 4 : Make Sure To Have More Than Rs.1000 In Your Account\n\t If You Don't Have More Than Rs.1000 Your Transaction Won't Be Successful")
    print("Step 5 : Wait For It To Process Until You A Get Message")
    print("\nIf You Follow These Steps Correctly, Your Choosen Operation Will Be Successful")
    Q1=int(input("\nPress 1 If You Want To Ask More Quetions OR Press 2 To Go To Previous Screen : "))
    if(Q1==1):
        print()
        Consultancy()
    elif(Q1==2):
        print()
        Home()
    else:
        print("Invalid Input")
        print()
        Home()

def Consultancy_Q5():
    print("\nThis Can Only Be Done If You Are Logged In Into Your Account(ONLY CASH)")
    print("\nStep 1 : Log In Into Your Account")
    print("Step 2 : Select Choice Number 8")
    print("Step 3 : Enter Your Choice In Which Currency You Want To Deal In")
    print("Step 4 : Enter Your Choice If You Want To Convert Into Your Choosen Currency\n\t OR Into Pakistani Rupees")
    print("Step 5 : Wait For It To Process Until You A Get Message And Then Collect Your Amount")
    print("\nIf You Follow These Steps Correctly, Your Choosen Operation Will Be Successful")
    Q1=int(input("\nPress 1 If You Want To Ask More Quetions OR Press 2 To Go To Previous Screen : "))
    if(Q1==1):
        print()
        Consultancy()
    elif(Q1==2):
        print()
        Home()
    else:
        print("Invalid Input")
        print()
        Home()

def Consultancy_Q6():
    print("\nThis Can Be Done On Home Screen As Well As When You Are Logged In Into Your Account(ONLY CASH)")
    print("\nHome Screen : ")
    print("Step 1 : Select Choice Number 4")
    print("Step 2 : Enter Your Choice Which Bill You Want To Pay")
    print("Step 3 : Enter The Required Details")
    print("Step 4 : Pay The Amount You Are Shown")
    print("\nLog In Screen : ")
    print("\nStep 1 : Log In Into Your Account")
    print("Step 2 : Select Choice Number 4")
    print("Step 3 : Enter Your Choice Which Bill You Want To Pay")
    print("Step 4 : Enter The Required Details")
    print("Step 5 : Pay The Amount You Are Shown")
    print("\nIf You Follow These Steps Correctly, Your Choosen Operation Will Be Successful")
    Q1=int(input("\nPress 1 If You Want To Ask More Quetions OR Press 2 To Go To Previous Screen : "))
    if(Q1==1):
        print()
        Consultancy()
    elif(Q1==2):
        print()
        Home()
    else:
        print("Invalid Input")
        print()
        Home()

def Consultancy_Q7():
    print("\nThis Can Be Done On Home Screen As Well As When You Are Logged In Into Your Account(ONLY CASH)")
    print("\nHome Screen : ")
    print("Step 1 : Select Choice Number 3")
    print("Step 2 : Enter Your 4 Digit Pin")
    print("Step 3 : Select The Amount You Want To Withdraw")
    print("Step 4 : Collect Your Amount")
    print("\nLog In Screen : ")
    print("\nStep 1 : Log In Into Your Account")
    print("Step 2 : Select Choice Number 3")
    print("Step 3 : Enter Your 4 Digit Pin")
    print("Step 4 : Select The Amount You Want To Withdraw")
    print("Step 5 : Collect Your Amount")
    print("\nIf You Follow These Steps Correctly, Your Choosen Operation Will Be Successful")
    Q1=int(input("\nPress 1 If You Want To Ask More Quetions OR Press 2 To Go To Previous Screen : "))
    if(Q1==1):
        print()
        Consultancy()
    elif(Q1==2):
        print()
        Home()
    else:
        print("Invalid Input")
        print()
        Home()

def Consultancy_Q8():
    print("\nThis Can Only Be Done If You Are Logged In Into Your Account")
    print("\nStep 1 : Log In Into Your Account")
    print("Step 2 : Select Choice Number 5")
    print("Step 3 : Enter Which Loan You Want To Apply To")
    print("Step 4 : Enter If You Want To Apply To Apply For A Short Term OR Loan Term Loan")
    print("Step 5 : Select Which Type Of Loan You Want")
    print("Step 6 : Wait For It To Process Until You See Your Information")
    print("\nIf You Follow These Steps Correctly, Your Choosen Operation Will Be Successful")
    Q1=int(input("\nPress 1 If You Want To Ask More Quetions OR Press 2 To Go To Previous Screen : "))
    if(Q1==1):
        print()
        Consultancy()
    elif(Q1==2):
        print()
        Home()
    else:
        print("Invalid Input")
        print()
        Home()

def ConsultancyB():
    print("\t\t\t\t\t=====================================")
    print("\t\t\t\t\t|\t      Consultancy\t    |")
    print("\t\t\t\t\t=====================================")
    print("\n\t\t\t\t1.How To Open Account\t\t2.How To Log In To Account\n\n\t\t\t\t3.How To Deposit Money\t\t4.How To Withdraw Money\n\n\t\t\t\t5.How To Exchange Currency\t6.How To Pay Utility Bill\n\n\t\t\t\t7.How To Use ATM\t\t8.How To Apply For Loan")
    choice=int(input("\nEnter Your Choice(OR Press 9 To Go Back) : "))
    if(choice==1):
        Consultancy_Q1B()
    elif(choice==2):
        Consultancy_Q2B()
    elif(choice==3):
        Consultancy_Q3B()
    elif(choice==4):
        Consultancy_Q4B()
    elif(choice==5):
        Consultancy_Q5B()
    elif(choice==6):
        Consultancy_Q6B()
    elif(choice==7):
        Consultancy_Q7B()
    elif(choice==8):
        Consultancy_Q8B()
    elif(choice==9):
        LoginAccount()
    else:
        print("Invalid Input")
        LoginAccount()

def Consultancy_Q1B():
    print("\nStep 1 : Go To Home Screen")
    print("Step 2 : Select Choice Number 1")
    print("Step 3 : Select Which Account You Want To Create\n\t Select Choice Number 1 For A Current Account OR Select Choice Number 2 For A Savings Account")
    print("Step 4 : Enter All The Required Details")
    print("Step 5 : Wait For It To Process Until You See Your Information On Screen")
    print("\nIf You Follow These Steps Correctly, Your Account Will Be Created")
    Q1=int(input("\nPress 1 If You Want To Ask More Quetions OR Press 2 To Go To Previous Screen : "))
    if(Q1==1):
        print()
        Consultancy()
    elif(Q1==2):
        print()
        LoginAccount()
    else:
        print("Invalid Input")
        print()
        LoginAccount()

def Consultancy_Q2B():
    print("\nStep 1 : Go To Home Screen")
    print("Step 2 : Select Choice Number 2")
    print("Step 3 : First Enter Your Name And Then Enter Your Account Number")
    print("Step 4 : Wait For It To Process Until You See Your Information On Screen And The Logged In Menu")
    print("\nIf You Follow These Steps Correctly, Choosen Operation Will Be Successful")
    Q1=int(input("\nPress 1 If You Want To Ask More Quetions OR Press 2 To Go To Previous Screen : "))
    if(Q1==1):
        print()
        Consultancy()
    elif(Q1==2):
        print()
        LoginAccount()
    else:
        print("Invalid Input")
        print()
        LoginAccount()

def Consultancy_Q3B():
    print("\nThis Can Only Be Done If You Are Logged In Into Your Account")
    print("\nStep 1 : Log In Into Your Account")
    print("Step 2 : Select Choice Number 1")
    print("Step 3 : Enter The Amount You Want To Deposit")
    print("Step 4 : Wait For It To Process Until You A Get Message")
    print("\nIf You Follow These Steps Correctly, Your Choosen Operation Will Be Successful")
    Q1=int(input("\nPress 1 If You Want To Ask More Quetions OR Press 2 To Go To Previous Screen : "))
    if(Q1==1):
        print()
        Consultancy()
    elif(Q1==2):
        print()
        LoginAccount()
    else:
        print("Invalid Input")
        print()
        LoginAccount()

def Consultancy_Q4B():
    print("\nThis Can Only Be Done If You Are Logged In Into Your Account")
    print("\nStep 1 : Log In Into Your Account")
    print("Step 2 : Select Choice Number 2")
    print("Step 3 : Enter The Amount You Want To Withdraw")
    print("Step 4 : Make Sure To Have More Than Rs.1000 In Your Account\n\t If You Don't Have More Than Rs.1000 Your Transaction Won't Be Successful")
    print("Step 5 : Wait For It To Process Until You A Get Message")
    print("\nIf You Follow These Steps Correctly, Your Choosen Operation Will Be Successful")
    Q1=int(input("\nPress 1 If You Want To Ask More Quetions OR Press 2 To Go To Previous Screen : "))
    if(Q1==1):
        print()
        Consultancy()
    elif(Q1==2):
        print()
        LoginAccount()
    else:
        print("Invalid Input")
        print()
        LoginAccount()

def Consultancy_Q5B():
    print("\nThis Can Only Be Done If You Are Logged In Into Your Account(ONLY CASH)")
    print("\nStep 1 : Log In Into Your Account")
    print("Step 2 : Select Choice Number 8")
    print("Step 3 : Enter Your Choice In Which Currency You Want To Deal In")
    print("Step 4 : Enter Your Choice If You Want To Convert Into Your Choosen Currency\n\t OR Into Pakistani Rupees")
    print("Step 5 : Wait For It To Process Until You A Get Message And Then Collect Your Amount")
    print("\nIf You Follow These Steps Correctly, Your Choosen Operation Will Be Successful")
    Q1=int(input("\nPress 1 If You Want To Ask More Quetions OR Press 2 To Go To Previous Screen : "))
    if(Q1==1):
        print()
        Consultancy()
    elif(Q1==2):
        print()
        LoginAccount()
    else:
        print("Invalid Input")
        print()
        LoginAccount()

def Consultancy_Q6B():
    print("\nThis Can Be Done On Home Screen As Well As When You Are Logged In Into Your Account(ONLY CASH)")
    print("\nHome Screen : ")
    print("Step 1 : Select Choice Number 4")
    print("Step 2 : Enter Your Choice Which Bill You Want To Pay")
    print("Step 3 : Enter The Required Details")
    print("Step 4 : Pay The Amount You Are Shown")
    print("\nLog In Screen : ")
    print("\nStep 1 : Log In Into Your Account")
    print("Step 2 : Select Choice Number 4")
    print("Step 3 : Enter Your Choice Which Bill You Want To Pay")
    print("Step 4 : Enter The Required Details")
    print("Step 5 : Pay The Amount You Are Shown")
    print("\nIf You Follow These Steps Correctly, Your Choosen Operation Will Be Successful")
    Q1=int(input("\nPress 1 If You Want To Ask More Quetions OR Press 2 To Go To Previous Screen : "))
    if(Q1==1):
        print()
        Consultancy()
    elif(Q1==2):
        print()
        LoginAccount()
    else:
        print("Invalid Input")
        print()
        LoginAccount()

def Consultancy_Q7B():
    print("\nThis Can Be Done On Home Screen As Well As When You Are Logged In Into Your Account(ONLY CASH)")
    print("\nHome Screen : ")
    print("Step 1 : Select Choice Number 3")
    print("Step 2 : Enter Your 4 Digit Pin")
    print("Step 3 : Select The Amount You Want To Withdraw")
    print("Step 4 : Collect Your Amount")
    print("\nLog In Screen : ")
    print("\nStep 1 : Log In Into Your Account")
    print("Step 2 : Select Choice Number 3")
    print("Step 3 : Enter Your 4 Digit Pin")
    print("Step 4 : Select The Amount You Want To Withdraw")
    print("Step 5 : Collect Your Amount")
    print("\nIf You Follow These Steps Correctly, Your Choosen Operation Will Be Successful")
    Q1=int(input("\nPress 1 If You Want To Ask More Quetions OR Press 2 To Go To Previous Screen : "))
    if(Q1==1):
        print()
        Consultancy()
    elif(Q1==2):
        print()
        LoginAccount()
    else:
        print("Invalid Input")
        print()
        LoginAccount()

def Consultancy_Q8B():
    print("\nThis Can Only Be Done If You Are Logged In Into Your Account")
    print("\nStep 1 : Log In Into Your Account")
    print("Step 2 : Select Choice Number 5")
    print("Step 3 : Enter Which Loan You Want To Apply To")
    print("Step 4 : Enter If You Want To Apply To Apply For A Short Term OR Loan Term Loan")
    print("Step 5 : Select Which Type Of Loan You Want")
    print("Step 6 : Wait For It To Process Until You See Your Information")
    print("\nIf You Follow These Steps Correctly, Your Choosen Operation Will Be Successful")
    Q1=int(input("\nPress 1 If You Want To Ask More Quetions OR Press 2 To Go To Previous Screen : "))
    if(Q1==1):
        print()
        Consultancy()
    elif(Q1==2):
        print()
        LoginAccount()
    else:
        print("Invalid Input")
        print()
        LoginAccount()

def FAQ():
    print("\t\t\t\t\t=====================================")
    print("\t\t\t\t\t|\t\tFAQs\t\t    |")
    print("\t\t\t\t\t=====================================")
    print("\n\t\t\t\t\t1.How Many Types Of Accounts Are Their?\n\n\t\t\t\t\t2.Can I Only Pay Utiltiy Bills In Cash?\n\n\t\t\t\t\t3.Can I Only Exchange Currency In Cash?\n\n\t\t\t\t\t4.Can Only I Apply For Loan?\n\n\t\t\t\t\t5.Can I Change My Account Information?\n\n\t\t\t\t\t6.Is This Online Banking?\n\n\t\t\t\t\t7.Can I Only Use ATM While logged Into My Account?\n\n\t\t\t\t\t8.How To Know Step By Step Information?")
    choice=int(input("\nEnter Your Choice(OR Press 9 To Go Back) : "))
    if(choice==1):
        FAQ_Q1()
    elif(choice==2):
        FAQ_Q2()
    elif(choice==3):
        FAQ_Q3()
    elif(choice==4):
        FAQ_Q4()
    elif(choice==5):
        FAQ_Q5()
    elif(choice==6):
        FAQ_Q6()
    elif(choice==7):
        FAQ_Q7()
    elif(choice==8):
        FAQ_Q8()
    elif(choice==9):
        LoginAccount()
    else:
        print("Invalid Input")
        LoginAccount()

def FAQ_Q1():
    print("\nAnswer : ")
    print("There Are Two Types Of Accounts Current Account & Savings Account.\nYou Can Create Both Type Of Accounts.")
    Q1=int(input("\nPress 1 If You Want To Ask More Quetions OR Press 2 To Go To Previous Screen : "))
    if(Q1==1):
        print()
        FAQ()
    elif(Q1==2):
        print()
        LoginAccount()
    else:
        print("Invalid Input")
        print()
        LoginAccount()

def FAQ_Q2():
    print("\nAnswer : ")
    print("Yes, You Can Only Pay Your Utility Bills In Cash Because Utility Bills Are Paid On Spot.")
    Q1=int(input("\nPress 1 If You Want To Ask More Quetions OR Press 2 To Go To Previous Screen : "))
    if(Q1==1):
        print()
        FAQ()
    elif(Q1==2):
        print()
        LoginAccount()
    else:
        print("Invalid Input")
        print()
        LoginAccount()

def FAQ_Q3():
    print("\nAnswer : ")
    print("Yes, You Can Only Exchange Currency In Cash Because Currencies Are Converted/Exchnaged On Spot.")
    Q1=int(input("\nPress 1 If You Want To Ask More Quetions OR Press 2 To Go To Previous Screen : "))
    if(Q1==1):
        print()
        FAQ()
    elif(Q1==2):
        print()
        LoginAccount()
    else:
        print("Invalid Input")
        print()
        LoginAccount()

def FAQ_Q4():
    print("\nAnswer : ")
    print("No, Anybody Can Apply For A Loan.\nBut One Of The People Who Have A Account In The Bank Should Be Logged In Into His/Her Account To Apply For Loan.")
    Q1=int(input("\nPress 1 If You Want To Ask More Quetions OR Press 2 To Go To Previous Screen : "))
    if(Q1==1):
        print()
        FAQ()
    elif(Q1==2):
        print()
        LoginAccount()
    else:
        print("Invalid Input")
        print()
        LoginAccount()

def FAQ_Q5():
    print("\nAnswer : ")
    print("No, You Cannot Change Your Account Information.")
    Q1=int(input("\nPress 1 If You Want To Ask More Quetions OR Press 2 To Go To Previous Screen : "))
    if(Q1==1):
        print()
        FAQ()
    elif(Q1==2):
        print()
        LoginAccount()
    else:
        print("Invalid Input")
        print()
        LoginAccount()

def FAQ_Q6():
    print("\nAnswer : ")
    print("No, This Isn't Online Banking Just A Banking System For The Ease Of People.")
    Q1=int(input("\nPress 1 If You Want To Ask More Quetions OR Press 2 To Go To Previous Screen : "))
    if(Q1==1):
        print()
        FAQ()
    elif(Q1==2):
        print()
        LoginAccount()
    else:
        print("Invalid Input")
        print()
        LoginAccount()

def FAQ_Q7():
    print("\nAnswer : ")
    print("No, You Can Use ATM While On The Home Screen As Well As While You Are Logged In To Your Account.")
    Q1=int(input("\nPress 1 If You Want To Ask More Quetions OR Press 2 To Go To Previous Screen : "))
    if(Q1==1):
        print()
        FAQ()
    elif(Q1==2):
        print()
        LoginAccount()
    else:
        print("Invalid Input")
        print()
        LoginAccount()

def FAQ_Q8():
    print("\nAnswer : ")
    print("You Can Know Step By Step Information By Choosing The Consultancy Option On Home Screen Or\nEither While You Are Logged In To Your Account.")
    Q1=int(input("\nPress 1 If You Want To Ask More Quetions OR Press 2 To Go To Previous Screen : "))
    if(Q1==1):
        print()
        FAQ()
    elif(Q1==2):
        print()
        LoginAccount()
    else:
        print("Invalid Input")
        print()
        LoginAccount()

def R_Facts():
    import random
    print("\nSo You Are Getting Bored And You Randomly Typed The Two Funny Numbers Together,\nWell That Is Good Now Here Is A Random Fact")
    Num=random.randint(1,30)
    print()
    print("Fact : ")
    f=open(f"C:/Users/Afzal computers/Desktop/DSA Project/Facts/{Num}.txt","r")
    print(f.read())
    print("\nWant To Hear Another Random Fact Or Want To Do Banking?\n\n1.Another Fact\n2.Boring Banking")
    Q1=int(input("\nEnter Your Choice : "))
    if(Q1==1):
        Num=random.randint(1,30)
        print()
        print("Fact : ")
        f=open(f"C:/Users/Afzal computers/Desktop/DSA Project/Facts/{Num}.txt","r")
        print(f.read())
        print("\nAlright That Is It Now Do Boring Banking, It Took Time To Make")
        print()
        Home()
    elif(Q1==2):
        print()
        Home()
    else:
        print("\nTch Tch, You Lost Your Chance Now Do Banking")
        print()
        Home()

def FullAccountInfo():
    from numpy import array
    print()
    print("Welcome Sir / Madam\n\nHere Are All The Accounts Present In The Bank : \n")
    import pyodbc
    conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=NOMIR-PC\SQLEXPRESS;'
                      'Database=Project;'
                      'Trusted_Connection=yes;')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM All_Accounts")
    print(f"========================================================================================================================")
    print(f"Account Type\tName\t\tPhone Number\tCNIC Number\t4-Digit PIN\tMoney In Account\tAccount Number")
    print()
    for row in cursor:
        print(f"{row[0]}\t\t{row[1]}\t\t{row[2]}\t{row[3]}\t{row[4]}\t\t{row[5]}\t\t\t{row[6]}")
        print()
    print(f"========================================================================================================================")
    print("\nHere Are All The Employees Present In The Bank : \n")
    cursor.execute("SELECT * FROM Employee_ID")
    Emp_ID=array([0 for i in range(10)])
    i=0
    print(f"========================================================================================================================")
    print(f"Employee ID")
    print()
    for row in cursor:
        print(f"{row[0]}",end=" ")
        Emp_ID[i]=row[0]
        i=i+1
    print()
    print(f"========================================================================================================================")
    Home()

Home()
