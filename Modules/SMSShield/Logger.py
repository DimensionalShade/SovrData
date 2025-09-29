import json
import datetime
import os

class Logger:
    def __init__(self, path="Storage/sms_log.json"):
        self.path = path
        self._ensure_log()

    def _ensure_log(self):
        if not os.path.exists(self.path):
            with open(self.path, "w") as f:
                json.dump([], f)

    def log(self, sender, message, status):
        entry = {
            "timestamp": datetime.datetime.utcnow().isoformat(),
            "sender": sender,
            "message": message,
            "status": status
        }
        with open(self.path, "r+") as f:
            log = json.load(f)
            log.append(entry)
            f.seek(0)
            json.dump(log, f, indent=2)
