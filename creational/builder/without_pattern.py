# Code to create a computer object
class Computer:
    def __init__(self, hdd, ram, graphics_card, bluetooth, os):
        self.hdd = hdd
        self.ram = ram
        self.graphics_card = graphics_card
        self.bluetooth = bluetooth
        self.os = os


if __name__ == "__main__":
    # Client Usage  

    # See how you need to pass multiple None for parameters you don't care about.
    # This becomes highly unreadable.

    gaming_pc = Computer(
        "2TB SSD", 
        "32GB", 
        "RTX 4090", 
        True, 
        "Windows 11", 
    )

    basic_pc = Computer(
        "500GB", 
        "8GB", 
        None, 
        None, 
        None, 
    )



