from Core.SessionManager import SessionManager
from Core.MessageRouter import MessageRouter
from Modules.SMSShield.Interceptor import Interceptor

class Layout:
    def __init__(self):
        self.session = SessionManager()
        self.router = MessageRouter()
        self.sms = Interceptor()

    def render(self):
        return {
            "header": "Eugram",
            "panels": ["Messages", "Contacts", "Settings"],
            "status": "ready"
        }

    def handle_input(self, source, payload):
        if source == "sms":
            self.sms.intercept(payload["sender"], payload["message"])
        elif source == "
mkdir -p Modules/GUI && cat > Modules/GUI/Layout.py <<EOF
from Core.SessionManager import SessionManager
from Core.MessageRouter import MessageRouter
from Modules.SMSShield.Interceptor import Interceptor

class Layout:
    def __init__(self):
        self.session = SessionManager()
        self.router = MessageRouter()
        self.sms = Interceptor()

    def render(self):
        return {
            "header": "Eugram",
            "panels": ["Messages", "Contacts", "Settings"],
            "status": "ready"
        }

    def handle_input(self, source, payload):
        if source == "sms":
            self.sms.intercept(payload["sender"], payload["message"])
        elif source == "user":
            self.router.route(payload)
