def Employee(): # This is my Employee Management Project
    print("<---------- Dhruv Project ---------->")
    dict={}
    ans='y'
    while True:
        print("\n1. Signup \n2. Login \n3. Forget Password \n4. Exit")
        choice=int(input("Enter the choice= "))
        if choice==1:
            q1=input("Enter your User Name= ")
            q2=input("Enter your password= ")
            q3=int(input("Enter your Mobile No.= "))
            dict['User']=q1
            dict['Password']=q2
            dict['Mobile']=q3
            print("Thanking for Registration.")
            print(dict)
        elif choice==2:
            q1=input("Enter the User Name= ")
            if dict['User']==q1:
                q2=input("Enter the Password= ")
                if dict['Password']==q2:
                    dict1={}
                    while True:
                        print('''\n1. Add Employee \n2. Delete Employee \n3. Edit Employee Details \n4. Search a Particular Employee \n5. List Records of All Employee \n6. Logout''')
                        choice=int(input("Enter Your Choice= "))
                        if choice==1:
                            a=int(input("How much id do you want to enter= "))
                            for i in range(a):
                                dict2={}
                                q1=int(input("Enter the Employee Id= "))
                                for j in range(1):
                                    q2=input("Enter the Employee First Name= ")
                                    q3=input("Enter the Employee Last Name= ")
                                    q4=input("Enter the Employee Post= ")
                                    q5=int(input("Enter the Employee Salary= "))
                                    q6=int(input("Enter the Employee Mobile No= "))
                                    dict2['First_Name']=q2
                                    dict2['Last_Name']=q3
                                    dict2['Post']=q4
                                    dict2['Salary']=q5
                                    dict2['Mobile']=q6
                                dict1[q1]=dict2
                                print("\n",dict1)
                        elif choice==2:
                            print(dict1)
                            q1=int(input("Enter the Employee Id= "))
                            if q1 in dict1:
                                dict1.pop(q1)
                                print("Id has been deleted Successfully")
                                print(dict1)
                            else:
                                print("The Id You Enter Doen't Match In The Database Please Check And Try Again")
                        elif choice==3:
                            a=int(input("Enter The Employee Id= "))
                            if a in dict1.keys():
                                while True:
                                    print("\n1. For First Name \n2. For Last Name \n3. For Post \n4. For Employee Salary \n5. For Mobile No. \n6. For Exit")
                                    choice=int(input("Enter Your Choice= "))
                                    if choice==1:
                                        q1=input("Please Enter the New Name= ")
                                        dict1[a]['First_Name']=q1
                                        print(dict1[a])
                                    elif choice==2:
                                        q1=input("Please Enter the Last Name= ")
                                        dict1[a]['Last_Name']=q1
                                        print(dict1[a])
                                    elif choice==3:
                                        q1=input("Enter the Post= ")
                                        dict1[a]['Post']=q1
                                        print(dict1[a])
                                    elif choice==4:
                                        q1=int(input("Enter Your Salary= "))
                                        dict1[a]['Salary']=q1
                                        print(dict1[a])
                                    elif choice==5:
                                        q1=int(input("Enter Your Moible No.= "))
                                        dict1[a]['Mobile']=q1
                                        print(dict1[a])
                                    elif choice==6:
                                        break
                                    else:
                                        print("No Employee id Doesn't Match")
                        elif choice==4:
                            a=int(input("Enter the Id you Want To Search= "))
                            if a in dict1:
                                print(dict1[a])
                        elif choice==5:
                            print("Here is the Record of All Employees",dict1)
                        elif choice==6:
                            print("Logout Sucessfully")
                            break
                else:
                    print("Please check your User Name and try Again")
        elif choice==3:
            q1=input("Enter Your User Name= ")
            if q1 in dict.values():
                q2=int(input("Enter Your Mobile Number= "))
                if q2 in dict.values():
                    q3=int(input("Enter Your New Mobile No.= "))
                    dict['Mobile']=q3
                    print("Your Mobile No is now change Please Try to Login")
                    print(dict)
        elif choice==4:
            print("Thanks for Using This Software.")
            break
Employee()