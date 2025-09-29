import json
from Storage.ModuleCache import ModuleCache
from Core.AuditTrail import AuditTrail

class VersionCheck:
    def __init__(self, latest_path="latest.json"):
        self.latest_path = latest_path
        self.cache = ModuleCache()
        self.audit = AuditTrail()

    def check(self):
        try:
            with open(self.latest_path, "r") as f:
                latest = json.load(f)
        except FileNotFoundError:
            latest = {}

        outdated = {}
        for module, info in latest.items():
            current = self.cache.cache.get(module, {})
            if current.get("version") != info.get("version"):
                outdated[module] = {
                    "current": current.get("version"),
                    "expected": info.get("version")
                }

        self.audit.record("Update.VersionCheck", "check", {"outdated": outdated})
        return outdated
