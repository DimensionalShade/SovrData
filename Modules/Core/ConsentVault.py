class ConsentVault:
    def __init__(self):
        self.vault = []

    def log_reveal(self, fragment, context):
        from datetime import datetime
        self.vault.append({
            "action": "reveal",
            "fragment": fragment,
            "context": context,
            "timestamp": datetime.utcnow().isoformat()
        })
        self._save()

    def _save(self):
        pass  # заглушка для будущей сериализации
