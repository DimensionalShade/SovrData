# Eugram Architecture

Eugram is a modular, privacy-focused chat system dedicated to Eugene. Every module is auditable, reproducible, and philosophically aligned with user sovereignty.

---

## 🧩 Core Modules

| Module           | Purpose                                 |
|------------------|------------------------------------------|
| ConsentVault     | Logs digital consent events              |
| AuditTrail       | Journals all actions across modules      |
| MessageRouter    | Routes messages across sessions          |
| SessionManager   | Tracks active user sessions              |
| KeyStore         | Manages cryptographic keys               |
| SMSShield        | Intercepts and filters SMS messages      |

---

## 🎨 GUI Modules

| Module             | Purpose                                 |
|--------------------|------------------------------------------|
| Layout             | Renders interface and handles input      |
| ThemeMidnightNeon  | Midnight background + neon accents       |
| Localization       | Language strings (ru, en, uk)            |

---

## 🗄️ Storage Modules

| Module         | Purpose                                 |
|----------------|------------------------------------------|
| ConfigStore    | Stores settings (language, theme, policy)|
| ModuleCache    | Tracks module status and versions        |

---

## 🔄 Update Modules

| Module         | Purpose                                 |
|----------------|------------------------------------------|
| VersionCheck   | Compares current vs latest versions      |
| ModuleSync     | Updates outdated modules                 |

---

## ⚖️ Legal Modules

| Module           | Purpose                                 |
|------------------|------------------------------------------|
| LicenseManager   | Validates module licenses                |

---

## 🧠 Philosophy

- **Reproducibility**: Every artifact is scriptable and auditable.
- **Consent**: All actions are logged and traceable.
- **Modularity**: Each component is replaceable and testable.
- **Sovereignty**: Users retain control over data, keys, and policies.

