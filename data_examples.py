from controller import VectorController
from domain.vector import Vector
from infrastructure.vector_repo import VectorRepository

if __name__ == "__main__":
    controller = VectorController(VectorRepository([
        Vector("1", "r", 1, [1, 2, 3]),
        Vector("2", "m", 2, [5, 6, 7]),
        Vector("3", "y", 1, [1, 5, 9, 10, 12])
    ]))
    new_vector = Vector("4", "r", 1, [1, 3])
    print("Original list:\n", controller)
    print("-" * 100)

    controller.add_vector("4", "y", 2, [5, 15, 20])
    print("After adding a new vector:\n", controller)
    print("-" * 100)

    print("Vector at index 2:", controller.get_vector_at_index(2))
    print("-" * 100)

    controller.update_at_index(1, "6", "y", 1, [1])
    print("After update 1st index:\n", controller)
    print("-" * 100)

    controller.update_by_name_id("4", "m", 2, [10, 20, 30, 40])
    print("After update vector with name_id 4:\n", controller)
    print("-" * 100)

    controller.delete_by_index(3)
    print("After deleting at index 3:\n", controller)
    print("-" * 100)

    controller.delete_by_name_id("2")
    print("After deleting vector with name_id 2:\n", controller)
    print("-" * 100)

    print("Vectors with sum 40", controller.get_vectors_with_given_sum(40))
    print("-" * 100)

    controller.delete_between_indexes(1, 3)
    print("After deleting between indexes 1 and 3:\n", controller)
    print("-" * 100)

    controller.update_with_scalar(10)
    print("After update with 10:\n", controller)
