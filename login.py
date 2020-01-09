import redis
import pickle
import userMenu

db = redis.Redis(host="localhost", port=6379, db=1)

def login():
    run = True
    while run:
        try:
            login_id = input('Please, Enter your info (press "Ctrl+C" to go back) \n>>ID: ')
            if db.exists(login_id):
                login_password = input('>>Password: ')  
                user_data = pickle.loads(db.get(login_id))
                user_password = user_data['password']
                if login_password == user_password:
                    userMenu.userMenu(login_id)
                else:
                    print('wrong password\n')
                    run = False
            else:
                print('no this user')
                run = False
        except KeyboardInterrupt:
            break
    
