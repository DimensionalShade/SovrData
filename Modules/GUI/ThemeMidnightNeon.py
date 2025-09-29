class ThemeMidnightNeon:
    def __init__(self):
        self.colors = {
            "background": "#0D0D0D",
            "accent": "#00FFFF",
            "text": "#FFFFFF",
            "warning": "#FF00FF",
            "success": "#00FF00"
        }

    def apply(self):
        return {
            "font": "Roboto",
            "size": 14,
            "colors": self.colors
        }
