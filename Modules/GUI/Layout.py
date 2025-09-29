import tkinter as tk
from Modules.Core.SessionManager import SessionManager
from Modules.Core.ConsentVault import ConsentVault
from Transport.LocalTransport import LocalTransport
from Storage.config import load_config

class Layout:
    def __init__(self, root):
        self.root = root
        self.session = SessionManager()

    def render_connection_screen(self):
        frame = tk.Frame(self.root, bg="#1e1e1e")
        frame.pack(fill="both", expand=True)

        label = tk.Label(frame, text="Подключение к устройству", fg="white", bg="#1e1e1e", font=("Arial", 16))
        label.pack(pady=20)

        entry = tk.Entry(frame, font=("Arial", 14))
        entry.pack(pady=10)
        entry.insert(0, "Введите IP-адрес")

        def connect():
            ip = entry.get()
            self.session.connect_peer(ip)

        def listen():
            self.session.connect_peer()

        btn_connect = tk.Button(frame, text="Подключиться", command=connect, bg="#007acc", fg="white", font=("Arial", 12))
        btn_connect.pack(pady=5)

        btn_listen = tk.Button(frame, text="Ожидать входящее", command=listen, bg="#444", fg="white", font=("Arial", 12))
        btn_listen.pack(pady=5)

    def render_chat_screen(self):
        config = load_config()
        vault = ConsentVault()
        transport = LocalTransport()

        frame = tk.Frame(self.root, bg="#121212")
        frame.pack(fill="both", expand=True)

        label = tk.Label(frame, text="Чат", fg="white", bg="#121212", font=("Arial", 16))
        label.pack(pady=10)

        entry = tk.Entry(frame, font=("Arial", 14))
        entry.pack(pady=10)

        def send():
            text = entry.get()
            transport.send_message({"text": text})
            entry.delete(0, tk.END)

        btn = tk.Button(frame, text="Отправить", command=send, bg="#007acc", fg="white", font=("Arial", 12))
        btn.pack(pady=5)

    def render_dimmed_fragment(self, parent, fragment, context):
        vault = ConsentVault()
        btn = tk.Button(parent, text="●●●", bg="#333", fg="white", font=("Arial", 12))
        def reveal():
            btn.config(text=fragment)
            vault.log_reveal(fragment, context)
        btn.config(command=reveal)
        btn.pack(padx=5, pady=5, anchor="w")
