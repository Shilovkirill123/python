def ask_user(ask):
    while True :
        try:
            ask=input('Как дела? ')
            if ask == 'Хорошо' :
                print('Рад за Вас')
        except KeyboardInterrupt:
                print('Пока')
                break
        
ask_user('Хорошо')
