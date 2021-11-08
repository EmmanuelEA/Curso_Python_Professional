def is_primenumber(num:int) -> int:
    varbol=True
    for ii in range(2,num):
        if num % ii == 0:
            varbol = False
            break
    if varbol==True:
        print("is prime number")
    else:
        print("isn't prime number")


def main():
    while True:
        number = int(input("Number: "))
        is_primenumber(number)


if __name__ == '__main__':
    main()