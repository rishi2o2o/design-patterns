from abc import ABC, abstractmethod

# --- Context Class ---
class Document:
    def __init__(self):
        self._state = DraftState(self) # Initial state is Draft

    def transition_to(self, state: 'State'):
        """Allows state objects to change the context's state."""
        self._state = state

    def render(self):
        """Delegates behavior to the current state object."""
        self._state.render()

    def publish(self):
        """Delegates behavior to the current state object."""
        self._state.publish()


# --- State Interface ---
class State(ABC):
    @abstractmethod
    def render(self) -> None:
        pass

    @abstractmethod
    def publish(self) -> None:
        pass


# --- Concrete States ---
class DraftState(State):
    def __init__(self, document):
        self.document = document

    def render(self) -> None:
        print("Draft State: Rendering draft preview for the author.")

    def publish(self) -> None:
        print("Draft State: Moving document to moderation.")
        self.document.transition_to(ModerationState(self.document))


class ModerationState(State):
    def __init__(self, document):
        self.document = document

    def render(self) -> None:
        print("Moderation State: Rendering review screen for the admin.")

    def publish(self) -> None:
        print("Moderation State: Approving and publishing the document.")
        self.document.transition_to(PublishedState(self.document))


class PublishedState(State):
    def __init__(self, document):
        self.document = document

    def render(self) -> None:
        print("Published State: Rendering public article for all readers.")

    def publish(self) -> None:
        print("Published State: Document is already published. Doing nothing.")
        

# --- Client Code ---
if __name__ == "__main__":
    doc = Document()

    # 1. Behavior in Draft State
    doc.render()
    doc.publish()  # Triggers transition to Moderation
    print("-" * 40)

    # 2. Behavior in Moderation State
    doc.render()
    doc.publish()  # Triggers transition to Published
    print("-" * 40)

    # 3. Behavior in Published State
    doc.render()
    doc.publish()  # Already published


