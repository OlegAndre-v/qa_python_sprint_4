import pytest
from main import BooksCollector


# добавил фикстуру в отдельны файл
@pytest.fixture(scope='function')
def books_collector():
    return BooksCollector()
