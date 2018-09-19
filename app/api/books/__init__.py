from flask import Blueprint

books = Blueprint('books', __name__)

import app.api.books.views