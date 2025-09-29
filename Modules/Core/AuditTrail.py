import json
import os
from datetime import datetime

class AuditTrail:
    def __init__(self, path="Storage/audit.json"):
        self.path = path
        self.entries = []
        if os.path.exists(self.path):
            try:
                with open(self.path, "r") as f:
                    self.entries = json.load(f)
            except:
                self.entries = []

    def record(self, module, action, context=None):
        entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "module": module,
            "action": action,
            "context": context or {}
        }
        self.entries.append(entry)
        self._save()

    def _save(self):
        with open(self.path, "w") as f:
            json.dump(self.entries, f, indent=2, ensure_ascii=False)

    def export(self):
        return self.entries
