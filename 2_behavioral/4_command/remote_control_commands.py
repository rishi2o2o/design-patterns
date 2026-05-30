from abc import ABC, abstractmethod

class Light:  # command receiver
    def turn_on(self):
        print("The light is ON")
        
    def turn_off(self):
        print("The light is OFF")


class Command(ABC):  # command interface
    @abstractmethod
    def execute(self):
        pass
    
    @abstractmethod
    def undo(self):
        pass

class LightOnCommand(Command): # concrete commands
    def __init__(self, light: Light):
        self.light = light
        
    def execute(self):
        self.light.turn_on()
        
    def undo(self):
        self.light.turn_off()

class LightOffCommand(Command):
    def __init__(self, light: Light):
        self.light = light
        
    def execute(self):
        self.light.turn_off()
        
    def undo(self):
        self.light.turn_on()


class RemoteControl:  # command invoker/sender
    """Remote control has 3 buttons - button a, button b and undo button"""

    def __init__(self, slot_a: Command, slot_b: Command):
        self._slot_a_command = slot_a
        self._slot_b_command = slot_b
        self._command_history = []

    def press_button_a(self):
        self._slot_a_command.execute()
        self._command_history.append(self._slot_a_command)

    def press_button_b(self):
        self._slot_b_command.execute()
        self._command_history.append(self._slot_b_command)
    
    def press_undo_button(self):
        if self._command_history:
            last_command = self._command_history.pop()
            last_command.undo()


if __name__ == "__main__":
    kitchen_light = Light()
    remote_control = RemoteControl(
                                        slot_a=LightOnCommand(kitchen_light),
                                        slot_b=LightOffCommand(kitchen_light),
                                    )
                        
    # 1. Switch light on
    print("-- Press light on button --")
    remote_control.press_button_a()

    # 2. Switch light off
    print("-- Press light off button --")
    remote_control.press_button_b()

    # 3. Undo last command (light switch off)
    print("-- Press undo button --")
    remote_control.press_undo_button()


