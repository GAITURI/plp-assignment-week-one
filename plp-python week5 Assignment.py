# Program 1: Superhero Class with Inheritance and Encapsulation

class Superhero:
    """A base class representing a superhero."""

    def __init__(self, name, secret_identity, strength_level):
        """
        Initializes a Superhero object.

        Args:
            name (str): The superhero's public name.
            secret_identity (str): The hero's civilian name.
            strength_level (int): A numerical value representing their strength.
        """
        self.name = name
        self.secret_identity = secret_identity
        # Using a leading underscore for encapsulation
        self._strength_level = strength_level
        self.is_active = True

    def display_info(self):
        """Prints the superhero's information."""
        print(f"Name: {self.name}")
        print(f"Secret Identity: {self.secret_identity}")
        print(f"Strength Level: {self._strength_level}")
        print(f"Status: {'Active' if self.is_active else 'Retired'}")

    def fight_crime(self, threat_level):
        """
        A method for the hero to fight crime.
        This will be overridden by subclasses.
        """
        if self._strength_level > threat_level:
            print(f"{self.name} successfully handled the threat!")
        else:
            print(f"{self.name} struggled with the threat...")

    def retire(self):
        """Changes the hero's status to retired."""
        self.is_active = False
        print(f"{self.name} has retired from hero work.")

    def get_strength(self):
        """A public method to access the private attribute."""
        return self._strength_level

class FlyingHero(Superhero):
    """A subclass for heroes who can fly."""

    def __init__(self, name, secret_identity, strength_level, max_altitude):
        """Initializes a FlyingHero object, inheriting from Superhero."""
        # Call the parent class constructor
        super().__init__(name, secret_identity, strength_level)
        self.max_altitude = max_altitude

    def fly(self):
        """A unique method for flying heroes."""
        print(f"{self.name} soars through the sky up to {self.max_altitude} feet!")

    def fight_crime(self, threat_level):
        """
        Overridden method demonstrating polymorphism.
        This version is different from the base class.
        """
        print(f"{self.name} swoops in from the air to handle the threat!")
        if self._strength_level * 1.5 > threat_level: # Bonus for flying!
            print(f"{self.name} successfully handled the threat!")
        else:
            print(f"{self.name} struggled with the threat...")

# Create instances of the classes
print("--- Creating our heroes ---")
hero_1 = Superhero("Captain Courage", "Steve Rogers", 85)
flying_hero_1 = FlyingHero("Aero-Knight", "Diana Prince", 95, 30000)

# Interact with the objects
print("\n--- Displaying hero info ---")
hero_1.display_info()
print("-" * 20)
flying_hero_1.display_info()

print("\n--- Testing methods ---")
hero_1.fight_crime(90)
flying_hero_1.fight_crime(90)
flying_hero_1.fly()

print("\n--- Retiring a hero ---")
hero_1.retire()
hero_1.display_info()

