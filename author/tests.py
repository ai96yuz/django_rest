import datetime
from unittest import mock


import pytz
from django.test import TestCase

from authentication.models import CustomUser
from author.models import Author
from book.models import Book
from order.models import Order

TEST_DATE = datetime.datetime(2017, 4, 10, 12, 00, tzinfo=pytz.utc)
TEST_DATE_END = TEST_DATE + datetime.timedelta(days=15)


class TestAuthorModel(TestCase):
    """Class for CustomUser Model test"""

    def setUp(self):
        """ Create a user object to be used by the tests """
        time_mock = datetime.datetime(2017, 4, 10, 12, 00, tzinfo=pytz.utc)
        with mock.patch('django.utils.timezone.now') as mock_time:
            mock_time.return_value = time_mock
            self.user = CustomUser(id=111, email='email@mail.com', password='1234', first_name='fname',
                                   middle_name='mname',
                                   last_name='lname')
            self.user.save()
            self.user_free = CustomUser(id=222, email='2email@mail.com', password='1234', first_name='2fname',
                                        middle_name='2mname',
                                        last_name='2lname')
            self.user_free.save()

            self.author1 = Author(id=101, name="author1", surname="s1", patronymic="p1")
            self.author1.save()

            self.author2 = Author(id=102, name="author2", surname="s2", patronymic="p2")
            self.author2.save()

            self.book1 = Book(id=101, name="book1", description="description1", count=1)
            self.book1.save()
            self.book1.authors.add(self.author1)
            self.book1.save()

            self.book2 = Book(id=102, name="book2", description="description2")
            self.book2.save()
            self.book2.authors.add(self.author2)
            self.book2.save()

            self.book3 = Book(id=103, name="book3", description="description3")
            self.book3.save()
            self.book3.authors.add(self.author1)
            self.book3.authors.add(self.author2)
            self.book3.save()

            self.order1 = Order(id=101, user=self.user, book=self.book1, plated_end_at=TEST_DATE)
            self.order1.save()
            self.order2 = Order(id=102, user=self.user, book=self.book2, plated_end_at=TEST_DATE)
            self.order2.save()
            self.order3 = Order(id=103, user=self.user, book=self.book3, end_at=TEST_DATE_END, plated_end_at=TEST_DATE)
            self.order3.save()

    def test__str__(self):
        """Test of the CustomUser.__str__() method"""
        author_returned = str(Author.objects.get(id=101))
        author_to_expect = "'id': 101, 'name': 'author1', 'surname': 's1', 'patronymic': 'p1'"

        self.assertEqual(author_returned, author_to_expect)

    def test__repr__(self):
        """Test of the CustomUser.__repr__() method"""
        author_returned = repr(Author.objects.get(id=102))
        author_to_expect = "Author(id=102)"

        self.assertEqual(author_returned, author_to_expect)

    def test_get_by_id_positive(self):
        """Positive test of the CustomUser.get_by_id() method"""
        author = Author.get_by_id(101)
        self.assertEqual(author.id, 101)
        self.assertEqual(author.name, 'author1')
        self.assertEqual(author.surname, "s1")
        self.assertEqual(author.patronymic, "p1")

    def test_get_by_id_negative(self):
        """Negative test of the CustomUser.get_by_id() method"""
        author = Author.get_by_id(999)
        self.assertIsNone(author)

    def test_delete_by_id_positive(self):
        """ Test of the CustomUser.delete_by_id() method """
        self.assertTrue(Author.delete_by_id(101))
        self.assertRaises(Author.DoesNotExist, Author.objects.get, pk=101)

    def test_delete_by_id_negative(self):
        """ Test of the CustomUser.delete_by_id() method """
        self.assertFalse(Author.delete_by_id(999))

    def test_get_all(self):
        """ Positive Test of the CustomUser.create method TEST_DATE_END"""
        authors = list(Author.get_all())
        authors.sort(key=lambda author: author.id)
        self.assertListEqual(authors, [self.author1, self.author2])

    def test_update(self):
        author = Author.objects.get(id=101)
        author.update(name="testName", surname="testSurname", patronymic="testPatronymic")

        author = Author.objects.get(id=101)
        self.assertIsInstance(author, Author)
        self.assertEqual(author.name, "testName")
        self.assertEqual(author.surname, "testSurname")
        self.assertEqual(author.patronymic, "testPatronymic")

    def test_update_only_name(self):
        author = Author.objects.get(id=101)
        author.update(name="testName")

        author = Author.objects.get(id=101)
        self.assertIsInstance(author, Author)
        self.assertEqual(author.name, "testName")
        self.assertEqual(author.surname, "s1")
        self.assertEqual(author.patronymic, "p1")

    def test_update_not_valid_name(self):
        author = Author.objects.get(id=101)
        author.update(name="testName" * 5)

        author = Author.objects.get(id=101)
        self.assertIsInstance(author, Author)
        self.assertEqual(author.name, "author1")
        self.assertEqual(author.surname, "s1")
        self.assertEqual(author.patronymic, "p1")

    def test_create(self):
        author = Author.create(name="testName", surname="s1", patronymic="p1")
        author = Author.objects.get(id=author.id)
        self.assertIsInstance(author, Author)
        self.assertEqual(author.name, "testName")
        self.assertEqual(author.surname, "s1")
        self.assertEqual(author.patronymic, "p1")

    def test_createnot_valid_surname(self):
        author = Author.create(name="testName", surname="s1" * 20, patronymic="p1")
        self.assertIsNone(author)
