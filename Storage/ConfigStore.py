import json
from Core.AuditTrail import AuditTrail

class ConfigStore:
    def __init__(self, path="config.json"):
        self.path = path
        self.audit = AuditTrail()
        self.config = {
            "language": "ru",
            "theme": "midnight_neon",
            "policy": "adaptive"
        }

    def load(self):
        try:
            with open(self.path, "r") as f:
                self.config = json.load(f)
                self.audit.record("Storage.ConfigStore", "load", self.config)
        except FileNotFoundError:
            self.save()
mkdir -p Storage && cat > Storage/ConfigStore.py <<EOF
import json
from Core.AuditTrail import AuditTrail

class ConfigStore:
    def __init__(self, path="config.json"):
        self.path = path
        self.audit = AuditTrail()
        self.config = {
            "language": "ru",
            "theme": "midnight_neon",
            "policy": "adaptive"
        }

    def load(self):
        try:
            with open(self.path, "r") as f:
                self.config = json.load(f)
                self.audit.record("Storage.ConfigStore", "load", self.config)
        except FileNotFoundError:
            self.save()

    def save(self):
        with open(self.path, "w") as f:
            json.dump(self.config, f, indent=2)
            self.audit.record("Storage.ConfigStore", "save", self.config)

    def set(self, key, value):
        self.config[key] = value
        self.save()
