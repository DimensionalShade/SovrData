import socket
import threading
from Storage.KeyStore import KeyStore
from Core.AuditTrail import AuditTrail

class DirectLink:
    def __init__(self, port=5050):
        self.port = port
        self.key_store = KeyStore()
        self.audit = AuditTrail()
        self.conn = None
        self.addr = None

    def start_listener(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(("", self.port))
        s.listen(1)
        self.conn, self.addr = s.accept()
        self.audit.record("Transport.DirectLink", "connected", {"peer": self.addr})
        threading.Thread(target=self.receive_loop).start()

    def connect_to_peer(self, ip):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, self.port))
        self.conn = s
        self.addr = ip
        self.audit.record("Transport.DirectLink", "connected", {"peer": ip})
        threading.Thread(target=self.receive_loop).start()

    def send(self, data):
        if self.conn:
            encrypted = self.key_store.encrypt(data)
            self.conn.sendall(encrypted)

    def receive_loop(self):
        while True:
            try:
                data = self.conn.recv(4096)
                if not data:
                    break
                decrypted = self.key_store.decrypt(data)
                self.audit.record("Transport.DirectLink", "received", {"data": decrypted})
            except:
                break
