import random

class BANK:
    _Holder_details=[]
    def create_account(self):
        print('---welcome to create account---')
        self.new_Account={}

        self.new_Account['Holder_name']=input('Enter Holder Name:')
        self.new_Account['Aadhar_number']=int(input('Enter Aadhar Number:'))
        self.new_Account['Mobile Number']=int(input('Enter Mobile Number:'))
        self.new_Account['Account_Number']=random.randint(000000000000,999999999999)
        self.new_Account['IFSC']='ICIC012345'

        n1=input('select type of account saving/zero:').lower()
        while True:
            if n1=='saving':
                n2=int(input('your selecting saving account you have to deposite 1000:'))

                if n2>=1000:
                    self.new_Account['Balance']=n2
                    break
                else:
                    print('Deposit 1000 Rupees')
            elif n1=='zero':
                n3=int(input('you are selecting zero account you have to deposit 500:'))

                if n3>=500:
                    self.new_Account['Balance']=n3
                    break
                else:
                    print('Deposit 500')
        
        print('---your Account created---')
        BANK._Holder_details.append(self.new_Account)
        print(BANK._Holder_details)


    def Deposit(self):
        print('---welcome to deposit---')

        while True:
            user_name=input('Enter Holder Name:')
            acc_num=int(input('Enter Account Number:'))
            deposit_acc=int(input('Enter Deposit Amount:'))

            for x in BANK._Holder_details:
                if x['Holder_name']==user_name and x['Account_Number']==acc_num:
                    x['Balance']+=deposit_acc
                    print('Deposit Successful')
                    print('Upload Balnace:', x['Balance'])
                    return 
            print('invalid account. Try again.')
            

    def withdraw(self):
        w1=input('Enter Holder Name:')
        while True:
         w2=int(input('Enter Account Number:'))
         Acc_Found=False
        
         for x in BANK._Holder_details:
            if x['Account_Number']==w2:
                Acc_Found=True

                w3=int(input('Withdraw Amount:'))
                if x['Balance']>w3:
                    x['Balance']-=w3
                else:
                    print('check your Balance:')
                return
         if not Acc_Found:
            print('invalid account number')


    def check_Details(self):
        print('---welcome to check details---')

        c1=int(input('Enter account Number:'))

        for x in BANK._Holder_details:
            if x['Account_Number']==c1:
                for k,v in x.items():
                    print(k,v)
            else:
                print('check your Account Number')


    def check_Balance(self):
        print('---welcome to check balance---') 

        b1=int(input('Enter Account Number:'))     

        print('---your Balance---')

        for x in BANK._Holder_details:
            if x['Account_Number']==b1:
                print('Your Balance:', x['Balance'])    
            else:
                print('Check your Account Number')


obj=BANK()
while True:
    print('''
          1.create Account
          2.Deposit
          3.withdraw
          4.Details
          5.Balance
          6.Exit
          ''')
    n4=int(input('Select Options:'))
    if n4==1:
        obj.create_account()

    elif n4==2:
        obj.Deposit()

    elif n4==3:
        obj.withdraw()

    elif n4==4:
        obj.check_Details()

    elif n4==5:
        obj.check_Balance()

    elif n4==6:
        break

            




