"""
Pizza Store - No Pattern (Starting Point)

This demonstrates the initial approach without any design pattern.
Problem: The orderPizza method is tightly coupled to concrete pizza classes.
Every time we add or remove a pizza type, we must modify this class.
This violates the Open-Closed Principle.
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


class PizzaStore:
    def order_pizza(self, pizza_type: str) -> Optional[Pizza]:
        pizza = None
        
        # PROBLEM: Direct instantiation with if-else chain
        # Every new pizza type requires modifying this code
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
        
        # The preparation process is consistent
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        
        return pizza


def main():
    """Demonstrate the pizza store without any pattern"""
    
    print("=" * 60)
    print("PIZZA STORE - NO PATTERN")
    print("=" * 60)
    print()
    
    store = PizzaStore()
    
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
    
    print("Customer 3 orders a veggie pizza:")
    print("-" * 60)
    pizza = store.order_pizza("veggie")
    if pizza:
        print(f"\nReceived: {pizza.get_name()}\n")
    
    print("=" * 60)
    print()
    
    print("PROBLEMS WITH THIS APPROACH:")
    print("-" * 60)
    print("1. PizzaStore is tightly coupled to concrete Pizza classes")
    print("2. Adding a new pizza type requires modifying PizzaStore.order_pizza()")
    print("3. Cannot easily create regional variations (NY-style, Chicago-style)")
    print("4. Violates Open-Closed Principle (open for extension, closed for modification)")
    print()
    print("NEXT STEP: Introduce Simple Factory to encapsulate object creation")
    print("=" * 60)


if __name__ == "__main__":
    main()

