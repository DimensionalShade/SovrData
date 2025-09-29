import json
import os

class Blocklist:
    def __init__(self, path="Storage/blocklist.json"):
        self.path = path
        self._ensure_list()

    def _ensure_list(self):
        if not os.path.exists(self.path):
            with open(self.path, "w") as f:
                json.dump([], f)

    def is_blocked(self, sender):
        with open(self.path, "r") as f:
            blocked = json.load(f)
            return sender in blocked

    def add(self, sender):
        with open(self.path, "r+") as f:
            blocked = json.load(f)
            if sender not in blocked:
                blocked.append(sender)
                f.seek(0)
                json.dump(blocked, f, indent=2)
