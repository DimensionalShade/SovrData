import json
import datetime

class AuditTrail:
    def __init__(self, log_path="Storage/audit_log.json"):
        self.log_path = log_path
        self._ensure_log()

    def _ensure_log(self):
        try:
            with open(self.log_path, "r") as f:
                json.load(f)
        except:
            with open(self.log_path, "w") as f:
                json.dump([], f)

    def record(self, source, event, details=None):
        entry = {
            "timestamp": datetime.datetime.utcnow().isoformat(),
            "source": source,
            "event": event,
            "details": details or {}
        }
        with open(self.log_path, "r+") as f:
            log = json.load(f)
            log.append(entry)
            f.seek(0)
            json.dump(log, f, indent=2)

    def get_log(self):
        with open(self.log_path, "r") as f:
            return json.load(f)
