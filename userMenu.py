import fetch
import redis
import pickle

db = redis.Redis(host="localhost", port=6379, db=1)

def userMenu(login_id):
    while True:
        data = pickle.loads(db.get(login_id))
        print('--------------hello ' + data['name'] + '--------------')
        print('your current balance is ' + str(data['money']))
        choice = ' 1) deposit \n 2) withdraw \n 3) Exit \n\n Your Choice (Only with number)>>'
        menu = input(choice)
        #deposit
        if menu == '1':
            cur_balance = fetch.deposit(data['money'])  
            data['money'] = cur_balance
            new_data = pickle.dumps(data)
            db.set(login_id, new_data)
        #withdraw
        elif menu == '2':
            cur_balance = fetch.withdraw(data['money'])  
            data['money'] = cur_balance
            new_data = pickle.dumps(data)
            db.set(login_id, new_data) 
        elif menu == '3':
            print('App closed,Thanks for using!')
            exit()
        else:
            print('\nError:wrong Input,Please check and try again\n')

