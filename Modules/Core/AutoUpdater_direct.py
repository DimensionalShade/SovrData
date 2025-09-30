import json
import VersionCheck
import ModuleCache
import AuditTrail

class AutoUpdater:
    def __init__(self):
        self.version_check = VersionCheck.VersionCheck()
        self.cache = ModuleCache.ModuleCache()
        self.audit = AuditTrail.AuditTrail()

    def update_all(self):
        updates = self.version_check.check_all()
        for module, url in updates.items():
            code = self.version_check.download(url)
            self.cache.store(module, code)
        self.audit.record(module, "updated")
        with open("version.txt", "w") as f:
            f.write(self.version_check.get_latest_version())
        self.audit.record(module, "updated")
        with open("version.txt", "w") as f:
            f.write(self.version_check.get_latest_version())
        return list(updates.keys())
