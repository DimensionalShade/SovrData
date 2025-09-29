class Localization:
    def __init__(self, lang="ru"):
        self.lang = lang
        self.strings = {
            "ru": {
                "header": "Еуграм",
                "messages": "Сообщения",
mkdir -p Modules/GUI && cat > Modules/GUI/Localization.py <<EOF
class Localization:
    def __init__(self, lang="ru"):
        self.lang = lang
        self.strings = {
            "ru": {
                "header": "Еуграм",
                "messages": "Сообщения",
                "contacts": "Контакты",
mkdir -p Modules/GUI && cat > Modules/GUI/Localization.py <<EOF
class Localization:
    def __init__(self, lang="ru"):
        self.lang = lang
        self.strings = {
            "ru": {
                "header": "Еуграм",
                "messages": "Сообщения",
                "contacts": "Контакты",
                "settings": "Настройки",
                "status_ready": "Готово"
            },
            "en": {
                "header": "Eugram",
                "messages": "Messages",
                "contacts": "Contacts",
                "settings": "Settings",
                "status_ready": "Ready"
            },
            "uk": {
                "header": "Єуграм",
                "messages": "Повідомлення",
                "contacts": "Контакти",
                "settings": "Налаштування",
                "status_ready": "Готово"
            }
        }

    def get(self, key):
        return self.strings.get(self.lang, {}).get(key, key)
