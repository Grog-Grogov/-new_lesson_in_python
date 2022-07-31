#Для примера с двумя аргументами написать обычную функцию add.
#️Написать анонимную функцию, которая получает 4 аргумента и складывает их между собой.
def new_len(q,w):
    return q + w
print(new_len(4,6))

asd = lambda a,b,c,d:a + b + c + d
print(asd(4,7,9,3))
print(new_len(44,77))


lambda a,b,c,v:a + b + c + v
print(lambda a,b,c,v:a + b + c + v)

a = [(1, 12), (4, 1), (9, 10), (13, -3)]
a.sort(key=lambda x: x[1])
print(a)
