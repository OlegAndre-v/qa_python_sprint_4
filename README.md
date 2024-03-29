# README для набора тестов BooksCollector
Этот README предоставляет обзор тестов для класса BooksCollector. Класс BooksCollector предназначен для управления коллекцией книг, позволяя пользователям добавлять новые книги, устанавливать жанры и управлять избранными.

## Структура тестов
Набор тестов организован в различные тестовые случаи, каждый из которых обращается к конкретным функциональностям класса BooksCollector. Вот краткое описание реализованных тестов:

- Добавление книг
  - test_add_new_book_add_one_valid_book
    - Этот тест проверяет метод add_new_book, добавляя одну допустимую книгу и проверяя, присутствует ли эта книга в коллекции.

  - test_add_new_book_add_two_books_same_name
      - Этот тест проверяет поведение при попытке добавить две книги с одинаковым именем. Ожидается, что в коллекции будет только один экземпляр.

  - test_add_new_book_add_invalid_book_name
      - Этот тест проверяет поведение при попытке добавить книгу с недопустимым именем. Ожидается, что в этом случае ни одна книга не добавляется.

- Установка жанров
  - test_set_book_genre_set_exist_genre
    - Этот тест проверяет метод set_book_genre, устанавливая существующий жанр для добавленной книги и проверяя, соответствует ли установленный жанр ожидаемому.

  - test_set_book_genre_set_invalid_genre
    - Этот тест проверяет метод set_book_genre, устанавливая недопустимый жанр для добавленной книги и проверяя, что установленный жанр пуст.

- Получение книг с определенным жанром
  - test_get_books_with_specific_genre_add_three_books
    - Этот тест проверяет метод get_books_with_specific_genre, добавляя три книги с разными жанрами и проверяя, что возвращаются только книги с заданным жанром.

  - test_get_books_for_children_add_three_books_only_one_for_children
    - Этот тест проверяет метод get_books_for_children, добавляя три книги с разными жанрами и убеждаясь, что возвращается только одна книга, предназначенная для детей.

- Управление избранными книгами
  - test_add_book_in_favorites_add_one_book_in_favorites
    - Этот тест проверяет метод add_book_in_favorites, добавляя одну книгу в избранное и проверяя, что эта книга присутствует в списке избранных.

  - test_delete_book_from_favorites_add_two_books_delete_one_book
    - Этот тест проверяет метод delete_book_from_favorites, добавляя две книги в избранное и удаляя одну из них. Ожидается, что в списке избранных остается только одна книга.

  ## Для запуска тестов должны быть установлены:
`pytest`
  
  ### Команда для запуска тестов
`pytest -v`

### Команда для оценки покрытия
`pytest --cov=main`

### Команда для подробной оценки покрытия с учетом ветвления
`pytest --cov=main --cov-branch --cov-report=html`
