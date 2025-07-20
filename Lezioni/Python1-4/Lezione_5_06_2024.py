with open("prova//Lezioni/file.txt") as file:
    pass

class ContextManagar:

    def __enter__(self):

        print("Risorsa Acquisita!")

        return self
    
    def __exit__(self, exc_type: Exception, exc_value, traceback: str):

        if exc_type is not None:

            pass

        print("Risorsa Rilasciata!")

        return False

with ContextManagar() as manager:

    print("Sono dentro with")