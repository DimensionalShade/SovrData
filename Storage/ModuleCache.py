import os
import json
from Core.AuditTrail import AuditTrail

class ModuleCache:
    def __init__(self, path="Storage/modules"):
        self.path = path
        self.audit = AuditTrail()
        os.makedirs(self.path, exist_ok=True)

    def store(self, name, code):
        file_path = os.path.join(self.path, f"{name}.py")
        with open(file_path, "w") as f:
            f.write(code)
        self.audit.record("ModuleCache", "store", {"module": name})

    def load(self, name):
        file_path = os.path.join(self.path, f"{name}.py")
        if os.path.exists(file_path):
            with open(file_path, "r") as f:
                code = f.read()
            self.audit.record("ModuleCache", "load", {"module": name})
            return code
        else:
            self.audit.record("ModuleCache", "load_failed", {"module": name})
            return None
