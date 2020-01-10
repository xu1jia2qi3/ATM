import redis
import pickle


db = redis.Redis(host="localhost", port=6379, db=1)


def register():
    while True:
        try:
            account_name = input('Enter your name: ')
            account_password = input('Enter Your Password: ')
            re_account_password = input('Re_enter Your Password: ')
        except KeyboardInterrupt:
            break

        if account_password != re_account_password:
            print('Password does not match, please try again')
            register()
        else:
            balance = 0
            # make sure account number is unique
            db_size = db.dbsize()
            account_number = str(db_size + 1)
            # write database
            result = pickle.dumps(
                {'name': account_name, 'password': account_password, 'money': balance})
            db.set(account_number, result)
            print('account created, you account is ' + account_number)


            # db.flushdb()
            # read_database = db.get('4')
            # youdict = pickle.loads(read_database)
            # print(youdict)
