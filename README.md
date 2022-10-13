# E-Book-Project
API Documentation
URLS                                                  METHOD         DESCRIPTION                              DATA
1-localhost:8000/token/                                post          to generate token                        username & password
2-localhost:8000/api/signup/                           post          to create user                           user details
3-localhost:8000/api/genres/                           get           to list all genres in ebook              null
4-localhost:8000/api/genres/{genre-id}/                get           to list a specific genre with id         null
5-localhost:8000/api/{genre-id}/add_books/             post          to add a book to a specific genre        book details
6-localhost:8000/api/{genre-id}/get_books/             get           to list all books in a specific genre    null
7-localhost:8000/api/books?genre=Non-Fiction           get           to filter books with genres              null
8-localhost:8000/api/books/{book-id}/add_review/       post          to add reviews to a specific book        review description

USER
1-I have created a superuser with usernam=niyas and password=niyas
2-with this super user i have created all six genres and also added books and reviews to the books
3-and runs with python manage.py runserver in thunderclient
