import json
class VersionCheck:
    def get_latest_version(self):
        with open("manifest.json") as f:
            manifest = json.load(f)
        versions = [info["version"] for info in manifest.values()]
        return max(versions)
    def get_current_version(self):
        try:
            with open("version.txt") as f:
                return f.read().strip()
        except FileNotFoundError:
            return "0.0.0"
    def get_current_version(self):
        return "0.0.1"
    def __init__(self):
        # сюда можно добавить инициализацию
        pass

    def check_all(self):
        import json
        with open("manifest.json") as f:
            manifest = json.load(f)
        updates = {}
        current_version = self.get_current_version()
        for name, info in manifest.items():
            if info["version"] > current_version:
                updates[name] = info["url"]
        print("VersionCheck: check_all() вызвано")
        return updates
        # временно возвращаем фиктивную "последнюю" версию
        return "0.0.2"

    def download(self, url):
        print(f"VersionCheck: download() вызвано для {url}")
        return f"# Заглушка: содержимое модуля с {url}\n"
