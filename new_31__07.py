def my_deco(sam_func):
    def wrapper():
        print('Hello my first deco')
        sam_func()
        print('qwerty')
        return sam_func
    return wrapper

@my_deco
def list_prin():
    print('первая функция декор')


list_prin = my_deco(list_prin)
list_prin()