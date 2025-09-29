from Transport.DirectLink import DirectLink
from Core.AuditTrail import AuditTrail

class SessionManager:
    def __init__(self):
        self.link = DirectLink()
        self.audit = AuditTrail()

    def connect_peer(self, ip=None):
        if ip:
            self.link.connect_to_peer(ip)
            self.audit.record("SessionManager", "connect_peer", {"mode": "active", "peer": ip})
        else:
            self.link.start_listener()
            self.audit.record("SessionManager", "connect_peer", {"mode": "passive"})
