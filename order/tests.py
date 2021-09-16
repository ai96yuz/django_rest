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


class TestOrderModel(TestCase):
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

    def test__str__end_at_is_None(self):
        """Test of the CustomUser.__str__() method"""
        order_returned = str(Order.objects.get(id=101))
        order_to_expect = "'id': 101, 'user': CustomUser(id=111), 'book': Book(id=101), 'created_at': '2017-04-10 12:00:00+00:00', 'end_at': None, 'plated_end_at': '2017-04-10 12:00:00+00:00'"

        self.assertEqual(order_returned, order_to_expect)

    def test__str__end_at_is_not_None(self):
        """Test of the CustomUser.__str__() method"""
        order = str(Order.objects.get(id=103))
        order_to_expect = "'id': 103, 'user': CustomUser(id=111), 'book': Book(id=103), 'created_at': '2017-04-10 12:00:00+00:00', 'end_at': '2017-04-25 12:00:00+00:00', 'plated_end_at': '2017-04-10 12:00:00+00:00'"

        self.assertEqual(order, order_to_expect)

    def test__repr__(self):
        """Test of the CustomUser.__repr__() method"""
        user_returned = repr(Order.objects.get(id=102))
        user_to_expect = "Order(id=102)"

        self.assertEqual(user_returned, user_to_expect)

    def test_get_by_id_positive(self):
        """Positive test of the CustomUser.get_by_id() method"""
        order = Order.get_by_id(101)
        self.assertEqual(order.id, 101)
        self.assertEqual(order.user, self.user)
        self.assertEqual(order.book, self.book1)
        self.assertEqual(order.created_at, TEST_DATE)
        self.assertEqual(order.end_at, None)
        self.assertEqual(order.plated_end_at, TEST_DATE)

    def test_get_by_id_negative(self):
        """Negative test of the CustomUser.get_by_id() method"""
        order = Order.get_by_id(55)
        self.assertIsNone(order)

    def test_delete_by_id_positive(self):
        """ Test of the CustomUser.delete_by_id() method """
        self.assertTrue(Order.delete_by_id(103))
        self.assertRaises(Order.DoesNotExist, Order.objects.get, pk=103)
        self.assertEqual(self.book3, Book.objects.get(id=103))
        self.assertEqual(self.user, CustomUser.objects.get(id=111))

    def test_delete_by_id_negative(self):
        """ Test of the CustomUser.delete_by_id() method """
        self.assertFalse(Order.delete_by_id(999))

    def test_create_positive(self):
        """ Positive Test of the CustomUser.create method """
        time_mock = datetime.datetime(2017, 4, 10, 12, 00, tzinfo=pytz.utc)
        with mock.patch('django.utils.timezone.now') as mock_time:
            mock_time.return_value = time_mock
            order = Order.create(self.user_free, self.book2, TEST_DATE_END)
            self.assertIsInstance(order, Order)
            self.assertEqual(order.user, self.user_free)
            self.assertEqual(order.book, self.book2)
            self.assertEqual(order.created_at, TEST_DATE)
            self.assertIsNone(order.end_at)
            self.assertEqual(order.plated_end_at, TEST_DATE_END)

    def test_create_negative_not_saved_user(self):
        """ Positive Test of the CustomUser.create method TEST_DATE_END"""
        user = CustomUser()
        order = Order.create(user, self.book2, TEST_DATE_END)
        self.assertIsNone(order)

    def test_create_negative_limit_book(self):
        """ Positive Test of the CustomUser.create method TEST_DATE_END"""

        order = Order.create(self.user_free, self.book1, TEST_DATE_END)
        self.assertIsNone(order)

    def test_get_all(self):
        """ Positive Test of the CustomUser.create method TEST_DATE_END"""
        orders = Order.get_all()
        self.assertListEqual(orders, [self.order1, self.order2, self.order3])

    def test_get_not_returned_books(self):
        """ Positive Test of the CustomUser.create method TEST_DATE_END"""
        orders = Order.get_not_returned_books()
        self.assertListEqual(orders, [self.order1, self.order2])

    def test_update_plated_end_at(self):
        order = Order.objects.get(id=101)
        new_date = TEST_DATE_END + datetime.timedelta(days=4)
        order.update(plated_end_at=new_date)

        order = Order.objects.get(id=101)
        self.assertEqual(order.id, 101)
        self.assertEqual(order.user, self.user)
        self.assertEqual(order.book, self.book1)
        self.assertEqual(order.created_at, TEST_DATE)
        self.assertEqual(order.end_at, None)
        self.assertEqual(order.plated_end_at, new_date)
    def test_update_end_at(self):
        order = Order.objects.get(id=101)
        new_date = TEST_DATE_END + datetime.timedelta(days=4)
        order.update(end_at=new_date)

        order = Order.objects.get(id=101)
        self.assertEqual(order.id, 101)
        self.assertEqual(order.user, self.user)
        self.assertEqual(order.book, self.book1)
        self.assertEqual(order.created_at, TEST_DATE)
        self.assertEqual(order.end_at, new_date)
        self.assertEqual(order.plated_end_at, TEST_DATE)