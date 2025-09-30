import json
from Core.VersionCheck import VersionCheck
from Storage.ModuleCache import ModuleCache
from Core.AuditTrail import AuditTrail

class AutoUpdater:
    def __init__(self):
        self.version_check = VersionCheck()
        self.cache = ModuleCache()
        self.audit = AuditTrail()

    def update_all(self):
        updates = self.version_check.check_all()
        for module, url in updates.items():
            code = self.version_check.download(url)
            self.cache.store(module, code)
            self.audit.record("AutoUpdater", "module_updated", {"module": module})
        return list(updates.keys())
