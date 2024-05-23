import os
import sys

DEFAULT_FILENAME = "words.txt"
DEFAULT_DUPLICATES = False

def sort_list(items, ascending=True):
    if not isinstance(items, list):
        raise RuntimeError(f"No puede ordenar {type(items)}")
    return sorted(items, reverse=(not ascending))

def remove_duplicates_from_list(items):
    return list(set(items))

if __name__ == "__main__":
    filename = DEFAULT_FILENAME
    remove_duplicates = DEFAULT_DUPLICATES
    if len(sys.argv) == 3:
        filename = sys.argv[1]
        remove_duplicates = sys.argv[2].lower() == "yes"
    else:
        print("Se debe indicar el fichero como primer argumento")
        print("El segundo argumento indica si se quieren eliminar duplicados")
        sys.exit(1)

    print(f"Se leerán las palabras del fichero {filename}")
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

    print(sort_list(word_list))
