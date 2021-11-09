import time


def fibo_gen(num):
    n1 = 0 
    n2 = 1
    counter = 0
    while True:
        if counter == 0:
            counter += 1
            yield n1
        elif counter == 1:
            counter += 1
            yield n2
        elif counter == num:
            raise StopIteration
        else:
            aux = n1 + n2
            #n1=n2
            #n2=aux
            n1, n2 = n2, aux
            counter += 1
            yield aux
            


if __name__ == '__main__':
    num = int(input('Max number: '))
    fibonnacci = fibo_gen(num)
    for element in fibonnacci:
        print(element)
        time.sleep(1)