#!/usr/bin/python

import sys
print ('Welcome to FouuLs\' tax calculator!')

print ('To start, enter your marital status:')

M = input('(1) Single, (2) Married filing jointly or qualifying \
widow(er), (3) Married filing separately, or (4) Head of Household:')
if M != 1 or M != 2 or M!= 3 or M!= 4:
        print('Error: Please enter a valid marital status and restart the program')


#Single
if M == "Single" or M == '1':
    T = int(input('Please insert your taxable income here:'))
    R = "tax rate"
    if T>0 and T<9325:
        R = .10 * T
    elif T>9326 and T<37950:
        R = .15 * T + 932.50
    elif T>37951 and T<91900:
        R = .25 * T + 5226.25
    elif T>919101 and T<191650:
        R = .28 * T + 18713.75
    elif T>191651 and T<416700:
        R = .33 * T + 46643.75
    elif T>416701 and T<418400:
        R = .35 * T + 120910.25
    elif 418401<T:
        R = float(.396) * float(T) + 121505.25
    else:
        print ('Error: Please type a valid numerical value for taxable \
    income')

    tax_owed = R
    print ("You owe $ {}" .format(tax_owed))
    sys.exit()

#Married Filing Jointly or Qualifying Widow
if M == "Married filing jointly or qualifying widower" or M == '2':
    T = int(input('Please insert your taxable income here:'))
    R = "tax rate"
    if T>0 and T<18650:
        R = .10 * T
    elif T>18651 and T<75900:
        R = .15 * 1865
    elif T>75901 and T<153100:
        R = .25 * T + 10452.50
    elif T>153101 and T<233350:
        R = .28 * T + 29752.50
    elif T>233351 and T<416700:
        R = .33 * T + 52222.50
    elif T>416701 and T<470700:
        R = .35 * T + 112728
    elif 470701<T:
        R = float(.396) * float(131628)
    else:
        print("Error: Please type in a valid numerical value for \
    taxable income")
    tax_owed = R
    print ("You owe $ {}" .format(tax_owed))
    sys.exit()

#Married Filing Separately
if M == "Married filing separately" or M == '3':
    T = int(input('Please insert your taxable income here:'))
    R = "tax rate"
    if T>0 and T<9325:
        R = .10 * T
    elif T>9326 and T<37950:
        R = .15 * T + 932.50
    elif T>37951 and T<76550:
        R = .25 * T + 5226.25
    elif T>76551 and T<116675:
        R = .28 * T + 14876.25
    elif T>116676 and T<208350:
        R = .33 * T + 26111.25
    elif T>208351 and T<235350:
        R = .35 * T + 56364
    elif 235351<T:
        R = .396 * T + 65814
    else:
        print("Error: Please type in a valid numerical value for \
    taxable income")
    tax_owed = R
    print ("You owe $ {}" .format(tax_owed))
    sys.exit()

#Head of Household
if M == "Head of Household" or M == '4':
    T = int(input('Please insert your taxable income here:'))
    R = "tax rate"
    if T>0 and T<9325:
        R = .10 * T
    elif T>9326 and T<37950:
        R = .15 * T + 1335
    elif T>37951 and T<91900:
        R = .25 * T + 6952.50
    elif T>919101 and T<191650:
        R = .28 * T + 27052.50
    elif T>191651 and T<416700:
        R = .33 * T + 49816.50
    elif T>416701 and T<418400:
        R = .35 * T + 117202.50
    elif T>418401:
        R = .396 * T + 126950
    else:
        print("Error: Please enter a valid numerical value for taxable \
    income")
    tax_owed = R
    print ("You owe $ {}" .format(tax_owed))
    sys.exit
