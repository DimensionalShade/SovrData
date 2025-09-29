from Modules.Privacy.DimShade import DimShade

class MessageRouter:
    def route(self, message):
        shade = DimShade(mode="adaptive")
        filtered = shade.apply(message["text"])
        message["text"] = filtered["dimmed_text"]
        message["mask_map"] = filtered["mask_map"]
        message["requires_consent"] = filtered["requires_consent"]
        return message
