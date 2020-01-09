def deposit(balance):
    try:
        cur_balance = balance
        print('Your current balance: ' + str(cur_balance))
        deposit = float(input('Enter deposit amount: '))
        if deposit > 0:
            cur_balance += deposit
        else:
            print('not vailate number')
        return(cur_balance)
    except KeyboardInterrupt:      
        return(balance)


def withdraw(balance):
    try:
        cur_balance = balance
        print('Your current balance: ' + str(cur_balance))
        withdraw = float(input('Enter deposit amount: '))
        if withdraw > 0:
            cur_balance -= withdraw
            if cur_balance > 0:
                return(cur_balance)
            else:
                print('balance can not below 0')
        else:
            print('not vailate number')
        return(balance)
    except KeyboardInterrupt:      
        return(balance)
