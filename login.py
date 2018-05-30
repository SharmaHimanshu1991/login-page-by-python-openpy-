import time
import re
import datetime
import openpyxl
import smtplib, time, xlrd, xlwt
wb = xlwt.Workbook()
ws = wb.add_sheet("login ")
input_open = int(input('Enter 1 to sign up and 2 for log in '))
if input_open == 1:
    print("Enter your detail to sign up ")


    x = 'y'
    while(x == 'y'):
        first_name = input('Enter your first name ')
        last_name = input('Enter your last name ')
        date_of_birth = input('Enter DOB ')
        #dob_time = datetime.strptime(date_of_birth, '%b %d %Y')
        mob_no = input('Enter your mob. no. ')
        mo=1
        while mo:
            if len(mob_no) != 10:
                print("please enter 10 digit mob no")
                mob_no = input('Enter your mob. no. again: ')
            else:
                mo=0
        address = input('Enter your address ')
        UserName = input("Enter the username to login into your accout ")
        
    
        print('Enter your username and password to log in ')
        
        
        p = True
        while p:
            PassWord = input("Now please create a password. ")
            PassWordCheck = input("Please Re Enter the password \n ")
            if PassWord.lower() == PassWordCheck.lower():
                if (len(PassWord)<6 or len(PassWord)>12):
                    continue
                elif not re.search("[a-z]",PassWord):
                    continue
                elif not re.search("[0-9]",PassWord):
                    continue
                elif not re.search("[A-Z]",PassWord):
                    continue
                elif not re.search("[$#@]",PassWord):
                    continue
                elif re.search("\s",PassWord):
                    continue
                else:
                    print("Valid Password")
                    print('Password succesfully saved')
                    p=False
                    break
            else:
                print ("Passwords Do Not Match!\nPlease Re Try.")
            

        '''file = open("Login.xls","a")
        file.write (UserName)
        file.write (",")
        file.write (PassWord)
        file.write("\n")
        file.close()'''

        print ("Your login details have been saved. ")
        x = input('Do you want to enter another detail: ')
        x = x.lower()
elif(input_open == 2):
    '''registered_users = open('Login.xls')
    username = input("enter the username to login into your accout")
    
    print('enter your password to log in')
    password = input("Now please enter your password. ")
    
    
    logged_in = False
    #with open('Login.txt', 'r') as registered_users:
       #   found = False'''
    with open('Login.xls') as file:
        for line in Login.xls:
            line = line.strip()
            if (username == line and password == line):
                print("successfully logged in ")
                found = True
                break
     
                if not found:
                    print("Username or password you enterd is incorrect")
    '''for line in registered_users:
        username, password = line.split(',')
        if (username,password in line(Login.xls)):
            print('successfully logged in')
        else:
            print('username or password is incorrect')'''
else:
    print ('Wrong input, try again')
    
    
