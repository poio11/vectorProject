from infrastructure.vector_repo import VectorRepository
from domain.vector import Vector
from controller import VectorController


def print_menu():
    '''
    Print the menu options
    :return:
    '''
    print("0 - Exit program")
    print("1 - Print menu")
    print("2 - Add a vector")
    print("3 - Get all vectors")
    print("4 - Get vector at index")
    print("5 - Update at index")
    print("6 - Update vector by name_id")
    print("7 - Delete at index")
    print("8 - Delete by name_id")
    print("9 - Plot")
    print("10 - Get the list of vectors having a given sum of elements")
    print("11 - Delete all vectors that are between two given indexes")
    print("12 - Update all vectors by adding a given scalar to each element")


def start(controller: VectorController):
    '''
    Start the menu type console
    :return:
    '''
    print_menu()
    command = input(">>> ")
    controller = VectorController(VectorRepository([
        Vector("1", "r", 1, [1, 2, 3]),
        Vector("2", "m", 2, [5, 6, 7]),
        Vector("3", "b", 1, [1, 5, 9, 10, 12]),
        Vector("4", "r", 1, [1, 3]),
        Vector("5", "g", 3, [11, 12, 13]),
        Vector("6", "m", 4, [52, 36, 72]),
        Vector("7", "y", 1, [9, 10, 12]),
        Vector("8", "r", 1, [1]),
        Vector("9", "r", 3, [6]),
        Vector("10", "b", 4, [4, 10, 12])
    ]))
    while command != "0":
        if command == "1":
            print_menu()
        elif command == "2":
            name_id = input("name_id = ")
            colour = input("colour = ")
            type = int(input("type = "))
            values = input("values = ")
            values = list(map(int, values.split(' ')))
            try:
                controller.add_vector(name_id, colour, type, values)
                print(controller)
            except IndexError as ie:
                print(ie)
            except ValueError as ei:
                print(ei)
        elif command == "3":
            # print(vector_list.get_all_vectors())
            print(controller)
        elif command == "4":
            index = int(input("index = "))
            try:
                print(controller.get_vector_at_index(index))
            except IndexError as ei:
                print(ei)
        elif command == "5":
            index = int(input("index = "))
            name_id = input("name_id = ")
            colour = input("colour = ")
            type = int(input("type = "))
            values = input("values = ")
            values = list(map(int, values.split(' ')))
            try:
                controller.update_at_index(index, name_id, colour, type, values)
                print(controller)
            except IndexError as ie:
                print(ie)
        elif command == "6":
            name_id = input("name_id = ")
            colour = input("colour = ")
            type = int(input("type = "))
            values = input("values = ")
            values = list(map(int, values.split(' ')))
            try:
                controller.update_by_name_id(name_id, colour, type, values)
                print(controller)
            except IndexError as ei:
                print(ei)
        elif command == "7":
            index = int(input("index = "))
            try:
                controller.delete_by_index(index)
                print(controller)
            except IndexError as ie:
                print(ie)
        elif command == "8":
            name_id = input(("name_id = "))
            try:
                controller.delete_by_name_id(name_id)
                print(controller)
            except Exception as ie:
                print(ie)
        elif command == "9":
            controller.plot()
        elif command == "10":
            sum = int(input("sum = "))
            print(controller.get_vectors_with_given_sum(sum))
        elif command == "11":
            index1 = int(input("index1 = "))
            index2 = int(input("index2 = "))
            try:
                controller.delete_between_indexes(index1, index2)
                print(controller)
            except IndexError as ei:
                print(ei)
        elif command == "12":
            scalar = int(input("scalar = "))
            controller.update_with_scalar(scalar)
            print(controller)
        else:
            print("Invalid command")
        command = input(">>> ")
