"""Creates Node for linked list. Identifies animal and next node."""
class Node:
    def __init__(self, animal):
        self.animal = animal
        self.next = None

""""The superclass for the subclasses Dog and Cat"""
class Animal:
    def __init__(self, name):
        self.name = name

"""Subclass of Animal superclass"""
class Dog(Animal):
    def __init__(self, name=""):
        super().__init__(name)
        self.species = "dog"

"""Subclass of Animal superclass"""
class Cat(Animal):
    def __init__(self, name=""):
        super().__init__(name)
        self.species = "cat"

"""Linked list. This linked list will take in instances of the subclasses Dog or Cat. """
class AnimalShelter:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, animal):
        new_node = Node(animal)
        if self.tail:
            self.tail.next = new_node
        self.tail = new_node
        if not self.head:
            self.head = new_node

    def dequeue(self, pref):
        if pref not in ["dog", "cat"] or not self.head:
            return None

        if self.head.animal.species == pref:
            animal = self.head.animal
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return animal

        current = self.head
        while current.next:
            if current.next.animal.species == pref:
                animal = current.next.animal
                current.next = current.next.next
                if current.next is None:
                    self.tail = current
                return animal
            current = current.next

        return None
