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
    def __init__(self, book_id: str, title: str, author: str):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self):
        self.is_borrowed = True

    def return_book(self):
        self.is_borrowed = False

class Member:
    def __init__(self, member_id: str, name: str):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []
        
    def borrow_book(self, book: Book):
        if not book.is_borrowed:
            self.borrowed_books.append(book)
            book.borrow()
        else:
            raise ValueError("Book is already borrowed")

    def return_book(self, book: Book):
        if book not in self.borrowed_books:
            raise ValueError("Book not borrowed by this member")            
        self.borrowed_books.remove(book)
        book.return_book()

class Library():
    def __init__(self):
        self.books = {}
        self.members = {}

    def add_book(self, book_id: str, title: str, author: str): 
        book = Book(book_id, title, author)
        self.books[book_id] = book

    def register_member(self, member_id:str, name: str): 
        member = Member(member_id, name)
        self.members[member_id] = member

    def borrow_book(self, member_id: str, book_id: str):
        if member_id in self.members and book_id in self.books:
            member: Member = self.members[member_id]
            book: Book = self.books[book_id]
            member.borrow_book(book)
        elif member_id not in self.members:
            raise ValueError("Member not found")
        else:
            raise ValueError("Book not found")
        
    def return_book(self, member_id: str, book_id: str):
        if member_id in self.members and book_id in self.books:
            member: Member = self.members[member_id]
            book: Book = self.books[book_id]
            member.return_book(book)

        

    def get_borrowed_books(self, member_id) -> list[Book]:
        if member_id in self.members:
            member: Member = self.members[member_id]
            list_title: list[str] = []
            for book in member.borrowed_books:
                list_title.append(book.title)
            return list_title

#Data una stringa s e una lista di stringhe wordDict, restituisce True se s può essere segmentato in una sequenza separata da spazi di una o più parole del dizionario; 
# False altrimenti. Tieni presente che la stessa parola nel dizionario può essere riutilizzata più volte nella segmentazione.
#Example: print(word_break("leetcode",["leet","code"]))
# -> True

def word_break(s, wordDict):
    dp = [False] * (len(s) + 1)
    dp[0] = True

    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in wordDict:
                dp[i] = True
                break

    return dp[-1]
        
'''
Progettare un semplice sistema bancario con i seguenti requisiti:

Classe del Account:
    Attributi:
        account_id: str - identificatore univoco per l'account.
        balance: float - il saldo attuale del conto.
    Metodi:
        deposit(amount: float) - aggiunge l'importo specificato al saldo del conto.
        get_balance(): restituisce il saldo corrente del conto.
Classe Bank:
    Attributi:
        accounts: dict[str, Account] - un dizionario per memorizzare gli account in base ai loro ID.
    Metodi:
        create_account(account_id): crea un nuovo account con l'ID specificato e un saldo pari a 0.
        deposit(account_id, amount): deposita l'importo specificato sul conto con l'ID fornito.
        get_balance(account_id): restituisce il saldo del conto con l'ID specificato.
'''

class Account:
    def __init__(self, account_id: str):
        self.account_id = account_id
        self.balance = 0.0
        
    def deposit(self, amount: float):
        if amount > 0:
            self.balance += amount  
        else:
            raise ValueError("L'importo del deposito deve essere positivo")
        
    def get_balance(self) -> float:
        return self.balance
    
class Bank:
    def __init__(self) -> float:
        self.accounts = {}
        
    def create_account(self, account_id):
        if account_id not in self.accounts:
            new_account = Account(account_id)
            self.accounts[account_id] = new_account
            return new_account 
        else:
            raise ValueError("L'account ID esiste già")
    
    def deposit(self, account_id, amount):
        if account_id in self.accounts:
            self.accounts[account_id].deposit(amount) 
        else:
            raise ValueError("Account ID non trovato")
    
    def get_balance(self, account_id):
        if account_id in self.accounts:
            return self.accounts[account_id].get_balance()
        else:
            raise ValueError("Account ID non trovato")
        
        
