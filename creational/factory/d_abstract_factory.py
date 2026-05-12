"""
Pizza Store - Abstract Factory Pattern

This demonstrates the Abstract Factory pattern, one of the Gang of Four design patterns.

DEFINITION:
"Provide an interface for creating families of related or dependent objects 
without specifying their concrete classes."

KEY CONCEPT:
Abstract Factory creates families of related objects. In this example, each region
has its own ingredient factory that creates region-specific ingredients (dough, 
sauce, cheese, etc.). The pizza uses these ingredients without knowing their 
concrete types.

IMPROVEMENTS OVER FACTORY METHOD:
- Creates families of related objects (ingredients)
- Ingredients are guaranteed to be compatible (all NY or all Chicago)
- Easy to swap entire product families
- Promotes consistency among products

STRUCTURE:
- Abstract Factory (PizzaIngredientFactory): Interface for creating ingredient families
- Concrete Factories (NYPizzaIngredientFactory, ChicagoPizzaIngredientFactory)
- Abstract Products (Dough, Sauce, Cheese, etc.): Ingredient interfaces
- Concrete Products (ThinCrustDough, ThickCrustDough, etc.): Specific ingredients
- Client (Pizza): Uses ingredients without knowing concrete types
"""

from abc import ABC, abstractmethod
from typing import Optional


# ============================================================================
# ABSTRACT PRODUCTS - Ingredient Interfaces
# ============================================================================

class Dough(ABC):
    """Abstract product - Dough interface"""
    
    @abstractmethod
    def __str__(self) -> str:
        pass


class Sauce(ABC):
    """Abstract product - Sauce interface"""
    
    @abstractmethod
    def __str__(self) -> str:
        pass


class Cheese(ABC):
    """Abstract product - Cheese interface"""
    
    @abstractmethod
    def __str__(self) -> str:
        pass


class Veggies(ABC):
    """Abstract product - Veggies interface"""
    
    @abstractmethod
    def __str__(self) -> str:
        pass


class Pepperoni(ABC):
    """Abstract product - Pepperoni interface"""
    
    @abstractmethod
    def __str__(self) -> str:
        pass


class Clams(ABC):
    """Abstract product - Clams interface"""
    
    @abstractmethod
    def __str__(self) -> str:
        pass


# ============================================================================
# CONCRETE PRODUCTS - NY Ingredients
# ============================================================================

class ThinCrustDough(Dough):
    """Concrete product - NY style dough"""
    
    def __str__(self) -> str:
        return "Thin Crust Dough"


class MarinaraSauce(Sauce):
    """Concrete product - NY style sauce"""
    
    def __str__(self) -> str:
        return "Marinara Sauce"


class ReggianoCheese(Cheese):
    """Concrete product - NY style cheese"""
    
    def __str__(self) -> str:
        return "Reggiano Cheese"


class Garlic(Veggies):
    """Concrete product - Garlic"""
    
    def __str__(self) -> str:
        return "Garlic"


class Onion(Veggies):
    """Concrete product - Onion"""
    
    def __str__(self) -> str:
        return "Onion"


class Mushroom(Veggies):
    """Concrete product - Mushroom"""
    
    def __str__(self) -> str:
        return "Mushrooms"


class RedPepper(Veggies):
    """Concrete product - Red Pepper"""
    
    def __str__(self) -> str:
        return "Red Pepper"


class SlicedPepperoni(Pepperoni):
    """Concrete product - NY style pepperoni"""
    
    def __str__(self) -> str:
        return "Sliced Pepperoni"


class FreshClams(Clams):
    """Concrete product - NY style clams"""
    
    def __str__(self) -> str:
        return "Fresh Clams from Long Island Sound"


# ============================================================================
# CONCRETE PRODUCTS - Chicago Ingredients
# ============================================================================

class ThickCrustDough(Dough):
    """Concrete product - Chicago style dough"""
    
    def __str__(self) -> str:
        return "Extra Thick Crust Dough"


class PlumTomatoSauce(Sauce):
    """Concrete product - Chicago style sauce"""
    
    def __str__(self) -> str:
        return "Tomato Sauce with Plum Tomatoes"


class MozzarellaCheese(Cheese):
    """Concrete product - Chicago style cheese"""
    
    def __str__(self) -> str:
        return "Shredded Mozzarella"


class BlackOlives(Veggies):
    """Concrete product - Black Olives"""
    
    def __str__(self) -> str:
        return "Black Olives"


class Spinach(Veggies):
    """Concrete product - Spinach"""
    
    def __str__(self) -> str:
        return "Spinach"


class Eggplant(Veggies):
    """Concrete product - Eggplant"""
    
    def __str__(self) -> str:
        return "Eggplant"


class SlicedPepperoniChicago(Pepperoni):
    """Concrete product - Chicago style pepperoni"""
    
    def __str__(self) -> str:
        return "Sliced Pepperoni"


class FrozenClams(Clams):
    """Concrete product - Chicago style clams"""
    
    def __str__(self) -> str:
        return "Frozen Clams from Chesapeake Bay"


# ============================================================================
# ABSTRACT FACTORY - Ingredient Factory Interface
# ============================================================================

class PizzaIngredientFactory(ABC):
    """
    Abstract Factory - defines interface for creating families of ingredients.
    
    Each method creates one type of ingredient. Concrete factories will
    implement these methods to create region-specific ingredients.
    
    This ensures that all ingredients created by a factory are compatible
    (all NY ingredients or all Chicago ingredients).
    """
    
    @abstractmethod
    def create_dough(self) -> Dough:
        pass
    
    @abstractmethod
    def create_sauce(self) -> Sauce:
        pass
    
    @abstractmethod
    def create_cheese(self) -> Cheese:
        pass
    
    @abstractmethod
    def create_veggies(self) -> list[Veggies]:
        pass
    
    @abstractmethod
    def create_pepperoni(self) -> Pepperoni:
        pass
    
    @abstractmethod
    def create_clam(self) -> Clams:
        pass


# ============================================================================
# CONCRETE FACTORIES - Regional Ingredient Factories
# ============================================================================

class NYPizzaIngredientFactory(PizzaIngredientFactory):
    """
    Concrete Factory - creates NY style ingredients.
    
    This factory creates a family of NY-style ingredients.
    All ingredients are guaranteed to be compatible.
    """
    
    def create_dough(self) -> Dough:
        return ThinCrustDough()
    
    def create_sauce(self) -> Sauce:
        return MarinaraSauce()
    
    def create_cheese(self) -> Cheese:
        return ReggianoCheese()
    
    def create_veggies(self) -> list[Veggies]:
        return [Garlic(), Onion(), Mushroom(), RedPepper()]
    
    def create_pepperoni(self) -> Pepperoni:
        return SlicedPepperoni()
    
    def create_clam(self) -> Clams:
        return FreshClams()


class ChicagoPizzaIngredientFactory(PizzaIngredientFactory):
    """
    Concrete Factory - creates Chicago style ingredients.
    
    This factory creates a family of Chicago-style ingredients.
    All ingredients are guaranteed to be compatible.
    """
    
    def create_dough(self) -> Dough:
        return ThickCrustDough()
    
    def create_sauce(self) -> Sauce:
        return PlumTomatoSauce()
    
    def create_cheese(self) -> Cheese:
        return MozzarellaCheese()
    
    def create_veggies(self) -> list[Veggies]:
        return [BlackOlives(), Spinach(), Eggplant()]
    
    def create_pepperoni(self) -> Pepperoni:
        return SlicedPepperoniChicago()
    
    def create_clam(self) -> Clams:
        return FrozenClams()


# ============================================================================
# CLIENT - Pizza Classes (use ingredient factories)
# ============================================================================

class Pizza(ABC):
    """
    Abstract Pizza - the client that uses the ingredient factory.
    
    Notice: Pizza doesn't know about concrete ingredient classes.
    It only knows about the abstract ingredient interfaces.
    """
    
    def __init__(self):
        self.name = ""
        self.dough: Optional[Dough] = None
        self.sauce: Optional[Sauce] = None
        self.cheese: Optional[Cheese] = None
        self.veggies: list[Veggies] = []
        self.pepperoni: Optional[Pepperoni] = None
        self.clam: Optional[Clams] = None
    
    @abstractmethod
    def prepare(self):
        """
        Abstract method - subclasses must implement.
        This is where the ingredient factory is used.
        """
        pass
    
    def bake(self):
        print("Baking for 25 minutes at 350 degrees")
    
    def cut(self):
        print("Cutting the pizza into diagonal slices")
    
    def box(self):
        print("Placing pizza in official PizzaStore box")
    
    def set_name(self, name: str):
        self.name = name
    
    def get_name(self) -> str:
        return self.name
    
    def __str__(self) -> str:
        """Display pizza with its ingredients"""
        result = [f"\n---- {self.name} ----"]
        if self.dough:
            result.append(str(self.dough))
        if self.sauce:
            result.append(str(self.sauce))
        if self.cheese:
            result.append(str(self.cheese))
        if self.veggies:
            result.append(", ".join(str(v) for v in self.veggies))
        if self.pepperoni:
            result.append(str(self.pepperoni))
        if self.clam:
            result.append(str(self.clam))
        return "\n".join(result)


class CheesePizza(Pizza):
    """
    Concrete Pizza - uses ingredient factory to get ingredients.
    
    Notice: This class doesn't know if it's making NY or Chicago style.
    The ingredient factory determines that!
    """
    
    def __init__(self, ingredient_factory: PizzaIngredientFactory):
        super().__init__()
        self.ingredient_factory = ingredient_factory
    
    def prepare(self):
        """Use the factory to create ingredients"""
        print(f"Preparing {self.name}")
        self.dough = self.ingredient_factory.create_dough()
        self.sauce = self.ingredient_factory.create_sauce()
        self.cheese = self.ingredient_factory.create_cheese()


class PepperoniPizza(Pizza):
    """Concrete Pizza - Pepperoni pizza"""
    
    def __init__(self, ingredient_factory: PizzaIngredientFactory):
        super().__init__()
        self.ingredient_factory = ingredient_factory
    
    def prepare(self):
        """Use the factory to create ingredients"""
        print(f"Preparing {self.name}")
        self.dough = self.ingredient_factory.create_dough()
        self.sauce = self.ingredient_factory.create_sauce()
        self.cheese = self.ingredient_factory.create_cheese()
        self.pepperoni = self.ingredient_factory.create_pepperoni()


class VeggiePizza(Pizza):
    """Concrete Pizza - Veggie pizza"""
    
    def __init__(self, ingredient_factory: PizzaIngredientFactory):
        super().__init__()
        self.ingredient_factory = ingredient_factory
    
    def prepare(self):
        """Use the factory to create ingredients"""
        print(f"Preparing {self.name}")
        self.dough = self.ingredient_factory.create_dough()
        self.sauce = self.ingredient_factory.create_sauce()
        self.cheese = self.ingredient_factory.create_cheese()
        self.veggies = self.ingredient_factory.create_veggies()


class ClamPizza(Pizza):
    """Concrete Pizza - Clam pizza"""
    
    def __init__(self, ingredient_factory: PizzaIngredientFactory):
        super().__init__()
        self.ingredient_factory = ingredient_factory
    
    def prepare(self):
        """Use the factory to create ingredients"""
        print(f"Preparing {self.name}")
        self.dough = self.ingredient_factory.create_dough()
        self.sauce = self.ingredient_factory.create_sauce()
        self.cheese = self.ingredient_factory.create_cheese()
        self.clam = self.ingredient_factory.create_clam()


# ============================================================================
# PIZZA STORE - Combines Factory Method with Abstract Factory
# ============================================================================

class PizzaStore(ABC):
    """
    Abstract PizzaStore - uses Factory Method pattern.
    
    This combines Factory Method (for creating pizzas) with
    Abstract Factory (for creating ingredients).
    """
    
    def order_pizza(self, pizza_type: str) -> Optional[Pizza]:
        """Template method - same for all stores"""
        pizza = self.create_pizza(pizza_type)
        
        if pizza is None:
            return None
        
        print(f"\n--- Making a {pizza.get_name()} ---")
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        
        return pizza
    
    @abstractmethod
    def create_pizza(self, pizza_type: str) -> Optional[Pizza]:
        """Factory method - subclasses implement"""
        pass


class NYPizzaStore(PizzaStore):
    """
    NY Pizza Store - creates pizzas with NY ingredient factory.
    
    This store uses the NY ingredient factory, so all pizzas
    will automatically have NY-style ingredients.
    """
    
    def create_pizza(self, pizza_type: str) -> Optional[Pizza]:
        """Create pizza with NY ingredient factory"""
        pizza = None
        ingredient_factory = NYPizzaIngredientFactory()
        
        if pizza_type == "cheese":
            pizza = CheesePizza(ingredient_factory)
            pizza.set_name("New York Style Cheese Pizza")
        elif pizza_type == "pepperoni":
            pizza = PepperoniPizza(ingredient_factory)
            pizza.set_name("New York Style Pepperoni Pizza")
        elif pizza_type == "veggie":
            pizza = VeggiePizza(ingredient_factory)
            pizza.set_name("New York Style Veggie Pizza")
        elif pizza_type == "clam":
            pizza = ClamPizza(ingredient_factory)
            pizza.set_name("New York Style Clam Pizza")
        else:
            print(f"Error: Unknown pizza type '{pizza_type}'")
            return None
        
        return pizza


class ChicagoPizzaStore(PizzaStore):
    """
    Chicago Pizza Store - creates pizzas with Chicago ingredient factory.
    
    This store uses the Chicago ingredient factory, so all pizzas
    will automatically have Chicago-style ingredients.
    """
    
    def create_pizza(self, pizza_type: str) -> Optional[Pizza]:
        """Create pizza with Chicago ingredient factory"""
        pizza = None
        ingredient_factory = ChicagoPizzaIngredientFactory()
        
        if pizza_type == "cheese":
            pizza = CheesePizza(ingredient_factory)
            pizza.set_name("Chicago Style Cheese Pizza")
        elif pizza_type == "pepperoni":
            pizza = PepperoniPizza(ingredient_factory)
            pizza.set_name("Chicago Style Pepperoni Pizza")
        elif pizza_type == "veggie":
            pizza = VeggiePizza(ingredient_factory)
            pizza.set_name("Chicago Style Veggie Pizza")
        elif pizza_type == "clam":
            pizza = ClamPizza(ingredient_factory)
            pizza.set_name("Chicago Style Clam Pizza")
        else:
            print(f"Error: Unknown pizza type '{pizza_type}'")
            return None
        
        return pizza


# ============================================================================
# DEMONSTRATION
# ============================================================================

def main():
    """Demonstrate the Abstract Factory pattern"""
    
    print("=" * 70)
    print("PIZZA STORE - ABSTRACT FACTORY PATTERN")
    print("=" * 70)
    
    # Create stores
    ny_store = NYPizzaStore()
    chicago_store = ChicagoPizzaStore()
    
    # Order from NY
    pizza = ny_store.order_pizza("cheese")
    if pizza:
        print(pizza)
    
    print("\n" + "=" * 70 + "\n")
    
    # Order from Chicago
    pizza = chicago_store.order_pizza("cheese")
    if pizza:
        print(pizza)
    
    print("\n" + "=" * 70 + "\n")
    
    # Order pepperoni from NY
    pizza = ny_store.order_pizza("pepperoni")
    if pizza:
        print(pizza)
    
    print("\n" + "=" * 70 + "\n")
    
    # Order veggie from Chicago
    pizza = chicago_store.order_pizza("veggie")
    if pizza:
        print(pizza)
    
    print("\n" + "=" * 70 + "\n")
    
    # Order clam from both
    pizza = ny_store.order_pizza("clam")
    if pizza:
        print(pizza)
    
    print("\n" + "=" * 70 + "\n")
    
    pizza = chicago_store.order_pizza("clam")
    if pizza:
        print(pizza)
    
    print("\n" + "=" * 70)
    print()
    
    print("KEY BENEFITS OF ABSTRACT FACTORY PATTERN:")
    print("-" * 70)
    print("✓ Creates families of related objects")
    print("  - All ingredients from one factory are compatible")
    print("  - NY factory creates NY ingredients, Chicago creates Chicago ingredients")
    print()
    print("✓ Isolates concrete classes")
    print("  - Client code (Pizza) doesn't know about concrete ingredient classes")
    print("  - Works with abstract interfaces (Dough, Sauce, Cheese, etc.)")
    print()
    print("✓ Promotes consistency among products")
    print("  - Guarantees that ingredients belong to the same family")
    print("  - Can't accidentally mix NY dough with Chicago sauce")
    print()
    print("✓ Easy to exchange product families")
    print("  - Just swap the factory to get a different family")
    print("  - Same pizza code works with any ingredient factory")
    print()
    print("✓ Supports Open-Closed Principle")
    print("  - Add new ingredient families without changing existing code")
    print("  - Add new ingredient types by extending the factory interface")
    print()
    
    print("PATTERN STRUCTURE:")
    print("-" * 70)
    print("Abstract Factory (PizzaIngredientFactory)")
    print("  ├─ createDough(), createSauce(), createCheese(), ...")
    print("  └─ Defines interface for creating ingredient families")
    print()
    print("Concrete Factories")
    print("  ├─ NYPizzaIngredientFactory - creates NY ingredients")
    print("  └─ ChicagoPizzaIngredientFactory - creates Chicago ingredients")
    print()
    print("Abstract Products")
    print("  ├─ Dough, Sauce, Cheese, Veggies, Pepperoni, Clams")
    print("  └─ Ingredient interfaces")
    print()
    print("Concrete Products")
    print("  ├─ ThinCrustDough, MarinaraSauce, ReggianoCheese, ... (NY)")
    print("  └─ ThickCrustDough, PlumTomatoSauce, MozzarellaCheese, ... (Chicago)")
    print()
    print("Client (Pizza)")
    print("  ├─ Uses ingredient factory to get ingredients")
    print("  └─ Doesn't know about concrete ingredient classes")
    print()
    
    print("ABSTRACT FACTORY vs FACTORY METHOD:")
    print("-" * 70)
    print("Factory Method:")
    print("  - Uses inheritance (subclasses decide which class to instantiate)")
    print("  - Creates one product")
    print("  - Example: PizzaStore.createPizza()")
    print()
    print("Abstract Factory:")
    print("  - Uses composition (object delegates to factory)")
    print("  - Creates families of related products")
    print("  - Example: PizzaIngredientFactory creates dough, sauce, cheese, etc.")
    print()
    print("This example combines BOTH patterns:")
    print("  - Factory Method: PizzaStore creates pizzas")
    print("  - Abstract Factory: PizzaIngredientFactory creates ingredients")
    print("=" * 70)


if __name__ == "__main__":
    main()

# Made with Bob
