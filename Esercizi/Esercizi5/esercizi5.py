#Date due stringhe s e t, restituire True se t è un anagramma di s, e False altrimenti.
#Un anagramma è una parola o una frase formata riorganizzando le lettere di una parola o frase diversa, 
#in genere utilizzando tutte le lettere originali esattamente una volta.
#Example: print(anagram("anagram","nagaram")
# -> True

def anagram(s: str, t: str) -> bool:
    s = s.lower()
    t = t.lower()
    if len(s) == len(t):
        if sorted(s) == sorted(t):
            return True
        return False
    return False 

#Data l'inizio di una lista concatenata, invertire la lista e restituire la lista invertita.
#Example: head = ListNode(val=1, next=ListNode(val=2, next=ListNode(val=3, next=ListNode(val=4, next=ListNode(val=5)))))
#print(reverse_list(head))
# -> [5, 4, 3, 2, 1]

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def reverse_list(head: ListNode) -> list[int]:
    
    val_list = []
    current_node = head
    while current_node != None:
        val_list.append(current_node.val)
        current_node = current_node.next
    val_list.reverse()
    return val_list

'''
Progettare un sistema di gestione della biblioteca con i seguenti requisiti:

    Classe Book:
        Attributi:
            book_id: str - Identificatore di un libro.
            title: str - titolo del libro.
            author: str - autore del libro
            is_borrowed: boolean - booleano che indica se il libro è in prestito o meno.
        Metodi:
            borrow()-Contrassegna il libro come preso in prestito se non è già preso in prestito.
            return_book()- Contrassegna il libro come restituito.

    Classe Member:
        Attributi:
            member_id: str - identificativo del membro.
            name: str - il nome del membro.
            borrowed_books: list[Book] - lista dei libri presi in prestito.
        Metodi:
            borrow_book(book): aggiunge il libro nella lista borrowed_books se non è già stato preso in prestito.
            return_book(book): rimuove il libro dalla lista borrowed_books.

    Classe Library:
        Attributi:
            books: dict[str, Book] - dizionario che ha per chiave l'id del libro e per valore l'oggetto Book
            members: dict[str, Member] - dizionario che ha per chiave l'id del membro e per valore l'oggetto Membro
        Methodi:
            add_book(book_id: str, title: str, author: str): Aggiunge un nuovo libro nella biblioteca.
            register_member(member_id:str, name: str): Iscrive un nuovo membro nella biblioteca.
            borrow_book(member_id: str, book_id: str): Permette al membro di prendere in prestito il libro.
            return_book(member_id: str, book_id: str): Permette al membro di restituire il libro.
            get_borrowed_books(member_id): list[Book] - restituisce la lista dei libri presi in prestito dal membro.
'''


class Book:
    def __init__(self, book_id: str, title: str, author: str, is_borrowed: bool):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed

    def borrow(self):
        pass

    def return_book(self):
        pass

class Member:
    def __init__(self, member_id: str, name: str, borrowed_books: list[Book]):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = borrowed_books

    def borrow_book(book):
        pass

    def return_book(book):
        pass

class Library:
    def __init__(self, books: dict[str, Book], members: dict[str, Member]):
        self.books = books
        self.members = members

    def add_book(self, book_id: str, title: str, author: str): 
        pass

    def register_member(self, member_id:str, name: str): 
        pass

    def borrow_book(member_id: str, book_id: str):
        pass

    def return_book(member_id: str, book_id: str):
        pass

    def get_borrowed_books(member_id) -> list[Book]:
        pass