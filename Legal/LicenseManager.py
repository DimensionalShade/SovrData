import json
from Core.AuditTrail import AuditTrail

class LicenseManager:
    def __init__(self, path="licenses.json"):
        self.path = path
        self.audit = AuditTrail()
        self.licenses = {}

    def load(self):
        try:
            with open(self.path, "r") as f:
                self.licenses = json.load(f)
                self.audit.record("Legal.LicenseManager", "load", self.licenses)
        except FileNotFoundError:
            self.save()

    def save(self):
        with open(self.path, "w") as f:
            json.dump(self.licenses, f, indent=2)
            self.audit.record("Legal.LicenseManager", "save", self.licenses)

    def validate(self, module):
        lic = self.licenses.get(module)
        valid = lic and lic.get("status") == "approved"
        self.audit.record("Legal.LicenseManager", "validate", {
            "module": module,
            "result": valid
        })
        return valid

    def get_terms(self, module):
        return self.licenses.get(module, {}).get("terms", "not found")
