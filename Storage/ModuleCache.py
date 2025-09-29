import json
from Core.AuditTrail import AuditTrail

class ModuleCache:
    def __init__(self, path="module_cache.json"):
        self.path = path
        self.audit = AuditTrail()
        self.cache = {}

    def load(self):
        try:
            with open(self.path, "r") as f:
                self.cache = json.load(f)
                self.audit.record("Storage.ModuleCache", "load", self.cache)
        except FileNotFoundError:
            self.save()

    def save(self):
        with open(self.path, "w") as f:
            json.dump(self.cache, f, indent=2)
            self.audit.record("Storage.ModuleCache", "save", self.cache)

    def set_status(self, module, status, version):
        self.cache[module] = {"status": status, "version": version}
        self.save()
