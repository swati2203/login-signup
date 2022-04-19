import json
import os
import re


def check_file(filname):
    if not os.path.exists(filname):
        a=open(filname,"w+")
        a.write("[]")
def read_data(filname):
    b=open(filname,"r")
    c=json.loads(b.read())
    return c
def signup(filname):
    user=input("enter your name")
    password=input("enter the password")
    if not(re.search("[a-z A-Z]",password) and re.search("[0-9]",password) and re.search("[@#$]",password)):
        print("password is not valid")
        return " "
    con_password=input("confirm the password")
    if con_password!=password:
        print("password not match")
        return " "
    contact=input("enter the contact number")
    if len(contact)==10:
        email=input("enter your email id")
        json_data=read_data(filname)
        for u in json_data:
            if u["name"]==user:
                print("user already exist")
                return " "
        json_data.append({"name":user,"password":password,"contact":contact,"email":email})
        a=open(filname,"w+")
        b=json.dumps(json_data,indent=2)
        a.write(b)
        print("signup sucessfully")
    else:
        print("check the contact number")
def login(filname):
    user1=input("enter the username")
    pwd=input("enter the password")
    json_data=read_data(filname)
    for user in json_data:
        if user["name"]==user1:
            break
    else:
        print("this user dosen't exist")
        return " "
    if user["password"]!=pwd:
        print("please check your password")
        return " "
    print("login sucessfully")
filname="signup.json"
check_file(filname)
print("welcome to login signup")
choice=input("enter the choice:- if you want to signup[1],if you want to login[2]")
if choice=="1":
    signup(filname)
elif choice=="2":
    login(filname)
else:
    print("check your choice")


