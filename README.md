# Eugram

**Eugram** is a modular, privacy-focused chat client dedicated to Eugene. It embodies a philosophy of user sovereignty, reproducibility, and formal consent.

## 🧭 Philosophy

- **Transparency**: Every module is a formal artifact with explicit function and audit trail.
- **Consent**: Private fragments require explicit user action to reveal, and every reveal is logged.
- **Automation**: All changes are executed via scripts—manual editing is strictly prohibited.
- **Auditability**: Every action is logged in `audit.json` and can be exported for review.

## 🧱 Architecture

- `Modules/Core/SessionManager.py` — peer-to-peer connection between devices.
- `Modules/Core/ConsentVault.py` — logs user consent for revealing private fragments.
- `Modules/Core/AuditTrail.py` — formalized logger for all actions.
- `Modules/Core/VersionCheck.py` — compares and updates modules based on `manifest.json`.
- `Modules/GUI/Layout.py` — GUI screens for connection, chat, and dimmed fragments.
- `Transport/LocalTransport.py` — local message routing.
- `Storage/ModuleCache.py` — stores and retrieves modules locally.
- `Storage/config.json` — privacy settings and dimshade mode.
- `manifest.json` — authoritative source of module versions and code.

## 🚀 Launch

    python main.py
