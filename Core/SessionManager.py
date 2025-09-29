import uuid
import json
import datetime

class SessionManager:
    def __init__(self, session_store="Storage/session_tokens.json"):
        self.session_store = session_store
        self._ensure_store()

    def _ensure_store(self):
        try:
            with open(self.session_store, "r") as f:
                json.load(f)
        except:
            with open(self.session_store, "w") as f:
                json.dump({}, f)

    def create_session(self, user_id):
        token = str(uuid.uuid4())
        entry = {
            "token": token,
            "created": datetime.datetime.utcnow().isoformat()
        }
        with open(self.session_store, "r+") as f:
            store = json.load(f)
            store[user_id] = entry
            f.seek(0)
            json.dump(store, f, indent=2)
        return token

    def get_session(self, user_id):
        with open(self.session_store, "r") as f:
            store = json.load(f)
            return store.get(user_id)
