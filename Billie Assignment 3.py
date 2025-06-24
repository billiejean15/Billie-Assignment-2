import json
library = {}
def save_library():
    with open('library.json', 'w') as file:
        json.dump(library, f)    
        print("Library loaded successfully.")
        except:
        print("Error loading library.")

def load_library():
    try:
        with open('library.json', 'r') as file:
            global library
            library = json.load(f)
    print("Library loaded successfully.")
    except FileNotFoundError:
        print("Library file not found")
    except json.JSONDecodeError:
        print("Error loading file from library.")

