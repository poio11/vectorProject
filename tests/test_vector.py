from unittest import TestCase
from domain.vector import Vector


class TestVector(TestCase):

    def setUp(self):
        '''
        This function will be run at the beginning of each test method
        :return:
        '''
        self.vector = Vector("1", "r", 1, [1, 2, 3])

    def test_create(self):
        # test getters
        self.assertEqual(self.vector.get_name_id(), "1")
        self.assertEqual(self.vector.get_colour(), "r")
        self.assertEqual(self.vector.get_type(), 1)
        self.assertEqual(self.vector.get_values(), [1, 2, 3])

        self.assertEqual(str(self.vector), "Vector 1 of color r, type 1 and values [1, 2, 3]")

        # test if error is raised when colour is not from the given values
        self.assertRaises(ValueError, Vector, "2", "t", 2, [1])

        # test if error is raised when type is not greater of equal with 1
        self.assertRaises(ValueError, Vector, "3", "r", -1, [2])

        # test if error is raised if values is empty
        self.assertRaises(ValueError, Vector, "4", "r", 1, [])

        # test setters

        # test if a error is raised when colour is not a proper value
        self.assertRaises(ValueError, self.vector.set_colour, "t")

        # test if a error is raised when type is not greater or equal with 1
        self.assertRaises(ValueError, self.vector.set_type, -1)

        # test if a error is raised if values is empty
        self.assertRaises(ValueError, self.vector.set_values, [])

    def test_add_scalar(self):
        scalar = 10
        self.assertEqual(self.vector.add_scalar(scalar), [11, 12, 13])

        scalar = 5
        self.assertEqual(self.vector.add_scalar(scalar), [16, 17, 18])

        scalar = 2
        self.assertEqual(self.vector.add_scalar(scalar), [18, 19, 20])

    def test_add(self):
        other = Vector("2", "r", 1, [5, 6, 7])
        self.assertEqual(self.vector.add(other.get_values()), [6, 7, 8])

        other = Vector("2", "r", 1, [1, 2, 3])
        self.assertEqual(self.vector.add(other.get_values()), [2, 3, 4])

        other = Vector("2", "r", 1, [5, 6])
        self.assertRaises(IndexError, self.vector.add, other.get_values())

    def test_substract(self):
        other = Vector("2", "r", 1, [5, 6, 7])
        self.assertEqual(self.vector.subtract(other.get_values()), [-4, -4, -4])

        other = Vector("2", "r", 1, [1, 6, 7])
        self.assertEqual(self.vector.subtract(other.get_values()), [0, -4, -4])

        other = Vector("2", "r", 1, [5, 6])
        self.assertRaises(IndexError, self.vector.add, other.get_values())

    def test_multiplication(self):
        other = Vector("2", "r", 1, [4, 5, 5])
        self.assertEqual(self.vector.multiplication(other.get_values()), 29)

        other = Vector("2", "r", 1, [1, 2, 3])
        self.assertEqual(self.vector.multiplication(other.get_values()), 14)

        other = Vector("2", "r", 1, [5, 6])
        self.assertRaises(IndexError, self.vector.multiplication, other.get_values())

    def test_sum(self):
        self.assertEqual(self.vector.sum_of_elements_in_vector(), 6)

        other = Vector("2", "r", 1, [5, 6, 7])
        self.assertEqual(other.sum_of_elements_in_vector(), 18)

        other = Vector("2", "r", 1, [10])
        self.assertEqual(other.sum_of_elements_in_vector(), 10)

    def test_product(self):
        self.assertEqual(self.vector.product_of_elements_in_vector(), 6)

        other = Vector("2", "r", 1, [5, 6, 7])
        self.assertEqual(other.product_of_elements_in_vector(), 210)

        other = Vector("2", "r", 1, [10])
        self.assertEqual(other.product_of_elements_in_vector(), 10)

    def test_avg(self):
        self.assertEqual(self.vector.average_of_elements_in_vector(), 1.3333333333333333)

        other = Vector("2", "r", 1, [5, 6, 7])
        self.assertEqual(other.average_of_elements_in_vector(), 4.0)

        other = Vector("2", "r", 1, [10])
        self.assertEqual(other.average_of_elements_in_vector(), 10)

    def test_min(self):
        self.assertEqual(self.vector.minimum_of_a_vector(), 1)

        other = Vector("2", "r", 1, [5, 6, 7])
        self.assertEqual(other.minimum_of_a_vector(), 5)

        other = Vector("2", "r", 1, [10])
        self.assertEqual(other.minimum_of_a_vector(), 10)

    def test_max(self):
        self.assertEqual(self.vector.maximum_of_a_vector(), 3)

        other = Vector("2", "r", 1, [5, 6, 7])
        self.assertEqual(other.maximum_of_a_vector(), 7)

        other = Vector("2", "r", 1, [10])
        self.assertEqual(other.maximum_of_a_vector(), 10)