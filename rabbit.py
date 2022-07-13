def rabbit_white(*args):
     return('bol', 'fix', 'coll', 'white', 2, [23], 'Зигмунд')
for i in rabbit_white():
    print(i)
    if i == 'white':
        print('В списке есть слово "white" - rabbit')
