import locale
from Storage.config import ConfigStore
from Core.AuditTrail import AuditTrail

class LanguageAdapt:
    def __init__(self):
        self.config = ConfigStore()
        self.audit = AuditTrail()
        self.language = self.detect_language()

    def detect_language(self):
        lang = self.config.get("language")
        if lang:
            self.audit.record("LanguageAdapt", "language_loaded", {"lang": lang})
            return lang
        system_lang = locale.getdefaultlocale()[0]
        self.audit.record("LanguageAdapt", "language_detected", {"lang": system_lang})
        return system_lang

    def set_language(self, lang_code):
        self.config.set("language", lang_code)
        self.language = lang_code
        self.audit.record("LanguageAdapt", "language_set", {"lang": lang_code})

    def get_language(self):
        return self.language
