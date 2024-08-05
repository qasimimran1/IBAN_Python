#!/usr/bin/env python3


# move the country code to the end of the number
# make chekc code 0 and append at the end of the number
# convert letters to numbers as per the key
# take modulo 97 
# subtract 98
#e.g IBAN # PK09MEZN0049010100033272
# Total characters should be 24
# Step 1 MEZN0049010100033272PK
# Step 2 MEZN0049010100033272PK00 "
# Step 3 231536240049010100033272262100 "
# Step 4 check_code = 231536240049010100033272262100 % 97
# Step 4 check_code =  98 - check_code

print("*** IBAN Generation Utility ****")

def generate_iban():
    key = {'A': '10', 'B':'11', 'C':'12','D':'13','E':'14','F':'15','G': '16','H': '17','I':'18','J':'19','K':'20','L':'21','M':'22',
           'N': '23', 'O':'24', 'P':'25','Q':'26','R':'27','S':'28','T': '29','U': '30','V':'31','W':'32','X':'33','Y':'34','Z':'35'
          }
    acc_num_str = ""
    print("Enter Country Code")

    country_code = input()
    if(country_code.isalpha()):
        country_code= country_code.upper()
    else:
        print("Wrong Format")
        exit(-1)
    
    print("Enter Bank Code")
    bank_code = input()
    if(bank_code.isalpha()):
        bank_code= bank_code.upper()
    else:
        print("Wrong Format")
        exit(-1)
    #print(bank_code)
    
    print("Enter Account Number including branch code")
    account_number = input()
    if(account_number.isdigit()):
        print('PASS')
    else:
        print("Wrong Format")
        exit(-1)

    account_numb_temp = ''
    if(( len(bank_code) + len(country_code) + len(account_number) ) < 22):
        for i in range(22 -( len(bank_code) + len(country_code) + len(account_number) )):
            account_numb_temp += '0'
        account_numb_temp += account_number
        account_number = account_numb_temp
    elif(( len(bank_code) + len(country_code) + len(account_number) ) == 22):
        account_number = account_number    


    acc_num_alph = country_code + '00' + bank_code + account_numb_temp

    print(acc_num_alph)


    if(len(bank_code) >= 2):
        for i in range(len(bank_code)) :
            acc_num_str = acc_num_str+(key[bank_code[i]])

    for i in range(len(account_number)):
        acc_num_str = acc_num_str+(account_number[i])


    for i in range(len(country_code)) :
        acc_num_str = acc_num_str+(key[country_code[i]])    

    for i in range(2) :
        acc_num_str = acc_num_str+'0'            

    account_num_digit = int(acc_num_str)             

    print(acc_num_str)

    print("account_num_digit", account_num_digit)

    #print("len", len(acc_num_str))

    check_code =  98 - (account_num_digit % 97)
    check_code = str(check_code)
    if(len(check_code)== 1):
        temp_check_code = '0'
        temp_check_code += check_code
        check_code = temp_check_code

    print(check_code)

    IBAN = country_code + check_code + bank_code + account_number

    print (IBAN)



    # print("Enter Full Account Number")
    # input_num = input()
    # print("len", len(input_num))





if __name__ == '__main__':
    generate_iban()