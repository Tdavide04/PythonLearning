# def get_time(func):

#     def wrapper(*args):
#         import time
        
#         start = time.time()

#         func(*args)

#         end = time.time()
#         elapsed_time = end - start
#         print(f"{elapsed_time=}")

#     return wrapper

# @get_time
# def say_hello(name: str) -> None:
#     print(f"Hello, {name}")

# say_hello("Davide")


# def generator():
#     yield "A"
#     yield "B"
#     yield "C"

# prova_generatore = generator()
# print(next(prova_generatore))
# print(next(prova_generatore))

import time
# from contextlib import contextmanager

# @contextmanager
# def context_manager_decorator(*args):

#     start_time: float = time.time()
#     yield
#     end_time: float = time.time()
#     elapsed_time = end_time - start_time
#     print(f"{elapsed_time=}")


def funzione(id: int):
    import time
    print(f"{id=} time {time.time()}")
    time.sleep(1.5)
    print(f"{id=} time {time.time()}")

if __name__ == "__main__":

    import threading

    # x: threading.Thread = threading.Thread(target=funzione, args=(1,))
    # print(f"Prima di runnare il Thread {time.time()}")
    # x.start()
    # print(f"Ho runnato il Thread {time.time()}")

    # print(f"Ho finito di runnare il Thread????? {time.time()}")

    lista_thread: list[threading.Thread] = []

    for id in range(3):

        x: threading.Thread = threading.Thread(target=funzione, args=(id,))
        lista_thread.append(x)
        print(f"Prima di runnare il Thread {time.time()}")
        x.start()
        print(f"Ho runnato il Thread {time.time()}")

    for t in lista_thread:

        t.join()
        print(f"Terminato!")
