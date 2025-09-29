from Modules.SMSShield.Blocklist import Blocklist
from Modules.SMSShield.Logger import Logger
from Core.AuditTrail import AuditTrail

class Interceptor:
    def __init__(self):
        self.audit = AuditTrail()
        self.blocklist = Blocklist()
        self.logger = Logger()

    def intercept(self, sender, message):
        # Заглушка: здесь будет логика фильтрации
        self.audit.record("SMSShield.Interceptor", "intercept", {
        if self.blocklist.is_blocked(sender):
            status = "blocked"
        else:
            status = "allowed"

        self.logger.log(sender, message, status)
        print(f"[{status.upper()}] SMS от {sender}: {message}")
            "sender": sender,
            "message": message
        })
        print(f"[INTERCEPTED] SMS от {sender}: {message}")
