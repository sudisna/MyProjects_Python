# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 17:50:32 2020

@author: sudis
"""


#Strong Random Password Generator

#ask user if s/he wants to create a new password
#if yes, generate a new password, according to the following rules: 
#between 8 and 12 characters
#containing at least one uppercase letter
#one lowercase letter
#one digit 
#one special character
import random
import string 

def create_password():
    input1=int(input(""" Do you want to create new password: 
1.YES
2.NO              
"""))#menu to choose what you want to do
    print("The choice entered: ",input1)
    if input1==1:
        qty_of_passwd = int(input('How many passwords do you need?'))
 
        passwd_len = int(input('How many characters in your password?'))
        password_generator(passwd_len,qty_of_passwd)   #takes you to the password_generator function  
    elif input1==2:
         print("Come back!! We secure your data") #exits the program
           

 

def random_password(length:int):
         
        chars=string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
        return ''.join(random.choice(chars) for x in range(length))
 
 
def password_generator(length, qty=1):
  
     if length < 8 :
        print("password length={} is too short,".format(length),
            "minimum length=8")
       
     elif length > 13:
        print("password length={} is too big,".format(length),
            "maximum length=12")
       
     else:
        print("Your passwords generated are: ")    
        for i in range(qty):
            print(random_password(length))



create_password()