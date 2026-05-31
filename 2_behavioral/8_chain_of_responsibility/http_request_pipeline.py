from abc import ABC, abstractmethod
from typing import Optional

# --- Handler Interface ---

class Handler(ABC):

    def __init__(self):
        self.next_handler: Optional[Handler] = None

    def set_next(self, handler: 'Handler') -> 'Handler':
        """Set the next handler in chain"""
        self.next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request) -> str:
        pass

    def forward(self, request):
        """Forward the request to next handler"""
        if self.next_handler:
            return self.next_handler.handle(request)
        return "✅ Request reached core business logic"


# --- Concrete Handlers ---

class AuthenticationHandler(Handler):
    """Step 1: Check if the user credentials are authenticated"""

    def handle(self, request) -> str:
        print("Checking authentication...")
        if not request["is_authenticated"]:
            return "❌ 401 Unauthorized"
        return self.forward(request)


class AdminValidationHandler(Handler):
    """Step 2: Check if the user has the required admin role"""

    def handle(self, request) -> str:
        print("Checking admin role...")
        if request["role"] != "admin":
            return "❌ 403 Forbidden"
        return self.forward(request)


class DataSanitizationHandler(Handler):
    """Step 3: Check for malicious input in request"""

    def handle(self, request) -> str:
        print("Checking input...")
        if "malicious_script" in request["body"]:
            return "❌ 400 Bad Request"
        return self.forward(request)


# --- Client Code ---
if __name__ == "__main__":

    # Initialize the individual handlers
    auth_step = AuthenticationHandler()
    admin_step = AdminValidationHandler()
    sanitize_step = DataSanitizationHandler()

    # Chain them together: Authentication -> Admin -> Sanitize
    auth_step.set_next(admin_step).set_next(sanitize_step)

    # Test requests
    requests_to_test = [
        {
            "is_authenticated": False, 
            "role": "guest", 
            "body": "Hello world"
        },
        {
            "is_authenticated": True, 
            "role": "user", 
            "body": "Show me dashboard"
        },
        {
            "is_authenticated": True, 
            "role": "admin", 
            "body": "<script>malicious_script</script>"
        },
        {
            "is_authenticated": True, 
            "role": "admin", 
            "body": "Safe admin command execution."
        }
    ]

    # Pass each request to first step of pipeline
    for index, request in enumerate(requests_to_test, 1):
        print(f"\n--- Processing Request #{index} ---")
        result = auth_step.handle(request)
        print(result)

