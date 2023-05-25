class Pet:
    
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]

    all = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        if isinstance(owner, Owner) or not owner:
            self.owner = owner
        else: 
            raise Exception
        if pet_type in Pet.PET_TYPES: 
            self.pet_type = pet_type 
        else: 
            raise Exception 
        self.add_pet(self)
       
    
    @classmethod
    def add_pet(cls, self): 
        cls.all.append(self)
        


class Owner:
    
    def __init__(self, name):
        self.name = name 

    def pets(self): 
        return [pet for pet in Pet.all if pet.owner == self]
    
    def add_pet(self, pet):
        if isinstance(pet, Pet):
            pet.owner = self 
        else: 
            raise Exception
    
    def get_sorted_pets(self):
        return sorted(self.pets(), key = lambda pet: pet.name)