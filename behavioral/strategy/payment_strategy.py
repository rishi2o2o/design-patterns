from abc import ABC, abstractmethod


class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount: float) -> None:
        pass


class CreditCardPayment(PaymentStrategy):
    def __init__(self, card_number: str, holder_name: str):
        self.card_number = card_number
        self.holder_name = holder_name

    def pay(self, amount: float) -> None:
        print(f"Paid ₹{amount} using Credit Card ending in {self.card_number[-4:]}.")
    

class PayPalPayment(PaymentStrategy):
    def __init__(self, email: str):
        self.email = email

    def pay(self, amount: float) -> None:
        print(f"Paid ₹{amount} via PayPal account: {self.email}.")


class ShoppingCart:
    def __init__(self):
        self.amount: float = 0.0
        self._payment_strategy: PaymentStrategy = None  

    def set_payment_method(self, strategy: PaymentStrategy) -> None:
        self._payment_strategy = strategy

    def add_item(self, price: float) -> None:
        self.amount += price

    def checkout(self) -> None:
        if not self._payment_strategy:
            print("Please select a payment method first.")
            return
        self._payment_strategy.pay(self.amount)

if __name__ == "__main__":

    # 1. pay using credit card
    cart = ShoppingCart()
    cart.add_item(1500.00)
    cart.add_item(450.50)

    card_strategy = CreditCardPayment("1234-5678-9876-5432", "John Doe")
    cart.set_payment_method(card_strategy)
    cart.checkout()

    # 2. pay using paypal
    cart2 = ShoppingCart()
    cart2.add_item(1500.00)
    cart2.add_item(450.50)
    paypal_strategy = PayPalPayment("john.doe@example.com")
    cart2.set_payment_method(paypal_strategy)
    cart2.checkout()



