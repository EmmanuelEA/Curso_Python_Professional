from datetime import datetime

def execution_time(func):
    def wrapper(*args, **kwargs): #Para poder pasar cualquier argumento o ninguno
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print("Pasaron " + str(time_elapsed.total_seconds()) + " segundos")
    return wrapper

@execution_time
def random_func():
    for _ in range(1,1000000):#si no me interesa obtener el indicie
        pass


@execution_time
def suma(a: int, b: int) -> int:
    return a + b


@execution_time
def saludo(nombre="Emmanuel"):
    print("Hola " + nombre)


saludo("Cesar")
suma(4,6)
random_func()