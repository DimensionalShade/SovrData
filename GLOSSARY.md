# Eugram: GLOSSARY.md

Формализованный справочник ошибок, стандартов и сигналов, используемых в проекте Eugram.

## 🧠 Ошибки и сигналы

- **port issues** — ошибка окружения Termux, связанная с сетевыми ограничениями или DNS
- **file closure anomaly** — файл не закрыт корректно, возможна потеря данных
- **sed fail** — ошибка при попытке редактирования файла через , возможно файл не существует
- **manual edit violation** — попытка ручного редактирования, нарушающая автоматизационные стандарты

## ⚙️ Стандарты

- Все изменения файлов — только через shell-команды (, , )
- Все модули фиксируются через On branch master
Your branch is ahead of 'origin/master' by 2 commits.
  (use "git push" to publish your local commits)

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	GLOSSARY.md
	Modules/Core/LicenseManager.py
	Modules/Privacy/
	Storage/config.json

nothing added to commit but untracked files present (use "git add" to track) с префиксом области (, , )
- Все действия логируются через 

## 📦 Артефакты

-  — источник версий модулей
-  — пользовательские настройки
-  — журнал действий и событий

