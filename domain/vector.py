import numpy as np


class Vector:
    '''
        a Vector is a structure of four elements:
            name_id - string - should be unique
            colour - one letter (possible values ‘r’, ‘g’, ‘b’, ‘y’ and ‘m’)
            type -  a positive integer greater or equal to 1
            values -  list of numbers
    '''

    colours = ['r', 'g', 'b', 'y', 'm']

    def __init__(self, name_id: str, colour: str, type: int, values: list):
        '''
        Constructor of the class. Creates a new Vector instance

        :param name_id: unique identifier of a vector
        :param colour: the colour of the vector
        :param type: the type of the vector
        :param values: the values of the vector

        Raises:
        --------
            ValueError
                raised if 'colour' is not one of the given values
            ValueError
                raised if the type is not greater or equal with 1
            ValueError
                raised if the values is empty

        '''
        self.__name_id = name_id

        if colour in self.colours:
            self.__colour = colour
        else:
            raise ValueError("The colour should be  r, g, b, y or m")
        if type >= 1:
            self.__type = type
        else:
            raise ValueError("The type should be greater or equal to 1")
        if len(values) > 0:
            self.__values = values
        else:
            raise ValueError("Add at least a value")

    # getters

    def get_name_id(self):
        '''
        getter method - get the name_id of the vector
        :return: name_id
        '''
        return self.__name_id

    def get_colour(self):
        '''
        getter method - get the colour of the vector
        :return: colour
        '''
        return self.__colour

    def get_type(self):
        '''
        getter method - get the type of the vector
        :return: type
        '''
        return self.__type

    def get_values(self):
        '''
        getter method - get the values of the vector
        :return: values
        '''
        return self.__values.copy()

    # setters

    def set_name_id(self, name_id):
        '''
        setter method - set the  name_id of the vector

        '''
        self.__name_id = name_id

    def set_colour(self, colour):
        '''
        setter method - set the colour
        :param colour: the new colour of the vector

        Rises:
        ------
            ValueError
                raised if 'colour' is not one of the given values
        '''
        if colour in self.colours:
            self.__colour = colour
        else:
            raise ValueError("The colour should be  r, g, b, y or m")

    def set_type(self, type):
        '''
        setter method - set the type of the vector
        :param type: the new type of the vector

        Raises:
        --------
            ValueError
                raised if the type is not greater or equal with 1
        '''
        if type >= 1:
            self.__type = type
        else:
            raise ValueError("The type should be greater or equal to 1")

    def set_values(self, values: list):
        '''
        setter method - set the values for the vector
        :param values:

        Raises:
        --------
            ValueError
                raised if the values is empty
        '''
        if len(values) > 0:
            self.__values = values.copy()
        else:
            raise ValueError("Add at least a value")

    def __str__(self):
        '''
        Converting a Vector object into a string
        :return:
        '''
        vect_str_repr = f"Vector {self.__name_id} of color {self.__colour}, type {self.__type} and values {self.__values}"
        return vect_str_repr

    def add_scalar(self, scalar):
        '''
        Scalar operation - Add a scalar to a vector
        :param scalar:
        :return:
        '''
        c = np.array(self.__values)
        c = c + scalar
        self.__values = c
        return list(self.__values)

    def add(self, other: list):
        '''
        Vector operations - Add two vectors
        :param other: the vector which will be add
        :return: the result vector
        '''
        if len(other) != len(self.__values):
            raise IndexError("The vectors doesn't have the same length")
        a = np.array(self.__values)
        b = np.array(other)
        c = np.array(a.all() + b)
        self.__values = c
        return list(self.__values)

    def subtract(self, other: list):
        '''
        Vector operations - Subtract two vectors
        :param other: the vector which will be subtract
        :return: the result vector
        '''
        if len(other) != len(self.__values):
            raise IndexError("The vectors doesn't have the same length")
        else:
            a = np.array(self.__values)
            b = np.array(other)
            c = a - b
            return list(c)

    def multiplication(self, other: list):
        '''
        Vector operations - Multiplication
        :param other: the vector with which we will multiplicate
        :return: the result vector
        '''
        if len(other) != len(self.__values):
            raise IndexError("The vectors doesn't have the same length")
        else:
            a = np.array(self.__values)
            b = np.array(other)
            c = a.dot(b)
            return c

    def sum_of_elements_in_vector(self):
        '''
        Reduction operations - Sum of elements in a vector
        :return: the sum of the elements in the vector
        '''
        a = np.array(self.__values)
        sum = a.sum()
        return sum

    def product_of_elements_in_vector(self):
        '''
        Reduction operations - Product of elements in a vector
        :return: the product of the elements in the vector
        '''
        product = 1
        for element in self.__values:
            product = product * element
        return product

    def average_of_elements_in_vector(self):
        '''
        Reduction operations - Average of elements in a vector
        :return: the average of the elements in the vector
        '''
        if len(self.__values) == 1:
            return self.__values[0]
        else:
            a = np.array(self.__values)
            avg = (a.min() + a.max()) / len(a)
            return avg

    def minimum_of_a_vector(self):
        '''
        Reduction operations - Minimum of a vector
        :return: the minimum of a vector
        '''
        a = np.array(self.__values)
        return a.min()

    def maximum_of_a_vector(self):
        '''
        Reduction operation - Maximum of a vector
        :return: the maximum of a vector
        '''
        a = np.array(self.__values)
        return a.max()
