from Core.AuditTrail import AuditTrail

class Firewall:
    def __init__(self):
        self.audit = AuditTrail()
        self.rules = []

    def allow(self, ip, port):
        self.rules.append({"ip": ip, "port": port, "action": "allow"})
        self.audit.record("NetGuard.Firewall", "allow", {"ip": ip, "port": port})

    def block(self, ip, port):
        self.rules.append({"ip": ip, "port": port, "action": "block"})
        self.audit.record("NetGuard.Firewall", "block", {"ip": ip, "port": port})

    def check(self, ip, port):
        for rule in self.rules:
            if rule["ip"] == ip and rule["port"] == port:
                return rule["action"]
        return "allow"
