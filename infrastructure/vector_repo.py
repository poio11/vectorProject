from domain.vector import Vector
from matplotlib import pyplot as plt
from typing import List


class VectorRepository:
    '''
    Represents a collection of Vector instances
    '''

    def __init__(self, vector_list: List[Vector] = []):
        '''
        Constructor of the class. Creates a new collection with Vector instances
        :param vector_list: list of vectors in the collection
        '''
        self.__vectors = []
        for vector in vector_list:
            if self.name_id_exists(vector.get_name_id()):
                raise IndexError(f"The vector with name_if {vector.get_name_id()} is already in the repository")
            self.__vectors.append(vector)

    def __str__(self):
        '''
        Returns the string representation of the repository
        :return: string representation of an instance
        '''
        repr_str = f"Number of vectors in the list: {len(self.__vectors)}\n"
        for vector in self.__vectors:
            repr_str += str(vector) + "\n"
        return str(repr_str)

    def add_vector_to_repository(self, vector: Vector):
        '''
        Add a vector to the repository
        :return:
        '''
        if self.name_id_exists(vector.get_name_id()):
            raise IndexError(f"name_id {vector.get_name_id()} exist in the Repository")
        else:
            return self.__vectors.append(vector)

    def get_all_vectors(self):
        '''
        Get all vectors
        :return: All vectors from the repository
        '''
        return self.__vectors

    def get_vector_at_index(self, index):
        '''
        Get a vector at a given index
        :param index: int
        Raises:
        --------
            IndexError
                raised if the index does not exist in the repository
        '''
        if 0 <= index < len(self.__vectors):
            return self.__vectors[index]
        else:
            raise IndexError(f"The index should be between 0 and {len(self.__vectors)}, but {index} got")

    def update_vector_at_index(self, index, name_id, colour, type, values):
        '''
        Update a vector at a given index
        :param index: the index of the vector which will be updated
        :param name_id: the new name_id of the vector at the given index
        :param colour: the new colour of the vector at the given index
        :param type: the new type of the vector at the given index
        :param values: the new values of the vector at the given index
        Raises:
        --------
            IndexError
                raised if the index does not exist in the repository
        '''
        if self.name_id_exists(name_id):
            raise IndexError(f"{name_id} already exist in Repository")
        try:
            if 0 <= index < len(self.__vectors):
                self.__vectors.insert(index, Vector(name_id, colour, type, values))
            else:
                raise IndexError(f"The index should be between 0 and {len(self.__vectors)}, but {index} got")
        except ValueError as ie:
            print(ie)

    def update_by_name_id(self, name_id, colour, type, values):
        '''
        Update a vector identified by name_id
        :param name_id: str
        :param colour: the new colour of the vector identified by name_id
        :param type: the new type of the vector identified by name_id
        :param values: the new values of the vector identified by name_id
        Raises:
        --------
            IndexError
                raised if name_id doesn't exist in the repository
        '''
        if self.name_id_exists(name_id):
            try:
                for index in range(len(self.__vectors)):
                    if self.__vectors[index].get_name_id() == name_id:
                        self.__vectors[index].set_colour(colour)
                        self.__vectors[index].set_type(type)
                        self.__vectors[index].set_values(values)
            except ValueError as ie:
                print(ie)
        else:
            raise IndexError(f"{name_id} doesn't exist in Repository")

    def delete_by_index(self, index):
        '''
        Delete a vector by index
        :param index: int
        Raises:
        --------
            IndexError
                raised of the index doesn't exist in the repository
        '''
        if 0 <= index < len(self.__vectors):
            del self.__vectors[index]
        else:
            raise IndexError(f"The index should be between 0 and {len(self.__vectors)}, but {index} got")

    def delete_by_name_id(self, name_id):
        '''
        Delete a vector by name_id
        :param name_id: str
        '''
        if self.name_id_exists(name_id):
            for index in range(len(self.__vectors) - 1):
                if self.__vectors[index].get_name_id() == name_id:
                    del self.__vectors[index]
        else:
            print(f"{name_id} doesn't exist in the Repository")

    def plot(self):
        '''

        :return:
        '''

        for vector in self.__vectors:
            if vector.get_type() == 1:
                type = "o"
            elif vector.get_type() == 2:
                type = "s"
            elif vector.get_type() == 3:
                type = "^"
            else:
                type = "d"
            plt.plot(range(len(vector.get_values())), vector.get_values(), vector.get_colour() + type)
        plt.show()

    def vectors_with_given_sum(self, sum):
        '''
        Get the list of vectors having a given sum of elements
        :param sum: int
        :return: the list of vectors having the sum of elements equal with sum
        '''
        result = VectorRepository()
        for vector in self.__vectors:
            if vector.sum_of_elements_in_vector() == sum:
                result.add_vector_to_repository(
                    Vector(vector.get_name_id(), vector.get_colour(), vector.get_type(), vector.get_values()))
        return result

    def delete_between_indexes(self, index1, index2):
        '''
        Delete all vectors that are between two given indexes
        :param index1: int
        :param index2: int
        '''
        if 0 <= index1 < len(self.__vectors):
            if 0 <= index2 < len(self.__vectors):
                del (self.__vectors[index1:index2 + 1])
            else:
                raise IndexError(f"The index should be between 0 and {len(self.__vectors)}, but {index2} got")
        else:
            raise IndexError(f"The index should be between 0 and {len(self.__vectors)}, but {index1} got")

    def update_with_scalar(self, scalar):
        '''
        Update all vectors by adding a given scalar to each element
        :param scalar: int
        '''
        for vector in self.__vectors:
            vector.add_scalar(scalar)

    def name_id_exists(self, name_id):
        '''
        Check if a vector exists in the repository
        :param name_id:
        :return:
        '''
        for vector in self.__vectors:
            if name_id == vector.get_name_id():
                return True
        return False
