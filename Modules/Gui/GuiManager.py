from Core.LanguageAdapt import LanguageAdapt
from Core.AuditTrail import AuditTrail

class GuiManager:
    def __init__(self):
        self.language_adapt = LanguageAdapt()
        self.audit = AuditTrail()
        self.language = self.language_adapt.get_language()
        self.audit.record("GuiManager", "language_initialized", {"lang": self.language})

    def render(self):
        if self.language.startswith("ru"):
            return "Добро пожаловать в Eugram"
        elif self.language.startswith("en"):
            return "Welcome to Eugram"
        else:
            return f"Welcome (lang: {self.language})"

    def switch_language(self, lang_code):
        self.language_adapt.set_language(lang_code)
        self.language = lang_code
        self.audit.record("GuiManager", "language_switched", {"lang": lang_code})
