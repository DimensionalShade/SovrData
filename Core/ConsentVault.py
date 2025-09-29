import json
import datetime

class ConsentVault:
    def __init__(self, storage_path="Storage/consent_log.json"):
        self.storage_path = storage_path
        self._ensure_log()

    def _ensure_log(self):
        try:
            with open(self.storage_path, "r") as f:
                json.load(f)
        except:
            with open(self.storage_path, "w") as f:
                json.dump([], f)

    def record_consent(self, user_id, action, scope):
        entry = {
            "timestamp": datetime.datetime.utcnow().isoformat(),
            "user_id": user_id,
            "action": action,
            "scope": scope
        }
        with open(self.storage_path, "r+") as f:
            log = json.load(f)
            log.append(entry)
            f.seek(0)
            json.dump(log, f, indent=2)

    def get_log(self):
        with open(self.storage_path, "r") as f:
            return json.load(f)
