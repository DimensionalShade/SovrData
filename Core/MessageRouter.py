from Core.ConsentVault import ConsentVault
from Core.AuditTrail import AuditTrail

class MessageRouter:
    def __init__(self):
        self.consent = ConsentVault()
        self.audit = AuditTrail()

    def route(self, user_id, message, target_module):
        # Проверка согласия
        self.consent.record_consent(user_id, "message_send", scope=target_module)
        # Логирование маршрута
        self.audit.record("MessageRouter", "route", {
            "user_id": user_id,
            "message": message,
            "target": target_module
        })
        # Здесь будет вызов модуля (заглушка)
        print(f"[ROUTED] → {target_module}: {message}")
