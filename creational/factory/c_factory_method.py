"""
Pizza Store - Factory Method Pattern

This demonstrates the Factory Method pattern, one of the Gang of Four design patterns.

DEFINITION:
"Define an interface for creating an object, but let subclasses decide which 
class to instantiate. Factory Method lets a class defer instantiation to subclasses."

KEY CONCEPT:
The Factory Method pattern uses inheritance. An abstract creator class defines
the factory method, and concrete subclasses override it to create specific products.

IMPROVEMENTS OVER SIMPLE FACTORY:
- Follows Open-Closed Principle (open for extension, closed for modification)
- Supports regional variations (NY-style, Chicago-style) without changing existing code
- Each franchise can have its own pizza creation logic
- No if-else chains in the factory method implementations

STRUCTURE:
- Creator (PizzaStore): Abstract class with factory method
- Concrete Creators (NYPizzaStore, ChicagoPizzaStore): Override factory method
- Product (Pizza): Abstract product interface
- Concrete Products (NYStyleCheesePizza, ChicagoStyleCheesePizza, etc.)
"""

from abc import ABC, abstractmethod
from typing import Optional


# ============================================================================
# PRODUCT HIERARCHY - Pizza classes
# ============================================================================

class Pizza(ABC):
    """
    Abstract Product - defines the interface for pizzas.
    Each pizza can have different preparation, baking, cutting methods.
    """
    
    def __init__(self):
        self.name = ""
        self.dough = ""
        self.sauce = ""
        self.toppings = []
    
    def prepare(self):
        """Default preparation - can be overridden"""
        print(f"Preparing {self.name}")
        print(f"Tossing dough: {self.dough}")
        print(f"Adding sauce: {self.sauce}")
        print("Adding toppings:")
        for topping in self.toppings:
            print(f"  {topping}")
    
    def bake(self):
        """Default baking - can be overridden"""
        print("Baking for 25 minutes at 350 degrees")
    
    def cut(self):
        """Default cutting - can be overridden"""
        print("Cutting the pizza into diagonal slices")
    
    def box(self):
        """Default boxing"""
        print("Placing pizza in official PizzaStore box")
    
    def get_name(self):
        return self.name


# ============================================================================
# CONCRETE PRODUCTS - NY Style Pizzas
# ============================================================================

class NYStyleCheesePizza(Pizza):
    """New York style cheese pizza - thin crust, tangy sauce"""
    
    def __init__(self):
        super().__init__()
        self.name = "NY Style Sauce and Cheese Pizza"
        self.dough = "Thin Crust Dough"
        self.sauce = "Marinara Sauce"
        self.toppings.append("Grated Reggiano Cheese")


class NYStylePepperoniPizza(Pizza):
    """New York style pepperoni pizza"""
    
    def __init__(self):
        super().__init__()
        self.name = "NY Style Pepperoni Pizza"
        self.dough = "Thin Crust Dough"
        self.sauce = "Marinara Sauce"
        self.toppings.append("Grated Reggiano Cheese")
        self.toppings.append("Sliced Pepperoni")
        self.toppings.append("Garlic")
        self.toppings.append("Onion")
        self.toppings.append("Mushrooms")
        self.toppings.append("Red Pepper")


class NYStyleVeggiePizza(Pizza):
    """New York style veggie pizza"""
    
    def __init__(self):
        super().__init__()
        self.name = "NY Style Veggie Pizza"
        self.dough = "Thin Crust Dough"
        self.sauce = "Marinara Sauce"
        self.toppings.append("Grated Reggiano Cheese")
        self.toppings.append("Garlic")
        self.toppings.append("Onion")
        self.toppings.append("Mushrooms")
        self.toppings.append("Red Pepper")


class NYStyleClamPizza(Pizza):
    """New York style clam pizza"""
    
    def __init__(self):
        super().__init__()
        self.name = "NY Style Clam Pizza"
        self.dough = "Thin Crust Dough"
        self.sauce = "White Garlic Sauce"
        self.toppings.append("Clams")
        self.toppings.append("Grated Reggiano Cheese")


# ============================================================================
# CONCRETE PRODUCTS - Chicago Style Pizzas
# ============================================================================

class ChicagoStyleCheesePizza(Pizza):
    """Chicago style cheese pizza - deep dish, chunky sauce"""
    
    def __init__(self):
        super().__init__()
        self.name = "Chicago Style Deep Dish Cheese Pizza"
        self.dough = "Extra Thick Crust Dough"
        self.sauce = "Plum Tomato Sauce"
        self.toppings.append("Shredded Mozzarella Cheese")
    
    def cut(self):
        """Chicago style uses square cuts"""
        print("Cutting the pizza into square slices")


class ChicagoStylePepperoniPizza(Pizza):
    """Chicago style pepperoni pizza"""
    
    def __init__(self):
        super().__init__()
        self.name = "Chicago Style Pepperoni Pizza"
        self.dough = "Extra Thick Crust Dough"
        self.sauce = "Plum Tomato Sauce"
        self.toppings.append("Shredded Mozzarella Cheese")
        self.toppings.append("Black Olives")
        self.toppings.append("Spinach")
        self.toppings.append("Eggplant")
        self.toppings.append("Sliced Pepperoni")
    
    def cut(self):
        """Chicago style uses square cuts"""
        print("Cutting the pizza into square slices")


class ChicagoStyleVeggiePizza(Pizza):
    """Chicago style veggie pizza"""
    
    def __init__(self):
        super().__init__()
        self.name = "Chicago Deep Dish Veggie Pizza"
        self.dough = "Extra Thick Crust Dough"
        self.sauce = "Plum Tomato Sauce"
        self.toppings.append("Shredded Mozzarella Cheese")
        self.toppings.append("Black Olives")
        self.toppings.append("Spinach")
        self.toppings.append("Eggplant")
    
    def cut(self):
        """Chicago style uses square cuts"""
        print("Cutting the pizza into square slices")


class ChicagoStyleClamPizza(Pizza):
    """Chicago style clam pizza"""
    
    def __init__(self):
        super().__init__()
        self.name = "Chicago Style Clam Pizza"
        self.dough = "Extra Thick Crust Dough"
        self.sauce = "Plum Tomato Sauce"
        self.toppings.append("Shredded Mozzarella Cheese")
        self.toppings.append("Frozen Clams from Chesapeake Bay")
    
    def cut(self):
        """Chicago style uses square cuts"""
        print("Cutting the pizza into square slices")


# ============================================================================
# CREATOR HIERARCHY - PizzaStore classes
# ============================================================================

class PizzaStore(ABC):
    """
    Abstract Creator - defines the factory method.
    
    This is the heart of the Factory Method pattern:
    - orderPizza() is the template method (same for all stores)
    - createPizza() is the factory method (varies by subclass)
    
    The factory method is abstract, forcing subclasses to provide
    their own implementation. This is where "subclasses decide which
    class to instantiate."
    """
    
    def order_pizza(self, pizza_type: str) -> Optional[Pizza]:
        """
        Template method - defines the algorithm for ordering pizza.
        This method is the same for all pizza stores.
        
        It calls the factory method (createPizza) to get the pizza,
        then performs the standard operations on it.
        """
        # Call the factory method - subclasses will provide the implementation
        pizza = self.create_pizza(pizza_type)
        
        if pizza is None:
            return None
        
        # These steps are the same for all stores
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        
        return pizza
    
    @abstractmethod
    def create_pizza(self, pizza_type: str) -> Optional[Pizza]:
        """
        Factory Method - abstract method that subclasses must implement.
        
        This is where the "magic" happens:
        - Each subclass decides which concrete Pizza class to instantiate
        - No if-else chains needed in subclasses (each type gets its own method)
        - New pizza types can be added without modifying existing code
        """
        pass


class NYPizzaStore(PizzaStore):
    def create_pizza(self, pizza_type: str) -> Optional[Pizza]:
        """Factory method implementation for NY style pizzas"""
        if pizza_type == "cheese":
            return NYStyleCheesePizza()
        elif pizza_type == "pepperoni":
            return NYStylePepperoniPizza()
        elif pizza_type == "veggie":
            return NYStyleVeggiePizza()
        elif pizza_type == "clam":
            return NYStyleClamPizza()
        else:
            print(f"Error: Unknown pizza type '{pizza_type}'")
            return None


class ChicagoPizzaStore(PizzaStore):
    def create_pizza(self, pizza_type: str) -> Optional[Pizza]:
        """Factory method implementation for Chicago style pizzas"""
        if pizza_type == "cheese":
            return ChicagoStyleCheesePizza()
        elif pizza_type == "pepperoni":
            return ChicagoStylePepperoniPizza()
        elif pizza_type == "veggie":
            return ChicagoStyleVeggiePizza()
        elif pizza_type == "clam":
            return ChicagoStyleClamPizza()
        else:
            print(f"Error: Unknown pizza type '{pizza_type}'")
            return None


# ============================================================================
# DEMONSTRATION
# ============================================================================

def main():
    """Demonstrate the Factory Method pattern"""
    
    print("=" * 70)
    print("PIZZA STORE - FACTORY METHOD PATTERN")
    print("=" * 70)
    print()
    
    # Create different franchise stores
    ny_store = NYPizzaStore()
    chicago_store = ChicagoPizzaStore()
    
    # Order from NY store
    print("Joel orders a cheese pizza from NY store:")
    print("-" * 70)
    pizza = ny_store.order_pizza("cheese")
    if pizza:
        print(f"\nJoel got a {pizza.get_name()}\n")
    
    print("=" * 70)
    print()
    
    # Order from Chicago store
    print("Ethan orders a cheese pizza from Chicago store:")
    print("-" * 70)
    pizza = chicago_store.order_pizza("cheese")
    if pizza:
        print(f"\nEthan got a {pizza.get_name()}\n")
    
    print("=" * 70)
    print()
    
    # Order pepperoni from NY
    print("Joel orders a pepperoni pizza from NY store:")
    print("-" * 70)
    pizza = ny_store.order_pizza("pepperoni")
    if pizza:
        print(f"\nJoel got a {pizza.get_name()}\n")
    
    print("=" * 70)
    print()
    
    # Order clam from Chicago
    print("Ethan orders a clam pizza from Chicago store:")
    print("-" * 70)
    pizza = chicago_store.order_pizza("clam")
    if pizza:
        print(f"\nEthan got a {pizza.get_name()}\n")
    
    print("=" * 70)
    print()
    
    print("KEY BENEFITS OF FACTORY METHOD PATTERN:")
    print("-" * 70)
    print("✓ Follows Open-Closed Principle")
    print("  - Open for extension: Add new store types without modifying existing code")
    print("  - Closed for modification: Existing stores don't need changes")
    print()
    print("✓ Encapsulates object creation")
    print("  - Each store knows how to create its own pizzas")
    print("  - Client code (orderPizza) doesn't know about concrete classes")
    print()
    print("✓ Supports variations through inheritance")
    print("  - NY and Chicago stores create different pizza styles")
    print("  - Same interface, different implementations")
    print()
    print("✓ Promotes loose coupling")
    print("  - PizzaStore depends on Pizza interface, not concrete classes")
    print("  - Easy to add new pizza types or store franchises")
    print()
    
    print("PATTERN STRUCTURE:")
    print("-" * 70)
    print("Creator (PizzaStore)")
    print("  ├─ orderPizza() - template method")
    print("  └─ createPizza() - factory method (abstract)")
    print()
    print("Concrete Creators")
    print("  ├─ NYPizzaStore - implements createPizza()")
    print("  └─ ChicagoPizzaStore - implements createPizza()")
    print()
    print("Product (Pizza)")
    print("  └─ prepare(), bake(), cut(), box()")
    print()
    print("Concrete Products")
    print("  ├─ NYStyleCheesePizza, NYStylePepperoniPizza, ...")
    print("  └─ ChicagoStyleCheesePizza, ChicagoStylePepperoniPizza, ...")
    print()
    
    print("NEXT STEP: Abstract Factory Pattern")
    print("-" * 70)
    print("The Abstract Factory pattern will allow us to create families")
    print("of related objects (ingredients) without specifying their")
    print("concrete classes, providing even more flexibility.")
    print("=" * 70)


if __name__ == "__main__":
    main()

