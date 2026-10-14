# Публикация в GitHub и дальнейшее использование

## 1. Создать репозиторий

На GitHub создайте пустой репозиторий, например `MeetingProtocolSkill`.

## 2. Загрузить подготовленные файлы

Распакуйте архив и выполните в папке `MeetingProtocolSkill`:

```bash
git init
git add .
git commit -m "Initial release meeting protocol skill v0.1.0"
git branch -M main
git remote add origin https://github.com/<ВАШ_LOGIN>/MeetingProtocolSkill.git
git push -u origin main
```

Если репозиторий уже клонирован локально, достаточно скопировать файлы в него и выполнить `git add .`, `git commit`, `git push`.

## 3. Использовать скилл

В новом чате приложите транскрипцию и при необходимости предыдущий протокол/контекст проекта. Затем укажите модели:

```text
Используй актуальный skill meeting-protocol-storage из репозитория:
https://github.com/<ВАШ_LOGIN>/MeetingProtocolSkill

Сформируй протокол по приложенной транскрипции.
Предыдущий протокол используй как источник фактов только если он относится к тому же проекту/этапу.
Не додумывай неизвестные поля — оставляй их пустыми.
На выходе нужен Confluence Storage Format XML. DOCX не нужен.
```

Основной файл скилла:

`portable-skills/meeting-protocol-storage/SKILL.md`

## 4. Обновлять версию

При изменениях обновляйте `release.json`, запускайте проверку и делайте новый commit/push:

```bash
python portable-skills/meeting-protocol-storage/scripts/validate_storage.py portable-skills/meeting-protocol-storage/templates/protocol-template.xml
python -m unittest discover -s tests -v
```
