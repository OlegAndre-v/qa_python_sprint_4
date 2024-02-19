import pytest


class TestBooksCollector:
    # test data
    book_1_char = 'Я'
    book_40_char = 'Приключения юного тестировщика и питона.'
    book = 'Пот, кровь и автоматизация'
    invalid_book = '12345678901234567890123456789012345678902'
    invalid_genre = 'Хентай'
    genre1 = 'Ужасы'
    genre2 = 'Мультфильмы'
    # test data

    # Привет, Ирина! Спасибо за твою работу!
    # Постарался учесть и добавить изменения по всем замечениям.

    @pytest.mark.parametrize('book_name, expected_books', [
        (book, {book: ''}),
        (book_1_char, {book_1_char: ''}),
        (book_40_char, {book_40_char: ''})
    ])
    def test_add_new_book_add_one_valid_book(self, books_collector, book_name, expected_books):
        books_collector.add_new_book(book_name)
        assert books_collector.get_books_genre() == expected_books

    # Убрал параметризацию
    def test_add_new_book_add_two_books_same_name(self, books_collector):
        books_collector.add_new_book(self.book)
        assert len(books_collector.get_books_genre()) == 1

    # up
    def test_add_new_book_add_invalid_book_name(self, books_collector):
        books_collector.add_new_book(self.invalid_book)
        assert books_collector.get_books_genre() == {}

    @pytest.mark.parametrize('book_name, genre_name, expected_genre', [
        (book, genre1, genre1),
        (book, genre2, genre2)
    ])
    def test_set_book_genre_set_exist_genre(self, books_collector, book_name, genre_name, expected_genre):
        books_collector.add_new_book(book_name)
        books_collector.set_book_genre(book_name, genre_name)
        assert books_collector.get_book_genre(book_name) == expected_genre

    @pytest.mark.parametrize('book_name, invalid_genre, expected_genre', [
        (book, invalid_genre, '')
    ])
    def test_set_book_genre_set_invalid_genre(self, books_collector, book_name, invalid_genre, expected_genre):
        books_collector.add_new_book(book_name)
        books_collector.set_book_genre(book_name, invalid_genre)
        assert books_collector.get_book_genre(book_name) == expected_genre

    @pytest.mark.parametrize('book_names, genres, expected_result', [
        ([book, book_40_char, book_1_char], [genre1, genre2, invalid_genre], [book])
    ])
    def test_get_books_with_specific_genre_add_three_books(self, books_collector, book_names, genres, expected_result):
        for book_name, genre in zip(book_names, genres):
            books_collector.add_new_book(book_name)
            books_collector.set_book_genre(book_name, genre)
        assert books_collector.get_books_with_specific_genre(genres[0]) == expected_result

    # Изменил набор данных для корректной параметризации.
    @pytest.mark.parametrize('book_name, genre, expected_result', [
        (book, genre2, 1),
        (book, genre1, 0)
    ])
    def test_get_books_for_children_add_three_books_only_one_for_children(self, books_collector, book_name, genre, expected_result):
        books_collector.add_new_book(book_name)
        books_collector.set_book_genre(book_name, genre)
        assert len(books_collector.get_books_for_children()) == expected_result

    @pytest.mark.parametrize('book_name, expected_result', [
        (book, [book])
    ])
    def test_add_book_in_favorites_add_one_book_in_favorites(self, books_collector, book_name, expected_result):
        books_collector.add_new_book(book_name)
        books_collector.add_book_in_favorites(book_name)
        assert books_collector.get_list_of_favorites_books() == expected_result

    @pytest.mark.parametrize('book_names, expected_result', [
        ([book, book_40_char], 1)
    ])
    def test_delete_book_from_favorites_add_two_books_delete_one_book(self, books_collector, book_names, expected_result):
        for book in book_names:
            books_collector.add_new_book(book)
            books_collector.add_book_in_favorites(book)
        books_collector.delete_book_from_favorites(book_names[0])
        assert len(books_collector.get_list_of_favorites_books()) == expected_result
