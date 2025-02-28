
class Pet:
    def __init__(self, name: str, species: str, year_of_birth: int):
        self.name = name
        self.species = species
        self.year_of_birth = year_of_birth


def new_pet(name: str, species: str, year_of_birth: int):
    """
    Creates and returns a new object of type Pet, as defined in the class Pet.
    """
    new_pet = Pet(name, species, year_of_birth)
    return new_pet

if __name__ == "__main__":
    fluffy = new_pet("Lousie", "monkey", 2001)
    print(fluffy.name)
    print(fluffy.species)
    print(fluffy.year_of_birth)