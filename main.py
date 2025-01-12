from datetime import datetime, timedelta


class Book:
    books = {}
    book_id = 1
    def __init__(self, book_name, author, year):
        self.book_id = Book.book_id
        Book.book_id += 1
        self.book_name = book_name
        self.author = author
        self.year = year
        self.status = "Available"

class User:
    users = {}
    user_id = 1
    def __init__(self, username, created_at, email):
        self.user_id = User.user_id
        User.user_id += 1
        self.username = username
        self.created_at = created_at
        self.email = email

class Issue:
    issues = {}
    issue_id = 1
    def __init__(self, book_id, user_id, issue_date, expected_return_date, status, fine):
        self.issue_id = Issue.issue_id
        Issue.issue_id += 1
        self.user_id = user_id
        self.book_id = book_id
        self.issue_date = issue_date
        self.expected_return_date = expected_return_date
        self.return_date = None
        self.status = status
        self.fine = fine

def register_user(username, email):
    user = User(username=username, email=email, created_at=datetime.now())
    User.users[user.user_id] = user
    return user

def get_user(user_id):
    return User.users[user_id]

def add_book(book_name, author, year):
    added_book = Book(book_name=book_name, author=author, year=year)
    Book.books[added_book.book_id] = added_book
    return added_book

def get_book(book_id):
    return Book.books[book_id]

def search_books(book_name=None, author=None):
    books = [book for book in Book.books if (book_name and book.book_name == book_name) or (author and book.author == author)]
    return [book.book_name for book in books]

def issue_book(book_id, user_id):
    book = Book.books[book_id]
    if book.status != "Available":
        return "Book not available"
    issue_obj = Issue(book_id, user_id, datetime.now(), datetime.now()+ timedelta(days=7), "issued", 0)
    book.status = "issued"
    Issue.issues[issue_obj.issue_id] = issue_obj
    return issue_obj

def get_issue_details(issue_id):
    return Issue.issues[issue_id]

def return_book(issue_id):
    issue_obj = Issue.issues[issue_id]
    return_date = datetime.now() + timedelta(days=10)
    issue_obj.return_date = return_date
    if return_date > issue_obj.expected_return_date:
        fine = 100*(return_date - issue_obj.expected_return_date).days
        issue_obj.fine = fine
    return_summary = issue_obj
    book = Book.books[issue_obj.book_id]
    book.status = "Available"
    issue_obj.status = "closed"
    return return_summary

book1 = add_book("Ikigai", "Hector Garcia", 2016)
book2 = add_book("Atomic Habits", "James Clear", 2018)
add_book("Save The Cat!", "Blake Snyder", 2005)

user1 = register_user("hiteshdullu", "hiteshdullu@gmail.com")
user2 = register_user("anuradhadullu", "anuradhadullu@gmail.com")

issue1 = issue_book(user1.user_id, book1.book_id)
print(issue1.__dict__)

return1 = return_book(issue1.issue_id)
print(return1.__dict__)



