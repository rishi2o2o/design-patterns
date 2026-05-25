from abc import ABC, abstractmethod
from turtle import window_width

# --- Abstract Products ---
class Button(ABC):
    @abstractmethod
    def render(self) -> str:
        pass

class Checkbox(ABC):
    @abstractmethod
    def render(self) -> str:
        pass

# --- Concrete Products (Windows) ---
class WindowsButton(Button):
    def render(self) -> str:
        return "windows button"

class WindowsCheckbox(Checkbox):
    def render(self) -> str:
        return "windows checkbox"


# --- Concrete Products (macOS) ---
class MacOSButton(Button):
    def render(self) -> str:
        return "macos button"

class MacOSCheckbox(Checkbox):
    def render(self) -> str:
        return "macos checkbox"


# --- Abstract Factory ---
class GUIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass


# --- Concrete Factories ---
class WindowsFactory(GUIFactory):
    def create_button(self) -> Button:
        return WindowsButton()
    
    def create_checkbox(self) -> Checkbox:
        return WindowsCheckbox()


class MacOSFactory(GUIFactory):
    def create_button(self) -> Button:
        return MacOSButton()
    
    def create_checkbox(self) -> Checkbox:
        return MacOSCheckbox()


if __name__ == "__main__":
    windows_factory = WindowsFactory()
    print(windows_factory.create_button().render())
    print(windows_factory.create_checkbox().render())

    macos_factory = MacOSFactory()
    print(macos_factory.create_button().render())
    print(macos_factory.create_checkbox().render())


