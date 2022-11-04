import string, secrets

chrs = string.ascii_letters 
numbers = string.digits

#Optional if you want to add punctuation to your pass
punctuations = string.punctuation

flag = True
while flag:
    print()
    choose = input('You want PIN or PASSWORD?\nType pin/password: ')
    length = input('Choose your PIN/PASSWORD length: ')

    normal_password = ''.join(secrets.choice(chrs + numbers) for i in range(int(length)))
    pin = ''.join(secrets.choice(numbers) for i in range(int(length)))

    #Complex password if you wish
    complex_password = ''.join(secrets.choice(chrs + numbers + punctuations) for i in range(int(length)))

    print('****************Python Password Generator********')

    if choose.lower() == 'password':
        optional = input('You want NORMAL or COMPLEX PASSWORD?\nType normal/complex: ')
        if optional.lower() == 'normal':
            print(normal_password)
        if optional.lower() == 'complex':
            print(complex_password)
    if choose.lower() == 'pin':
        print(pin)
    choice = input('Do you want to ReGenerator?\nType yes/no: ')
    if choice.lower() == 'yes':
        flag = True
    else:
        flag = False