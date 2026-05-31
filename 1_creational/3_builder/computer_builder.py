class Computer:
    def __init__(self, builder):
        self.hdd = builder.hdd
        self.ram = builder.ram
        self.graphics_card = builder.graphics_card
        self.bluetooth = builder.bluetooth
        self.os = builder.os

    def __str__(self):
        return (f"Computer Specs: [RAM: {self.ram}, HDD: {self.hdd}, "
                f"GPU: {self.graphics_card}, BT: {self.bluetooth}, OS: {self.os}]")


# ComputerBuilder handles the creation of Computer objects
class ComputerBuilder:
    def __init__(self, hdd, ram) -> None:
        # Mandatory parameters handled in constructor
        self.hdd = hdd
        self.ram = ram

        # Optional parameters initialized to sensible defaults
        self.graphics_card = None
        self.bluetooth = False
        self.os = None

    def set_graphics_card(self, gpu_model):
        self.graphics_card = gpu_model
        return self  # this enables method chaining

    def set_bluetooth(self, enabled):
        self.bluetooth = enabled
        return self

    def set_os(self, os_name):
        self.os = os_name
        return self

    def build(self) -> Computer:
        return Computer(self)


if __name__ == "__main__":
    # Client Usage
    # See how you can set the parameters you want in a readable way.

    gaming_pc = (ComputerBuilder("2TB SSD", "32GB")
                           .set_graphics_card("RTX 4090")
                           .set_bluetooth(True)
                           .build())
    
    basic_pc = ComputerBuilder("500GB HDD", "8GB").build()

    print(gaming_pc)
    print(basic_pc)


