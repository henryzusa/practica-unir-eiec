import os
import sys

DEFAULT_FILENAME = "words.txt"
DEFAULT_DUPLICATES = False
DEFAULT_ORDER_ASC = True


def sort_list(items, ascending):
def sort_list(items, ascending=True):
    if not isinstance(items, list):
        raise RuntimeError(f"No puede ordenar {type(items)}")
    return sorted(items, reverse=(not ascending))

def remove_duplicates_from_list(items):
    return list(set(items))

if __name__ == "__main__":
    filename = DEFAULT_FILENAME
    remove_duplicates = DEFAULT_DUPLICATES
    ascending_order = DEFAULT_ORDER_ASC
    if len(sys.argv) == 4:
        filename = sys.argv[1]
        remove_duplicates = sys.argv[2].lower() == "yes"
        ascending_order = False if sys.argv[3] == "desc" else DEFAULT_ORDER_ASC
    else:
        print("The file must be indicated as the first argumen")
        print("The second argument indicates whether you want to eliminate duplicates")
        print("The third argument indicates whether the type of sorting (ascending or descending)")
        sys.exit(1)

    print(f"The words from the file will be read {filename}")
    file_path = os.path.join(".", filename)
    try:
        with open(file_path, "r") as file:
            word_list = [line.strip() for line in file]
    except FileNotFoundError:
        print(f"El fichero {filename} no existe")
        word_list = ["ravenclaw", "gryffindor", "slytherin", "hufflepuff"]
    except IOError as e:
        print(f"Error al abrir o leer el fichero: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Se produjo un error inesperado: {e}")
        sys.exit(1)

    if remove_duplicates:
        word_list = remove_duplicates_from_list(word_list)

    print(sort_list(word_list, ascending_order))
