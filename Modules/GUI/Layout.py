from Modules.GUI.ThemeMidnightNeon import ThemeMidnightNeon
from Modules.GUI.Localization import Localization
from Storage.ConfigStore import ConfigStore

class Layout:
    def __init__(self):
        self.config = ConfigStore()
        self.config.load()
        self.theme = ThemeMidnightNeon()
        self.local = Localization(lang=self.config.config.get("language", "ru"))

    def render_main_screen(self):
        header = self.local.get("header")
        status = self.local.get("status_ready")
        messages_label = self.local.get("messages")
        contacts_label = self.local.get("contacts")
        settings_label = self.local.get("settings")

        return {
            "header": {
                "text": header,
                "status": status,
                "style": self.theme.header_style()
            },
            "message_list": {
                "items": [],
                "style": self.theme.message_style()
            },
            "navigation": {
                "buttons": [
                    {"label": messages_label, "active": True},
                    {"label": contacts_label, "active": False},
                    {"label": settings_label, "active": False}
                ],
                "style": self.theme.nav_style()
            }
        }
