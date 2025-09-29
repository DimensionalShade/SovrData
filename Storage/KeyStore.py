from cryptography.hazmat.primitives.asymmetric import x25519
from cryptography.hazmat.primitives import serialization
from Core.AuditTrail import AuditTrail

class KeyStore:
    def __init__(self):
        self.private_key = x25519.X25519PrivateKey.generate()
        self.public_key = self.private_key.public_key()
        self.shared_key = None
        self.audit = AuditTrail()

    def get_public_bytes(self):
        return self.public_key.public_bytes(
            encoding=serialization.Encoding.Raw,
            format=serialization.PublicFormat.Raw
        )

    def exchange_keys(self, peer_public_bytes):
        peer_key = x25519.X25519PublicKey.from_public_bytes(peer_public_bytes)
        self.shared_key = self.private_key.exchange(peer_key)
        self.audit.record("KeyStore", "exchange_keys", {"shared_key": self.shared_key.hex()})
        return self.shared_key
