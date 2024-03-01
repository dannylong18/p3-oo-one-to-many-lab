class Pet:
    
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner = ''):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)

        if self.pet_type not in Pet.PET_TYPES:
            raise Exception ('Invalid pet type!')
        

class Owner:
    
    def __init__(self, name):
        self.name = name

    def pets(self, pet = ''):
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        if not isinstance (pet, Pet):
            raise Exception ("pet must be an instance of class Pet!")

        pet.owner = self
        
    def get_sorted_pets(self, pet = ''):
        return sorted(self.pets(), key=lambda x: x.name)
        
        