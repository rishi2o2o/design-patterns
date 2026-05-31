from abc import ABC, abstractmethod

# --- Abstract Product ---
class Burger(ABC):
    @abstractmethod
    def prepare(self) -> str:
        pass

# --- Concrete Products ---
class CheeseBurger(Burger):
    def prepare(self) -> str:
        return "cheese burger"

class VeggieBurger(Burger):
    def prepare(self) -> str:
        return "veggie burger"


# --- Creator ---
class BurgerFactory(ABC):
    @abstractmethod
    def create_burger(self) -> Burger:
        pass

    def order_burger(self) -> str:
        burger = self.create_burger()
        return burger.prepare()

# --- Concrete Creators ---
class CheeseBurgerFactory(BurgerFactory):
    def create_burger(self) -> Burger:
        return CheeseBurger()


class VeggieBurgerFactory(BurgerFactory):
    def create_burger(self) -> Burger:
        return VeggieBurger()


if __name__ == "__main__":
    cheese_factory = CheeseBurgerFactory()
    print(cheese_factory.order_burger())

    veggie_factory = VeggieBurgerFactory()
    print(veggie_factory.order_burger())


