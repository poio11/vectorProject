from domain.vector import Vector
from infrastructure.vector_repo import VectorRepository

from typing import List


class VectorController:
    '''
    Controller class to reach the logical layer
    '''

    def __init__(self, vector_repository: VectorRepository = VectorRepository()):
        '''
        Constructor of the class. Creating a new controller
        :param vector_repository: VectorRepository
                vector repository which will be "controlled" by the class. Defaults to VectorRepository()
        '''
        self.__vector_repository = vector_repository

    def __str__(self) -> str:
        '''
        :return: string representation of the controller
        '''
        return str(self.__vector_repository)

    def add_vector(self, name_id: str, colour: str, type: int, values: list):
        '''
        Add new book instance to the repository
        :param name_id: the name_id of the new vector
        :param colour: the colour of the new vector
        :param type: the type of the new vector
        :param values: the values of the new vector
        '''
        self.__vector_repository.add_vector_to_repository(Vector(name_id, colour, type, values))

    def get_vectors(self) -> List[Vector]:
        '''
        Get all vectors
        :return: all vectors in the repository
        '''
        return self.__vector_repository.get_all_vectors()

    def get_vector_at_index(self, index):
        '''
        Get a vector at a given index
        :param index: int
        :return: vector instance at the given index
        '''
        return self.__vector_repository.get_vector_at_index(index)

    def update_at_index(self, index: int, name_id: str, colour: str, type: int, values: list):
        '''
        Update a vector at a given index
        :param index: the index of the vector which will be updated
        :param name_id: the new name_id of the vector at the given index
        :param colour: the new colour of the vector at the given index
        :param type: the new type of the vector at the given index
        :param values: the new values of the vector at the given index
        '''
        self.__vector_repository.update_vector_at_index(index, name_id, colour, type, values)

    def update_by_name_id(self, name_id: str, colour: str, type: int, values: list):
        '''
        Update a vector identified by name_id
        :param name_id: str
        :param colour: the new colour of the vector identified by name_id
        :param type: the new type of the vector identified by name_id
        :param values: the new values of the vector identified by name_id
        '''
        self.__vector_repository.update_by_name_id(name_id, colour, type, values)

    def delete_by_index(self, index):
        '''
        Delete a vector by index
        :param index: int
        '''
        self.__vector_repository.delete_by_index(index)

    def delete_by_name_id(self, name_id):
        '''
        Delete a vector by name_id
        :param name_id: str
        '''
        self.__vector_repository.delete_by_name_id(name_id)

    def plot(self):
        '''
        Plot all vectors in a chart based on the type and colour of each vector
        :return:
        '''
        self.__vector_repository.plot()

    def get_vectors_with_given_sum(self, sum):
        '''
        Get the list of vectors having a given sum of elements
        :param sum: int
        :return: the list of vectors having the sum of elements equal with sum
        '''
        return self.__vector_repository.vectors_with_given_sum(sum)

    def delete_between_indexes(self, index1, index2):
        '''
        Delete all vectors that are between two given indexes
        :param index1: int
        :param index2: int
        '''
        self.__vector_repository.delete_between_indexes(index1, index2)

    def update_with_scalar(self, scalar):
        '''
        Update all vectors by adding a given scalar to each element
        :param scalar: int
        '''
        self.__vector_repository.update_with_scalar(scalar)
