from Transport.DirectLink import DirectLink
from Core.AuditTrail import AuditTrail

class LocalTransport:
    def __init__(self):
        self.link = DirectLink()
        self.buffer = []
        self.audit = AuditTrail()

    def send_message(self, message):
        if self.link.conn:
            self.link.send(message["text"])
            self.audit.record("Transport.LocalTransport", "sent", {"text": message["text"]})
        else:
            self.buffer.append(message)
            self.audit.record("Transport.LocalTransport", "buffered", {"text": message["text"]})

    def flush_buffer(self):
        if self.link.conn:
            for msg in self.buffer:
                self.link.send(msg["text"])
                self.audit.record("Transport.LocalTransport", "flushed", {"text": msg["text"]})
            self.buffer.clear()
