Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
Author: Kandyce Rodnney
Dated Created:April 3, 2022
Course: ITT103
Purpose: To show consie and complexity to the peseudocode pesentd in part A of the Assignment 
salesperson_number = int(input("Enter salesperson number: "))
sale_amount = int(input("Enter sales amount: "))
Class = int(input("Enter your class: "))

if Class == 1: #If class is 1

        if sale_amount <= 1000: #If sale amount less than or equal to 1000
                comission = (6 * sale_amount)/100 #6% comission 

        elif sale_amount > 1000 and sale_amount < 2000: #If sale amount is greater than 1000 but less than
                                                                                                        #2000
                comission = (7 * sale_amount)/100 #7% comission

        else:
                comission = (10 * sale_amount)/100 #10% comission

elif Class == 2: #If class is 2
        #Same conditions as above, only the comission percentage is different
        if sale_amount < 1000:
                comission = (4 * sale_amount)/100

        else:
                comission = (6 * sale_amount)/100

elif Class == 3: #If class is 3
        comission = (4.5 * sale_amount)/100

else:#If any invalid class is entered
        print("Invalid Class entered")