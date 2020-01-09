import register
import login

print('                                  This is my APP, Welcome!                                 ')
print('========================================  Welcome  ========================================')
# main page for the app


def mainApp():
    while True:
        try:
            choice = '\n 1) Login \n 2) Register \n 3) Exit \n\n Your Choice (Only with number)>>'
            menu = input(choice)
            if menu == '1':
                login.login()
            elif menu == '2':
                register.register()
            elif menu == '3':
                print('App closed,Thanks for using!')
                exit()
            else:
                print('\nError:wrong Input,Please check and try again\n')
        except KeyboardInterrupt:
            print('\nApp closed,Thanks for using!')
            exit()


mainApp()
