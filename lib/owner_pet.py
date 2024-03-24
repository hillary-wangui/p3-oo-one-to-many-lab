class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return sorted([pet.name for pet in Pet.all if isinstance(pet.owner, Owner) and pet.owner.name == self.name])

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("pet must be of type Pet")
        pet.owner = self

    def get_sorted_pets(self):
        sorted_pets = [pet for pet in Pet.all if isinstance(pet.owner, Owner) and pet.owner.name == self.name]
        sorted_pets.sort(key=lambda x: x.name)
        return sorted_pets


class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in self.PET_TYPES:
            raise Exception("Invalid pet type")
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        self.all.append(self)
