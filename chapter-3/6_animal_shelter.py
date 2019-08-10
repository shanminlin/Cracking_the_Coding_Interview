"""
Chapter 3 - Problem 3.6 - Animal Shelter
Problem:
An animal shelter, which holds only dogs and cats, operates on a strictly "first in, first out" basis.
People must adopt either the "oldest" (based on arrival time) of all animals at the shelter, or they
can select whether they would prefer a dog or a cat (and will receive the oldest animal of that type).
They cannot select which specific animal they would like. Create the data structures to maintain this
system and implement operations such as enqueue, dequeueAny, dequeueDog, and dequeueCat. You may use
the built-in LinkedList data structure.

Solution:
1. Clarify the question:
Repeat the question:
Clarify assumptions: - What if the stack is full and we try to add more elements?
                       (Assume no maximum capacity.)
                     - What if the stack is empty and we try to remove elements from this empty stack?
                       (A warning or an error message is thrown.)

2. Inputs and outputs:


3. Test and edge cases:
edge: We can also take in an empty stack or None object.
test: We can also take in regular inputs like this: [2, 3, 1, 5, 4] and we need to return 1.

4. Brainstorm solution:


5. Runtime analysis:
Time complexity:
Space complexity:

6. Code
"""
import unittest

class AnimalShelter:
    def __init__(self):
        self.cats = []
        self.dogs = []

    def enqueue(self, animal):
        if animal.__class__ == Cat:
            self.cats.append(animal)
        else:
            self.dogs.append(animal)

    def dequeue_any(self):
        if len(self.cats):
            return self.dequeue_cat()
        return self.dequeue_dog()

    def dequeue_cat(self):
        if len(self.cats) == 0:
            return None
        cat = self.cats[0]
        self.cats = self.cats[1:]
        return cat

    def dequeue_dog(self):
        if len(self.dogs) == 0:
            return None
        dog = self.dogs[0]
        self.dogs = self.dogs[1:]
        return dog


class Animal:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Cat(Animal):
    pass


class Dog(Animal):
    pass


class Test(unittest.TestCase):
    def test_animal_shelter(self):
        shelter = AnimalShelter()
        shelter.enqueue(Cat("Abby"))
        shelter.enqueue(Dog("Bubble"))
        shelter.enqueue(Cat("Coffee"))
        shelter.enqueue(Cat("Doufu"))
        shelter.enqueue(Dog("Elly"))
        self.assertEqual(str(shelter.dequeue_any()), "Hanzack")
        self.assertEqual(str(shelter.dequeue_any()), "Garfield")
        self.assertEqual(str(shelter.dequeue_dog()), "Pluto")
        self.assertEqual(str(shelter.dequeue_dog()), "Clifford")
        self.assertEqual(str(shelter.dequeue_cat()), "Tony")
        self.assertEqual(str(shelter.dequeue_cat()), "None")
        self.assertEqual(str(shelter.dequeue_any()), "Blue")


if __name__ == "__main__":
    unittest.main()