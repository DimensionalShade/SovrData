from Core.AuditTrail import AuditTrail

class Interceptor:
    def __init__(self):
        self.audit = AuditTrail()

    def intercept(self, sender, message):
        # Заглушка: здесь будет логика фильтрации
        self.audit.record("SMSShield.Interceptor", "intercept", {
            "sender": sender,
            "message": message
        })
        print(f"[INTERCEPTED] SMS от {sender}: {message}")
