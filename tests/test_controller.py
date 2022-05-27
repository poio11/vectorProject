from unittest import TestCase

from domain.vector import Vector
from infrastructure.vector_repo import VectorRepository
from controller import VectorController


class TestVectorController(TestCase):

    def setUp(self):
        self.empty_controller = VectorController(VectorRepository())
        self.vector_controller = VectorController(VectorRepository([Vector("1", "r", 1, [1, 2, 3])]))
        self.lor_controller = VectorController(VectorRepository([
            Vector("2", "r", 1, [1, 2, 3]),
            Vector("3", "m", 2, [5, 6, 7]),
            Vector("4", "y", 1, [1, 5, 9, 10, 12])
        ]))
        self.new_vector = Vector("5", "r", 1, [1, 3])

    def test_create(self):
        self.assertEqual(len(self.empty_controller.get_vectors()), 0)
        self.assertEqual(len(self.vector_controller.get_vectors()), 1)
        self.assertEqual(len(self.lor_controller.get_vectors()), 3)

        self.assertEqual(str(self.empty_controller), "Number of vectors in the list: 0\n")
        self.assertEqual(str(self.vector_controller), "Number of vectors in the list: 1\nVector 1 of color r, type 1 and values [1, 2, 3]\n")
        self.assertEqual(str(self.lor_controller), "Number of vectors in the list: 3\nVector 2 of color r, type 1 and values [1, 2, 3]\nVector 3 of color m, type 2 and values [5, 6, 7]\nVector 4 of color y, type 1 and values [1, 5, 9, 10, 12]\n")

    def test_get_vector_at_index(self):
        for index in range(-2, 2):
            self.assertRaises(IndexError, self.empty_controller.get_vector_at_index, index)
        for index in range(-2, 0):
            self.assertRaises(IndexError, self.vector_controller.get_vector_at_index, index)
            self.assertRaises(IndexError, self.lor_controller.get_vector_at_index, index)
        for index in range(1, 100):
            self.assertRaises(IndexError, self.vector_controller.get_vector_at_index, index)
        for index in range(3, 100):
            self.assertRaises(IndexError, self.lor_controller.get_vector_at_index, index)

        res = self.vector_controller.get_vector_at_index(0)
        self.assertEqual(res.get_name_id(), "1")
        self.assertEqual(res.get_colour(), "r")
        self.assertEqual(res.get_type(), 1)
        self.assertEqual(res.get_values(), [1, 2, 3])

        res = self.lor_controller.get_vector_at_index(2)
        self.assertEqual(res.get_name_id(), "4")
        self.assertEqual(res.get_colour(), "y")
        self.assertEqual(res.get_type(), 1)
        self.assertEqual(res.get_values(), [1, 5, 9, 10, 12])

    def test_update_at_index(self):
        for index in range(-2, 2):
            self.assertRaises(IndexError, self.empty_controller.update_at_index, index, "", "r", 1, [1])
        for index in range(-2, 0):
            self.assertRaises(IndexError, self.vector_controller.update_at_index, index, "", "r", 1, [])
            self.assertRaises(IndexError, self.lor_controller.update_at_index, index, "", "r", 1, [])
        for index in range(1, 100):
            self.assertRaises(IndexError, self.vector_controller.update_at_index, index, "", "r", 1, [])
        for index in range(3, 100):
            self.assertRaises(IndexError, self.lor_controller.update_at_index, index, "", "r", 1, [])

        self.vector_controller.update_at_index(0, self.new_vector.get_name_id(), self.new_vector.get_colour(), self.new_vector.get_type(), self.new_vector.get_values())
        res = self.vector_controller.get_vector_at_index(0)
        self.assertEqual(res.get_name_id(), "5")
        self.assertEqual(res.get_colour(), "r")
        self.assertEqual(res.get_type(), 1)
        self.assertEqual(res.get_values(), [1, 3])

        self.lor_controller.update_at_index(1, self.new_vector.get_name_id(), self.new_vector.get_colour(), self.new_vector.get_type(), self.new_vector.get_values())
        res = self.lor_controller.get_vector_at_index(1)
        self.assertEqual(res.get_name_id(), "5")
        self.assertEqual(res.get_colour(), "r")
        self.assertEqual(res.get_type(), 1)
        self.assertEqual(res.get_values(), [1, 3])

    def test_update_by_name_id(self):
        #
        self.assertRaises(IndexError, self.empty_controller.update_by_name_id, "1", "r", 1, [1])
        #
        self.assertRaises(IndexError, self.vector_controller.update_by_name_id, "5", "r", 1, [1])
        #
        self.assertRaises(IndexError, self.lor_controller.update_by_name_id, "6", "r", 1, [1])

        self.vector_controller.update_at_index(0, self.new_vector.get_name_id(), self.new_vector.get_colour(), self.new_vector.get_type(), self.new_vector.get_values())
        res = self.vector_controller.get_vector_at_index(0)
        self.assertEqual(res.get_name_id(), "5")
        self.assertEqual(res.get_colour(), "r")
        self.assertEqual(res.get_type(), 1)
        self.assertEqual(res.get_values(), [1, 3])

        self.lor_controller.update_at_index(1, self.new_vector.get_name_id(), self.new_vector.get_colour(), self.new_vector.get_type(), self.new_vector.get_values())
        res = self.lor_controller.get_vector_at_index(1)
        self.assertEqual(res.get_name_id(), "5")
        self.assertEqual(res.get_colour(), "r")
        self.assertEqual(res.get_type(), 1)
        self.assertEqual(res.get_values(), [1, 3])

    def test_delete_by_index(self):
        for index in range(-2, 2):
            self.assertRaises(IndexError, self.empty_controller.update_at_index, index, "", "r", 1, [1])
        for index in range(-2, 0):
            self.assertRaises(IndexError, self.vector_controller.update_at_index, index, "", "r", 1, [])
            self.assertRaises(IndexError, self.lor_controller.update_at_index, index, "", "r", 1, [])
        for index in range(1, 100):
            self.assertRaises(IndexError, self.vector_controller.update_at_index, index, "", "r", 1, [])
        for index in range(3, 100):
            self.assertRaises(IndexError, self.lor_controller.update_at_index, index, "", "r", 1, [])

        name_id = self.vector_controller.get_vector_at_index(0).get_name_id()
        self.vector_controller.delete_by_index(0)
        for vector in self.vector_controller.get_vectors():
            self.assertNotEqual(name_id, vector.get_name_id())

        name_id = self.lor_controller.get_vector_at_index(1).get_name_id()
        self.lor_controller.delete_by_index(1)
        for vector in self.lor_controller.get_vectors():
            self.assertNotEqual(name_id, vector.get_name_id())

        name_id = self.lor_controller.get_vector_at_index(1).get_name_id()
        self.lor_controller.delete_by_index(1)
        for vector in self.lor_controller.get_vectors():
            self.assertNotEqual(name_id, vector.get_name_id())

    def test_delete_by_name_id(self):
        #
        self.assertRaises(IndexError, self.empty_controller.update_by_name_id, "1", "r", 1, [1])
        #
        self.assertRaises(IndexError, self.vector_controller.update_by_name_id, "5", "r", 1, [1])
        #
        self.assertRaises(IndexError, self.lor_controller.update_by_name_id, "6", "r", 1, [1])

        name_id = "2"
        self.lor_controller.delete_by_name_id(name_id)
        for vector in self.lor_controller.get_vectors():
            self.assertNotEqual(name_id, vector.get_name_id())

        name_id = "3"
        self.lor_controller.delete_by_name_id(name_id)
        for vector in self.lor_controller.get_vectors():
            self.assertNotEqual(name_id, vector.get_name_id())
