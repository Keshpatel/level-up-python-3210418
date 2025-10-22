import pickle

# Function to save a dictionary
def save_dict(dictionary, filename):
    """Save a Python dictionary as a binary file."""
    with open(filename, 'wb') as file:  # 'wb' = write binary
        pickle.dump(dictionary, file)
    print(f"Dictionary saved successfully to '{filename}'")

# Function to load a dictionary
def load_dict(filename):
    """Load a dictionary from a binary file."""
    with open(filename, 'rb') as file:  # 'rb' = read binary
        loaded_dict = pickle.load(file)
    print(f"Dictionary loaded successfully from '{filename}'")
    return loaded_dict



def save_dict(dict_to_save, file_path):
    with open(file_path, 'wb') as file:
        pickle.dump(dict_to_save, file)

def load_dict(file_path):
    with open(file_path, 'rb') as file:
        return pickle.load(file)


# commands used in solution video for reference
if __name__ == '__main__':
    test_dict = {1: 'a', 2: 'b', 3: 'c'}
    save_dict(test_dict, 'test_dict.pickle')
    recovered = load_dict('test_dict.pickle')
    print(recovered)  # {1: 'a', 2: 'b', 3: 'c'}


    # Original dictionary
my_data = {
    "name": "Tom",
    "language": "Python",
    "topics": ["Pickle", "Lists", "Functions"],
    "level": "Intermediate"
}

# Save the dictionary
save_dict(my_data, "my_data.pkl")

# Load it back
restored_data = load_dict("my_data.pkl")

# Verify content
print("Restored Dictionary:", restored_data)

