from flask import Flask, redirect, render_template, request
from flask import Blueprint
from models.book import Book
from repositories import book_repository
from repositories import author_repository

books_blueprint = Blueprint("books", __name__)

@books_blueprint.route("/books")
def books():
    books = book_repository.select_all()
    return render_template("books/index.html", all_books = books)

@books_blueprint.route("/<id>/book/", methods=['GET'])
def book(id):
    book = book_repository.select(id)
    return render_template("books/book.html", book = book)

@books_blueprint.route("/books/new", methods=['GET'])
def new_book():
    authors = author_repository.select_all()
    return render_template("/books/new.html", existing_authors = authors)

@books_blueprint.route("/books", methods=['POST'])
def add_book():
    title = request.form['title']
    author_id = request.form['author_id']
    author = author_repository.select(author_id)
    book = Book(title, author)
    book_repository.add_book(book)
    return redirect('/books')


