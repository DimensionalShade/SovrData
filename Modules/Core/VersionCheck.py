import json
import os
from Storage.ModuleCache import ModuleCache
from Core.AuditTrail import AuditTrail

class VersionCheck:
    def __init__(self, manifest_path="manifest.json"):
        self.manifest_path = manifest_path
        self.cache = ModuleCache()
        self.audit = AuditTrail()

    def check(self):
        if not os.path.exists(self.manifest_path):
            self.audit.record("VersionCheck", "manifest_missing")
            return {}

        with open(self.manifest_path, "r") as f:
            manifest = json.load(f)

        results = {}
        for name, data in manifest.items():
            cached = self.cache.load(name)
            if cached != data.get("code"):
                results[name] = "update_needed"
                self.audit.record("VersionCheck", "version_mismatch", {"module": name})
            else:
                results[name] = "up_to_date"
        return results

    def update(self):
        with open(self.manifest_path, "r") as f:
            manifest = json.load(f)

        for name, data in manifest.items():
            self.cache.store(name, data.get("code"))
            self.audit.record("VersionCheck", "module_updated", {"module": name})
