def mystring(string):
    def multi(num):
        assert type(string) == str, "solo puedes utilizar cadenas"
        return string*num
    return multi


def make_repeater_of(n):
    def repeater(string):
        return string * n
    return repeater


def run():
    mystr = mystring("hola")
    print(mystr(2))
    repeat_5 = make_repeater_of(5)
    print(repeat_5("Hola"))


if __name__ == '__main__':
    run()