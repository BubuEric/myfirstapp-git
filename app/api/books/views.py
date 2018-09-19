from app.api.books import books

@books.route('/')
def books_index():
    return 'books api'
