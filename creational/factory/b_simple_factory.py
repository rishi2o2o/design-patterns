"""
Pizza Store - Simple Factory Pattern

This demonstrates the Simple Factory pattern (also called Static Factory).
Note: Simple Factory is NOT one of the Gang of Four design patterns,
but it's a common programming idiom and a good stepping stone to understanding
the Factory Method pattern.

IMPROVEMENT OVER NO PATTERN:
- Encapsulates object creation in a separate class
- PizzaStore is no longer coupled to concrete Pizza classes
- Changes to pizza creation are localized to SimplePizzaFactory

REMAINING ISSUES:
- Still uses if-else chain (just moved to factory)
- Cannot easily support regional variations (NY-style, Chicago-style)
- Factory is not extensible without modification
"""

from typing import Optional


class Pizza:
    """Base Pizza class"""
    
    def __init__(self):
        self.name = ""
        self.dough = ""
        self.sauce = ""
        self.toppings = []
    
    def prepare(self):
        print(f"Preparing {self.name}")
        print(f"Tossing dough: {self.dough}")
        print(f"Adding sauce: {self.sauce}")
        print("Adding toppings:")
        for topping in self.toppings:
            print(f"  {topping}")
    
    def bake(self):
        print("Baking for 25 minutes at 350 degrees")
    
    def cut(self):
        print("Cutting the pizza into diagonal slices")
    
    def box(self):
        print("Placing pizza in official PizzaStore box")
    
    def get_name(self):
        return self.name


class CheesePizza(Pizza):
    """Concrete Cheese Pizza"""
    
    def __init__(self):
        super().__init__()
        self.name = "Cheese Pizza"
        self.dough = "Regular Crust"
        self.sauce = "Marinara Pizza Sauce"
        self.toppings.append("Fresh Mozzarella")
        self.toppings.append("Parmesan")


class PepperoniPizza(Pizza):
    """Concrete Pepperoni Pizza"""
    
    def __init__(self):
        super().__init__()
        self.name = "Pepperoni Pizza"
        self.dough = "Regular Crust"
        self.sauce = "Marinara Pizza Sauce"
        self.toppings.append("Fresh Mozzarella")
        self.toppings.append("Pepperoni")


class VeggiePizza(Pizza):
    """Concrete Veggie Pizza"""
    
    def __init__(self):
        super().__init__()
        self.name = "Veggie Pizza"
        self.dough = "Regular Crust"
        self.sauce = "Marinara Pizza Sauce"
        self.toppings.append("Fresh Mozzarella")
        self.toppings.append("Onions")
        self.toppings.append("Bell Peppers")
        self.toppings.append("Mushrooms")
        self.toppings.append("Olives")


class ClamPizza(Pizza):
    """Concrete Clam Pizza"""
    
    def __init__(self):
        super().__init__()
        self.name = "Clam Pizza"
        self.dough = "Thin Crust"
        self.sauce = "White Garlic Sauce"
        self.toppings.append("Clams")
        self.toppings.append("Grated Parmesan")


class SimplePizzaFactory:
    """
    Simple Factory - Encapsulates pizza creation logic.
    """
    
    def create_pizza(self, pizza_type: str) -> Optional[Pizza]:
        pizza: Optional[Pizza] = None
        
        # Object creation is now centralized
        if pizza_type == "cheese":
            pizza = CheesePizza()
        elif pizza_type == "pepperoni":
            pizza = PepperoniPizza()
        elif pizza_type == "veggie":
            pizza = VeggiePizza()
        elif pizza_type == "clam":
            pizza = ClamPizza()
        else:
            print(f"Error: Unknown pizza type '{pizza_type}'")
            return None
        
        return pizza


class PizzaStore:
    def __init__(self, factory: SimplePizzaFactory):
        self.factory = factory
    
    def order_pizza(self, pizza_type: str) -> Optional[Pizza]:
        # Delegate object creation to the factory
        pizza = self.factory.create_pizza(pizza_type)
        
        if pizza is None:
            return None
        
        # The ordering process remains the same
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        
        return pizza


def main():
    """Demonstrate the Simple Factory pattern"""
    
    print("=" * 60)
    print("PIZZA STORE - SIMPLE FACTORY PATTERN")
    print("=" * 60)
    print()
    
    # Create the factory
    factory = SimplePizzaFactory()
    
    # Create the store with the factory
    store = PizzaStore(factory)
    
    # Order some pizzas
    print("Customer 1 orders a cheese pizza:")
    print("-" * 60)
    pizza = store.order_pizza("cheese")
    if pizza:
        print(f"\nReceived: {pizza.get_name()}\n")
    
    print("=" * 60)
    print()
    
    print("Customer 2 orders a pepperoni pizza:")
    print("-" * 60)
    pizza = store.order_pizza("pepperoni")
    if pizza:
        print(f"\nReceived: {pizza.get_name()}\n")
    
    print("=" * 60)
    print()
    
    print("Customer 3 orders a clam pizza:")
    print("-" * 60)
    pizza = store.order_pizza("clam")
    if pizza:
        print(f"\nReceived: {pizza.get_name()}\n")
    
    print("=" * 60)
    print()
    
    print("Customer 4 orders an invalid pizza:")
    print("-" * 60)
    pizza = store.order_pizza("hawaiian")
    if pizza:
        print(f"\nReceived: {pizza.get_name()}\n")
    else:
        print("\nOrder failed - pizza type not available\n")
    
    print("=" * 60)
    print()
    
    print("IMPROVEMENTS OVER NO PATTERN:")
    print("-" * 60)
    print("✓ Object creation is encapsulated in SimplePizzaFactory")
    print("✓ PizzaStore is decoupled from concrete Pizza classes")
    print("✓ Changes to pizza creation are localized to one class")
    print("✓ Multiple stores can share the same factory")
    print()
    
    print("REMAINING LIMITATIONS:")
    print("-" * 60)
    print("✗ Still has if-else chain (just moved to factory)")
    print("✗ Cannot easily support regional variations (NY, Chicago styles)")
    print("✗ Factory must be modified to add new pizza types")
    print("✗ Still violates Open-Closed Principle")
    print()
    
    print("NEXT STEP: Factory Method Pattern")
    print("-" * 60)
    print("The Factory Method pattern will allow subclasses to decide")
    print("which pizza to create, enabling regional variations without")
    print("modifying existing code.")
    print("=" * 60)


if __name__ == "__main__":
    main()

