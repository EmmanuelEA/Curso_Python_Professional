def countstring(func):
    def wrapper(*args, **kwargs): 
        print("Cuenta la cantidad de letras en el texto")
        func(*args,**kwargs)
        return wrapper
    return wrapper

a = """
Esto es una prueba para contar letras o palabras 
en una variable con texto
""" 

@countstring
def contar(texto,p):
    print(f'Hay {texto.count(p)} "{p}" en la variable')


contar(a, "a")